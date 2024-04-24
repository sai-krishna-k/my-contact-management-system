import tkinter as tk
from tkinter import messagebox
import credentials as cr
import pymysql
from main import Management



class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("940x480")
        self.root.resizable(True, True)

        self.label_username = tk.Label(self.root, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self.root, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        # MySQL database configuration
        self.host = cr.host
        self.user = cr.user
        self.password = cr.password
        self.database = cr.database

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Establish a connection to MySQL
        try:
            connection = pymysql.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )

            cursor = connection.cursor()
            query = "SELECT username, password FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                db_username, db_password = result
                if password == db_password and username == db_username:
                    self.root.destroy()
                    root = tk.Tk()
                    app = Management(root)
                    root.mainloop()
                else:
                    messagebox.showerror("Login failed", "Invalid username or password")
            else:
                messagebox.showerror("Login failed", "Invalid username or password")

        except pymysql.Error as error:
            messagebox.showerror("Database Error", f"Error while connecting to MySQL: {error}")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                if connection.is_connected():
                    cursor.close()
                    connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
