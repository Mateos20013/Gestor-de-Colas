# Gestor de Colas - Recordatorio de Citas Médicas

Este proyecto demuestra el uso de un gestor de colas tanto en local (RabbitMQ) como en la nube (Azure Service Bus) para el envío y recepción de recordatorios de citas médicas.

## 🔄 ¿Qué hace?

- Envía mensajes con los datos de una cita (nombre, fecha, hora, especialidad, ubicación).
- Recibe esos mensajes desde una cola para mostrar el recordatorio al usuario.

## 🖥️ Archivos incluidos

| Archivo                      | Descripción                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| productor_citas.py          | Envía recordatorios a RabbitMQ (modo local).                               |
| consumidor_citas.py         | Escucha y recibe recordatorios desde RabbitMQ.                             |
| productor_citas_azure.py    | Envía recordatorios a una cola de Azure Service Bus.                       |
| consumidor_citas_azure.py   | Escucha y recibe recordatorios desde Azure Service Bus.                    |

## ☁️ Azure Service Bus

Para la versión en la nube se utilizó un namespace llamado `gestioncitas` y una cola llamada `citas`, configurados desde Azure Portal.

## 🚀 Tecnologías utilizadas

- Python 3.x
- RabbitMQ
- Azure Service Bus
- Biblioteca azure-servicebus

## 📌 Notas

Este proyecto es parte de una práctica académica sobre gestores de colas. Fue subido a GitHub como entrega final.

---

© 2025 Mateo Sotomayor
