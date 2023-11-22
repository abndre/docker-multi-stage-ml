# Dockerfile
# Estágio 1: Construção
FROM python:3.8 AS builder

# Copiar os arquivos necessários
COPY requirements.txt .
COPY app app
COPY model model

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Estágio 2: Execução
FROM python:3.8-slim

# Copiar a partir do estágio de construção
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /app /app

# Definir o diretório de trabalho para /app
WORKDIR /app

# Expor a porta da aplicação FastAPI
EXPOSE 8000

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]