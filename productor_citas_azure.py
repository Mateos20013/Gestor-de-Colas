# productor_citas_azure.py

from azure.servicebus import ServiceBusClient, ServiceBusMessage
import json
from datetime import datetime
import config_azure  # Importamos la configuración

# Función para crear un mensaje de cita
def crear_mensaje_cita():
    cita = {
        "paciente": "Juan Perez",
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "doctor": "Dra. López",
        "motivo": "Chequeo general"
    }
    return json.dumps(cita)

# Función para enviar el mensaje
def enviar_mensaje(mensaje):
    with ServiceBusClient.from_connection_string(conn_str=config_azure.CONNECTION_STR, logging_enable=True) as client:
        sender = client.get_queue_sender(queue_name=config_azure.QUEUE_NAME)
        with sender:
            servicebus_message = ServiceBusMessage(mensaje)
            sender.send_messages(servicebus_message)
            print("✅ Mensaje enviado a Azure Service Bus.")

if __name__ == "__main__":
    mensaje = crear_mensaje_cita()
    print("📤 Enviando mensaje:", mensaje)
    enviar_mensaje(mensaje)
