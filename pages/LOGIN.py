import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def autenticar():
    return "usuario" in st.session_state

def login():
    st.sidebar.image("https://i.imgur.com/JwwPz4t.png")
    
    if autenticar():
        st.warning("Você já está logado. Por favor, saia da conta para acessar o login.")
        if st.button("Sair da Conta"):
            del st.session_state["usuario"]
            st.success("Você saiu da conta com sucesso!")
        return

    st.image("https://i.imgur.com/l4ikPiE.png")
    st.header("JUNTE-SE A NÓS NOVAMENTE!")

    nome = st.text_input("Digite seu nome de Usuário")
    email_parte = st.text_input("Digite a parte do seu e-mail antes de @gmail.com")
    senha = st.text_input("Digite sua senha", type="password")
    cpf = st.text_input("Digite seu CPF", placeholder="XXX.XXX.XXX-XX")
    genero = st.radio("Selecione seu Gênero", ["Masculino", "Feminino"])

    if st.button("Logar"):
        if not nome or not email_parte or not senha:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        elif len(nome) < 4:
            st.error("O nome de usuário deve ter pelo menos 4 caracteres.")
        elif '@gmail.com' in email_parte:
            st.error("Não é necessário digitar '@gmail.com', o sistema irá adicionar automaticamente.")
        elif len(email_parte) < 6:
            st.error("A parte antes de '@gmail.com' deve ter pelo menos 6 caracteres.")
        elif len(senha) < 8:
            st.error("A senha deve ter pelo menos 8 caracteres.")
        else:
            email = f"{email_parte}@gmail.com"
            
            st.session_state.usuario = {
                "nome": nome,
                "email": email,
                "senha": senha,
                "cpf": cpf,
                "genero": genero
            }
            st.success(f"Login realizado com sucesso!")

login()
