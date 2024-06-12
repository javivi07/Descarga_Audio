import tkinter as tk
from pytube import YouTube
import os
import threading

def download_audio():
    status_label.config(text="Generando...")
    url = entry.get()
    if not url.strip():
        status_label.config(text="Error, indica una URL")
        return
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    # Especificar la ruta de descarga local
    download_folder = os.path.join(os.getcwd(), "Descargas")
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    out_file = audio.download(output_path=download_folder)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    status_label.config(text="Generado con éxito")

def start_download():
    threading.Thread(target=download_audio).start()

# Crear la ventana
root = tk.Tk()
root.title("Descargar Audio de YouTube")
root.geometry("500x200")  # Tamaño de la ventana
root.configure(bg="#333333")  # Color de fondo
root.minsize(700, 300)  # Establecer tamaño mínimo de la ventana
root.maxsize(700, 300)  # Establecer tamaño máximo de la ventana
root.resizable(False, False)  # Deshabilitar la capacidad de redimensionar la ventana


# Título grande centrado
title_label = tk.Label(root, text="Conversor a MP3", font=("Arial", 20), bg="#333333", fg="white")
title_label.pack()

# Frame para contener el título y la entrada
input_frame = tk.Frame(root, bg="#333333")
input_frame.pack(pady=20)

# Título más pequeño al lado del input
url_label = tk.Label(input_frame, text="URL", font=("Arial", 12), bg="#333333", fg="white")
url_label.pack(side=tk.LEFT, padx=10)

# Entrada para el enlace de YouTube
entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
entry.pack(side=tk.LEFT)

# Botón para generar la descarga
generate_button = tk.Button(root, text="Generar", command=start_download, bg="#4CAF50", fg="white", font=("Arial", 12))
generate_button.pack(pady=20)

# Etiqueta para mostrar el estado de la descarga
status_label = tk.Label(root, text="Esperando URL...", bg="#333333", fg="white", font=("Arial", 12))
status_label.pack(pady=10)

root.mainloop()