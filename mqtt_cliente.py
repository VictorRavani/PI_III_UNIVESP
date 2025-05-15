import paho.mqtt.client as mqtt
import threading

mqtt_data = {"mensagem": "Aguardando mensagens..."}

def on_connect(client, userdata, flags, rc):
    print("Conectado ao MQTT com código:", rc)
    client.subscribe("univesp/Pi3")

def on_message(client, userdata, msg):
    print(f"Mensagem recebida: {msg.payload.decode()}")
    mqtt_data["mensagem"] = msg.payload.decode()

def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("broker.emqx.io", 1883, 60)

    thread = threading.Thread(target=client.loop_forever)
    thread.daemon = True
    thread.start()
