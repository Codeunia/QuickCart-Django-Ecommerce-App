# 🛒 QuickCart – Django E-commerce App

A beginner-friendly eCommerce platform built with Django. This project helps you learn core concepts of Django such as views, models, templates, routing, and user sessions by simulating an online shopping experience.

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

QuickCart-Django-Ecommerce-App/
│
├── quickcart/ # Main Django project
├── store/ # App with views, models, urls
├── templates/ # HTML templates
├── static/ # CSS, JS, Images
├── .env # Secret key and settings (not tracked)
├── manage.py
└── requirements.txt

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/cybernova2/QuickCart-Django-Ecommerce-App.git
cd QuickCart-Django-Ecommerce-App
2. Create and Activate Virtual Environment
bash
Copy code
python -m venv myenv
myenv\Scripts\activate       # For Windows
# OR
source myenv/bin/activate    # For Mac/Linux
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the root of the project and add:

ini
Copy code
SECRET_KEY=your-django-secret-key-here
DEBUG=True
Update your settings.py like this:

python
Copy code
from decouple import config

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)
5. Apply Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
6. Create a Superuser
bash
Copy code
python manage.py createsuperuser
Follow the prompts to set up the admin user.

7. Run the Server
bash
Copy code
python manage.py runserver
Visit: http://127.0.0.1:8000

🔐 Admin Panel
Access: http://127.0.0.1:8000/admin

Make sure to register all models in store/admin.py:

python
Copy code
from .models import Product, Customer, Order

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
👨‍💻 Contributor
cybernova2