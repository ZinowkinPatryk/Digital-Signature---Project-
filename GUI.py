import tkinter as tk
from tkinter import filedialog, ttk
import os

file_paths = {
    "document": None,
    "hash": None,
    "public_key": None
}
#Metoda w ktorej bedziemy okreslac co ma sie dziac po kliknieciu podpis lub weryfikacja
def execute_action(action):
    if action == "Podpis":
        print("Podpisuje")
    elif action == "Weryfikacja":
        print("Weryfikacja")
#Metoda ktora aktualizuje wyglad ui po zmianie akcji
def update_ui(event=None):
    for button in options_frame.winfo_children():
        button.destroy()
    for key in file_paths:
        file_paths[key] = None
    action = action_var.get()
    file_format = file_format_var.get()
    if file_format == "PDF":
        doc_extension = [("Pliki PDF", "*pdf")]
    else:
        doc_extension = [("Pliki txt", "*txt")]
    if action == "Weryfikacja":
        if file_format == "TXT":
            create_picker("hash", "Wybierz plik hasza", [("Pliki tekstowe", "*.txt")])
            create_picker("document", "Wybierz dokument oryginalny", doc_extension)
            create_picker("public_key", "Wybierz klucz publiczny",[("Klucze PEM", "*.pem")])


        else:
            create_picker("document", "Wybierz dokument oryginalny", doc_extension)
            create_picker("public_key", "Wybierz klucz publiczny",
                          [("Klucze PEM", "*.pem")])
        create_button(action, action)

    elif action == "Podpis":
        create_picker("document", "Wybierz dokument oryginalny", doc_extension)
        create_button(action, action)


#Tworzenie pary - przycisk i label
def create_picker(key, button_text, file_type):
    row_frame = tk.Frame(options_frame, bg="#212121")
    row_frame.pack(pady=10, fill="x")
    label = tk.Label(row_frame, text="Nie wybrano pliku", bg="#2B6CB0", fg="#DFE6E9", width=30)
    label.pack(side="right", padx=10)
    btn = tk.Button(row_frame, text=button_text, bg="#2B6CB0", fg="#DFE6E9", width=30,
                    command=lambda k=key, l=label, f=file_type: pick_file(k, l, f))
    btn.pack(side="left", padx=10)
#Tworzenie przycisku button_text to tekst wyswietlajacy sie na przycisku,
#a action to akcja jaka bedzie wykonywal w execute action beda metody podpisywania i weryfikacji dokumentu
def create_button(button_text, action):
    row_frame = tk.Frame(options_frame, bg="#212121")
    row_frame.pack(pady=10, fill="x")
    btn = tk.Button(row_frame, text=button_text, bg="#2B6CB0", fg="#DFE6E9", width=40,
                    command=lambda: execute_action(action))
    btn.pack()
#Funkcja, pozwalajaca wybrac plik
def get_file_path(file_type):
    file_path = filedialog.askopenfilename(filetypes=file_type)
    return file_path
def get_file_name(file_path ):
        file_name = os.path.basename(file_path)
        return file_name
def pick_file(key, button, file_type):
    path= get_file_path(file_type)
    if path:
        file_name = get_file_name(path)
        file_paths[key] = path
        button.config(text=file_name)





#Tworzenie okna głównego aplikacji
root = tk.Tk()
root.title("Digital-Signature")
root.resizable(False, False)
root.geometry("720x540")
root.configure(bg="#212121")

#Frame dla sekcji wyboru formatu oraz akcji
top_frame = tk.Frame(root, bg="#212121")
top_frame.place(x=360, y=80, anchor="center")

#Dropbox dla Akcji
action_var = tk.StringVar(value="Podpis")
action_label = tk.Label(top_frame, text="Wybierz działanie:", bg="#212121", fg="#DFE6E9")
action_label.grid(row=0, column=0, padx=20, pady=5)
action_combo = ttk.Combobox(top_frame, textvariable=action_var, values=["Podpis", "Weryfikacja"], state="readonly")
action_combo.grid(row=1, column=0, padx=20)
action_combo.bind("<<ComboboxSelected>>", update_ui) # Nasłuchiwanie zmian

#Dropbox dla Formatu
file_format_var = tk.StringVar(value="TXT")
format_label = tk.Label(top_frame, text="Wybierz format:", bg="#212121", fg="#DFE6E9")
format_label.grid(row=0, column=1, padx=20, pady=5)
format_combo = ttk.Combobox(top_frame, textvariable=file_format_var, values=["TXT", "PDF"], state="readonly")
format_combo.grid(row=1, column=1, padx=20)
format_combo.bind("<<ComboboxSelected>>", update_ui) # Nasłuchiwanie zmian

#Sekcja gdzie pojawiaja sie przyciski
# Ramka, w której będą pojawiać się przyciski
options_frame = tk.Frame(root, bg="#212121")
options_frame.place(x=360, y=280, anchor="center")

#Pierwsze zaladowanie przyciskow, bez tego trzeba wybrac recznie dzialanie lub format aby sie cos pojawilo
update_ui()

# Odpalenie pętli głównej
root.mainloop()

