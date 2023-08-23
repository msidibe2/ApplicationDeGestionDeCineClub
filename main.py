#!/usr/bin/env python3
# -- coding: utf-8 --


import Utilisateur 
import  Employe 

import Periode
import Evenement
import Lieu
import Presentation
import Projection 
import Debat

 

def main():
    if __name__=="__main__":
        main()
e1=Employe.Employe()
u1=Utilisateur.Utilisateur()
p1=Periode.Periode()
l1=Lieu.Lieu()
evnt1=Evenement.Evenement()
d1=Debat.Debat(4)
project1=Projection.Projection()
present1=Presentation.Presentation("David")

print(d1.nb_participant)
print(present1.Presentateur) 
e1.creerEmploye('Dupont', 'Ghislain', 'dupont.ghislain@gmail.com')
print(e1.nom, e1.prenom, e1.coordonnees)
print(project1.prixPlace)
l1.creerLieu("500", "avenue de ISTY", "SALAH", "debat")  # creation d'un lieu dans la BD
p1.creerPeriode("disponible", "3")                       # creation d'une periode dans la BD
d1.creerDebat("8")
present1.creerPresentation(present1.Presentateur)          # creation d'une presentation dans la BD
project1.creerProjection(project1.titre)         
evnt1.creerEvenement("Projection", "3", "300", "20")
e1.creerEmploye("SY", "Rone", "sy.rone@gmail.com", 7, "02/02/2020 au 23/02/2020") # un employe avec idPeriode(foreign key)=7
u1.creerUtilisateur("ILLY", "2020")
evnt1.supprimerEvenement(1)
evnt1.modifierEvenement()
evnt1.consulterEvenement()





