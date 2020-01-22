#!/usr/bin/env python
# coding: utf-8

# # Ejercicio Excepciones

# Oscar Eduardo Carranza Salazar

# In[1]:


#Clase Persona con nombre, num_cuenta y edad


# In[2]:


import re

class Persona:
    def __init__(self):
        #Valores por defecto en caso de que el usuario no ingrese datos correctos
        #Notar que estos atributos son privados y solo pueden modificarse por medio de los métodos setter's
        self._edad=99
        self._numC=0
        self._nombre="q"
    def setEdad(self, edad):
        if(edad <=0):
            raise ValueError("La edad debe ser positiva")
        if(edad <18):
            raise ValueError("Debes ser mayor de edad")
        if (type(edad) != int):
            raise Exception("Tu edad debe ser un numero entero")
        self._edad=edad
    def setNombre(self, nombre):
        if (type(nombre) != str):
            raise Exception("Tu nombre debe ser una cadena")
        p=re.match('[a-zA-Z]+', nombre) #Uso expresiones regulares para asegurara que solo haya letras en el nombre
        if(len(nombre)!=p.end() -p.start()):
            raise Exception("Tu nombre solo puede contener letras del abecedario ingles")
        self._nombre=nombre
    def setNumCta(self, numC):
        if(numC<0):
             raise ValueError("No hay numeros de cuenta negativos")
        if(numC>32000) :  #Condición que yo quiero que se cumpla por capricho
            raise ValueError("Error de numero de cuenta. Favor de Verificar")
        if (type(numC) != int):
            raise Exception("Tu Numero de cuenta debe ser un numero entero")
        self._numC=numC   
    def __str__(self):
        return 'Nombre: ' +str(self._nombre) + '. Edad: ' +str(self._edad) + '. Num Cuenta. ' +str(self._numC)


# In[3]:


#Probemos excepciones haciendo objetos de la clase persona


# In[4]:


try:
    a=Persona()
    a.setEdad(-10)
except ValueError as e:
    print(e)


# In[5]:


try:
    b=Persona()
    b.setNumCta(-655)
except Exception as e:
    print(e)


# In[6]:


try:
    c=Persona()
    c.setNumCta(32001)
except Exception as e:
    print(e)


# In[7]:


d= Persona()

#Ingreso atributos de objeto 'd' con las funciones setter
#Para evitar que se detenga mi programa coloco bloques de código try-except
#En caso de que el usuario ingrese datos incorrectos se pondrán los valores predefinidos en el __init__

try:
    d.setEdad(16)
except ValueError as e:
    print(e)
    
try:
    d.setNumCta(64199)
except Exception as e:
    print(e)
    
try:
    d.setNombre(444)
except Exception as e:
    print(e)

print()
print(d)


# In[8]:


f=Persona()

try:
    f.setEdad(-5)
except ValueError as e:
    print(e)
    
try:
    f.setNumCta(-98)
except Exception as e:
    print(e)
    
try:
    f.setNombre("Pepe")
except Exception as e:
    print(e)

print()
print(f)


# In[9]:


#Ejemplo donde usuario ingresa por el teclado datos
g=Persona()

try:
    g.setEdad(int(input("Dame tu edad: ")))
except ValueError as e:
    print(e)
    
try:
    g.setNumCta(int(input("Dame tu Numero de Cuenta: ")))
except Exception as e:
    print(e)
    
try:
    g.setNombre(input("Dame tu Nombre: "))
except Exception as e:
    print(e)

print()
print(g)


# In[ ]:




