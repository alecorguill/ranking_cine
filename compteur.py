import operator
#Liste des noms des fichiers des tops
liste_top = ["classement_rotten.txt","classement_sensc111.txt","classement_cahiercine.txt","classement_timeout.txt",
             "classement_top100bfi.txt","classement_top100sc.txt","classement_topafi.txt"]

#Retourne le classement par points des films
def compteur_point():
    classement_point = {}
    for file in liste_top:
        fichier_class = open(file,"r")
        classement = fichier_class.read().casefold()
        liste_film = classement.split('\n')
        classement_film = 1
        for film in liste_film:
            try:
                classement_point[film] += point(classement_film)
            except KeyError:
                #Oui je peux eviter de calculer deux fois point
                classement_point.setdefault(film, point(classement_film))
                pass
            classement_film += 1
    return sorted(classement_point.items(), key=operator.itemgetter(1),reverse=True)

def is_ponc(s):
    return (s == ':') or (s == '!') or(s == '.')


#Retourne le nombre de points associé au classement
def point(classement):
    return 101 - classement

    '''
    if(classement == 1):
        return 11
    elif(classement == 2):
        return 11
    elif(classement == 2):
        return 10
    if(classement < 90 and classement >= 100):
        return 1
    elif (classement < 80 and classement >= 90):
        return 2
    elif (classement < 70 and classement >= 80):
        return 3
    elif (classement < 60 and classement >= 70):
        return 4
    elif (classement < 50 and classement >= 60):
        return 5
    elif (classement < 40 and classement >= 50):
        return 6
    elif (classement < 30 and classement >= 40):
        return 7
    elif (classement < 20 and classement >= 0):
        return 10
    else:
        return 100
'''

resultat = compteur_point()
print(resultat)

f_res = open("resultat.txt",'w')
for couple in resultat:
    f_res.write(str(couple[0]) + " " + str(couple[1]) + '\n')

f_res.close()

