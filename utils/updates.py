from rooms import States_Room


def update_room_state(room_list):
    while True:
        comando = input("INGRESE EL CUARTO QUE ESTARA SUCIO: A,B \n")
        if comando.upper() == "A":
            print("CUARTO A ESTA AHORA SUCIO \n")
            room_list[0].state = States_Room.DIRTY
        elif comando.upper() == "B":
            print("CUARTO B ESTA AHORA SUCIO \n")
            room_list[1].state = States_Room.DIRTY
        else:
            print("Comando no reconocido. Inténtelo de nuevo.\n")


def update_room_state_gui(room_name, room_list):
    if room_name.upper() == "A":
        print("CUARTO A ESTA AHORA SUCIO \n")
        room_list[0].state = States_Room.DIRTY
    elif room_name.upper() == "B":
        print("CUARTO B ESTA AHORA SUCIO \n")
        room_list[1].state = States_Room.DIRTY
    else:
        print("room_name no reconocido. Inténtelo de nuevo.\n")

