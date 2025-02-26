# Newsletter (Django, PostgreSQL, Celery)

🚀 A **small microservice Newsletter** built with Django, PostgreSQL, and Celery.

## 🌟 Features

✅ Sends bulk email to all subscribers.
✅ Admin creates post that is sent as email to all users.  
✅ Sending email is done in background via celery.

---

## 📌 Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Background Tasks:** Celery + Redis (message broker)
- **Web Server:** Gunicorn

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Pradhansumit/Newsletter.git
cd Newsletter
```

### 2️⃣ Create & Configure Environment Variables

Create a `.env` file in the root directory:

```ini
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=*
DATABASE_URL=postgres://myuser:password@pgdb:5432/newsletter

EMAIL_HOST = email_host
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = your gmail address
EMAIL_HOST_PASSWORD = gmail password
```

## 📡 API Endpoints

### ️Subscribe to newsletter

**Request:**

```http
POST /api/subscribe/
Content-Type: application/json
{
    "email": "xyz@example.com"
}
```

## 🛠 Running Celery Worker

Celery handles background jobs (e.g., tracking click analytics).  
Start the worker manually if needed:

```bash
celery -A config.celery worker -l INFO
```

---
