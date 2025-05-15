import requests
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import time
from dotenv import load_dotenv
import os

load_dotenv()
# Configuarções do banco de dados
DATABASE_URL = os.getenv("DATABASE_KEY")

# Criação do engine e sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Definição do modelo de dados
class BitcoinDados(Base):
  __tablename__ = 'bitcoin_dados'
  id = Column(Integer, primary_key=True)
  valor = Column(Float)
  criptomoeda = Column(String(10))
  moeda = Column(String(10))
  timestamp = Column(DateTime)

# Cria a tabela se não existir
Base.metadata.create_all(engine)

def extrair_dados_bitcoin():
  """"Extrai o JSON completo da API da Coinbase"""
  url = 'https://api.coinbase.com/v2/prices/spot'
  resposta = requests.get(url)
  return resposta.json( )

def tratar_dados_bitcoin(dados_json):
  """"Transforma os dados brutos da API e adiciona timestamp"""
  valor = float(dados_json['data']['amount'])
  criptomoeda = dados_json['data']['base']
  moeda = dados_json['data']['currency']
  dados_tratados = BitcoinDados(
    valor=valor,
    criptomoeda=criptomoeda,
    moeda=moeda,
    timestamp=datetime.now()
  )
  return dados_tratados

def salvar_dados_sqlalchemy(dados):
  """"Salva dados no PostgreSQL usando SQLALchemy"""
  with Session() as session:
    session.add(dados)
    session.commit()
    print("Dados salvos no PostgreSQL")

if __name__ == '__main__':
  while True:
    dados_json = extrair_dados_bitcoin()
    dados_tratados = tratar_dados_bitcoin(dados_json)
    # Mostrar os dados tratados
    print("Dados tratados:")
    # print(dados_tratados.__dict__)
    # Salvar no PostgreSQL
    salvar_dados_sqlalchemy(dados_tratados)
    # Pausa por 15 segundos
    print("Aguardando 15 segundos ... ")
    time.sleep(15)








# def transformar(dados_json):
#   valor = dados_json['data']['amount']
#   criptomoeda = dados_json['data']['base']
#   moeda = dados_json['data']['currency']
#   dados_tratados = {
#     'valor': valor,
#     'criptomoeda': criptomoeda,
#     'moeda': moeda,
#     'timestamp': datetime.now().isoformat()
#   }
#   return dados_tratados

# def load(dados_tratados):
#   db = TinyDB('db.json')
#   db.insert(dados_tratados)
#   print('Dados salvos com sucesso!')




