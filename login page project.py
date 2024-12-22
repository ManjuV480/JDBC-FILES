from tkinter import *
import tkinter.messagebox as msg
import mysql.connector
import re

root = Tk()
root.geometry("400x400")
root.title("Registration Form")
root.config(bg="cadetblue")

def register_data():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    # Basic input validation
    if not username or not password or not email:
        msg.showerror("Input Error", "All fields are required!")
        return
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        msg.showerror("Input Error", "Invalid email format!")
        return

    try:
        mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='Manju', database='register_db')
        mycursor = mydb.cursor()

        mycursor.execute("INSERT INTO registration (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        mydb.commit()
        
        msg.showinfo("Registration", "Registration Successful")
    
    except mysql.connector.Error as err:
        msg.showerror("Database Error", f"Error: {err}")
    
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

username_label = Label(root, text="Username:", bg="cadetblue", font=('bold', 20))
username_label.place(x=20, y=50)

password_label = Label(root, text="Password:", bg="cadetblue", font=('bold', 20))
password_label.place(x=20, y=150)

email_label = Label(root, text="Email:", bg="cadetblue", font=('bold', 20))
email_label.place(x=20, y=250)

username_entry = Entry()
username_entry.place(x=180, y=50)

password_entry = Entry(show='*')  # Mask password input
password_entry.place(x=180, y=150)

email_entry = Entry()
email_entry.place(x=180, y=250)

register_button = Button(root, text="Register", command=register_data)
register_button.place(x=150, y=300)

root.mainloop()
