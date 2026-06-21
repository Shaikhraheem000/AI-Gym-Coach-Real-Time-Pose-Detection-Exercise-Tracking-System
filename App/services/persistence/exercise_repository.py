import bcrypt
from datetime import datetime
from services.persistence.supabase_client import get_supabase_client

def init_db() -> None:
    # Supabase tables are managed via the Supabase Dashboard, so no initialization needed here.
    pass

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def get_user(username: str) -> dict:
    client = get_supabase_client()
    response = client.table('users').select('*').eq('username', username).execute()
    if len(response.data) > 0:
        return response.data[0]
    return None

def create_user(username: str, password: str, weight_kg: float) -> dict:
    client = get_supabase_client()
    hashed_password = hash_password(password)
    
    data = {
        "username": username,
        "password_hash": hashed_password,
        "weight_kg": weight_kg
    }
    
    response = client.table('users').insert(data).execute()
    if len(response.data) > 0:
        return response.data[0]
    return None

def authenticate_user(username: str, password: str) -> dict:
    user = get_user(username)
    if user and check_password(password, user['password_hash']):
        return user
    return None

def add_exercise(user_id: int, exercise_name: str, reps: int, sets: int, time_seconds: int, calories_burned: float = 0.0):
    client = get_supabase_client()
    today_str = datetime.utcnow().strftime('%Y-%m-%d')
    
    # Check if this exercise was already done today by this user
    # Supabase doesn't easily allow Date() casting in the filter, so we filter by gte/lte
    response = client.table('exercises') \
        .select('*') \
        .eq('user_id', user_id) \
        .eq('exercise_name', exercise_name) \
        .gte('created_at', f"{today_str}T00:00:00Z") \
        .lte('created_at', f"{today_str}T23:59:59Z") \
        .execute()
        
    if len(response.data) > 0:
        # Update existing record for today
        existing_id = response.data[0]['id']
        current_reps = response.data[0]['reps']
        current_sets = response.data[0]['sets']
        current_time = response.data[0]['time_seconds']
        current_cals = response.data[0].get('calories_burned', 0.0)
        
        update_data = {
            "reps": current_reps + reps,
            "sets": current_sets + sets,
            "time_seconds": current_time + time_seconds,
            "calories_burned": current_cals + calories_burned
        }
        client.table('exercises').update(update_data).eq('id', existing_id).execute()
    else:
        # Insert new record
        insert_data = {
            "user_id": user_id,
            "exercise_name": exercise_name,
            "reps": reps,
            "sets": sets,
            "time_seconds": time_seconds,
            "calories_burned": calories_burned
        }
        client.table('exercises').insert(insert_data).execute()

def get_users_exercises(user_id: int) -> list:
    client = get_supabase_client()
    response = client.table('exercises').select('*').eq('user_id', user_id).order('created_at', desc=True).execute()
    return response.data
