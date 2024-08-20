import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

def toggle_password():
    if show_password_var.get():
        entryPassword.config(show="")
    else:
        entryPassword.config(show="*")

def add():
    credential_type = entryType.get()
    username = entryName.get()
    password = entryPassword.get()
    
    # Check if all fields are filled
    if credential_type and username and password:
        credentials_exist = False
        
        # Check if the credentials already exist
        try:
            with open("passwords.txt", 'r') as f:
                for k in f:
                    i = k.split(' ')
                    if len(i) == 3 and i[0] == credential_type and i[1] == username:
                        credentials_exist = True
                        break
        except FileNotFoundError:
            pass  # If the file does not exist, we'll create it when adding the new entry
        
        if credentials_exist:
            messagebox.showinfo("Info", "Credentials already saved!")
        else:
            with open("passwords.txt", 'a') as f:
                f.write(f"{credential_type} {username} {password}\n")
            messagebox.showinfo("Success", "Password added successfully!")
    else:
        messagebox.showerror("Error", "Please fill out all fields")


def getlist():
    passwords = []
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                if len(i) == 3:  # Ensure the line has exactly 3 parts
                    passwords.append((i[0], i[1], i[2].strip()))
    except FileNotFoundError:
        messagebox.showerror("Error", "No passwords found!")
        return

    # Create a new window for displaying the list in a table
    table_window = tk.Toplevel(app)
    table_window.title("List of Passwords")
    table_window.geometry("550x350")

    # Create a Treeview widget with columns for sequence, type, username, and password
    tree = ttk.Treeview(table_window, columns=("Seq", "Type", "Username", "Password"), show="headings", height=10)
    
    # Configure the columns
    tree.column("Seq", anchor="center", width=50)  # Column for sequence numbers
    tree.column("Type", anchor="center", width=150)
    tree.column("Username", anchor="center", width=150)
    tree.column("Password", anchor="center", width=150)
    
    # Set column headings
    tree.heading("Seq", text="No.")
    tree.heading("Type", text="Credential Type")
    tree.heading("Username", text="Username")
    tree.heading("Password", text="Password")

    # Insert the passwords into the Treeview with sequence numbers
    for idx, password in enumerate(passwords, start=1):
        tree.insert("", "end", values=(idx, password[0], password[1], password[2]))

    # Add a scrollbar to the Treeview
    scrollbar = ttk.Scrollbar(table_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # Layout the Treeview and scrollbar
    tree.pack(side="left", fill=tk.BOTH, expand=True, padx=10, pady=10)
    scrollbar.pack(side="right", fill="y")


def get():
    credential_type = entryType.get()
    username = entryName.get()
    passwords = {}
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                if len(i) == 3:  # Ensure the line has exactly 3 parts
                    passwords[(i[0], i[1])] = i[2].strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "No passwords found!")

    if passwords:
        mess = "Your passwords:\n"
        for (ctype, user), pwd in passwords.items():
            if ctype == credential_type and user == username:
                mess += f"{ctype} - {username}: {pwd}\n"
                break
        else:
            mess += "No Such Username Exists !!"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "EMPTY LIST!!")

def delete():
    credential_type = entryType.get()
    username = entryName.get()
    temp_passwords = []
    deleted = False

    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                if len(i) == 3 and (i[0] != credential_type or i[1] != username):
                    temp_passwords.append(f"{i[0]} {i[1]} {i[2].strip()}")
                elif len(i) == 3:
                    deleted = True

        with open("passwords.txt", 'w') as f:
            for line in temp_passwords:
                f.write(f"{line}\n")

        if deleted:
            messagebox.showinfo("Success", f"Credentials for {username} deleted successfully!")
        else:
            messagebox.showerror("Error", f"No credentials found for {username}!")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting credentials for {username}: {e}")

def update():
    credential_type = entryType.get()
    username = entryName.get()
    new_password = entryPassword.get()
    temp_passwords = []
    user_exists = False

    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                if len(i) == 3:
                    if i[0] == credential_type and i[1] == username:
                        temp_passwords.append(f"{credential_type} {username} {new_password}")
                        user_exists = True
                    else:
                        temp_passwords.append(f"{i[0]} {i[1]} {i[2].strip()}")

        if user_exists:
            with open("passwords.txt", 'w') as f:
                for line in temp_passwords:
                    f.write(f"{line}\n")
            messagebox.showinfo("Success", f"Password for {username} updated successfully!")
        else:
            messagebox.showerror("Error", f"No credentials found for {username}!")
    except Exception as e:
        messagebox.showerror("Error", f"Error updating password for {username}: {e}")

if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("560x350")
    app.title("Secured Password Manager")
    
    # Load the background image
    background_image = Image.open("c:/Users/Ishan/Downloads/cyber-security.jpg")  # Replace with your image path
    background_image = background_image.resize((560, 370), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(background_image)

    # Create a label to hold the background image
    background_label = tk.Label(app, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Configure grid for centering
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure(2, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(2, weight=1)
    app.grid_rowconfigure(3, weight=1)
    app.grid_rowconfigure(4, weight=1)
    app.grid_rowconfigure(5, weight=1)
    app.grid_rowconfigure(6, weight=1)
    app.grid_rowconfigure(7, weight=1)

    # Common styles
    font_style = ('Arial', 10)

    # Credential Type block
    labelType = tk.Label(app, text="CREDENTIAL TYPE:", bg='#ffffff', font=font_style)
    labelType.grid(row=0, column=0, padx=15, pady=15, sticky="e")
    entryType = tk.Entry(app, font=font_style)
    entryType.grid(row=0, column=1, padx=15, pady=15)

    # Username block
    labelName = tk.Label(app, text="USERNAME:", bg='#ffffff', font=font_style)
    labelName.grid(row=1, column=0, padx=15, pady=15, sticky="e")
    entryName = tk.Entry(app, font=font_style)
    entryName.grid(row=1, column=1, padx=15, pady=15)

    # Password block with masking
    labelPassword = tk.Label(app, text="PASSWORD:", bg='#ffffff', font=font_style)
    labelPassword.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entryPassword = tk.Entry(app, show="*", font=font_style)
    entryPassword.grid(row=2, column=1, padx=10, pady=5)

    # Show Password checkbox
    show_password_var = tk.BooleanVar()
    show_password_checkbox = tk.Checkbutton(app, text="Show Password", variable=show_password_var, command=toggle_password)
    show_password_checkbox.grid(row=2, column=2, padx=10, pady=5)

    # Button styles
    button_style = {'bg': '#ffffff', 'fg': '#000000', 'font': font_style}

    # Add button
    buttonAdd = tk.Button(app, text="Add", command=add, **button_style)
    buttonAdd.grid(row=3, column=1, padx=15, pady=8, sticky="we")

    # Get button
    buttonGet = tk.Button(app, text="Get", command=get, **button_style)
    buttonGet.grid(row=4, column=1, padx=15, pady=8, sticky="we")

    # List Button
    buttonList = tk.Button(app, text="List", command=getlist, **button_style)
    buttonList.grid(row=5, column=1, padx=15, pady=8, sticky="we")

    # Delete button
    buttonDelete = tk.Button(app, text="Delete", command=delete, **button_style)
    buttonDelete.grid(row=6, column=1, padx=15, pady=8, sticky="we")

    # Update button
    buttonUpdate = tk.Button(app, text="Update Password", command=update, **button_style)
    buttonUpdate.grid(row=7, column=1, padx=15, pady=8, sticky="we")

    app.mainloop()
