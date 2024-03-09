class VaccumModel1:

    def __init__(self):
        self.default_status = "arrival_a"
        self.status = {"is_dirty_a","is_dirty_b","finish_clean_a","finish_clean_b",
                        "arrival_a","arrival_b", 'is_clean_a', "is_clean_b"}
        self.perception = { 'limpio', 'sucio', 'mover', 'termino mover' }
        self.rules = {
            "is_dirty_a":"vacuum_the_floor_a",
            "is_dirty_b":"vacuum_the_floor_b",

            "finish_clean_a":"suspended_a",
            "finish_clean_b":"suspended_b",
            
            "arrival_a": "examine_a",
            "is_clean_a" : "moving_room_b",

            "arrival_b": "examine_b",
            "is_clean_b": "moving_room_a",
            
        }
        self.model = [
            ('arrival_a', 'examine_a', 'limpio', 'is_clean_a'),
            ('arrival_a', 'examine_a', 'sucio', 'is_dirty_a'),
            ('is_dirty_a', 'vacuum_the_floor_a', 'limpio', 'finish_clean_a'),
            ('finish_clean_a', 'suspended_a', 'mover', 'arrival_a'),
            ('is_clean_a', 'moving_room_b', 'termino mover', 'arrival_b'),

            ('arrival_b', 'examine_b', 'limpio', 'is_clean_b'),
            ('arrival_b', 'examine_b', 'sucio', 'is_dirty_b'),
            ('is_dirty_b', 'vacuum_the_floor_b', 'limpio', 'finish_clean_b'),
            ('finish_clean_b', 'suspended_b', 'mover', 'arrival_b'),
            ('is_clean_b', 'moving_room_a', 'termino mover', 'arrival_a'),
        ]
        self.actions = {"examine_a": "Ingrese estado del cuarto A",
            "examine_b": "Ingrese estado del cuarto B",

        	"vacuum_the_floor_a": "Aspirando cuarto A",
            "vacuum_the_floor_b": "Aspirando cuarto B",

            "suspended_a": "descansando.",
            "suspended_b": "descansando.",

            "moving_room_b" : "moviendose al cuarto B",
            "moving_room_a" : "moviendose al cuarto A",
        }
    
    def updateStatus(self, presentStatus, presentAction, perception):
        newStatus = self.existInModel(presentStatus, presentAction, perception)
        return presentStatus if newStatus is None else newStatus

        
    def existInModel(self, presentStatus, presentAction, perception):
        patern = (presentStatus, presentAction, perception)
        matching_transition = next((transition[3] for transition in self.model if transition[:3] == patern), None)
        return matching_transition

    
    def printValues(self,presentStatus, presentAction,textToPrint):
        print("--------------------------------")
        print("\nCurrently Status: " + presentStatus)
        print("Currently Action: " + presentAction + "\n")
        print(textToPrint)
    