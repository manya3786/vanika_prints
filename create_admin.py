"""
Run this once after setting up the database to create your admin login.

Usage (from the project root, with your virtual environment active):

    python create_admin.py

It will ask for a username and password and insert the admin securely
(password hashed with Werkzeug) into the `admins` table.
"""
import getpass
from app import create_app
from app import models


def main():
    app = create_app()
    with app.app_context():
        print("=== Create Vanika Prints Admin Account ===")
        username = input("Choose an admin username: ").strip()

        existing = models.get_admin_by_username(username)
        if existing:
            print(f"An admin with username '{username}' already exists.")
            return

        full_name = input("Admin full name (optional): ").strip() or None
        password = getpass.getpass("Choose a password (min 6 characters): ")
        confirm = getpass.getpass("Confirm password: ")

        if len(password) < 6:
            print("Password too short. Please run the script again.")
            return
        if password != confirm:
            print("Passwords did not match. Please run the script again.")
            return

        models.create_admin(username, password, full_name)
        print(f"\nAdmin account '{username}' created successfully!")
        print("You can now log in at http://127.0.0.1:5000/admin/login")


if __name__ == '__main__':
    main()
