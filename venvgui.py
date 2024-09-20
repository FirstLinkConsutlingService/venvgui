import subprocess
import tkinter as tk
from tkinter import messagebox

def list_envs():
    env_list = subprocess.check_output(['conda', 'env', 'list']).decode('utf-8')
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, env_list)

def create_env():
    env_name = env_entry.get()
    if env_name:
        subprocess.run(['conda', 'create', '--name', env_name, '-y'])
        messagebox.showinfo("Success", f"Environment '{env_name}' created successfully!")
        list_envs()
    else:
        messagebox.showerror("Error", "Please enter an environment name.")

app = tk.Tk()
app.title("Conda Environment Manager")

tk.Label(app, text="New Environment Name:").pack(pady=5)
env_entry = tk.Entry(app)
env_entry.pack(pady=5)

tk.Button(app, text="Create Environment", command=create_env).pack(pady=10)

tk.Button(app, text="List Environments", command=list_envs).pack(pady=5)

text_box = tk.Text(app, height=10, width=50)
text_box.pack(pady=10)

list_envs()

app.mainloop()


