from modules.master.window.master_window_open import MasterWindowOpen

class WindowOpen(MasterWindowOpen):

    def __init__(self, file) -> None:

        """
        
        """

        super().__init__()

        #
        self.file = file
    
    def __Open__(self) -> dict:

        """
        
        """
        
        super().__Open__()
        # line list
        line_list = []
        # line list split
        line_list_split = []
        # dimensions dict
        dimensions_dict = {}

        #
        with open(self.file, 'r') as file:

            #
            for line in file:
                
                #
                line_list.append(line.replace("\n",""))
            
            #
            for i in range(len(line_list)):
                #
                line_list_split = line_list[i].split(":")
                #
                dimensions_dict[line_list_split[0].replace(" ", "")] = line_list_split[1].replace(" ", "")
                
        return dimensions_dict

    
