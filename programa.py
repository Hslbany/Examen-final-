from tkinter import ttk
from tkinter import *
import math
import datetime

class Desk:
    def __init__(self, window):
        # Initializations
        
        #ancho
        an = 600
        #alto
        altura = 200
        
     
        self.wind = window

        
        self.wind.geometry(str(an)+'x'+str(altura))

        self.wind.columnconfigure(0, weight=1)
        self.wind.title('Examen')
        frame = LabelFrame(self.wind)
        frame.grid(row = 0, column = 0, columnspan = 5, pady = 20)      
        
        Label(frame, text = 'Ingresa tu nombre: ').grid(row = 1, column = 0)
       
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, columnspan = 6)

        Label(frame, text = 'Ingresa tu apellido: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, columnspan = 6)

        Label(frame, text = 'Ingresa el día que naciste: ').grid(row = 3, column = 0)
        self.var3 = Entry(frame)
        self.var3.grid(row = 3, columnspan = 6)

        Label(frame, text = 'Ingresa el mes en que naciste: ').grid(row = 4, column = 0)
        self.var4 = Entry(frame)
        self.var4.grid(row = 4, columnspan = 6)

        Label(frame, text = 'Ingresa el año en que naciste: ').grid(row = 5, column = 0)
        self.var5 = Entry(frame)
        self.var5.grid(row = 5, columnspan = 6)


        
        Button(frame, text = 'fecha en binario', command = self.b1).grid(row = 6, column = 0 , sticky = W + E)
        Button(frame, text = 'días vividos', command = self.b2).grid(row = 6, column = 1 , sticky = W + E)
        Button(frame, text = 'N. y A. par o impar', command = self.b3).grid(row = 6, column = 2 , sticky = W + E)
        Button(frame, text = '# de vocales y consonantes', command = self.b4).grid(row = 6, column = 3 , sticky = W + E)
        Button(frame, text = 'N. y A. al revés', command = self.b5).grid(row = 6, column = 4 , sticky = W + E)
 


        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    
    def b1(self):
        d=int(self.var3.get())
        m=int(self.var4.get())
        a=int(self.var5.get())
        bdia=format(d, '0b' )
        bmes=format(m, '0b')
        ba=format(a, '0b')

        self.message['text'] = 'tu fecha de nacimiento es: {}/{}/{} y su equivalente en binario es:{}/{}/{}'.format(d,m,a,bdia,bmes,ba)


    def b2(self):
            
        d=int(self.var3.get())
        m=int(self.var4.get())
        a=int(self.var5.get())
        nacimiento = datetime.datetime(a, m, d)
        hoy = datetime.datetime.now()
        diferencia = hoy - nacimiento
        dias = diferencia.days
        self.message['text'] = 'fecha de nacimiento: {}/{}/{}, dias vividos: {} dias'.format(d,m,a,dias)

    def b3(self):
        nombre=str(self.var1.get())
        apellido=str(self.var2.get())
        nnombre=int(len(nombre))
        napellido=int(len(apellido))
        if nnombre%2==0 and napellido %2==0 :
            self.message['text'] = '{} {} su nombre es par y su apellido es par'.format(nombre,apellido)
        elif nnombre%2==0 and napellido %2==1:
            self.message['text'] = '{} {} su nombre es par y tu apellido es impar'.format(nombre,apellido)
        elif nnombre%2==1 and napellido %2==0:
            self.message['text'] = '{} {} su nombre es impar y tu apellido es par'.format(nombre,apellido)
        else:
            self.message['text'] = '{} {} su nombre es impar y tu apellido es impar'.format(nombre,apellido)

    def b4(self):
        nombre=str(self.var1.get())
        apellido=str(self.var2.get())
        contador = 0
        for carac in nombre:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                contador = contador+1
        for carac in apellido:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                contador = contador+1
        contadornombre=len(nombre)
        contadorapellido=len(apellido)
        consonante=contadornombre+contadorapellido-contador

        self.message['text'] = 'Su nombre y apellido tienen {} vocales y {} consonantes'.format(contador,consonante)
     

    def b5(self):
        nombre=str(self.var1.get())
        apellido=str(self.var2.get())
        c1 = ""
        c2= ""
        for letra in nombre:
            c1 = letra + c1
        for letra1 in apellido:
            c2 = letra1 + c2
        self.message['text'] = '{} {} o al revez {} {}'.format(nombre,apellido,c1,c2)


    

if __name__ == '__main__':
    
    
    window = Tk()
    app = Desk(window)
    window.mainloop()

