#!/usr/bin/env python
# coding: utf-8

# # Ejercicio 1: Animales

# Carranza Salazar Oscar Eduardo

# In[1]:


class Perro:
    def __init__(self, Nombre):  #es lo equivalente a un 'constructor' 
        #Va: doble guión bajo init doble guión bajo (self, argumentos)
        self.Nombre=Nombre
        print('A dog has born')
    def Ladrar(self):
        print(self.Nombre, 'esta ladrando')


# In[2]:


class Pitbull(Perro):  #esta clase hereda de 'Perro'
    def __init__(self, Nombre):
        Perro.__init__(self, Nombre)
        print('Perro creado')
    def Trucos(self):
        print('Dar la patita')


# In[3]:


Canela=Perro("Canela")
Canela.Ladrar()


# In[4]:


uu=Pitbull('Conde')
uu.Ladrar()


# In[5]:


class Pug(Perro): #Esta clase hereda de 'Perro'
    def __init__(self, Nombre, edad):  #es lo equivalente a un 'constructor' 
        self.Nombre=Nombre
        self.edad=edad
    def info(self):
        print("Un pug llamado: " + self.Nombre + " tiene " +str(self.edad) + " años")
    def Ladrar(self):
        #Usando el pilar de polimorfismo se sobreescribe este método
        print("Guau Guau")
    def dormir(self):
        print(self.Nombre +" está dormido")


# In[6]:


olliver=Pug("olliver", 2)
olliver.info()
olliver.Ladrar()
olliver.dormir()

