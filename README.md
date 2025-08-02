# 🛒 QuickCart – Django E-commerce App

A beginner-friendly eCommerce platform built with Django. This project helps you learn core Django concepts such as views, models, templates, routing, and user sessions by simulating an online shopping experience.

---

## 📌 Features

- 🏠 Home Page with product listings  
- 🔍 Product detail view  
- ➕ Add to cart / 🗑 Remove from cart  
- 💰 Checkout simulation (no payment gateway)  
- 🔐 Admin panel to manage products  
- 🎨 Basic frontend using HTML & CSS  

---

## 🛠 Tech Stack

- **Backend:** Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite (Django default)

---

## 📁 Project Structure

```
QuickCart-Django-Ecommerce-App/
│
├── quickcart/             # Main Django project
├── store/                 # Store app (views, models, urls)
├── templates/             # HTML templates
├── static/                # CSS, JS, Images
├── .env                   # Secret key and config (not tracked)
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/cybernova2/QuickCart-Django-Ecommerce-App.git
cd QuickCart-Django-Ecommerce-App
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate       # On Windows
# OR
source myenv/bin/activate    # On Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root and add:

```
SECRET_KEY=your-django-secret-key-here
DEBUG=True
```

Update `settings.py` like this:

```python
from decouple import config

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Admin Panel

Access: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Make sure to register all models (e.g., Product, Customer, Order) in `store/admin.py` to manage them from the admin panel.

---

## 🧪 Testing

To test functionality:

- Add products using the admin panel.
- Try adding/removing items from cart.
- Check cart total and checkout flow.

---

## 👨‍💻 Contributor

- [cybernova2](https://github.com/cybernova2)

---

