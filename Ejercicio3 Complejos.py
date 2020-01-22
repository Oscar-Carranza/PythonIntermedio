#!/usr/bin/env python
# coding: utf-8

# # EJERCICIO Complejos

# In[1]:


import math


# In[2]:


class Complejo:
    def __init__(self, r, i):
        self._r=r  #Atributos privados
        self._i=i
    def modulo(self):
        m=math.sqrt(self._r**2+self._i**2)
        print(m)
    def mostrar(self):
        print('C= (', self._r, ')+ j (', self._i, ')')
    def getParteReal(self):
        return self._r
    def getParteImag(self):
        return self._i
    def __add__(self, otro):
              return Complejo(self._r +otro._r, self._i +otro._i)
    def __sub__(self, otro):
              return Complejo(self._r -otro._r, self._i -otro._i)
    def __mul__(self, otro):
        return Complejo(self._r*otro._r -self._i*otro._i, self._r*otro._i +otro._r*self._i)
    def __truediv__ (self, otro):
        parte1=((self._r*otro._r) +(self._i*otro._i))/((otro._r**2) +(otro._i**2))
        parte2=((otro._r*self._i)-(self._r*otro._i))/((otro._r**2) +(otro._i**2))
        return Complejo(parte1, parte2)


# In[3]:


x=Complejo(9, 12)


# In[4]:


x.modulo()


# In[5]:


x.mostrar()


# In[6]:


#tratando de acceder a los atributos 8los cuales son privados y no se puede).
#Me mandaría un error


# In[7]:


print(x.r)
print(x.i)


# In[8]:


#Obtengo los atributos por medio de los métodos getter


# In[9]:


x.getParteReal()


# In[10]:


x.getParteImag()


# In[11]:


y=Complejo(1, 2)


# In[12]:


z=x+y


# In[13]:


z.mostrar()


# In[14]:


w=x*y


# In[15]:


w.mostrar()


# In[16]:


v=x/y


# In[17]:


v.mostrar()


# In[18]:


v.modulo()


# In[19]:


type(v)


# In[ ]:




