
name_list = [] 

class fixture_template:
    def __init__(self, name: str):
        self.name = name
        if self.check_name():
            msg = "The name allready exists, try another name..."
            print(msg)
            return
        name_list.append(self.name)
        self.weight = 0
        self.poweravg = 0
        self.powermax = 0
        self.connector = None
        self.powerlinkable = False
        self.dim = False
        self.modes = []

    # Adding DMX modes to fixture template
    def add_mode(self, ch_count: int, name: str):
        for mode in self.modes:
            if name in mode:
                msg = "modename allready exists, try another name"
                return
        n_mode = (ch_count, name)
        self.modes.append(n_mode)

    # Setting values for template
    def set_weight(self, weight: int):
        self.weight = weight

    def set_powermax(self, power: int):
        self.powermax = power
    
    def set_poweravg(self, power: int):
        self.poweravg = power
    
    def set_dim(self, val: bool):
        self.dim = val
    
    def set_powerlinkable(self, val: bool):
        self.powerlinkable = val
    
    def set_connector(self, con: str):
        self.connector = con

    # Checking if fixture template name is occupied
    def check_name(self):
        if self.name in name_list:
            return True
