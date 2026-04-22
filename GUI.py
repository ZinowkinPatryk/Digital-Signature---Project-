import tkinter as tk
from tkinter import filedialog
import os
import re

#Funkcja, pozwalajaca wybrac plik
def get_file_path():
    file_path = filedialog.askopenfilename(filetypes=[("Pliki tekstowe","*.txt")])
    return file_path
def get_file_name(file_path):
    if file_path:
        file_name = file_path.os.path.basename(file_path)
        file_label.configure(text = file_name)
def pick_file():
    file_path= get_file_path()
    get_file_name(file_path)



#Tworzenie okna głównego aplikacji
root = tk.Tk()
root.title("Digital-Signature")
#Blokada powieksziania okna
root.resizable(False, False)
#Ustawienie wielkosci okna
root.geometry("720x540")
#Ustawienie koloru okna
root.configure(bg="#212121")
#Tworzenie przycisku do wybrania dokumentu
button_pick_document = tk.Button(root, text="Wybierz dokument do podpisania",bg="#2B6CB0",fg="#DFE6E9",command = pick_file)
#Ustawienie przycisku w oknie
button_pick_document.place(x=360,y=310,anchor="center")
#Tworzenie label, który wyswietli nazwe pliku
file_label = tk.Label(root,text="Nie wybrano pliku do podpisania",bg="#2B6CB0",fg="#DFE6E9" )
file_label.place(x=360,y=280,anchor="center")




#Odpalenie pętli gółwnej
root.mainloop()

