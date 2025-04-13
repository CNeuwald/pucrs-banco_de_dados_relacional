# Script to rank police departments (DPs) in the capital by the number of occurrences
import sqlalchemy as sa
import sqlalchemy.orm as orm
import sys
sys.path.append('c:\\Users\\Rafael\\OneDrive\\Área de Trabalho\\PUCRS\\ORM\\bdrelacional\\')
try:
    import Ocorrencias as oc
except ModuleNotFoundError:
    print("The module 'Ocorrencias' could not be found. Ensure 'Ocorrencias.py' exists in the specified directory.")
    raise

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DP(Base):
    __tablename__ = 'DP'
    codDP = Column(Integer, primary_key=True)
    nome = Column(String)

# Database connection
engine = sa.create_engine('sqlite:///DB/ocorrencias.db')
sessao = orm.sessionmaker(bind=engine)()

# Query to rank police departments (DPs) in the capital by the number of occurrences
try:
   RankDP = sessao.query(
    DP.nome.label('DP'),
    sa.func.sum(Ocorrencias.qtde).label('Total')
).join(
    Ocorrencias, Ocorrencias.codDP == DP.codDP
).join(
    Municipio, Ocorrencias.codIBGE == Municipio.codIBGE
).where(
    Municipio.municipio == 'Capital'
).group_by(
    DP.nome
).order_by(
    sa.func.sum(Ocorrencias.qtde).desc()
).all()

    # Print the ranking
    print("Ranking das Delegacias de Polícia na Capital:")
    for dp, total in RankDP:
        print(f"Delegacia: {dp}, Total de Ocorrências: {total}")

except Exception as e:
    print(f"Erro ao executar a consulta: {e}")
    raise