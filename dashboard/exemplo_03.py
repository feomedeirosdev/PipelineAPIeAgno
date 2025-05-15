import streamlit as st
import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

# Carrega veriáveis de ambiente do arquivo .env
load_dotenv()

# Lê a variável DATABASE_URL
DATABASE_URL = os.getenv('DATABASE_KEY')

def ler_dados_postgres():
  """Lê os dados do banco PostgreSQL e retorna como DataFrame"""
  try:
    conn = psycopg2.connect(DATABASE_URL)
    query = 'SELECT * FROM bitcoin_dados ORDER BY timestamp DESC'
    df = pd.read_sql(query, conn)
    conn.close()
    return df
  except Exception as e:
    st.error(f"Erro ao conectar no PostgreSQL: {e}")
    return pd.DataFrame()

st.set_page_config(page_title="Dashboard de Preços do Bitcoin", layout='wide')
def main():
  st.title("📊 Dashboard com Preços do Bitcoin") 
  st.write("Esse dashbord exibe os dados do preço do Bitcoin coletados periodicamente em um banco PostgreSQL")

  df = ler_dados_postgres()

  if not df.empty:
    st.subheader("📈 Dados Rescentes")
    st.dataframe(df)

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by='timestamp')

    st.subheader("📉 Evolução do preço do Bitcoin")
    st.line_chart(data=df, x='timestamp', y='valor', use_container_width=True)

    st.subheader("📈 Estatísticas Gerais")
    col1, col2, col3 = st.columns(3)
    col1.metric("Preço Atual", f"${df['valor'].iloc[-1]:,.2f}")
    col2.metric("Preço Máximo", f"${df['valor'].max():,.2f}")
    col3.metric("Preço Mínimo", f"${df['valor'].min():,.2f}")
  else:
    st.warning("Nenhum dado encontrado no banco de dados PostgreSQL.")

if __name__ == "__main__":
  main()