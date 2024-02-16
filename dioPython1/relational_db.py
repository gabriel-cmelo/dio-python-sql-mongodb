from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String)
    endereco = Column(String)
    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    saldo = Column(Float)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship('Cliente', back_populates='contas')

# SQLite database in memory for testing purposes
engine = create_engine('sqlite:///:memory:')

# Create the tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Inserting data into the tables
client1 = Cliente(nome='João', cpf='12345678999', endereco='Rua A', contas=[Conta(tipo='Corrente', agencia='001', num=123, saldo=1000.0)])
client2 = Cliente(nome='Maria', cpf='12345678988', endereco='Rua B', contas=[Conta(tipo='Corrente', agencia='001', num=124, saldo=1500.0)])
client3 = Cliente(nome='Rafael', cpf='12345678977', endereco='Rua C', contas=[Conta(tipo='Corrente', agencia='001', num=125, saldo=2000.0)])
client4 = Cliente(nome='Carlos', cpf='12345678966', endereco='Rua D', contas=[Conta(tipo='Corrente', agencia='001', num=126, saldo=2500.0)])
client5 = Cliente(nome='Julia', cpf='12345678955', endereco='Rua E', contas=[Conta(tipo='Corrente', agencia='001', num=127, saldo=3000.0)])
session.add(client1)
session.add(client2)
session.add(client3)
session.add(client4)
session.add(client5)
session.commit()

# Querying data
cliente_query = session.query(Cliente).filter_by(nome='Maria').first()
print(f'Cliente: {cliente_query.nome}, Contas: {[(conta.tipo, conta.saldo) for conta in cliente_query.contas]}')
