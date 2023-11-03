# coding: utf-8
 
from tkinter import * 

fenetre = Tk()

# bouton = Checkbutton(fenetre, text="checkbutton")
# bouton.pack()

# # radiobutton
# value = StringVar() 
# bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
# bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
# bouton3 = Radiobutton(fenetre, text="Peu être", variable=value, value=3)
# bouton1.pack()
# bouton2.pack()
# bouton3.pack()

# #liste
# liste = Listbox(fenetre)
# liste.insert(1, "Python")
# liste.insert(2, "PHP")
# liste.insert(3, "jQuery")
# liste.insert(4, "CSS")
# liste.insert(5, "Javascript")

# liste.pack()

# #canvas
# canvas = Canvas(fenetre, width=150, height=120, background='yellow')
# ligne1 = canvas.create_line(75, 0, 75, 120)
# ligne2 = canvas.create_line(0, 60, 150, 60)
# txt = canvas.create_text(75, 60, text="piscine", font="Arial 16 italic", fill="blue")
# canvas.pack()

# def alert():
#     showinfo("alerte", "Bravo!")

# menubar = Menu(fenetre)

# menu1 = Menu(menubar, tearoff=0)
# menu1.add_command(label="Créer", command=alert)
# menu1.add_command(label="Editer", command=alert)
# menu1.add_separator()
# menu1.add_command(label="Quitter", command=fenetre.quit)
# menubar.add_cascade(label="Fichier", menu=menu1)

# menu2 = Menu(menubar, tearoff=0)
# menu2.add_command(label="Couper", command=alert)
# menu2.add_command(label="Copier", command=alert)
# menu2.add_command(label="Coller", command=alert)
# menubar.add_cascade(label="Editer", menu=menu2)

# menu3 = Menu(menubar, tearoff=0)
# menu3.add_command(label="A propos", command=alert)
# menubar.add_cascade(label="Aide", menu=menu3)

# fenetre.config(menu=menubar)

# filename = askopenfilename(title="Ouvrir votre document",filetypes=[('csv files','.csv'),('all files','.*')])
# fichier = open(filename, "r")
# content = fichier.read()
# fichier.close()

# Label(fenetre, text=content).pack(padx=10, pady=10)


fenetre.mainloop()
