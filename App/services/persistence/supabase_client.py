import os
import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

@st.cache_resource
def get_supabase_client() -> Client:
    """
    Initializes and caches the Supabase client.
    First checks environment variables (for local), then safely checks Streamlit secrets (for production).
    """
    # 1. Try environment variables first (from .env)
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_KEY") or os.environ.get("SUPABASE_KEY")
    
    # 2. Safely try Streamlit secrets if not found in environment
    if not url or not key:
        try:
            url = st.secrets.get("SUPABASE_URL")
            key = st.secrets.get("SUPABASE_SERVICE_KEY") or st.secrets.get("SUPABASE_KEY")
        except Exception:
            pass # No secrets file found locally
            
    if not url or not key:
        st.error("Supabase credentials are missing. Please configure them in .env or Streamlit Secrets.")
        st.stop()
        
    return create_client(url, key)
