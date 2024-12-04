import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def feedback():
    if "usuario" not in st.session_state:
        st.error("Você precisa se cadastrar ou logar para acessar esta página.")
        return  

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

    st.image("https://i.imgur.com/lGeVfvb.png")

    st.sidebar.image("https://i.imgur.com/JwwPz4t.png")
    st.header("Conte-nos sua Experiência")
    feedback_text = st.text_area("Digite seu Feedback:")

    if st.button("Enviar"):
        if feedback_text.strip():
            st.success("Feedback enviado! Obrigado por compartilhar sua experiência conosco.")
        else:
            st.warning("Por favor, digite um feedback antes de enviar.")

feedback()
