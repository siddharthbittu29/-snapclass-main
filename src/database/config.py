import streamlit as st
from supabase import create_client, Client

# supabase: Client = create_client(
#     st.secrets["SUPABASE_URL"], 
#     st.secrets["SUPABASE_KEY"]
# )


import streamlit as st
from supabase import create_client

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

st.write("Supabase URL:", url)

supabase = create_client(url, key)

try:
    result = supabase.table("teachers").select("*").limit(1).execute()
    st.success("Supabase Connected")
except Exception as e:
    st.error(f"Supabase Error: {e}")