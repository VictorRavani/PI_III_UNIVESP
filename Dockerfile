# Usa uma imagem leve do Python
FROM python:3.11-slim

# Define diretório de trabalho no container
WORKDIR /app

# Atualiza e instala o cliente do PostgreSQL para ter pg_isready
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Copia o requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia todos os arquivos da aplicação
COPY . .

# Deixa o script executável
RUN chmod +x wait-for-postgres.sh

# Expõe a porta 5000
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "main.py"]

