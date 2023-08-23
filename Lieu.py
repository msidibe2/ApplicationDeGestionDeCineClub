#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import connexion
class Lieu:
    
    requete=""
    def __init__(self):
        self.idLieu=5
        self.nombDePlace=300
        self.adresse='2 avenue de listy'
        self.responsable='Jean Paul'
        self.typeEvenement='projection'
        
    def creerLieu(self, np, ad, r, tE):
        requete ="insert into Lieu(nombDePlace, adresse, responsable, typeEvenement) values ( '"+np+"', '"+ad+"', '"+r+"', '"+tE+"');"
        self.nombDePlace=np
        self.adresse=ad 
        self.responsable=r 
        self.typeEvenement=tE
        c1= connexion.connexion()
        c1.creerRequete(requete)


        
  