# Vanika Prints — Full-Stack E-Commerce & Services Website

A complete, working full-stack web application for **Vanika Prints** (sublimation printing +
photography services), built with:

- **Backend:** Python Flask (Blueprints, sessions, secure password hashing)
- **Database:** MySQL (accessed via PyMySQL, manageable through phpMyAdmin/XAMPP)
- **Frontend:** Server-rendered HTML5 templates (Jinja2) + CSS3 + Vanilla JavaScript (no build step)

Every feature listed in the brief — registration/login, product & service browsing, cart,
COD checkout, order tracking, customer↔admin chat, and a full admin dashboard — is wired to
real database tables. There is no static/demo data layer; everything reads and writes to MySQL.

---

## 1. Project Structure

```
vanika_prints/
├── run.py                      # Entry point: `python run.py`
├── create_admin.py             # Interactive script to create your admin login
├── config.py                   # Reads settings from .env
├── .env.example                # Copy to .env and fill in your DB credentials
├── requirements.txt
├── database/
│   └── schema.sql               # Full MySQL schema + seed categories/products/services
└── app/
    ├── __init__.py               # App factory, blueprint registration, error pages
    ├── db.py                     # MySQL connection helper (PyMySQL, dict cursors)
    ├── models.py                 # All data-access functions (raw parameterized SQL)
    ├── auth_utils.py              # @login_required / @admin_login_required decorators
    ├── utils.py                   # Secure image upload helper
    ├── routes/
    │   ├── auth.py                # Customer register / login / logout / profile
    │   ├── customer.py            # Home, product listing/detail, about, contact
    │   ├── cart.py                 # Add / update / remove cart items
    │   ├── orders.py               # Checkout (COD), order history, order detail
    │   ├── services.py             # Service listing, booking inquiries
    │   ├── chat.py                  # Customer chat with admin
    │   └── admin.py                 # Admin auth, products, orders, users, services,
    │                                 inquiries, chat — the whole admin dashboard
    ├── templates/
    │   ├── base.html               # Customer-facing layout (header/nav/footer)
    │   ├── auth/                   # login.html, register.html, profile.html
    │   ├── customer/               # home, products, product_detail, cart, checkout,
    │   │                             orders, order_detail, services, service_detail,
    │   │                             chat, contact, about, my_inquiries
    │   └── admin/
    │       ├── admin_base.html      # Admin layout with sidebar
    │       ├── login.html, dashboard.html
    │       ├── products.html, product_form.html
    │       ├── orders.html, order_detail.html
    │       ├── users.html
    │       ├── services.html, service_form.html
    │       ├── inquiries.html
    │       └── chat_threads.html, chat_detail.html
    └── static/
        ├── css/style.css            # Full responsive design system
        ├── js/main.js                # Cart AJAX, live chat polling, nav toggle, etc.
        └── uploads/                  # Uploaded product/service images land here
```

---

## 2. Windows + XAMPP Setup (step‑by‑step)

These steps assume you are new to the command line — every step is spelled out.

### Step 1 — Install prerequisites

1. Install **XAMPP** (includes MySQL + phpMyAdmin) from https://www.apachefriends.org if you
   don't already have it. During setup, make sure **MySQL** is selected as a component.
2. Install **Python 3.10+** from https://www.python.org/downloads/ — during installation,
   tick the box **"Add Python to PATH"** (important, or the `python` command won't work).

### Step 2 — Start MySQL

1. Open the **XAMPP Control Panel**.
2. Click **Start** next to **MySQL**. Wait until it turns green. You do *not* need to start
   Apache — Flask runs its own web server.

### Step 3 — Create the database

1. In XAMPP Control Panel, click **Admin** next to MySQL (or open
   http://localhost/phpmyadmin in your browser).
2. Click the **SQL** tab at the top.
3. Open the file `database/schema.sql` from this project in a text editor (Notepad is fine),
   copy the entire contents, paste them into the SQL box in phpMyAdmin, and click **Go**.
4. You should now see a new database called **vanika_prints** in the left sidebar, with all
   13 tables (users, admins, categories, products, product_images, services,
   service_inquiries, cart_items, orders, order_items, order_status_history, payments,
   messages) plus sample categories, products, and services already inserted.

### Step 4 — Open a terminal in the project folder

1. Extract/copy this project folder somewhere convenient, e.g. `C:\Projects\vanika_prints`.
2. Open **File Explorer**, navigate into that folder.
3. Click the address bar, type `cmd`, and press **Enter**. A black terminal window opens
   already pointed at this folder. (Alternatively: Start Menu → type "cmd" → Enter, then run
   `cd C:\Projects\vanika_prints`.)

### Step 5 — Create a virtual environment and install dependencies

Type each line below into that terminal, pressing Enter after each one:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

You'll know the virtual environment is active because the line in your terminal will start
with `(venv)`.

### Step 6 — Configure your database connection

1. In the project folder, make a copy of `.env.example` and rename the copy to `.env`
   (in File Explorer: right-click `.env.example` → Copy → Paste → rename to `.env`).
2. Open `.env` in Notepad. The defaults already match a fresh XAMPP install
   (`DB_USER=root`, `DB_PASSWORD=` blank, `DB_HOST=localhost`) — XAMPP's MySQL has no
   root password by default, so usually **you don't need to change anything**.
3. If you did set a root password in XAMPP, put it after `DB_PASSWORD=`.

### Step 7 — Create your admin login

Still in the same terminal (with `(venv)` showing), run:

```
python create_admin.py
```

Follow the prompts to choose an admin username and password. This writes a securely
hashed password into the `admins` table — remember these credentials, you'll use them to
log into the admin dashboard.

### Step 8 — Run the website

```
python run.py
```

You should see output ending with something like:
```
 * Running on http://127.0.0.1:5000
```

Open your browser and go to:

- **Customer site:** http://127.0.0.1:5000/
- **Admin dashboard:** http://127.0.0.1:5000/admin/login (use the username/password you
  created in Step 7)

Leave this terminal window open while you use the site — closing it stops the server.
To stop it manually, click inside the terminal and press `Ctrl + C`.

### Next time you want to run the site

You don't need to repeat every step — just:
1. Start MySQL in the XAMPP Control Panel.
2. Open a terminal in the project folder, run `venv\Scripts\activate`, then `python run.py`.

---

## 3. Managing the database via phpMyAdmin

Because everything is stored in plain MySQL tables (no ORM abstraction), you can freely
inspect or edit data directly in phpMyAdmin (http://localhost/phpmyadmin → `vanika_prints`
database) — e.g. to manually adjust stock, inspect orders, or back up your data via
**Export**.

---

## 4. Feature Checklist

**Customer**
- Register / login (hashed passwords, sessions) ✅
- Browse products by category, search ✅
- Product detail: multiple images, price, stock, description, category, related products ✅
- Add to cart / update quantity / remove ✅
- Checkout with shipping details, Cash on Delivery ✅
- Order history + live order status tracker (Pending → Confirmed → Packed → Out for
  Delivery → Delivered) ✅
- Chat with admin (polling-based live chat) ✅
- Browse & inquire about services (photography, pre-wedding, baby shoot, wedding video
  editing, wedding album design) ✅
- Fully responsive (mobile / tablet / desktop) ✅

**Admin** (`/admin/login`)
- Secure separate admin login/session ✅
- Add / edit / delete products, multi-image upload ✅
- Manage categories, price, stock, description, active/hidden status ✅
- View all registered users, block/unblock accounts ✅
- View & manage all orders, update status with a full audit trail ✅
- View customer + shipping + payment details per order ✅
- Manage services (add/edit/delete, cover image, starting price) ✅
- View & update service booking inquiries ✅
- Chat with any customer ✅
- Dashboard with live stats (users, products, orders, pending orders, revenue, new
  inquiries) ✅

---

## 5. Security notes

- Passwords (both customer and admin) are hashed with Werkzeug's `generate_password_hash`
  (PBKDF2) — never stored in plain text.
- All SQL queries are parameterized (no string-formatted SQL), preventing SQL injection.
- Sessions are server-side Flask sessions with `HttpOnly` + `SameSite=Lax` cookies.
- Uploaded files are renamed to random UUIDs and restricted to image extensions
  (`png/jpg/jpeg/gif/webp`), with a 10MB size cap.
- Admin routes are protected by an `@admin_login_required` decorator, fully separate from
  customer sessions.

## 6. Notes on sample data

The seed data in `database/schema.sql` includes one row per product category with no
placeholder photo attached (to avoid shipping broken stock-photo links) — they'll show a
neutral placeholder graphic on the site until you upload real photos for them via
**Admin → Products → Edit → Add More Images**. Everything else (users, orders, chat,
inquiries) starts empty and fills up naturally as you use the site.
