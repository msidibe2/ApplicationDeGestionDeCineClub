#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
import connexion
class Evenement:
    requete=" "
    def __init__(self):
        self.idEvenement=10
        self.typeEvenement='projection' 
        self.duree=3
        self.prixPlace= 10
        self.nombDePLace=200                                                             
    def creerEvenement(self, idE , tE , dE, xp, np):
        requete="insert into Evenement(typeEvenement, duree, nombreDePlace,  prixPlace ) values ('"+tE+"', '"+dE+"', '"+np+"', '"+xp+"');"
        self.idEvenement=idE 
        self.typeEvenement=tE 
        self.duree=dE
        self.prixPlace= xp
        self.nombDePLace=np
        c7=connexion.connexion()
        c7.creerRequete(requete)
    def supprimerEvenement(self, idEvenement):
        requete="delete from Evenement where   idEvenement is idEvenement;"
        self.idEvenement=idEvenement
        c8=connexion.connexion()
        c8.creerRequete(requete)
    def modifierEvenement(self, idEvenement,  tE, duree, prixPlace, nombDePlace):  
        requete="update Evenement set typeEvenement =='Tenis', duree ==dure, prixPlace==prixPlace, nombDePlace==nombdePlace where idEvenement is 1;"
        self.idEvenement=idEvenement 
        self.typeEvenement=tE 
        self.duree=duree
        self.prixPlace= prixPlace
        self.nombDePLace=nombDePlace
        c9=connexion.connexion()
        c9.creerRequete(requete)
    def consulterEvenement(self ):
        requete="select * from Evenement ;"
        #self.idEvenement=idE 
        c10=connexion.connexion()
        c10.creerRequete(requete)
        
        