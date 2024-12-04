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
st.header("Doe e ajude a transformar vidas! 💸")
st.write(""" Apoie a Transformação!

Em um mundo onde cada gesto de solidariedade conta, sua ajuda é fundamental para promover mudanças reais e impactar a vida de quem mais precisa. É com imenso prazer que a ONG Esperança e Futuro apresenta sua nova campanha de doações, que visa transformar a vida de milhares de crianças e famílias em situação de vulnerabilidade social.

Por que sua doação é tão importante?
Com o seu apoio, podemos fornecer acesso à educação de qualidade, alimentação, cuidados médicos e apoio psicológico para quem vive em condições de extrema necessidade. Estamos construindo um futuro melhor para essas pessoas, e você pode fazer parte dessa transformação.

Cada contribuição, independente do valor, é um passo a mais para a construção de um mundo mais justo e igualitário. Seja a mudança que você deseja ver no mundo!

Nosso compromisso com a transparência
Toda doação será destinada de maneira responsável, com prestação de contas regular aos nossos apoiadores, garantindo que cada centavo seja usado para cumprir nossa missão de levar esperança e oportunidades a quem mais precisa.

Acredite no poder da solidariedade. Juntos, somos mais fortes!

Para mais informações sobre a ONG, acesse nosso site ou entre em contato!
        """)
st.write("Como contribuir? A sua doação pode ser realizada de maneira simples e segura através da chave de doação 074.321.953-82 ou pelo QR CODE abaixo.")
st.image("https://i.imgur.com/Me2BjCt.jpeg")