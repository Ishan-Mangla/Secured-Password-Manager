**Secured Password Manager**
This is a simple graphical user interface (GUI) application built using Python's Tkinter library.
The application acts as a password manager, allowing users to securely store, retrieve, update, and delete credentials.
It uses a text file to store credentials locally.

**Features**
1. Add Credentials: Users can store new credentials (credential type, username, and password) in the local storage.
2. Show Password: A checkbox to toggle the visibility of the password field.
3. Retrieve Credentials: Users can retrieve and view specific credentials based on the credential type and username.
4. List All Credentials: Displays all stored credentials in a table format in a new window.
5. Update Credentials: Users can update the password for existing credentials.
6. Delete Credentials: Users can delete specific credentials from the local storage.
   
**Project Structure**
-> passwords.txt: A text file used to store the credentials in the format credential_type username password.
-> Main Script: The script creates a Tkinter window with various buttons and entry fields for managing credentials.
**How to Use**

Step 1 - Run the Application: Execute the Python script to open the GUI.
Step 2 - Add a Credential: Enter the credential type, username, and password, then click the "Add" button.

**View Credentials:**
-> To retrieve a specific credential, enter the credential type and username, then click "Get".
-> To list all credentials, click the "List" button.
-> Update a Credential: Enter the credential type, username, and new password, then click "Update Password".
-> Delete a Credential: Enter the credential type and username, then click "Delete".

**Dependencies**
-> Python 3.x
-> Tkinter (included with Python standard library)
-> PIL (Pillow): Used for handling and displaying images. Install via pip install pillow.

**Notes**
1. The application stores credentials in plain text in passwords.txt. This is for educational purposes only and is not secure for storing sensitive data.
2. The background image should be placed in the specified path, or the path can be updated in the script.


