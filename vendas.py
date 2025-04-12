import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

# Database engine
engine = sa.create_engine('sqlite:///DB/vendas.db')

# Base class for ORM models
Base = declarative_base()

# Tabela Cliente
class Cliente(Base):
    __tablename__ = 'clientes'
    
    cpf = sa.Column(sa.CHAR(14), primary_key=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email = sa.Column(sa.VARCHAR(50), nullable=False)
    genero = sa.Column(sa.CHAR(1))
    salario = sa.Column(sa.DECIMAL(10, 2))
    dia_mes_aniversario = sa.Column(sa.CHAR(5))
    bairro = sa.Column(sa.VARCHAR(50))
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))

# Tabela Fornecedor
class Fornecedor(Base):
    __tablename__ = 'fornecedor'
    
    registro_fornecedor = sa.Column(sa.INTEGER, primary_key=True, index=True)
    nome_fantasia = sa.Column(sa.VARCHAR(50), nullable=False)
    razao_social = sa.Column(sa.VARCHAR(50), nullable=False)
    cidade = sa.Column(sa.VARCHAR(50), nullable=False)
    uf = sa.Column(sa.CHAR(2), nullable=False)

# Tabela Produto
class Produto(Base):
    __tablename__ = 'produto'
    
    codBarras = sa.Column(sa.INTEGER, primary_key=True, index=True)
    registro_fornecedor = sa.Column(sa.INTEGER, sa.ForeignKey('fornecedor.registro_fornecedor', ondelete='NO ACTION'), onupdate='CASCADE')
    dscproduto = sa.Column(sa.VARCHAR(100), nullable=False)
    genero = sa.Column(sa.CHAR(1))

# Tabela Vendedor
class Vendedor(Base):
    __tablename__ = 'vendedor'
    
    registro_vendedor = sa.Column(sa.INTEGER, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), nullable=False)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email = sa.Column(sa.VARCHAR(50), nullable=False)
    genero = sa.Column(sa.CHAR(1))

# Tabela Vendas
class Vendas(Base):
    __tablename__ = 'vendas'
    
    idTransacao = sa.Column(sa.INTEGER, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), sa.ForeignKey('clientes.cpf', ondelete='NO ACTION', onupdate='CASCADE'), index=True)
    registro_vendedor = sa.Column(sa.INTEGER, sa.ForeignKey('vendedor.registro_vendedor', ondelete='NO ACTION', onupdate='CASCADE'), index=True)
    codBarras = sa.Column(sa.INTEGER, sa.ForeignKey('produto.codBarras', ondelete='NO ACTION', onupdate='CASCADE'), index=True)

# Create tables
try:
    Base.metadata.create_all(engine)
    print('Tabelas criadas!')
except Exception as e:
    print(f'Erro ao criar tabelas: {e}')