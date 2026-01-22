# SIMPLE-ORDER-API


A basic Django REST API to create orders.

---

## Quick Start

### 1. Install Dependencies
```bash
pip install django djangorestframework
```

### 2. Initialize Database
```bash
python manage.py migrate
```

### 3. Run Server
```bash
python manage.py runserver
```

---

## How to Use (API Endpoint)

**Endpoint**
```
POST http://127.0.0.1:8000/order/
```

**Headers**
```
Content-Type: application/json
```

**Payload**
```json
{
  "customer": 1,
  "product": 1,
  "quantity": 5
}
```

> ⚠️ Ensure Customer (ID 1) and Product (ID 1) exist in the database.
