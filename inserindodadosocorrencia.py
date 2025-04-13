
import os
import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import Scripts as oc  # Importing the module with table definitions

# Path to the CSV/Excel files
endereco = 'C:\\Users\\Rafael\\OneDrive\\Área de Trabalho\\PUCRS\\ORM\\pucrs-banco_de_dados_relacional\\Scripts\\'

# Validate file paths
required_files = ['dp.csv', 'ResponsavelDP.xlsx', 'municipio.csv', 'ocorrencias.xlsx']
missing_files = [file for file in required_files if not os.path.exists(endereco + file)]

if missing_files:
    print(f"Erro: Os seguintes arquivos estão ausentes no diretório {endereco}:")
    for file in missing_files:
        print(f"- {file}")
    exit()

# Load data from CSV/Excel files
try:
    dp = pd.read_csv(endereco + 'dp.csv')
    responsavelDP = pd.read_excel(endereco + 'ResponsavelDP.xlsx')
    municipio = pd.read_csv(endereco + 'municipio.csv')
    ocorrencias = pd.read_excel(endereco + 'ocorrencias.xlsx')
except Exception as e:
    print(f"Erro ao carregar arquivos: {e}")
    exit()

# Convert data to DataFrames
tbDP = pd.DataFrame(dp)
tbResponsavelDP = pd.DataFrame(responsavelDP)
tbMunicipio = pd.DataFrame(municipio)
tbOcorrencias = pd.DataFrame(ocorrencias)

# Database connection
try:
    engine = sa.create_engine('sqlite:///DB/ocorrencias.db')
    conn = engine.connect()
    metadata = sa.MetaData()  # Removido o argumento 'bind'
    sessao = sa.orm.sessionmaker(bind=engine)()
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    exit()

# Insert data into DP table
try:
    DadosDP = tbDP.to_dict(orient='records')
    tabela_DP = sa.Table(oc.DP.__tablename__, metadata, autoload_with=engine)  # Passando 'autoload_with=engine'
    conn.execute(tabela_DP.insert(), DadosDP)
    sessao.commit()
    print('Dados inseridos na tabela DP')
except Exception as e:
    print(f"Erro ao inserir dados na tabela DP: {e}")
    sessao.rollback()

# Insert data into ResponsavelSP table
try:
    DadosRespDP = tbResponsavelDP.to_dict(orient='records')
    tabela_respDP = sa.Table(oc.ResponsavelSP.__tablename__, metadata, autoload_with=engine)
    conn.execute(tabela_respDP.insert(), DadosRespDP)
    sessao.commit()
    print('Dados inseridos na tabela ResponsavelSP')
except Exception as e:
    print(f"Erro ao inserir dados na tabela ResponsavelSP: {e}")
    sessao.rollback()

# Insert data into Municipio table
try:
    DadosMunicipio = tbMunicipio.to_dict(orient='records')
    tabela_municipio = sa.Table(oc.Municipio.__tablename__, metadata, autoload_with=engine)
    conn.execute(tabela_municipio.insert(), DadosMunicipio)
    sessao.commit()
    print('Dados inseridos na tabela Municipio')
except Exception as e:
    print(f"Erro ao inserir dados na tabela Municipio: {e}")
    sessao.rollback()

# Insert data into Ocorrencias table
try:
    DadosOcorrencia = tbOcorrencias.to_dict(orient='records')
    tabela_ocorrencia = sa.Table(oc.Ocorrencias.__tablename__, metadata, autoload_with=engine)
    conn.execute(tabela_ocorrencia.insert(), DadosOcorrencia)
    sessao.commit()
    print('Dados inseridos na tabela Ocorrencias')
except Exception as e:
    print(f"Erro ao inserir dados na tabela Ocorrencias: {e}")
    sessao.rollback()
