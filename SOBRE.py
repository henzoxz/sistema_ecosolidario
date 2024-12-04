import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    body {
        background-color: #191970;  # Cor de fundo clara
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.sidebar.image("https://i.imgur.com/JwwPz4t.png")
st.image("https://i.imgur.com/vYA6xPs.png")
st.header("Sobre Nós")
st.write(""" 
        Eco Solidário ONG fundada por Henry, Hugo, Henzo, Guilherme e Bruno, com a missão de apoiar pessoas em situação de vulnerabilidade, incluindo moradores de rua e refugiados. Nosso objetivo é arrecadar fundos e itens essenciais como alimentos, roupas, cobertores, produtos de higiene e materiais de primeira necessidade, para proporcionar dignidade e suporte às pessoas que mais necessitam. 
        Através de campanhas de arrecadação e parcerias com empresas e voluntários, buscamos aliviar o sofrimento imediato e oferecer um acolhimento humanitário. 
        Além disso, a Eco Solidário promove a inclusão social e a conscientização sobre as questões enfrentadas por essas populações, integrando ações de solidariedade com práticas sustentáveis e o compromisso com os direitos humanos, criando um impacto positivo tanto nas vidas das pessoas atendidas quanto na sociedade como um todo
        """)