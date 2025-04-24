# Flasco-Backend

## Índice

- [Instalação](#instalação)
- [Execução](#execução)

## Instalação

### Clonando o Repositório

```bash
git clone git@github.com:DevPills/FLASCO-Backend.git
```

## Execução

### Buildando e Iniciando os Contêineres

Para construir as imagens Docker e iniciar a aplicação localmente, execute:
```bash
docker compose -f docker-compose.local.yaml up -d
```

### Acessando a aplicação

Após inicializar, a aplicação estará disponível em:
- API: [localhost:8000](http://localhost:8000)
- Swagger: [localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [localhost:8000/redoc](http://localhost:8000/redoc)