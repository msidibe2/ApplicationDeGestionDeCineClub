#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 

import tkinter as tk
from tkinter import Frame, Label, Entry, OptionMenu, Checkbutton, IntVar, StringVar,   Button 
#import Utilisateur
def constuire_widget(frame):
    frame.tkraise()
  
cadre_p=tk.Tk()    #construction  de la fenetre principale
cadre_p.geometry('1080x760')
cadre_p.config(bg="light green")  #fenetre principale, ses dimensions et la couleur d'arrière-plan

cadre_p.title("BIENVENUE SUR LE SITE DE LOISIRS DE LA MAIRIE ")

widget1 = Frame(cadre_p, bg="light green")
widget1.place(x=10, y=3, width=1280, height=9000)   # 1 er widget de coordonnees (x,y) et de taille(width, height)
l0= Label(widget1, text="Se connecter à l'application", width=50, font=(15), bg='white',fg='green')
l0.place(x=220, y=35)
l1= Label(widget1, text='Identifiant: ', font=(10))
l1.place(x=230, y=85)
champ_7=Entry(widget1, width=40)
champ_7.place(x=400, y=85)
l2= Label(widget1, text='Password', font=(10))
l2.place(x=230, y=125)
champ_8=Entry(widget1, width=40)
champ_8.place(x=400, y=125)
# creation d'un bouton avec ses configurations et son rôle
Button(widget1, text="se connecter", width=13, font=(8), bg='blue',fg='black', command=lambda:constuire_widget(widget2)).place(x=450,y=170)  
Button(widget1, text='Créer un compte',font=(25), width=30,bg='blue',fg='black', command=lambda:constuire_widget(widget3)).place(x=900,y=50)
b1=Button(widget1, text='Suivant',font=(20), width=30,bg='brown',fg='white', command=lambda:constuire_widget(widget2)).place(x=380,y=600)

widget2= Frame(cadre_p, bg="light green")
widget2.place(x=10, y=3, width=1280, height=900)
list = ['Listes des évèvenements', 'Presentation', 'Projection','Debat'];
choix=StringVar()
droplist=OptionMenu(widget2, choix, *list)
droplist.config(width=25)
choix.set('Listes des évèvenements') 
droplist.place(x=10, y=20)
l5 = Label(widget2, text="Evènement par période",width=27,font=("bold", 12))
l5.place(x=310,y=25) 
Button(widget2, text="Retour à la page d'accueil", width=20, bg='brown', fg='white', command=lambda:constuire_widget(widget1)).place(x=180,y=600) 
Button(widget2, text="Réserver un évènement", width=20, bg='brown', fg='white', command=lambda:constuire_widget(widget4)).place(x=150,y=350)
Button(widget2, text="Ajouter un évènement", width=20, bg='brown', fg='white', command=lambda:constuire_widget(widget4)).place(x=400,y=350) 
Button(widget2, text="Modifier un évènement", width=20, bg='brown', fg='white', command=lambda:constuire_widget(widget4)).place(x=650,y=350) 
Button(widget2, text="Supprimer un évènement", width=20, bg='brown', fg='white', command=lambda:constuire_widget(widget4)).place(x=900,y=350)  

widget3 = Frame(cadre_p, bg="light green")
widget3.place(x=10, y=3, width=1280, height=900)
Button(widget3, text='Se connecter pour voir les évènements', width=20,bg='brown',fg='white', command=lambda:constuire_widget(widget2)) 
l3 = Label(widget3, text="Créer un compte utilisateur", width=50,font=("bold", 10))
l3.place(x=50,y=40)
l4 = Label(widget3, text="Nom", width=17,font=("bold", 10))
l4.place(x=60,y=100)
champ_4 = Entry(widget3, width=40)
champ_4.place(x=400,y=100) 
l2 = Label(widget3, text="Password", width=17,font=("bold", 10))
l2.place(x=60,y=160)
champ2 = Entry(widget3, width=40)
champ2.place(x=400,y=160)
Button(widget3, text='Valider', width=8, bg='blue',fg='black').place(x=260, y=240)
Button(widget3, text="Retour à la page d'accueil", width=20, bg='brown', fg='white', command=lambda:constuire_widget(widget1)).place(x=180,y=600) 
 
widget4= Frame(cadre_p, bg="light green")
widget4.place(x=10, y=3, width=1280, height=900)
l5 = Label(widget4, text="Evènements concernés",width=40,font=("bold", 20))
l5.place(x=200,y=30)
l55= Label(widget4, text="Date: ") 
l55.place(x=500, y=100)
champ_55=Entry(widget4, width=60)
champ_55.place(x=550, y=100)
champ_56=Entry(widget4, width=60)
champ_56.place(x=550, y=140)
champ_57=Entry(widget4, width=60)
champ_57.place(x=550, y=210)
var1 = IntVar()
Checkbutton(widget4, text="Presentation", variable=var1).place(x=210,y=100)
var2 = IntVar()
Checkbutton(widget4, text="Projection", variable=var2).place(x=210,y=140)
var3 = IntVar()
Checkbutton(widget4, text="Debat", variable=var3).place(x=210,y=210)
Button(widget4, text="Retour à la page d'accueil", width=20, bg='brown', fg='white', command=lambda:constuire_widget(widget1)).place(x=180,y=600) 

cadre_p.mainloop()   #affichage de la fenetre principale