#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import connexion
import  Evenement
class Projection(Evenement.Evenement):
    requete=""
    titre="les mysteres du numerique"
    def __init__(self, titre):
          Evenement.Evenement.__init__(self)
          self.titre=titre 
    def creerProjection(self, t):
         self.titre=t
         requete="insert into Projection(titre) values ('"+t+"');"
         c5=connexion.connexion()
         c5.creerRequete(requete)
         