#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import connexion
class Utilisateur:
    requete=" "
    def __init__(self):
        self.idUtilisateur=100
        self.nom="DA"
        self.Password='1234'
    def creerUtilisateur(self, n, pw):  #foncion permettant de creer un utilsateur dans la base de donnees
       requete="insert into Utilisateur(nom, motDePasse) values ('"+n+"', '"+pw+"');"
       self.nom=n
       self.Password=pw
       c8=connexion.connexion()
       c8.creerRequete(requete)
       
    
    
    