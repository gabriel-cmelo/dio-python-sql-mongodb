from pymongo import MongoClient

# Conectando ao MongoDB Atlas
client = MongoClient('mongodb+srv://gabrielcmelo:Q6hoff6K3IX6rNxO@clusterpytestdio.l0zztbq.mongodb.net/?retryWrites=true&w=majority')

# Criando um banco de dados
db = client['banco_nosql']

# Criando a coleção 'bank'
bank_collection = db['bank']

# Inserindo documentos na coleção
cliente_document1 = {
    'id': 1,
    'nome': 'João',
    'cpf': '12345678999',
    'endereco': 'Rua A',
    'contas': [
        {
            'id': '123',
            'tipo': 'Corrente',
            'agencia': '001',
            'num': 123,
            'saldo': 1000
        }
    ]
}
cliente_document2 = {
    'id': 2,
    'nome': 'Maria',
    'cpf': '12345678988',
    'endereco': 'Rua B',
    'contas': [
        {
            'id': '124',
            'tipo': 'Corrente',
            'agencia': '001',
            'num': 124,
            'saldo': 1500
        }
    ]
}
cliente_document3 = {
    'id': 3,
    'nome': 'José',
    'cpf': '12345678977',
    'endereco': 'Rua C',
    'contas': [
        {
            'id': '125',
            'tipo': 'Corrente',
            'agencia': '001',
            'num': 125,
            'saldo': 2000
        }
    ]
}
cliente_document4 = {
    'id': 4,
    'nome': 'Laura',
    'cpf': '12345678966',
    'endereco': 'Rua D',
    'contas': [
        {
            'id': '126',
            'tipo': 'Corrente',
            'agencia': '001',
            'num': 126,
            'saldo': 2500
        }
    ]
}
cliente_document5 = {
    'id': 5,
    'nome': 'Carlos',
    'cpf': '12345678955',
    'endereco': 'Rua E',
    'contas': [
        {
            'id': '128',
            'tipo': 'Corrente',
            'agencia': '001',
            'num': 128,
            'saldo': 3000
        }
    ]
}

bank_collection.insert_one(cliente_document1)
bank_collection.insert_one(cliente_document2)
bank_collection.insert_one(cliente_document3)
bank_collection.insert_one(cliente_document4)
bank_collection.insert_one(cliente_document5)

# Recuperação de informações por pares chave-valor
resultado = bank_collection.find({'nome': 'José'})
for documento in resultado:
    print(f'Cliente: {documento["nome"]}, Contas: {[(conta["tipo"], conta["saldo"]) for conta in documento["contas"]]}')
