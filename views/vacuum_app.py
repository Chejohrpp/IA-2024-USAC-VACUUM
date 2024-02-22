import tkinter as tk
import threading
import time
from entities.vacuum import Vacuum
from rooms import get_list_of_rooms, States_Room
from utils.updates import update_room_state_gui

class VacuumApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Test de Aspiradora")

        # Obtiene la lista de habitaciones
        self.room_list = get_list_of_rooms()

        # Creamos instancia de la aspiradora
        self.vacuum = Vacuum("aspiradora", self.room_list[0], self.room_list)
        self.vacuum_thread = threading.Thread(target=self.vacuum.run)
        self.vacuum_thread.daemon = True
        self.vacuum_thread.start()

        # Creamos los elementos de la interfaz
        self.label_message = tk.Label(root, text="INGRESE EL CUARTO QUE ESTARA SUCIO: A,B", font=("Arial", 16))
        self.label_message.pack()

        self.entry = tk.Entry(root, font=("Arial", 16))
        self.entry.pack()

        self.button = tk.Button(root, text="Enviar", font=("Arial", 16), command=self.send_dirty_room)
        self.button.pack()

        self.label_status = tk.Label(root, text="", font=("Arial", 16))
        self.label_status.pack()

        self.label_room_a = tk.Label(root, text="CUARTO A", font=("Arial", 18))
        self.label_room_a.pack()

        self.label_room_b = tk.Label(root, text="CUARTO B", font=("Arial", 18))
        self.label_room_b.pack()

        # Crear contenedor para los labels
        self.labels_container = tk.Frame(root)
        self.labels_container.pack()

        # Crear los labels dentro del contenedor
        self.label_vacuum_state = tk.Label(self.labels_container, text="Estado", font=("Arial", 18))
        self.label_vacuum_state.grid(row=0, column=0, padx=16)

        self.label_current_room = tk.Label(self.labels_container, text="current", font=("Arial", 18))
        self.label_current_room.grid(row=0, column=1, padx=16)

        self.listbox_vacuum_state = tk.Listbox(root, width=120, height=10)
        self.listbox_vacuum_state.pack()

        self.thread = threading.Thread(target=self.update_vacuum_state)
        self.thread.daemon = True
        self.thread.start()

    def send_dirty_room(self):
        room_name = self.entry.get()
        update_room_state_gui(room_name, self.room_list)   
        self.room_state()     
        
    def room_state(self):
        self.label_room_a.config(text=self.room_list[0].to_string(), font=("Arial", 16))
        self.label_room_b.config(text=self.room_list[1].to_string(), font=("Arial", 16))
        
    def update_vacuum_state(self):
        while True:
            self.listbox_vacuum_state.insert(tk.END,self.vacuum.message_state())
            self.listbox_vacuum_state.yview_moveto(1.0)  # Mover automáticamente el Listbox hacia abajo
            self.room_state()
            self.label_vacuum_state.config(text=f"ESTADO : {self.vacuum.state}", font=("Arial", 16))
            self.label_current_room.config(text=f"HABITACION ACTUAL : {self.vacuum.room.name}", font=("Arial", 16))
            time.sleep(self.vacuum.sleep_time)
