from azure.servicebus import ServiceBusClient
import config_azure
import json

def recibir_mensajes(max_mensajes=10):
    with ServiceBusClient.from_connection_string(conn_str=config_azure.CONNECTION_STR, logging_enable=True) as client:
        receiver = client.get_queue_receiver(queue_name=config_azure.QUEUE_NAME, max_wait_time=5)

        with receiver:
            print("🎧 Esperando mensajes...")
            for mensaje in receiver.receive_messages(max_message_count=max_mensajes, max_wait_time=10):
                try:
                    # Reconstruye el cuerpo del mensaje
                    mensaje_body = b"".join([b for b in mensaje.body])
                    datos = json.loads(mensaje_body.decode("utf-8"))  # Decodificar JSON
                    print(f"✅ Mensaje recibido: {datos}")
                except Exception as e:
                    print(f"⚠️ Error al procesar mensaje: {mensaje}")
                
                # Confirmar la lectura del mensaje
                receiver.complete_message(mensaje)
            print("📥 Lectura finalizada.")

if __name__ == "__main__":
    recibir_mensajes()
