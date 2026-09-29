import streamlit as st
from supabase import create_client, Client


url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]


try:
    with st.spinner("Please wait... Preparing SnapClass for you..."):
        # Create Supabase client
        supabase: Client = create_client(url, key)

        # Verify that the database is reachable
        supabase.table("teachers").select("teacher_id").limit(1).execute()

except Exception:
    st.error(
        "SnapClass is currently unable to connect to its services. "
        "Please check your internet connection and try again."
    )
    st.stop()