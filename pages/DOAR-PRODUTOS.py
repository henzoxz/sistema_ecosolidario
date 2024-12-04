import streamlit as st
import random
import string

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.image("https://i.imgur.com/UHGwDLB.png")

st.sidebar.image("https://i.imgur.com/JwwPz4t.png")

def autenticar():
    return "usuario" in st.session_state

st.title("Adicione produtos à sua lista! 📦")

if 'itens' not in st.session_state:
    st.session_state.itens = []

imagens = {
    "Lençóis": "https://i.imgur.com/jP1SE2D.png",
    "Cesta Básica 1": "https://i.imgur.com/sTGvcto.png",
    "Cesta Básica 2": "https://calvo.com.br/wp-content/uploads/2022/09/CESTA-GIRASSOL-PREMIUM.png",
    "Remédios": "https://catracalivre.com.br/wp-content/uploads/2018/04/como-conseguir-remedio-de-graca-iStock.jpg",
    "Itens de Limpeza": "https://i.imgur.com/GyArPQZ.png",
    "Fardo de Água": "https://i.imgur.com/6dtlVK7.png",
    "Fraldas": "https://i.imgur.com/S9dLWs6.png",
    "Brinquedos Novos": "https://i.imgur.com/vck252y.png",
    "Brinquedos Usados": "https://i.imgur.com/6giRhIr.png",
    "Leite em Pó": "https://i.imgur.com/oMdnx7T.png",
    "Roupas de Frio": "https://i.imgur.com/MIXCJht.png",
    "Kit de Primeiros Socorros": "https://i.imgur.com/BevGWBI.png",
    "Kit Escolar": "https://i.imgur.com/6dSoGaD.png",
    "Kit de Panelas": "https://i.imgur.com/pI1nkyO.png",
    "Kit de Higine Pessoal": "https://i.imgur.com/iBOceTl.png"
}

st.subheader("Escolha um produto:")
produto = st.selectbox("Selecione o produto que deseja adicionar:", list(imagens.keys()))

st.image(imagens[produto], caption=produto, width=300)

novo_item = st.text_input("Digite um nome adicional ou deixe em branco para continuar:")

if st.button("Adicionar"):
    if produto:
        item_com_icone = f"{produto} - {novo_item if novo_item else 'Sem descrição'}"
        st.session_state.itens.append(item_com_icone)
        st.success(f"Produto '{item_com_icone}' adicionado com sucesso!")
    else:
        st.error("Por favor, selecione um produto.")

if st.session_state.itens:
    st.subheader("Produtos adicionados:")
    for item in st.session_state.itens:
        st.write(f"- {item}")

    if autenticar():
        usuario = st.session_state["usuario"]
        st.write(f"Bem-vindo, *{usuario['nome']}*! Escolha um produto para doar:")

        doacao = st.selectbox("Selecione um produto para doar:", st.session_state.itens)

        if st.button("Doar"):
            if doacao:
                st.session_state.itens.remove(doacao)

                if "doacoes" not in usuario:
                    usuario["doacoes"] = []

                produto_nome = doacao.split(" - ")[0]
                usuario["doacoes"].append({
                    "produto": produto_nome,
                    "imagem": imagens[produto_nome]
                })

                ticket_num = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                st.success(f"Produto '{doacao}' doado com sucesso por *{usuario['nome']}*!")
                st.write(f"Seu número de ticket é: {ticket_num}")
                st.write("Pronto! Agora basta você entrar em contato conosco pelo email contatoecosolidario@gmail.com e nos enviar seu número de ticket que realizaremos a doação em seu nome.")
            else:
                st.error("Por favor, selecione um produto para doar.")
    else:
        st.error("Você precisa se cadastrar ou logar para doar produtos!")
else:
    st.write("Nenhum produto adicionado ainda.")