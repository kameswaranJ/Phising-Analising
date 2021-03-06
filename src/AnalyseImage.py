# -*- coding: utf-8 -*-
"""

La fonction analyseLienImage retourne un nombre entre 0 et 1

"""


def analyseLienImage(tabLien, nom):
    """

    :param tabLien: tableau avec tous les liens dans le mail
    :param nom: nom de l'envoyeur
    :return: pourcentage de retour
    """
    
    ratio = 0
    nombreLiens = len(tabLien)
    nombreLiensConformes = 0
    lien = ""
    
    if nombreLiens > 0: 
        
        for i in range(len(tabLien)):
        
            lien = tabLien[i]
            
            if (lien.lower().find(nom.lower()) != -1):
                
                nombreLiensConformes = nombreLiensConformes + 1

        ratio = nombreLiensConformes / nombreLiens
    
    return ratio
