import streamlit as st
import re

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def format_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) <= 3:
        return cpf
    elif len(cpf) <= 6:
        return f"{cpf[:3]}.{cpf[3:]}"
    elif len(cpf) <= 9:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}"
    elif len(cpf) <= 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf


def conta():
    st.sidebar.image("https://i.imgur.com/JwwPz4t.png")

    st.header("INFORMAÇÕES DA SUA CONTA")

    if "usuario" in st.session_state:
        usuario = st.session_state["usuario"]

        if usuario["nome"] and usuario["email"]:
            if usuario["genero"] == "Masculino":
                st.image("https://cdn-icons-png.flaticon.com/512/6076/6076526.png", width=150)
            elif usuario["genero"] == "Feminino":
                st.image("https://cdn-icons-png.flaticon.com/256/6075/6075732.png", width=150)

            st.write(f"Usuário: {usuario['nome']}")
            st.write(f"E-mail: {usuario['email']}")
            if usuario.get("cpf"):
                st.write(f"CPF: {format_cpf(usuario['cpf'])}")
            st.write(f"Gênero: {usuario['genero']}")

            if "doacoes" in usuario and usuario["doacoes"]:
                st.subheader("Produtos Doados:")
                for doacao in usuario["doacoes"]:
                    st.image(doacao["imagem"], caption=doacao["produto"], width=150)
            else:
                st.info("Você ainda não doou nenhum produto.")
        else:
            st.warning(
                "Algumas informações estão faltando. Por favor, complete sua conta para aproveitar ao máximo os recursos disponíveis."
            )

        if st.button("Sair da Conta"):
            del st.session_state["usuario"]
            st.success("Você saiu da conta com sucesso!")
            st.stop()
    else:
        st.error("Não há dados de usuário registrados ou logados.")

conta()