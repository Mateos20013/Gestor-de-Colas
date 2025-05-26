import pika
import json

def callback(ch, method, properties, body):
    cita = json.loads(body)
    print("📅 Recordatorio de cita médica:")
    print(f"👤 Paciente: {cita['paciente']}")
    print(f"📆 Fecha: {cita['fecha']}")
    print(f"⏰ Hora: {cita['hora']}")
    print(f"🏥 Especialidad: {cita['especialidad']}")
    print(f"📍 Lugar: {cita['ubicacion']}\n")

conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()

canal.queue_declare(queue='recordatorios')
canal.basic_consume(queue='recordatorios', on_message_callback=callback, auto_ack=True)

print("🎧 Esperando recordatorios de citas...\n")
canal.start_consuming()
