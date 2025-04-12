import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

# Database engine
engine = sa.create_engine('sqlite:///DB/dpexercicio.db')

# Base class for ORM models
Base = declarative_base()

# Tabela DP
class DP(Base):
    __tablename__ = 'dp'

    codDP = sa.Column(sa.INTEGER, primary_key=True, nullable=False, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    endereco = sa.Column(sa.VARCHAR(255), nullable=False)

# Tabela ResponsavelSP
class ResponsavelSP(Base):
    __tablename__ = 'responsavelsp'
    
    codDP = sa.Column(sa.INTEGER, sa.ForeignKey('dp.codDP', ondelete='NO ACTION', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
    delegado = sa.Column(sa.VARCHAR(100), nullable=False)

# Tabela Municipio
class Municipio(Base):
    __tablename__ = 'municipio'
    
    codIBGE = sa.Column(sa.INTEGER, primary_key=True, nullable=False, index=True)
    municipio = sa.Column(sa.VARCHAR(100), nullable=False)
    regiao = sa.Column(sa.VARCHAR(25), nullable=False)

# Tabela Ocorrencias
class Ocorrencias(Base):
    __tablename__ = 'ocorrencias'
    
    idRegistro = sa.Column(sa.INTEGER, primary_key=True, nullable=False, index=True)
    codDP = sa.Column(sa.INTEGER, sa.ForeignKey('dp.codDP', ondelete='NO ACTION', onupdate='CASCADE'), index=True, nullable=False)
    codIBGE = sa.Column(sa.INTEGER, sa.ForeignKey('municipio.codIBGE', ondelete='NO ACTION', onupdate='CASCADE'), index=True, nullable=False)
    ano = sa.Column(sa.CHAR(4), nullable=False)
    mes = sa.Column(sa.VARCHAR(2), nullable=False)
    ocorrencia = sa.Column(sa.VARCHAR(100), nullable=False)
    qtde = sa.Column(sa.INTEGER, nullable=False)

# Create tables
try:
    Base.metadata.create_all(engine)
    print('Tabelas criadas!')
except Exception as e:
    print(f'Erro ao criar tabelas: {e}')