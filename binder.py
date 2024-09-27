import os
from pypdf import PdfMerger
from tkinter import Tk, filedialog
import tkinter as tk
from tkinter import ttk

def scegli_cartella():
    """Funzione per selezionare una cartella contenente i PDF"""
    folder = filedialog.askdirectory(title="Seleziona la cartella contenente i PDF")
    if folder:
        unisci_pdf(folder, "output_unito.pdf")  # Specifica il nome del file PDF finale
        return folder_path

def unisci_pdf(folder_path, output_pdf="unito.pdf"):
    """Unisce tutti i file PDF presenti nella cartella specificata"""
    pdf_merger = PdfMerger()

    # Ottiene tutti i file .pdf nella cartella
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf') or f.endswith('.PDF')]
    pdf_files.sort()  # Opzionale: Ordina i file per nome
    n_file = len(pdf_files)
    label_file.configure(text=f"Numero pdf : {n_file}")
    
    # Aggiungi ogni PDF al PdfMerger
    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        prog.step(100/n_file)
        print(f"Unendo: {pdf_path}")
        pdf_merger.append(pdf_path)
        root.update_idletasks()

    # Salva il PDF unito
    output_path = os.path.join(folder_path, output_pdf)
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)
    
    print(f"PDF uniti e salvati come {output_path}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title('PDF Binder 1.0')
    root.geometry("250x150")
    #root.iconbitmap("img/favicon/fav.ico")
    button = tk.Button(root, text="Scegli  Cartella", command=scegli_cartella, width=15)
    button.grid(row=0, column=0, padx=10, pady=10)
    label_file = tk.Label(text="")
    label_file.grid(row=2, column=0, padx=10, pady=10)
    prog = ttk.Progressbar(root, orient="horizontal", length=235, mode='determinate')
    prog.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky ='W')
    root.mainloop()
    
