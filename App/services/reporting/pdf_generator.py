import os
from fpdf import FPDF
from datetime import datetime

def generate_workout_pdf(user_name: str, exercises: list) -> str:
    """Generates a PDF report of the user's workouts and returns the filepath."""
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, f"Apna AI Coach - Workout Report for {user_name}", ln=True, align="C")
    pdf.ln(5)
    
    # Date
    pdf.set_font("helvetica", "I", 10)
    pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="R")
    pdf.ln(5)
    
    # Table Header
    pdf.set_font("helvetica", "B", 10)
    col_widths = [40, 40, 20, 20, 30, 30]
    headers = ["Date", "Exercise", "Sets", "Reps", "Time (s)", "Calories"]
    
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, border=1, align="C")
    pdf.ln()
    
    # Table Body
    pdf.set_font("helvetica", "", 10)
    total_cals = 0.0
    total_time = 0
    total_reps = 0
    
    for ex in exercises:
        # Supabase returns ISO timestamps: "2024-05-12T14:32..."
        created_at = ex.get('created_at', '')[:10]
        name = ex.get('exercise_name', '').replace('_', ' ').title()
        sets = str(ex.get('sets', 0))
        reps = str(ex.get('reps', 0))
        time_s = str(ex.get('time_seconds', 0))
        cals = f"{ex.get('calories_burned', 0.0):.1f}"
        
        pdf.cell(col_widths[0], 10, created_at, border=1, align="C")
        pdf.cell(col_widths[1], 10, name, border=1, align="C")
        pdf.cell(col_widths[2], 10, sets, border=1, align="C")
        pdf.cell(col_widths[3], 10, reps, border=1, align="C")
        pdf.cell(col_widths[4], 10, time_s, border=1, align="C")
        pdf.cell(col_widths[5], 10, cals, border=1, align="C")
        pdf.ln()
        
        total_cals += float(ex.get('calories_burned', 0.0))
        total_time += ex.get('time_seconds', 0)
        total_reps += ex.get('reps', 0)
        
    pdf.ln(10)
    
    # Summary
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, "Summary", ln=True)
    pdf.set_font("helvetica", "", 10)
    pdf.cell(0, 10, f"Total Reps: {total_reps}", ln=True)
    pdf.cell(0, 10, f"Total Time: {total_time} seconds", ln=True)
    pdf.cell(0, 10, f"Total Calories Burned: {total_cals:.1f} kcal", ln=True)
    
    # Save to a temporary file
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
        
    filepath = os.path.join(temp_dir, f"workout_report.pdf")
    pdf.output(filepath)
    return filepath
