import random
import threading
import time
from states import State
from rooms import States_Room
from rooms import Types_Room

class VacuumDumb(threading.Thread):
    def __init__(self, name, room, room_list):
        super().__init__()
        self.name = name
        self.room = room
        self.room_list = room_list
        self.state = State.IZQUIERDA
        self.take_break = 0
        self.sleep_time = 1

    def run(self):
        while True:
            print(self.message_state())
            time.sleep(self.sleep_time)
            self.update_state()

    def update_state(self):
        # if random.random() < 0.5:  # Probabilidad de cambio de estado
        self.state = random.choice([State.DERECHA, State.IZQUIERDA,
                                    State.LIMPIAR, State.NO_HACER_NADA])
        self.known_the_room_by_direccion()
        

    def known_the_room_by_direccion(self):
        if self.room.state == States_Room.DIRTY and self.state == State.LIMPIAR:
            self.room.state = States_Room.CLEAN
        elif self.state == State.IZQUIERDA:
                self.room = self.room_list[0]
        elif self.state == State.DERECHA:
            self.room = self.room_list[1]
        

    def message_state(self):
        return (f"{self.name} está en el estado {self.state} en el {self.room.name} donde esta {self.room.state} \n")

