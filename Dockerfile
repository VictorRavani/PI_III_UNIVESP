# Usa uma imagem leve do Python
FROM python:3.11-slim

# Define diretório de trabalho no container
WORKDIR /app

# Copia o requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia todos os arquivos da aplicação
COPY . .

# Expõe a porta 5000
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "main.py"]
