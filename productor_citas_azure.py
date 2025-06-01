from azure.servicebus import ServiceBusClient, ServiceBusMessage


CONNECTION_STR = ""
QUEUE_NAME = "citas-medicas-queue"

# Crear cliente
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

with servicebus_client:
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        # Envía un mensaje
        message = ServiceBusMessage("¡Hola! Este es un mensaje de prueba")
        sender.send_messages(message)
        print("Mensaje enviado correctamente.")
s