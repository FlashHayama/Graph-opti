class Lecture:
    def __init__(self) -> None:
        pass

    def lecture_donnee(self,num):
        with open("data/data" + num + ".dat","r") as f:
            nbrs = list()
            is_integer = 0
            for line in f:
                if "#" in line:
                    # on saute la ligne
                    continue
                data = line.split()
                if is_integer<3:
                    if is_integer==0:
                        N=data[0]
                    else:
                        if is_integer==1:
                            E=data[0]
                        else:
                            B=data[0]
                    is_integer+=1
                else:
                    nbrs.append(data[0])