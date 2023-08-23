#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

class connexion:
    def __init__(self):
        self.requete=""       
    def creerRequete(self, requete):
        connection=sqlite3.connect("Loisirs_DBase.db")
        cur=connection.cursor()
        cur.execute(requete)
        connection.commit()
        connection.close()
        
        
    
'''
connection=sqlite3.connect("Loisirs_DBase.db")
cur=connection.cursor()
requete="insert into Lieu(nombDePlace, adresse, responsable, typeEvenement) values ( 400, 'rue de Velizy', 'Charles', 'Presentation')"

cur.execute(requete)
connection.commit()
connection.close()
'''