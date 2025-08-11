import tkinter as tk
import threading
import time
import pyautogui

# Variável de controle
executando = False

def manter_ativo():
    global executando
    while executando:
        pyautogui.click()  # Simula um clique do mouse
        print("Clique executado para manter ativo.")
        time.sleep(5)  # Intervalo de 5 segundos

def iniciar():
    global executando
    if not executando:
        executando = True
        # Executa em uma thread separada para não travar a interface
        threading.Thread(target=manter_ativo, daemon=True).start()

def parar():
    global executando
    executando = False
    print("Execução cancelada.")

# Criando interface
root = tk.Tk()
root.title("Manter PC Ativo")
root.geometry("250x120")

btn_executar = tk.Button(root, text="Executar", command=iniciar, bg="green", fg="white", font=("Arial", 12))
btn_executar.pack(pady=10)

btn_cancelar = tk.Button(root, text="Cancelar", command=parar, bg="red", fg="white", font=("Arial", 12))
btn_cancelar.pack(pady=5)

root.mainloop()
