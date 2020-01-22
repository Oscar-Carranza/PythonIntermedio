#!/usr/bin/env python
# coding: utf-8

# # PROGRAMACIÓN CON HILOS

# In[1]:


#Haciendo un programa sin hilos


# In[2]:


import time
import datetime


# In[3]:


def consultar(id_persona):
    time.sleep(2) #sleep for 2[s]

def guardar(id_persona, data):
    time.sleep(3) #sleep for 3[s]

tiempo_inicial=datetime.datetime.now()
consultar(10)
guardar(2, 'Python')
tiempo_final=datetime.datetime.now()

deltaTiempo=tiempo_final.second -tiempo_inicial.second
print("Tiempo transcurrido: " +str(deltaTiempo))  #Imprime: 5


# In[4]:


#Ten cuidado con los hilos, no vayas a matar a la compu


# In[5]:


import threading #Vamos a utilizar hilos

def consultar(id_persona):
    time.sleep(2) #sleep for 2[s]

def guardar(id_persona, data):
    time.sleep(3) #sleep for 3[s]

tiempo_inicial=datetime.datetime.now()

t1=threading.Thread(name='hilo1', target=consultar, args= (1, )) #Mando llamara la función consultar desde este hilo
t2=threading.Thread(name='hilo2', target=guardar, args=(1, 'ow' )) #Mando llamara la función guardar desde este hilo
#Notar que args recibe una tupla

t1.start() #Hilo1 empieza
t2.start() #Hilo2 empieza

#Estos hilos no regresan al hilo principal

tiempo_final=datetime.datetime.now()

deltaTiempo=tiempo_final.second -tiempo_inicial.second
print("Tiempo transcurrido: " +str(deltaTiempo)) #Imprime: 0


# In[6]:


import threading #Vamos a utilizar hilos

def consultar(id_persona):
    time.sleep(2) #sleep for 2[s]

def guardar(id_persona, data):
    time.sleep(3) #sleep for 3[s]

tiempo_inicial=datetime.datetime.now()

t1=threading.Thread(name='hilo1', target=consultar, args= (1, )) #Mando llamara la función consultar desde este hilo
t2=threading.Thread(name='hilo2', target=guardar, args=(1, 'ow' )) #Mando llamara la función guardar desde este hilo
#Notar que args recibe una tupla

t1.start() #Hilo1 empieza
t2.start() #Hilo2 empieza

t1.join() #termina de ejecutar el hilo y regresa al hilo principal (al main del programa)
t2.join() #termina de ejecutar el hilo y regresa al hilo principal (al main del programa)

tiempo_final=datetime.datetime.now()

deltaTiempo=tiempo_final.second -tiempo_inicial.second
print("Tiempo transcurrido: " +str(deltaTiempo))  #Imprime: 3


# In[7]:


#Ejercicio: hacer una función y ejecutarla por medio de hilos

import threading #Vamos a utilizar hilos

def saludo(nombre):
    print('Vamos a mandar un saluuuuu do do do a ', nombre);
    time.sleep(4)


tiempo_inicial=datetime.datetime.now()

t1=threading.Thread(name='hilo1', target=saludo, args= ('Oscar', ))


t1.start() #Hilo1 empieza
t1.join() 

print('Sigue corriendo hilo principal')
tiempo_final=datetime.datetime.now()

deltaTiempo=tiempo_final.second -tiempo_inicial.second


print("Tiempo transcurrido: " +str(deltaTiempo)) 


# In[ ]:




