import threading
import time
from states import State
from rooms import States_Room
from rooms import Types_Room

class Vacuum(threading.Thread):
    def __init__(self, name, room, room_list):
        super().__init__()
        self.name = name
        self.room = room
        self.room_list = room_list
        self.state = State.IZQUIERDA
        self.take_break = 0
        self.sleep_time = 3

    def run(self):
        while True:
            print(self.message_state())
            time.sleep(self.sleep_time)
            self.update_state()

    def update_state(self):
        #implementar la limpiez de la habitacion
        if self.take_break >= 1 and self.take_break < 3:
            self.state = State.NO_HACER_NADA
            self.take_break += 1
        elif self.take_break >= 3:
            self.take_break = 0
            self.known_the_direction_by_room()
        elif self.room.state == States_Room.DIRTY and self.state == State.LIMPIAR:
            self.room.state = States_Room.CLEAN
            self.known_the_direction_by_room()
            self.take_break += 1
        elif self.room.state == States_Room.DIRTY:
            self.state = State.LIMPIAR
        elif self.state == State.DERECHA:
            self.state = State.IZQUIERDA
            self.room = self.room_list[0]
        elif self.state == State.IZQUIERDA:
            self.state = State.DERECHA
            self.room = self.room_list[1]

    def known_the_direction_by_room(self):
        if self.room.name == Types_Room.A:
                self.state = State.IZQUIERDA
        else:
            self.state = State.DERECHA
        

    def message_state(self):
        return (f"{self.name} está en el estado {self.state} en el {self.room.name} donde esta {self.room.state} \n")

