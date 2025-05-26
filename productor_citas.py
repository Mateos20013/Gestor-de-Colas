import pika
import json

cita = {
    "paciente": "Tony Chen",
    "fecha": "2025-05-21",
    "hora": "10:00",
    "especialidad": "Medicina General",
    "ubicacion": "Clínica San Rafael"
}

conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()
canal.queue_declare(queue='recordatorios')

mensaje = json.dumps(cita)
canal.basic_publish(exchange='', routing_key='recordatorios', body=mensaje)

print("✅ Recordatorio de cita enviado.")
conexion.close()
