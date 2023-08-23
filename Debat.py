#!/usr/bin/env python3
# -- coding: utf-8 --


import   Evenement
import connexion

class Debat(Evenement.Evenement):
  requete=""
  
  nb_participant = 5
  def __init__(self, nb_participant):
	    Evenement.Evenement.__init__(self)
	    self.nb_participant = nb_participant
  def creerDebat(self, n):
     requete="insert into Debat(nb_participant) values ('"+n+"');"
     self.nb_participant=n
     c3=connexion.connexion()
     c3.creerRequete(requete)
