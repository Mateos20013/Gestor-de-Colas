# Gestor de Colas - Recordatorio de Citas Médicas

Este proyecto demuestra el uso de un gestor de colas tanto en local (RabbitMQ) como en la nube (Azure Service Bus) para el envío y recepción de recordatorios de citas médicas.

---

## 📋 ¿Qué hace?

- 📤 Envía mensajes con los datos de una cita (nombre, fecha, hora, especialidad, ubicación) a una cola.
- 📥 Recibe esos mensajes desde una cola para mostrar el recordatorio al usuario.

---

## 📂 Archivos incluidos

| Archivo                   | Descripción                                             |
|---------------------------|---------------------------------------------------------|
| `productor_citas.py`      | Envía recordatorios a RabbitMQ (modo local).            |
| `consumidor_citas.py`     | Escucha y recibe recordatorios desde RabbitMQ.          |
| `productor_citas_azure.py`| Envía recordatorios a una cola de Azure Service Bus.    |
| `consumidor_citas_azure.py`| Escucha y recibe recordatorios desde Azure Service Bus. |
| `config_azure.py`         | Contiene la cadena de conexión y el nombre de la cola para Azure. |

---

## 🌐 Azure Service Bus

Para la versión en la nube, se utilizó un **namespace** llamado `gestioncitas` y una **cola** llamada `citas`, configurados desde el portal de Azure.  
El archivo `config_azure.py` contiene la **cadena de conexión** y el **nombre de la cola**.

---

## 🚀 Tecnologías utilizadas

- Python 3.x
- RabbitMQ
- Azure Service Bus
- Biblioteca `azure-servicebus`

---

## ⚙️ Cómo ejecutar

1️⃣ Configura tu archivo `config_azure.py` con los datos de tu Azure Service Bus:
```python
# config_azure.py
CONNECTION_STR = "Endpoint=sb://<NAMESPACE>.servicebus.windows.net/;SharedAccessKeyName=<POLICY_NAME>;SharedAccessKey=<PRIMARY_KEY>"
QUEUE_NAME = "citas-medicas-queue"
