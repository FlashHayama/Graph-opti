class Tri:
    def __init__(self) -> None:
        pass
    
    def fusion(tableau):
        tableauTrie = []
        for i in range(0,len(tableau)):
            tableauTrie = fusion(tableauTrie,tableau[i])
                
        return tableauTrie
                    

    def triFusion(tableau1,tableau2):
        indice_tableau1 = 0
        indice_tableau2 = 0    
        taille_tableau1 = len(tableau1)
        taille_tableau2 = len(tableau2)
        tableau_fusionne = []
        while indice_tableau1<taille_tableau1 and indice_tableau2<taille_tableau2:
            if tableau1[indice_tableau1] > tableau2[indice_tableau2]:
                tableau_fusionne.append(tableau1[indice_tableau1])
                indice_tableau1 += 1
            else:
                tableau_fusionne.append(tableau2[indice_tableau2])
                indice_tableau2 += 1
        while indice_tableau1<taille_tableau1:
            tableau_fusionne.append(tableau1[indice_tableau1])
            indice_tableau1+=1
        while indice_tableau2<taille_tableau2:
            tableau_fusionne.append(tableau2[indice_tableau2])
            indice_tableau2+=1
        return tableau_fusionne