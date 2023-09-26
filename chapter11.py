#!/usr/bin/env python
# coding: utf-8

# In[1]:


help("")


# In[2]:


dir("")


# In[3]:


class Apple:
    pass


# In[4]:


class Apple:
    color=" "
    flavour=" "
jonagold=Apple()
jonagold.color="red"
jonagold.flavour="sweet"
golden=Apple()
golden.color="yellow"
golden.flavour="sour"
print(jonagold.color)
print(jonagold.flavour)
print(golden.color)
print(golden.flavour)


# In[5]:


print(jonagold.color.upper())


# In[8]:


class Flower:
    color=" "
rose=Flower()
rose.color="red"
voilet=Flower()
voilet.color="purple"
this_pun_is_for_you="sugar is sweet and so are you"
print("roses are {}".format(rose.color))
print("voilets are {}".format(voilet.color))
print(this_pun_is_for_you)


# In[9]:


print("roses are {} and voilets are {}".format(rose.color,voilet.color))


# In[14]:


class Cat:
    pass
mycat=Cat()


# In[13]:


class Cat:
    def speak(self):
     print("meow meow.......")
mycat=Cat()
mycat.speak()
    


# In[15]:


class Cat:
    name = ""
    def speak(self):
        print("Meow! I'm {}! Meow".format(self.name))
myLuna = Cat()
myLuna.name = "Luna"
myLuna.speak()


# In[16]:


class Cat:
    name = ""
    def speak(self):
        print("Meow! I'm {}! Meow".format(self.name))
myLuna = Cat()
myLuna.name = "Luna"
myLuna.speak()
mybella = Cat()
mybella.name = "bella"
mybella.speak()


# In[17]:


class Cat:
    years = 0
    def age (self):
        return self.years * 12
myLuna = Cat()
myLuna.years = 2
myLuna.age()


# In[21]:


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
jonagold = Apple("red", "sweet")
print(jonagold.color)


# In[20]:


jonagold = Apple("red", "sweet")
print(jonagold)


# In[31]:


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
         return "Apple color is  {} and Apple flavor {}".format(self.color,self.flavor)
jonagold=Apple("red","sour")
print(jonagold)


# In[32]:


help(Apple)


# In[34]:


def to_seconds(hours, minutes, seconds): 
    """Returns the amount of seconds in the given hours, minutes and seconds.""" 
    return hours*3600+minutes*60+seconds 


# In[35]:


help(to_seconds)


# In[37]:


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return print("hi, my name is {}".format(self.name))
some_person = Person("Arooj") 
print(some_person.greeting())


# In[42]:


class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
class Apple(Fruit):
    pass
class Grape(Fruit):
    pass
jonagold = Fruit("red", "sweet")
print(jonagold.color)


# In[44]:


granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")
print(granny_smith.color)
print(carnelian.flavor)


# In[45]:


class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Cat(Animal):
    sound = "Meow!"
    
myLuna = Cat("Luna")
myLuna.speak()


# In[46]:


class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Cat(Animal):
    sound = "Meow!"
    
myLuna = Cat("Luna")
myLuna.speak()

class Cow(Animal):
    sound = "Moooo"
    
myCow = Cow("Milky")
myCow.speak()


# In[68]:



class Repository:
    def __init__(self):
        self.packages = {}
    def add_package(self, package):
        self.packages[package.name] = package
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result


# In[69]:


import random 
random.randint(1,10)   


# In[70]:


random.randint(1,10) 


# In[71]:


random.randint(1,10)


# In[72]:


import datetime 
now = datetime.datetime.now() 
type(now) 
print(now) 


# In[74]:


now.year 


# In[75]:


print(now + datetime.timedelta(days=28)) 


# In[ ]:




