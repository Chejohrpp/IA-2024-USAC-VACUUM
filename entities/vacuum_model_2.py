class VaccumModel2:

    def __init__(self):
        self.default_status = "arrival_a"
        self.status = {"is_dirty_a","is_dirty_b","finish_clean_a","finish_clean_b",
                        "arrival_a","arrival_b", 'is_clean_a', "is_clean_b"}
        self.perception = { 'limpio', 'sucio', 'termino mover', 'timer' }
        self.rules = {
            "is_dirty_a":"vacuum_the_floor_a",
            "is_dirty_b":"vacuum_the_floor_b",

            "finish_clean_a":"moving_room_b_check",
            "finish_clean_b":"moving_room_a_check",

            "check_a": "examine_a",
            "check_b": "examine_b",

            "check_a_clean": "suspended_a",
            "check_b_clean": "suspended_b",

            "scan_a" : "examine_a",
            "scan_b" : "examine_b",
            
            "arrival_a": "examine_a",
            "is_clean_a" : "moving_room_b",

            "arrival_b": "examine_b",
            "is_clean_b": "moving_room_a",

            "pre_check_a": "moving_room_a_check",
            "pre_check_b": "moving_room_b_check",

            "is_clean_a1": "moving_room_b",
            "is_clean_b1": "moving_room_a",

            "arrival_a1": "examine_a",
            "arrival_b1": "examine_b",
            
        }
        self.model = [
            ('arrival_a', 'examine_a', 'limpio', 'is_clean_a'),
            ('is_clean_a', 'moving_room_b', 'termino mover', 'arrival_b'),
            ('is_clean_a1', 'moving_room_b', 'termino mover', 'arrival_b1'),

            ('arrival_a1', 'examine_a', 'limpio', 'pre_check_b'),

            ('arrival_a', 'examine_a', 'sucio', 'is_dirty_a'),
            ('is_dirty_a', 'vacuum_the_floor_a', 'limpio', 'finish_clean_a'),
            
            ('finish_clean_a', 'moving_room_b_check', 'termino mover', 'check_b'),

            ('pre_check_a','moving_room_a_check','termino mover','check_a'),

            ('check_a','examine_a','limpio','check_a_clean'),
            ('check_a','examine_a','sucio','is_dirty_a'),
            ('check_a_clean', 'suspended_a', 'timer', 'scan_a'),

            ('scan_a', 'examine_a', 'limpio', 'is_clean_a1'),
            ('scan_a', 'examine_a', 'sucio', 'is_dirty_a'),

            ('arrival_b', 'examine_b', 'limpio', 'pre_check_a'),
            ('arrival_b1', 'examine_b', 'limpio', 'is_clean_b'),

            ('arrival_b', 'examine_b', 'sucio', 'is_dirty_b'),
            ('is_dirty_b', 'vacuum_the_floor_b', 'limpio', 'finish_clean_b'),
            ('finish_clean_b', 'moving_room_a_check', 'termino mover', 'check_a'),
            ('is_clean_b', 'moving_room_a', 'termino mover', 'arrival_a1'),
            ('is_clean_b1', 'moving_room_a', 'termino mover', 'arrival_a'),


            ('pre_check_b','moving_room_b_check','termino mover','check_b'),
            ('check_b','examine_b','limpio','check_b_clean'),
            ('check_b','examine_b','sucio','is_dirty_b'),
            ('check_b_clean', 'suspended_b', 'timer', 'scan_b'),

            ('scan_b', 'examine_b', 'limpio', 'is_clean_b1'),
            ('scan_b', 'examine_b', 'sucio', 'is_dirty_b'),

        ]
        self.actions = {"examine_a": "Ingrese estado del cuarto A",
            "examine_b": "Ingrese estado del cuarto B",

        	"vacuum_the_floor_a": "Aspirando cuarto A",
            "vacuum_the_floor_b": "Aspirando cuarto B",

            "suspended_a": "descansando.",
            "suspended_b": "descansando.",

            "moving_room_b" : "moviendose al cuarto B",
            "moving_room_a" : "moviendose al cuarto A",

            "moving_room_a_check" : "ir a revisar el cuarto A",
            "moving_room_b_check" : "ir a revisar el cuarto B"
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
    