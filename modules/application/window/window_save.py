from modules.master.window.master_window_save import MasterWindowSave
from modules.application.window.window_frame import WindowFrame

class WindowSave(MasterWindowSave):

    """
    
    """
    
    def __init__(self, file) -> None:

        super().__init__(file)

        #
        self.keyList = ["available","maximum"]
        #
        self.valuelist = ["width","height","dimensions"]
        #
        self.WinFrame = WindowFrame()

    def __Save__(self) -> dict:

        """
        
        """
        
        super().__Save__()
        
        #
        with open(self.file, 'w') as file_:
            
            """
            
            """
            #
            dimensions_dict = {}
            #
            for indice_a in self.keyList:
                #
        
                dimensions = self.WinFrame.__wrap_dimensions__(indice_a)
                #
                indice_b = 0
                
                while indice_b <= 2:
                    
                    #
                    var_line = ""
                    #
                    var_dict = ""

                    #
                    if indice_b == 0:

                        var_line = "{}_{} : {}\n".format(indice_a, self.valuelist[indice_b], dimensions[0])
                        var_dict = "{}".format(dimensions[0])
                    
                    elif indice_b == 1:
 
                        var_line = "{}_{} : {}\n".format(indice_a, self.valuelist[indice_b], dimensions[1])
                        var_dict = "{}".format(dimensions[1])

                    else:

                        var_line = "{}_{} : {}x{}\n".format(indice_a, self.valuelist[indice_b], dimensions[0], dimensions[1])
                        var_dict = "{}x{}".format(dimensions[0], dimensions[1])
                
                    # 
                    dimensions_dict["{}_{}".format(indice_a, self.valuelist[indice_b])] = var_dict
                    #
                    file_.write(var_line)
                    
                    #
                    indice_b = indice_b + 1  

        return dimensions_dict