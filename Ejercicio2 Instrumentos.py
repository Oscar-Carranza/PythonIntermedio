#!/usr/bin/env python
# coding: utf-8

# # Ejercicios Instrumentos musicales

# CARRANZA SALAZAR OSCAR EDUARDO

# Tipos de instrumentos :
#     - Viento
#     -Cuerda
#     -Percusión
#     -Instrumentoss eléctricos

# In[1]:


class Instrumento:
    def __init__(self, tipo, nombreInstrum): 
        self.tipo=tipo
        self.nombreInstrum=nombreInstrum
    def solo(self):
        print(self.nombreInstrum + " esta en un solo")
    def afinar(self):
        print(self.nombreInstrum + " afinandose")
    def musica(self):
        print('Tocando melodía')
    def unirConcierto(self):
        print(self.nombreInstrum +" se esta uniendo al Concierto")
        self.musica()
       
       
# Referencias de los tipos de Instrumentos musicales:
#  https://es.wikipedia.org/wiki/Instrumento_musical#Clasificación


# In[2]:


class InstrumentoCuerdas(Instrumento):
    def __init__(self, nombreInstrum, numCuerdas, trastes, mastil): 
        #los atributos de trastes y mastil pueden ser True o False (si tienen o no tienen respectivamente)
        tip='Cuerdas'
        nom=nombreInstrum
        Instrumento.__init__(self, tip, nom)
        self.numCuerdas=numCuerdas
        self.trastes=trastes
        self.mastil=mastil
    def descanso(self): 
        #El instrumento descansa de tocar
        print("...")


# In[3]:


class InstrumentoViento(Instrumento):
    def __init__(self, nombreInstrum, material): 
        tip='Viento'
        nom=nombreInstrum
        Instrumento.__init__(self, tip, nom)
        self.material=material


# In[4]:


class InstrumentoPercusion(Instrumento):
    def __init__(self, nombreInstrum): 
        tip='Percusion'
        nom=nombreInstrum
        Instrumento.__init__(self, tip, nom)


# In[5]:


class Arpa(InstrumentoCuerdas):
    pass #No hagas nada con la clase


# In[6]:


class Piano(InstrumentoPercusion):
    def __init__(self, nombreInstrum):
        nom=nombreInstrum
        InstrumentoPercusion.__init__(self, nom)
        print('Has creado un Piano')
    def musica(self):
        #sobreescribo el método
        print('plinplin el piano')


# In[7]:


#el piano es un instrumento de percusión
#Referencia:  https://www.pianomundo.com.ar/rockpop/¿que-clase-de-instrumento-es-el-piano/


# In[8]:


class Bateria(InstrumentoPercusion):
    def __init__(self, nombreInstrum):
        nom=nombreInstrum
        InstrumentoPercusion.__init__(self, nom)
        print('Has creado una Bateria') 
    def musica(self):
        #sobreescribo el método
        print('tratra la bateria')


# In[9]:


class Trompeta(InstrumentoViento):
    def __init__(self, nombreInstrum, material):
        nom=nombreInstrum
        mat=material
        InstrumentoViento.__init__(self, nom, mat)
        print('Has creado una Trompeta') 
    def musica(self):
        #sobreescribo el método
        print('tuntun  la trompeta')


# In[10]:


class Guitarra(InstrumentoCuerdas):
    def __init__(self, nombreInstrum, numCuerdas, trastes, mastil):
        nom=nombreInstrum
        numC=numCuerdas
        tra=trastes
        ma=mastil
        InstrumentoCuerdas.__init__(self, nom, numC, tra, ma )
        print('Has creado una Guitarra') 
    def musica(self):
        #sobreescribo el método
        print('taratara  la guitarra')


# In[11]:


class Acordeon(InstrumentoViento):
    def __init__(self, nombreInstrum, material):
        nom=nombreInstrum
        mat=material
        InstrumentoViento.__init__(self, nom, mat)
        print('Has creado un Acordeon') 
    def musica(self):
        #sobreescribo el método
        print('bumbum  el acordeon')


# In[12]:


#Probemos las clases...


# In[13]:


p=Piano('piano')


# In[14]:


p.solo()


# In[15]:


p.musica()


# In[16]:


p.afinar()


# In[17]:


p.unirConcierto()


# In[18]:


#Hagamos un cocnierto con una cancion muy conocida


# In[19]:


#creamos objetos, es decir, hago instancias de clase


# In[20]:


b =Bateria('bateria')


# In[21]:


t= Trompeta('trompeta', 'metal')


# In[22]:


g=Guitarra('guitarra', 6, True, True)


# In[23]:


a=Acordeon('acordeon', 'plastico')


# In[24]:


#Empezemos con el concierto


# In[25]:


p.musica()


# In[26]:


b.musica()


# In[27]:


t.musica()


# In[28]:


g.musica()


# In[29]:


a.musica()


# In[ ]:




