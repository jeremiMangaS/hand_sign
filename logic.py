class HandGesture :

    # fingers = []
    
    def __init__(self):
        self.command_list = {
            "command_1" : [True, True, True, True, True],
            "command_2" : [False, True, False, False, False],
            "command_3" : [False, False, True, False, False], 
            "command_4" : [False, False, False, True, False],
            "command_5" : [False, False, False, False, True]
        }

    # status of hand : up & down
    # Using the ratio of the tip of the finger to the pip of the fingers
     # fingers : thumb, index, middle, ring, little
    def fngrs_status(self, handlandmarks) :
        # thumb = [2, 3, 4]
        # index = [6, 7, 8]
        # middle = [10, 11, 12]
        # ring = [14, 15, 16]
        # little = [18, 19, 20]

        # rjoints_fngrs = [5, 9, 13, 17]
        tip_fngrs = [8, 12, 16, 20]
        pip_fngrs = [6, 10, 14, 18]

        fngrs_list = []

        # thumb use horizontal direc    
        if handlandmarks[4].x < handlandmarks[2].x :
            fngrs_list.append(True)
        else : 
            fngrs_list.append(False)
        # 4 fingers
        for i in range(0, 4) :
            if handlandmarks[tip_fngrs[i]].y < handlandmarks[pip_fngrs[i]].y :
                fngrs_list.append(True) # up
            else :
                fngrs_list.append(False) # down
        
        return fngrs_list


    def command_status(self, fngrs) :
        #
        for command, gesture in self.command_list.items() :
            if fngrs == gesture : 
                return command
        # print("Halo")
    # def command_status(fngrs) :
    #     if fngrs == [True, True, True, True, True] :
    #         return "command_1"
        
    #     elif fngrs == [False, True, False, False, False] :
    #         return "command_2"

    #     elif fngrs == [False, False, True, False, False] :
    #         return "command_3"

    #     elif fngrs == [False, False, False, True, False] :
    #         return "command_4"

    #     elif fngrs == [False, False, False, False, True] :
    #         return "command_5"
        
    #     else :
    #         return "zero"