class Lecture:
    def __init__(self) -> None:
        self.N = 0
        self.E = 0
        self.B = 0
        self.nbrs = []
        pass

    def lecture_donnee(self,num):
        with open("data/data" + str(num) + ".dat","r") as f:
            is_integer = 0
            for line in f:
                if "#" in line:
                    # on saute la ligne
                    continue
                data = line.split()
                if is_integer<3:
                    if is_integer==0:
                        self.N=int(data[0])
                    else:
                        if is_integer==1:
                            self.E=int(data[0])
                        else:
                            self.B=int(data[0])
                    is_integer+=1
                else:
                    self.nbrs.append(int(data[0]))