import streamlit as st
import sqlite3
@st.cache (allow_output_mutation=True)
cur=sqlite3.connect('contact.db',check_same_thread=False)
st.write('Contact Information')
with st.form(key='Contact'):
    name=st.text_input('Name:')
    email=st.text_input('Email-id:')
    address=st.text_area('Address:')
    bt=st.form_submit_button('Submit')
    if bt:
        cur.execute('''CREATE TABLE IF NOT EXISTS 
                    details (Name TEXT(50), Email TEXT(50), Address TEXT(100))
                    ''')
        cur.commit()
        cur.execute('''INSERT INTO details(Name, Email, Address) 
                    VALUES(?,?,?)
                    ''',(name,email,address))
        cur.commit()
        st.success('Form submitted')
        
