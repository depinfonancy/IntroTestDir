# -*- coding: utf-8 -*-

# Commentaire divers :
#   - on peut remarquer que le code de mot_plus_long
#     et motScrabbleMax est mutualisable
#   - certaines fonctions pourraient être écrite de
#     manière plus courte en utilisant les fonctions
#     fourni par python, par exemple la fonction max de
#     python prenant deux paramètres
#   - bien entendu, c'est une manière de faire parmi d'autre,
#     et de nombreuses améliorations sont possibles

import sys, getopt

###########################
# Chargement d'un lexique #
###########################

def  lectureLexique(nom):
    """ retourne le lexique (sous forme de liste) contenu dans le fichier nom
        (attention: suppose la présence d'un mot par ligne) """
    lexique = []
    f =  open (nom,  'r' )
    for  ligne  in  f:
        # enlève caractère de fin de ligne
        lexique.append( ligne[: -1] )
    f.close()
    return lexique

####################
# Calcul de scores #
####################

def scoreLongueur(mot) :
    return len(mot)

# Initialisation mapping lettre -> score
# au sens du scrabble
score_lettre = { '?' :  0 }
for  e  in  'aeilnorstu' :
    score_lettre[e] =  1
for  e  in  'dgm' :
    score_lettre[e] =  2
for  e  in  'bcp' :
    score_lettre[e] =  3
for  e  in  'fhv' :
    score_lettre[e] =  4
for  e  in  'jq' :
    score_lettre[e] =  8
for  e  in  'kwxyz' :
    score_lettre[e] =  10

def scoreScrabble(mot):
    """ calcul et retourne le score du mot avec les regles du scrabble  """
    res =  0
    for  c  in  mot:
        res += score_lettre[c]
    return  res

assert scoreScrabble("z")==10
assert scoreScrabble("qwerty")==2*10+1*8+3*1

##########################################
# Ecrivabilité et recherche dans lexique #
##########################################

def ecrivable(mot, tirage) :
    """ test si le mot peut etre ecrit avec les caracteres du tirage """
    t_tmp  = list(tirage)   #  copie du tirage (ne pas détruire tirage en paramètre)
    for c in mot:
        if c in t_tmp:
            t_tmp.remove(c)
        else :
            return False
    return True

# test base
assert ecrivable("voir", "ortiv")
assert not ecrivable("abc", "azerty")
# test lettre muliple
assert ecrivable("zebre","erzbe")
assert not ecrivable("zebre","erzba")


def motEcrivable(lexique, tirage):
    """ retourne les mot écrivable à partir du tirage contenue dans le lexique """
    L = []
    for mot in lexique:
        if ecrivable(mot,tirage):
            L.append(mot)
    return L

assert set(motEcrivable(["dirac","bidule","rat","test"], "tdraic")) == set(["dirac","rat"])
assert set(motEcrivable(["dirac","bidule","rat","test"], "detis")) == set()


def  motScrabbleMax(list_mot):
    """ retourne la chaine et le score maximal (au sens du scrabble) contenu dans list_mot """
    res = ''
    s_max = 0
    for mot in list_mot:
        s = scoreScrabble(mot)
        if ( s > s_max):
            res =  mot
            s_max = s
    return (res, s_max)

assert motScrabbleMax(["coz","zebu"])==("zebu",10+2*1+3)
assert motScrabbleMax(["zebu","coz"])==("zebu",10+2*1+3)

def  scrabbleMax(lexique, tirage):
    """ retourne le meilleur mot (au sens du scrabble) écrit grace au lettre de tirage parmi
        les mots présents dans le lexique """
    return motScrabbleMax(motEcrivable(lexique,tirage))[0]

#########################################
# Test additionnel et Cas d'utilisation #
#########################################

if __name__ == "__main__":

    if len(sys.argv)>2 :
        # Chargement d'un lexique
        lexique = lectureLexique( '../data/frenchssaccent.dic' )

        nb = int(sys.argv[1])
        if nb>0 :
            lexique = lexique[0:nb]

        for t in sys.argv[2:] :
            print("  le mot de score max pour [%s] est : [%s]" % (t , scrabbleMax(lexique, t)) )
    elif len(sys.argv)==2 :
        print("not enough parameters")


