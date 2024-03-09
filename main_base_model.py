from entities.vacuum_model_1 import VaccumModel1
from entities.vacuum_model_2 import VaccumModel2

vacuum_model = VaccumModel2()

#default values to initialize
presentStatus = vacuum_model.default_status
presentAction = vacuum_model.rules[presentStatus]
vacuum_model.printValues(presentStatus,presentAction,vacuum_model.actions[presentAction])

while(True):
    print("Ingrese la percepcion. e.g:" + str(vacuum_model.perception))
    perception = input()
    presentStatus = vacuum_model.updateStatus(presentStatus,presentAction,perception)
    presentAction = vacuum_model.rules[presentStatus]
    textToPrint = vacuum_model.actions[presentAction]
    vacuum_model.printValues(presentStatus,presentAction,textToPrint)
