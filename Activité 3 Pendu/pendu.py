# On import la fonction unidecode pour éviter les soucis d'accents et de majuscules
from unidecode import unidecode

# Création de la classe Pendu = tous les attributs et méthodes nécessaires pour 
class Pendu:
    # On crée les attributs de base pour le jeu
    vies = 0
    mot_a_deviner = ""
    mot_a_afficher = ""
    # Une liste des lettres que l'utilisateur a tenté
    lettres_proposees = []

    ####################################################
    #      1e METHODE : Initialisation du jeu          #
    ####################################################


    def initialisation(mot_a_deviner, vies):
        mot_a_deviner = unidecode(mot_a_deviner).upper()
        print("Le mot pour cette parti est : ", mot_a_deviner)
        data_etat_du_jeu = {
            "vies" : vies,
            "mot_a_deviner" : mot_a_deviner,
            "mot_a_afficher" : "-" * len(mot_a_deviner),
            "defaite" : False,
            "victoire" : False,
            "entree" : "",
            "lettres_proposees" : []
        }

        return data_etat_du_jeu
    
    ####################################################
    #              2e METHODE : Deviner                #
    ####################################################
    
    # On crée notre méthode deviner qui va permettre de réaliser le fonctionnement générale 
    def deviner(etat_du_jeu, entree):
        # On récupère toute nos variables pour les mettres à jour
        global vies
        global mot_a_deviner
        global mot_a_afficher
        global lettres_proposees 

        # On met à jour toutes les variables de notre classe
        vies = etat_du_jeu["vies"]
        mot_a_deviner = etat_du_jeu["mot_a_deviner"]
        mot_a_afficher = etat_du_jeu["mot_a_afficher"]
        lettres_proposees  = etat_du_jeu["lettres_proposees"]

        # Données retournées par deviner()

        data_retour = {
            "defaite" : False,
            "victoire" : False,
            "derniere_entree" : ""
        }

        entree = unidecode(entree)

        # On vérifie si l'utilisateur a tenté un mot ou une lettre
        if len(entree) == 0 :
            message = "Propose quelque chose"
        elif len(entree) == 1 :
            message = Pendu.deviner_lettre(entree)
        else:
            message = Pendu.deviner_mot(entree)
        
        # On met à jour notre data_retour
        data_retour["vies"] = vies
        data_retour["mot_a_deviner"] = mot_a_deviner
        data_retour["mot_a_afficher"] = mot_a_afficher
        data_retour["lettres_proposees"] = lettres_proposees
        data_retour["message"] = message

        # On vérifie si le joueur
        data_retour["victoire"] = not "-" in mot_a_afficher
        if vies == 0:
            data_retour["defaite"] = True

        # On renvoie nos données du jeu
        return data_retour

    ####################################################
    #            3e METHODE : Deviner lettre           #
    ####################################################

    def deviner_lettre(entree):
        global lettres_proposees
        global mot_a_deviner
        global vies

        #On vérifie si la lettre a déjà été proposée
        if entree in lettres_proposees:
            return "Tu as déjà proposé cette lettre !!"
        # Sinon on l'ajoute à liste des lettres proposées
        # On vérifie si elle appartient au mot
        # Si oui on a
        else:
            lettres_proposees.append(entree)
            if entree in mot_a_deviner:
                Pendu.actualisation_mot_a_afficher(entree)
                return "Bonne pioche, le mot contient cette lettre !!!"
            else:
                vies -= 1
                return "Oups, cette lettre n'est pas dans le mot !!!"


    ####################################################
    #            4e METHODE : Deviner mot              #
    ####################################################

    def deviner_mot(entree):
        global mot_a_deviner
        global vies
        global mot_a_afficher

        # On vérifie que l'entrée correspond bien au mot à deviner
        if entree == mot_a_deviner:
            mot_a_afficher = entree
            return "Bravo, tu as trouvé le mot !!!"
        else:
            vies -= 1
            return "Dommage, ce n'est pas le bon mot !!!"
        

    ####################################################
    #    5e METHODE : Actualisation mot à afficher     #
    ####################################################
    
    # On vérifie si chaque lettre du mot == à l'entrée
    def actualisation_mot_a_afficher(lettre):
        global mot_a_deviner
        global mot_a_afficher
        # On parcourt grâce à une boucle notre mot_a_deviner
        for i in range(len(mot_a_deviner)):
            # On vérifie dans mot_a_deviner si la lettre est à la position i
            if lettre == mot_a_deviner[i]:
                # On passe par une liste car les str sont immuables
                mot_tmp = list(mot_a_afficher)
                # On ajoute à lettre à la bonne position cad i
                mot_tmp [i] = lettre
                # On récupère le str avec la méthode
                mot_a_afficher = "".join(mot_tmp)