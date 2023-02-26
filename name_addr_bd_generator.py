#!/usr/bin/env python
# coding: utf-8

# In[37]:


import random
import datetime


# In[38]:


def name_dict(dict_name, addr): # Func for creating dictionary with names from text file
    i = 0
    with open(addr, encoding='utf8') as file:
        file = file.readlines()
        for line in file:
            name, qty = line.split()
            for num in range(int(qty)):
                dict_name[i] = name
                i += 1
    return

def addr_dict(dict_name, addr): # Func for creating dictionary with address data
    with open(addr, encoding='utf8') as file:
        i=0    
        for line in file:                       
            dict_name[i] = line.strip()
            i += 1
    return

def rand_house(city): # Func that generates random house num or house + apt num depends where it is located           
    if 'город' in city.lower():
        house = 'дом номер ' + str(random.randint(1,100)) +' квартира '+ str(random.randint(1,100))
    else:
        house = 'дом номер ' + str(random.randint(1,100)) +' '
    return house

def rand_dob(): # Func for creating a single random date of birth
    d1, d2 = datetime.date(1950,1,1), datetime.date(2006,1,1)
    delta = (d2-d1).days   
    return d1+ datetime.timedelta(days = random.randint(0, delta))

def random_client(): # Func for generating multiple client data items
    
    # Generating gender and selecting name dictionaries
    gen=random.choice([ 
        [male_names_dict, male_father_names_dict, male_family_names_dict], 
        [female_names_dict, female_father_names_dict, female_family_names_dict]])
    
    # Generating full name
    name =random.choice(gen[2]) + ' ' + random.choice(gen[0]) + ' ' + random.choice(gen[1]) 
    
    # Generating city
    city = random.choice(city_dict)
    
    # Generating street name
    street = random.choice(strt_dict)
    
    # Generating street address
    house = rand_house(city)
    
    # Generating date of birth
    dob = rand_dob()
    
    return name, street, house, city, dob
        


# In[39]:


male_names_dict = {} # Creating and filling dict with male names
male_names_addr = r'C:\Users\ASUS\Desktop\mfn1.txt'
name_dict(male_names_dict, male_names_addr)    


# In[40]:


male_father_names_dict = {} # Creating and filling dict with male father names
male_father_names_addr = r'C:\Users\ASUS\Desktop\msn1.txt'
name_dict(male_father_names_dict, male_father_names_addr)


# In[41]:


male_family_names_dict = {} # Creating and filling dict with male familly names
male_family_names_addr = r'C:\Users\ASUS\Desktop\famn.txt'
name_dict(male_family_names_dict, male_family_names_addr)


# In[42]:


female_names_dict = {} # Creating and filling dict with female names
female_names_addr = r'C:\Users\ASUS\Desktop\ffn.txt'
name_dict(female_names_dict, female_names_addr)


# In[43]:


female_father_names_dict = {} # Creating and filling dict with female father names
female_father_names_addr = r'C:\Users\ASUS\Desktop\fsn.txt'
name_dict(female_father_names_dict, female_father_names_addr)


# In[44]:


female_family_names_dict = {} # Creating and filling dict with female familly names
female_family_names_addr = r'C:\Users\ASUS\Desktop\famn2.txt'
name_dict(female_family_names_dict, female_family_names_addr)


# In[45]:


city_dict = {} # Creating and filling dict with cities (and villages)
city_addr = r'C:\Users\ASUS\Desktop\city1.txt'
addr_dict(city_dict, city_addr)


# In[46]:


strt_dict = {} # Creating and filling dict with streets
strt_addr = r'C:\Users\ASUS\Desktop\strt1.txt'
addr_dict(strt_dict, strt_addr)


# In[48]:


for i in range(20):
    name, street, house, city, dob = random_client()
    print(name, 'дата рождения', dob, street, house, city)
    







