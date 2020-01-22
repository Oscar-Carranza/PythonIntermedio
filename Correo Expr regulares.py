#!/usr/bin/env python
# coding: utf-8

# # Expresiones regulares correo

# Carranza Salazar Oscar Eduardo

# In[1]:


import re


# In[2]:


expresionMAlESCRITA=r"\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2, 6}\b" #OJO: Esto es mal: NO PONER ESPACIOS


# In[3]:


expresion=r"\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b"  #Aqui si esta todo bien


# In[4]:


#Pongo un correo válido


# In[5]:


entrada1=input('Ingresa tu correo: ')


# In[6]:


#¿Es valido el correo?
if (re.match(expresion, entrada1)):
    print('Correo válido')
else:
    print('Correo inválido')


# In[7]:


#Pongo un correo inválido


# In[8]:


entrada2=input('Ingresa tu correo: ')


# In[9]:


#¿Es valido el correo?
if (re.match(expresion, entrada2)):
    print('Correo válido')
else:
    print('Correo inválido')


# In[ ]:




