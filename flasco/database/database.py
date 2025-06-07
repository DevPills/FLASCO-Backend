# # seu arquivo database.py CORRIGIDO

# from sqlalchemy.ext.asyncio import (
#     create_async_engine,
#     async_sessionmaker,
#     AsyncSession
# )
# from flasco.settings import settings

# # Adicione o argumento `connect_args` aqui
# engine = create_async_engine(
#     settings.DATABASE_URL,
#     connect_args={"ssl": 'require'},  # <--- ESTA É A LINHA IMPORTANTE
# )

# AsyncSessionLocal = async_sessionmaker(
#     engine, class_=AsyncSession, expire_on_commit=False
# )

# async def get_async_session():
#     async with AsyncSessionLocal() as db:
#         yield db

# seu arquivo database.py CORRIGIDO (Opção 2)
# database.py - USANDO A OPÇÃO B (SEGURA)

import ssl
# import os # Não precisa de 'os' se o caminho for absoluto
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from flasco.settings import settings

print("--- INICIANDO CONFIGURAÇÃO DO BANCO DE DADOS ---")

# Caminho para o certificado
ca_path = '/home/alexandre/FLASCO-Backend/prod-ca-2021.crt'

# Cria o contexto SSL
ssl_context = ssl.create_default_context(cafile=ca_path)

db_connect_args = {
    "ssl": ssl_context,
    "statement_cache_size": 0,
}

# VAMOS IMPRIMIR OS ARGUMENTOS QUE SERÃO USADOS
print(f"Argumentos de conexão (connect_args): {db_connect_args}")

# Passa o contexto SSL para a engine
engine = create_async_engine(
    settings.DATABASE_URL,
    connect_args={
        "ssl": ssl_context,  # <-- CORREÇÃO: PASSE A VARIÁVEL AQUI

    },
)
print("--- ENGINE CRIADA COM SUCESSO ---")

AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_async_session():
    async with AsyncSessionLocal() as db:
        yield db