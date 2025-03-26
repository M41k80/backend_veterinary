
# Veterinary Clinic Backend

Este es el backend de la plataforma para la gestión de una clínica veterinaria. Está desarrollado con Django REST Framework (DRF) y proporciona una API para gestionar citas, usuarios, veterinarios, pagos y un sistema de inventario de productos y venta de los mismos.

This is the backend of the platform for managing a veterinary clinic. It's developed with the Django REST Framework (DRF) and provides an API for managing appointments, users, veterinarians, payments, and a product inventory and sales system.

## 🚀 Características principales

📅 Gestión de citas: Dueños de mascotas pueden agendar, modificar y cancelar citas.
Appointment Management: Pet owners can schedule, modify, and cancel appointments.

👨‍⚕️ Gestión de veterinarios: Administración de horarios y disponibilidad.
Veterinary Management: Managing schedules and availability.

📩 Mensajería: Comunicación entre veterinarios y dueños de mascotas.
Messaging: Communication between veterinarians and pet owners.

📊 Dashboard de estadísticas: Reportes y análisis en tiempo real.
Statistics Dashboard: Real-time reporting and analysis.

🛒 Tienda: Venta de productos y servicios veterinarios.
Store: Sale of veterinary products and services.

🔔 Notificaciones: Alertas para citas, mensajes y vencimiento de vacunas.
Notifications: Alerts for appointments, messages, and vaccine expiration dates.

💳 Pagos: Integración con Stripe para pagos en línea.
Payments: Stripe integration for online payments.

🔥 Notificaciones Push: Soporte para Firebase Cloud Messaging (FCM).
Push Notifications: Support for Firebase Cloud Messaging (FCM).

⚡ Tareas en segundo plano: Celery con Redis para ejecución de tareas programadas.
Background Tasks: Celery with Redis for scheduled task execution.

## 🏗️ Tecnologías utilizadas

Backend: Django REST Framework (DRF)

Base de Datos: SQLite (en desarrollo), PostgreSQL (producción)

Autenticación: JSON Web Tokens (JWT)

Mensajería en tiempo real: Django Channels con Redis

Cola de tareas: Celery + Redis

Notificaciones Push: Firebase Cloud Messaging (FCM)

Pagos: Stripe

Documentación: Swagger (drf-yasg)

Despliegue: Railway / Heroku


## 📂 Estructura del proyecto

backend_veterinary/

│── apps/

│   ├── appointments/   # Gestión de citas

│   ├── store/          # Tienda de productos y servicios

│   ├── users/          # Gestión de usuarios y roles

│   ├── schedules/      # Horarios de los veterinarios

│   ├── communications/ # Mensajería interna

|   |__ dashboard/      # Admin Dashboard

|   |__ pets/           # Mascotas          

│   ├── medicalRecord/  # Historial médico de mascotas

│   ├── reviews/        # Valoraciones de veterinarios

│   ├── notifications/  # Sistema de notificaciones

|   |__ services/       # Servicios de la Clinica

│── config/             # Configuración del proyecto

│── requirements.txt    # Dependencias del proyecto

│── README.md           # Documentación


## 🔧 Instalación y configuración

 1️⃣ Clonar el repositorio
 1️⃣ Clonar el repositorio

git clone https://github.com/M41k80/backend_veterinary.git

cd backend_veterinary

2️⃣ Crear y activar un entorno virtual

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3️⃣ Instalar dependencias

pip install -r requirements.txt

4️⃣ Configurar variables de entorno

Crea un archivo .env en la raíz del proyecto y agrega tus credenciales:

SECRET_KEY='tu_secreto'
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # Cambiar a PostgreSQL en producción
STRIPE_SECRET_KEY='tu_stripe_secret'
STRIPE_PUBLIC_KEY='tu_stripe_public'
EMAIL_HOST_USER='tu_email'
EMAIL_HOST_PASSWORD='tu_password'
CELERY_BROKER_URL='redis://localhost:6379/0'
CELERY_RESULT_BACKEND='redis://localhost:6379/0'
FCM_API_KEY='tu_fcm_api_key'

5️⃣ Aplicar migraciones y correr el servidor

python manage.py migrate
python manage.py runserver

## 📖 Documentación de la API

Para acceder a la documentación de la API generada con Swagger, inicia el servidor y accede a:

http://localhost:8000/swagger/

⚙️ Configuración avanzada

🔔 Notificaciones Push (FCM)

Este backend utiliza Firebase Cloud Messaging (FCM) para notificaciones push. Asegúrate de configurar la API Key en el archivo .env.

PUSH_NOTIFICATIONS_SETTINGS = {
    "FCM_API_KEY": os.getenv('FCM_API_KEY'),
    "FCM_ERROR_TIMEOUT": 10,
}

⏳ Tareas en segundo plano con Celery

Celery se usa para manejar tareas en segundo plano, como recordatorios de citas y vencimiento de vacunas.

Ejecuta el worker de Celery:

celery -A config worker --loglevel=info

Ejecuta el scheduler de Celery Beat:

celery -A config beat --loglevel=info

📧 Configuración de correo SMTP

El backend utiliza un servidor SMTP para enviar notificaciones por correo.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

🚀 Despliegue

El proyecto puede ser desplegado en Railway o Heroku.

Ejemplo de configuración en Railway:

railway init
railway add database postgresql
railway up

## 🛠️ Contribuir

Si deseas contribuir a este proyecto, puedes hacer un fork y enviar un pull request con tus mejoras. ¡Toda ayuda es bienvenida! 🚀


## 📞 Contacto

Si tienes dudas o sugerencias, contáctame en:
m41k80@icloud.com 

@m41k80mp Instagram.
