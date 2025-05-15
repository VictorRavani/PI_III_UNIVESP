from flask import Blueprint, render_template
from mqtt_cliente import mqtt_data

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template("index.html", mensagem=mqtt_data["mensagem"])