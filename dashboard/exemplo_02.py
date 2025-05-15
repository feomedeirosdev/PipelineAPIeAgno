import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Componentes Streamlit", layout="wide")

st.title("🎯 Demonstração dos 20 Principais Componentes do Streamlit")

# 1. Texto
st.header("1. Texto e Markdown")
st.markdown("**Markdown é útil para formatação _rica_**.")

# 2. Código
st.subheader("2. Código formatado")
st.code("import numpy as np", language="python")

# 3. Tabelas
st.subheader("3. Tabela e DataFrame")
df = pd.DataFrame({
    'Coluna A': range(1, 6),
    'Coluna B': np.random.randn(5)
})
st.dataframe(df)

# 4. Botão
st.subheader("4. Botão")
if st.button("Clique aqui"):
    st.success("Você clicou no botão!")

# 5. Checkbox
st.subheader("5. Checkbox")
if st.checkbox("Mostrar gráfico"):
    st.line_chart(np.random.randn(50))

# 6. Radio
st.subheader("6. Radio")
opcao = st.radio("Escolha uma cor:", ["Vermelho", "Verde", "Azul"])
st.write(f"Você escolheu: {opcao}")

# 7. Selectbox
st.subheader("7. Selectbox")
item = st.selectbox("Escolha um item:", ["Maçã", "Banana", "Laranja"])
st.write(f"Selecionado: {item}")

# 8. Multiselect
st.subheader("8. Multiselect")
opcoes = st.multiselect("Escolha múltiplas opções:", ["Python", "C++", "Go", "Rust"])
st.write("Você selecionou:", opcoes)

# 9. Slider
st.subheader("9. Slider")
valor = st.slider("Selecione um valor", 0, 100, 25)
st.write(f"Valor: {valor}")

# 10. Number input
st.subheader("10. Input numérico")
numero = st.number_input("Digite um número:", min_value=0, max_value=100)
st.write(f"Você digitou: {numero}")

# 11. Text input
st.subheader("11. Input de texto")
nome = st.text_input("Qual seu nome?")
if nome:
    st.write(f"Bem-vindo, {nome}!")

# 12. Text area
st.subheader("12. Área de texto")
texto = st.text_area("Digite sua opinião:")
if texto:
    st.write("Você escreveu:", texto)

# 13. Date input
st.subheader("13. Data")
data = st.date_input("Escolha uma data")
st.write("Data selecionada:", data)

# 14. Time input
st.subheader("14. Hora")
hora = st.time_input("Escolha um horário")
st.write("Horário selecionado:", hora)

# 15. File uploader
st.subheader("15. Upload de arquivos")
arquivo = st.file_uploader("Faça upload de um CSV")
if arquivo:
    df_uploaded = pd.read_csv(arquivo)
    st.write("Prévia do arquivo:", df_uploaded.head())

# 16. Color picker
st.subheader("16. Seletor de cor")
cor = st.color_picker("Escolha uma cor", "#00f900")
st.write(f"Cor escolhida: {cor}")

# 17. Progress bar
st.subheader("17. Barra de progresso")
with st.spinner("Carregando..."):
    for i in range(100):
        time.sleep(0.01)
        st.progress(i + 1)

# 18. Expander
st.subheader("18. Expansor de conteúdo")
with st.expander("Clique para ver mais"):
    st.write("Este é um conteúdo adicional escondido.")

# 19. Sidebar
st.sidebar.title("19. Exemplo de Sidebar")
st.sidebar.info("Este é um painel lateral com widgets.")
st.sidebar.selectbox("Escolha uma opção:", ["A", "B", "C"])

# 20. Metric
st.subheader("20. Métrica")
st.metric(label="Variação de temperatura", value="32°C", delta="+3°C")

st.success("✅ Fim da demonstração dos 20 principais componentes!")

st.markdown("---")
st.markdown("Feito por: **Mak**, o melhor assistente pessoal de desenvolvimento 🚀")


