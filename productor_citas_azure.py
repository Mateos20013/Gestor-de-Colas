from azure.servicebus import ServiceBusClient, ServiceBusMessage
import json
from datetime import datetime
import config_azure

# Función para crear un mensaje de cita con un ID único
def crear_mensaje_cita(numero):
    cita = {
        "paciente": f"Paciente {numero}",
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "doctor": f"Doctor {numero}",
        "motivo": "Chequeo general"
    }
    return json.dumps(cita)

# Función para enviar múltiples mensajes
def enviar_mensajes(cantidad):
    with ServiceBusClient.from_connection_string(conn_str=config_azure.CONNECTION_STR, logging_enable=True) as client:
        sender = client.get_queue_sender(queue_name=config_azure.QUEUE_NAME)
        with sender:
            for i in range(1, cantidad + 1):
                mensaje_contenido = crear_mensaje_cita(i)
                servicebus_message = ServiceBusMessage(mensaje_contenido)
                sender.send_messages(servicebus_message)
                print(f"✅ Mensaje {i} enviado: {mensaje_contenido}")

if __name__ == "__main__":
    enviar_mensajes(10)  # Envía 10 mensajes
