import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def autenticar():
    return "usuario" in st.session_state

def cadastro():
    st.sidebar.image("https://i.imgur.com/JwwPz4t.png")
    
    if autenticar():
        st.warning("Você já está logado. Por favor, saia da conta para criar um novo cadastro.")
        if st.button("Sair da Conta"):
            del st.session_state["usuario"]
            st.success("Você saiu da conta com sucesso!")
        return

    st.image("https://i.imgur.com/mBNwZGW.png")
    st.header("CADASTRE-SE")

    nome = st.text_input("Digite seu nome de Usuário")
    email_parte = st.text_input("Digite a parte do seu e-mail antes de @gmail.com")
    senha = st.text_input("Digite sua senha", type="password")
    senhanovamente = st.text_input("Digite sua senha novamente", type="password")
    cpf = st.text_input("Digite seu CPF (opcional)", placeholder="XXX.XXX.XXX-XX")
    genero = st.radio("Selecione seu gênero", ("Masculino", "Feminino"))

    if st.button("CADASTRE-SE"):
        if not nome or not email_parte or not senha or not senhanovamente:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        elif len(nome) < 4:
            st.error("O nome de usuário deve ter pelo menos 4 caracteres.")
        elif '@gmail.com' in email_parte:
            st.error("Não é necessário digitar '@gmail.com', o sistema irá adicionar automaticamente.")
        elif len(email_parte) < 6:
            st.error("A parte antes de '@gmail.com' deve ter pelo menos 6 caracteres.")
        elif len(senha) < 8:
            st.error("A senha deve ter pelo menos 8 caracteres.")
        elif senha != senhanovamente:
            st.error("As senhas não coincidem. Por favor, insira a mesma senha digitada acima.")
        else:
            email = f"{email_parte}@gmail.com"
            
            st.session_state.usuario = {
                "nome": nome,
                "email": email,
                "senha": senha,
                "cpf": cpf,
                "genero": genero
            }
            st.success(f"CADASTRO REALIZADO COM SUCESSO! BEM-VINDO A ECO SOLIDÁRIO!")

def conta():
    st.sidebar.image("https://i.imgur.com/JwwPz4t.png")
    st.header("INFORMAÇÕES DA SUA CONTA")

    if not autenticar():
        st.warning("Você precisa estar logado para acessar esta página.")
        return
    
    usuario = st.session_state["usuario"]
    
    if usuario["genero"] == "Masculino":
        st.image("https://cdn-icons-png.flaticon.com/512/6076/6076526.png", width=150)
    elif usuario["genero"] == "Feminino":
        st.image("https://cdn-icons-png.flaticon.com/256/6075/6075732.png", width=150)
    
    st.write(f"Usuário: {usuario['nome']}")
    st.write(f"E-mail: {usuario['email']}")
    st.write(f"Gênero: {usuario['genero']}")
    if usuario["cpf"]:
        st.write(f"CPF: {usuario['cpf']}")

    if st.button("Sair da Conta"):
        del st.session_state["usuario"]
        st.success("Você saiu da conta com sucesso!")

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
    email = st.text_input("Digite seu e-mail")
    senha = st.text_input("Digite sua senha", type="password")
    cpf = st.text_input("Digite seu CPF (opcional)", placeholder="XXX.XXX.XXX-XX")
    genero = st.radio("Selecione seu Gênero", ["Masculino", "Feminino"])

    if st.button("Logar"):
        st.session_state.usuario = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "cpf": cpf,
            "genero": genero
        }
        st.success("Login realizado com sucesso!")

page = st.selectbox("Escolha a página", ["Cadastro", "Login", "Conta"])

if page == "Cadastro":
    cadastro()
elif page == "Conta":
    conta()
elif page == "Login":
    login()
