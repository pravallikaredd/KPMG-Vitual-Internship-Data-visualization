
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[2]:


import pandas as pd
import numpy as np
import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import math as ma


# In[3]:


kmpgex = pd.ExcelFile('KPMG_final.xlsx')
kmpgex.sheet_names
df = pd.read_excel('KPMG_final.xlsx', sheetname="NewCustomerList")


# In[4]:


df.rename(columns={"Note: The data and information in this document is reflective of a hypothetical situation and client. This document is to be used for KPMG Virtual Internship purposes only. ":"fname"}, inplace = True)
df.rename(columns={"Unnamed: 1":"lname",
                   "Unnamed: 2":"gender",
                   "Unnamed: 3":"3y_bike_purchases",
                   "Unnamed: 4":"DOB",
                   "Unnamed: 5":"JT",
                   "Unnamed: 6":"Category"}, inplace = True)
df.rename(columns={"Unnamed: 7":"wealth_segement",
                   "Unnamed: 8":"D_Indicator",
                   "Unnamed: 9":"owns_car",
                   "Unnamed: 10":"tencure",
                   "Unnamed: 11":"address",
                   "Unnamed: 12":"postcode"}, inplace = True)
df.rename(columns={"Unnamed: 13":"state",
                   "Unnamed: 14":"country",
                   "Unnamed: 15":"prop_val",
                   "Unnamed: 21":"rank",
                   "Unnamed: 22":"value"}, inplace = True)
df=df.iloc[1:]
df


# In[5]:


df["state"].value_counts()


# In[9]:


y = np.array([506,266,228])
y1=[0,0,0]
s= y.sum()
y1[0]=(y[0]/s)*100
y1[1]=(y[1]/s)*100
y1[2]=(y[2]/s)*100

    
x =np.array(['NSW','VIC','QLD'])
plt.figure()
plt.bar(x,y1)
plt.xlabel('states')
plt.ylabel('percentage of customers')


# In[10]:


plt.savefig('states')


# In[11]:


kmpgex = pd.ExcelFile('KPMG_final.xlsx')
kmpgex.sheet_names
df1 = pd.read_excel('KPMG_final.xlsx', sheetname="Transactions")


# In[12]:


df1


# In[16]:


df1.rename(columns={"Note: The data and information in this document is reflective of a hypothetical situation and client. This document is to be used for KPMG Virtual Internship purposes only. ":"transaction_id"}, inplace = True)
df1.rename(columns={"Unnamed: 1":"product_id",
                   "Unnamed: 2":"customer_id",
                   "Unnamed: 3":"transaction_date",
                   "Unnamed: 4":"online_order",
                   "Unnamed: 5":"order_status",
                   "Unnamed: 6":"brand"}, inplace = True)
df1.rename(columns={"Unnamed: 7":"product_line",
                   "Unnamed: 8":"product_class",
                   "Unnamed: 9":"product_size",
                   "Unnamed: 10":"list_price",
                   "Unnamed: 11":"standard_cost",
                   "Unnamed: 12":"product first sold date"}, inplace = True)

df1=df1.iloc[1:]
df1


# In[25]:


x= np.array(['Online purchase','Inshop purchase'])


# In[28]:


y=np.array([0,0])
for i in range(2,len(df1['online_order'])):
    if df1['online_order'][i]==True:
        y[0]+=1
    else:
        y[1]+=1
y


# In[33]:


s=y.sum()
y1=[0,0]
s= y.sum()
y1[0]=(y[0]/s)*100
y1[1]=(y[1]/s)*100

plt.figure()
plt.bar(x,y1,width=0.4)
plt.xlabel('Mode of Purchase')
plt.ylabel('Percentage of customers')


# In[34]:


plt.savefig('image4')


# In[35]:


df1["brand"].value_counts()


# In[37]:


y = [4252,3312,3295,3043,2990,2910]
x = ['Solex','Giant','WeareA2B','OHM','Trek','Norco']
plt.figure()
plt.bar(x,y,width=0.4)
plt.xlabel('Brands')
plt.ylabel('No. of sales')


# In[38]:


plt.savefig('imgage5.png')


# In[43]:


df1['product_class'].value_counts()


# In[44]:


x= ['Low','Medium','High']
y= [2964,13825,3013]
plt.figure()
plt.bar(x,y,width=0.3)
plt.xlabel('Product class')
plt.ylabel('No. of purchases')


# In[45]:


plt.savefig('image6.png')


# In[46]:


df1['product_size'].value_counts()


# In[50]:


x= ['small','Medium','Large']
y= [2837,12989,3976]
plt.figure()
plt.bar(x,y,width=0.3)
plt.xlabel('Product size')
plt.ylabel('No. of purchases')


# In[51]:


plt.savefig('image7.png')


# In[52]:


df1['product_line'].value_counts()


# In[53]:


x=['Standard','Road','Touring','Mountain']
y = [14175,3970,1234,432]
plt.figure()
plt.bar(x,y,width=0.2)
plt.xlabel('Product line')
plt.ylabel('No. of purchases')


# In[54]:


plt.savefig('image8.png')

