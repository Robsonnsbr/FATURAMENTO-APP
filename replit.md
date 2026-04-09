# Telos Consultoria - Sistema de Gestão

## Visão Geral
Backend FastAPI + SQLAlchemy para gestão de clientes, faturamento RH, relatórios e integrações com sistemas externos (Senior, MSSQL).

## Arquitetura

- **Backend**: FastAPI (Python 3.11) + SQLAlchemy ORM
- **Banco de Dados**: PostgreSQL gerenciado pelo Replit (via DATABASE_URL)
- **Templates**: Jinja2
- **Autenticação**: Token-based com sessão em memória

## Estrutura do Projeto

```
app/
├── main.py              # Ponto de entrada FastAPI
├── db.py                # Configuração SQLAlchemy
├── config.py            # Variáveis de configuração
├── session_manager.py   # Gerenciamento de sessões
├── models/              # Modelos SQLAlchemy
├── routers/             # Rotas da API
├── services/            # Lógica de negócio
├── templates/           # Templates Jinja2 HTML
└── static/              # Arquivos estáticos
```

## Banco de Dados

- **Tipo**: PostgreSQL gerenciado pelo Replit
- **DATABASE_URL**: Definido automaticamente como variável de ambiente
- O dump inicial (`dump.sql`) foi importado com todos os dados

## Workflow

- **Nome**: `Start application`
- **Comando**: `uvicorn app.main:app --host 0.0.0.0 --port 5000 --proxy-headers --forwarded-allow-ips='*'`
- **Porta**: 5000

## Credenciais Padrão

- **Email**: `ti@grupoopus.com`
- **Senha**: `telos@2026`

## Variáveis de Ambiente

- `DATABASE_URL` — URL de conexão com banco PostgreSQL (gerenciado pelo Replit)
- `DOMAIN_API` — Domínio da API Senior (opcional)
- `API_KEY` — Chave API Senior (opcional)
- `MSSQL_HOST`, `MSSQL_PORT`, `MSSQL_DB`, `MSSQL_USER`, `MSSQL_PASS` — Conexão MSSQL (opcional)

## Dependências Principais

Ver `requirements.txt`:
- fastapi, uvicorn, sqlalchemy, psycopg2-binary, jinja2, pandas, openpyxl, passlib, python-dotenv, pydantic
