
import streamlit as st

def login():
    st.sidebar.subheader("🔐 Login de Acesso")
    usuario = st.sidebar.text_input("Usuário")
    senha = st.sidebar.text_input("Senha", type="password")
    
    if st.sidebar.button("Entrar"):
        if usuario == "admin" and senha == "admin123":
            st.success("✅ Acesso liberado!")
            return True
        else:
            st.error("❌ Usuário ou senha inválidos.")
            return False
    return False
