from tkinter import *
calcul = "" 

def equalclick(): 
    try: 
        global calcul 
 
        result = str(eval(calcul)) 
        equation.set(result) 
        calcul = result
 
    except: #Message d'erreur pour les entrées incorrectes ou les opérations illégales.

        equation.set(" ---Error--- ")
        calcul = "" 

def click(num): 
    global calcul #Instruction qui permet d'utiliser la variable en dehors de sa fonction
    calcul = calcul + str(num) 
    equation.set(calcul) 
 
def delete(): #Fonction qui permet d'effacer les résultats d'un calcul
    global calcul 
    calcul = "" 
    equation.set("") 

if __name__ == "__main__": 
    machine = Tk() 
    machine.title("Calculatrice9000 de ZayZay") 
    machine.geometry("330x315")
    machine.configure(background='pink')
    equation = StringVar() 
    formule_field = Entry(machine, textvariable=equation) 
    formule_field.grid(columnspan=4,  pady= 30 , padx = 20 , ipadx = 20 , ipady = 10)

    #Nous allons créer les boutons de la calculatrice ; averc leurs valeurs et leurs emplacements.

    btn_1 = Button(machine, text=' 1 ', command=lambda: click(1), height=2, width=10) 
    btn_1.grid(row=2, column=0) 
 
    btn_2 = Button(machine, text=' 2 ', command=lambda: click(2), height=2, width=10) 
    btn_2.grid(row=2, column=1) 
 
    btn_3 = Button(machine, text=' 3 ', command=lambda: click(3), height=2, width=10) 
    btn_3.grid(row=2, column=2) 
 
    btn_4 = Button(machine, text=' 4 ', command=lambda: click(4), height=2, width=10) 
    btn_4.grid(row=3, column=0) 
 
    btn_5 = Button(machine, text=' 5 ', command=lambda: click(5), height=2, width=10) 
    btn_5.grid(row=3, column=1) 
 
    btn_6 = Button(machine, text=' 6 ', command=lambda: click(6), height=2, width=10) 
    btn_6.grid(row=3, column=2) 
 
    btn_7 = Button(machine, text=' 7 ', command=lambda: click(7), height=2, width=10) 
    btn_7.grid(row=4, column=0) 
 
    btn_8 = Button(machine, text=' 8 ', command=lambda: click(8), height=2, width=10) 
    btn_8.grid(row=4, column=1) 
 
    btn_9 = Button(machine, text=' 9 ', command=lambda: click(9), height=2, width=10) 
    btn_9.grid(row=4, column=2) 
 
    btn_0 = Button(machine, text=' 0 ', command=lambda: click(0), height=2, width=10) 
    btn_0.grid(row=5, column=0) 
 
    plus = Button(machine, text=' - ', command=lambda: click("-"), height=2, width=10) 
    plus.grid(row=2, column=3) 
 
    minus = Button(machine, text=' + ', command=lambda: click("+"), height=2, width=10) 
    minus.grid(row=3, column=3) 
 
    multiply = Button(machine, text=' x ', command=lambda: click("*"), height=2, width=10) 
    multiply.grid(row=4, column=3) 
 
    divide = Button(machine, text=' / ', command=lambda: click("/"), height=2, width=10) 
    divide.grid(row=5, column=3) 
 
    equal = Button(machine, text=' = ', command=equalclick, height=2, width=10)
    equal.grid(row=6, column=3)

    Decimal = Button(machine, text=',', command=lambda: click(','), height=2, width=10) 
    Decimal.grid(row=5, column=1) 

    percent= Button(machine, text='%', command=lambda: click('%'), height=2, width=10) 
    percent.grid(row=5, column=2)

  #La touche Delete qui permet d'effacer un calcul
    delete = Button(machine, text='Delete', command=delete, height=2, width=10) 
    delete.grid(row=6, column=2)

    racine_carree = Button(machine, text="\U0000221A", command=lambda: click("**0.5"), height=2, width=10) 
    racine_carree.grid(row=6, column=1) 

    puissance_carree = Button(machine, text="x\U000000B2", command=lambda: click("**2"), height=2, width=10) 
    puissance_carree.grid(row=6, column=0)   
    
    machine.mainloop()