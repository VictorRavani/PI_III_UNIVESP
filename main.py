from flask import Flask
from configuration import configure_all
from dotenv import load_dotenv
from mqtt_cliente import start_mqtt
import os

load_dotenv()  # carrega variáveis do .env para o ambiente

#inicializacao
app = Flask(__name__)

configure_all(app)

start_mqtt() 

#execucao
app.run(debug=True)
