import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import vendas as vd

# Path to the CSV file
endereco = 'C:\\Users\\Rafael\\OneDrive\\Área de Trabalho\\PUCRS\\ORM\\pucrs-banco_de_dados_relacional\\Dados\\Exemplo\\Dados_Exemplo\\'
vendedor = pd.read_csv(endereco + 'vendedor.csv', sep=';')
tbVendedor = pd.DataFrame(vendedor)

# Database engine and session
engine = sa.create_engine('sqlite:///DB/vendas.db')
sessao = orm.sessionmaker(bind=engine)()
   
# Insert data into the Vendedor table
for i in range(len(tbVendedor)):
    dados_vendedor = vd.Vendedor(
        registro_vendedor=int(tbVendedor['registro_vendedor'][i]),
        cpf=tbVendedor['cpf'][i],
        nome=tbVendedor['nome'][i],
        genero=tbVendedor['genero'][i],
        email=tbVendedor['email'][i],
    )

    try:
        sessao.add(dados_vendedor)
        sessao.commit()
        print(f"Dados inseridos: {dados_vendedor.nome}")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
        sessao.rollback()