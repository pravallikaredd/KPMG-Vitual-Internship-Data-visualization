
# coding: utf-8

# In[163]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[164]:


#get_ipython().run_line_magic('matplotlib', 'nootebook')
import pandas as pd
import numpy as np
import datetime
import matplotlib as mpl
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import warnings
import math as ma
warnings.filterwarnings("ignore")
mpl.get_backend()


# In[165]:


kmpgex = pd.ExcelFile('KPMG_final.xlsx')
kmpgex.sheet_names
df = pd.read_excel('KPMG_final.xlsx', sheetname="CustomerDemographic")
#list(df)


# In[166]:


df.rename(columns={"Note: The data and information in this document is reflective of a hypothetical situation and client. This document is to be used for KPMG Virtual Internship purposes only. ":"customer_id"}, inplace = True)
df.rename(columns={"Unnamed: 1":"fname",
                   "Unnamed: 2":"lname",
                   "Unnamed: 3":"gender",
                   "Unnamed: 4":"3y_bike_purchases",
                   "Unnamed: 5":"DOB",
                   "Unnamed: 6":"JT"}, inplace = True)
df.rename(columns={"Unnamed: 7":"Category",
                   "Unnamed: 8":"wealth_segement",
                   "Unnamed: 9":"D_Indicator",
                   "Unnamed: 10":"default",
                   "Unnamed: 11":"owns_car",
                   "Unnamed: 12":"tenure"}, inplace = True)
df=df.iloc[1:]
df


# In[167]:


def check_NA():
    ret = []
    temp = list(df)
    for each in temp:
        ret.append(df[each].isna().sum())
    return ret

NaNlist = check_NA()
print(NaNlist, len(NaNlist))
# need to check columns
check = []
k     = -1
for i in NaNlist:
    k += 1
    if i > 0:
        check.append(k)
def check_unique():
    temp = list(df)
    mydict = {}
    for i in range(3, 13):
        ct = 0
        if NaNlist[i] > 0:
            ct = len(df[temp[i]].unique()) - 1
        else:
            ct = len(df[temp[i]].unique())
        mydict[temp[i]] = (ct, df[temp[i]].unique())
    return mydict


# In[168]:


x = list(df['gender'])


# In[169]:


x


# In[172]:


print(df["DOB"][1].ctime().split(" ")[4])
df["Age"] = 0
lenn = len(df["DOB"])
k    = 0
for i in range(1, lenn):
    if isinstance(df["DOB"][i], datetime.date):
        tl = len(df["DOB"][i].ctime().split(" "))
        df["Age"][i] += int(2019 - int(df["DOB"][i].ctime().split(" ")[tl-1]))
    elif isinstance(df["DOB"][i], str):
        tl = len(df["DOB"][i].split("-"))
        df["Age"][i] += int(2019 - int(df["DOB"][i].split("-")[tl-1])) 

print(k)


# In[ ]:


df


# In[171]:


len(list(df['tencure']))


# In[173]:


x = np.array(list(df['Age']))
x


# In[174]:


y = np.array( list(df['tencure']))
y


# In[175]:


plt.figure()
plt.scatter(x,y)
ax=plt.gca()
ax.axis([0,90,0,70])
plt.xlabel('Age')
plt.ylabel('Tenure')


# In[176]:


gender = np.array([0,0,0])
bike = np.array([0,0,0])
for each in df['gender']:
    if each[0] == "F":
        gender[0] += 1
    elif each[0] == "M":
        gender[1] += 1
    else:
        gender[2] += 1
bike[0] += df['3y_bike_purchases'][df['gender'] == 'Male'].sum() + df['3y_bike_purchases'][df['gender'] == 'M'].sum()
bike[1] += df['3y_bike_purchases'][df['gender'] == 'Female'].sum() + df['3y_bike_purchases'][df['gender'] == 'F'].sum()
bike[2] += df['3y_bike_purchases'][df['gender'] == 'U'].sum()


# In[177]:


gender


# In[178]:


bike


# In[189]:


x = np.array(['Male','Female','Unknown'])
plt.figure()
plt.bar(x,bike)


# In[190]:


y=bike.sum()
y


# In[191]:


y =np.array([0,0,0])
for i in range(len(y)):
    y[0]=(bike[0]/bike.sum())*100
    y[1]=(bike[1]/bike.sum())*100
    y[2]=(bike[2]/bike.sum())*100
y

    


# In[192]:


plt.figure()
plt.bar(x,y)
plt.xlabel('Gender')
plt.ylabel('Percentage of bikes bought in last 3 years')


# In[193]:


age=np.array([0,0,0,0])
for i in range(1,len(df['Age'])):
    if df['Age'][i]<=25:
        age[0]+=1
    elif df['Age'][i]>25 and df['Age'][i]<50:
        age[1]+=1
    elif df['Age'][i]>=50 and df['Age'][i]<60:
        age[2]+=1
    else:
        age[3]+=1
age


# In[69]:


x = np.array(['<25','25-50','50-60','>60'])
plt.figure()
plt.bar(x,age)
plt.xlabel('Age range')
plt.ylabel('no.of customers')


# In[194]:


fgen=[]
fage=[]
mgen=[]
mage=[]
ugen=[]
uage=[]
for i in df.index:
    if df['gender'][i]=='Female':
        fgen.append(i)
        fage.append(df['Age'][i])
    elif df['gender'][i]=='Male':
        mgen.append(i)
        mage.append(df['Age'][i])
    if df['gender'][i]=='U':
        ugen.append(i)
        uage.append(df['Age'][i])
mage


# In[184]:


far=np.array([0,0,0,0])
for i in range(1,len(fage)):
    if fage[i]<=25:
        far[0]+=1
    elif fage[i]>25 and fage[i]<50:
        far[1]+=1
    elif fage[i]>=50 and fage[i]<60:
        far[2]+=1
    else:
        far[3]+=1
far
    


# In[195]:


x = np.array(['<25','25-50','50-60','>60'])
mar=np.array([0,0,0,0])
for i in range(1,len(mage)):
    if mage[i]<=25:
        mar[0]+=1
    elif mage[i]>25 and mage[i]<50:
        mar[1]+=1
    elif mage[i]>=50 and mage[i]<60:
        mar[2]+=1
    else:
        mar[3]+=1
mar


# In[186]:


uar=np.array([0,0,0,0])
for i in range(1,len(uage)):
    if uage[i]<=25:
        uar[0]+=1
    elif uage[i]>25 and uage[i]<50:
        uar[1]+=1
    elif uage[i]>=50 and uage[i]<60:
        uar[2]+=1
    else:
        uar[3]+=1
uar


# In[196]:


plt.figure()
plt.bar(x,far,label='female')
plt.bar(x,mar,label='male')
plt.bar(x,uar,label='unknown gender')
plt.xlabel('age ranges')
plt.ylabel('no.of customers for each gender')
plt.legend()
plt.savefig('image2.png')


# In[197]:


x = np.array([0,0])
for i in df.index:
    if df['owns_car'][i]=='Yes':
        x[0]+=1
    else:
        x[1]+=1
x


# In[125]:


y = np.array(['owns_car','no_car'])
plt.figure()
plt.bar(y,x)
plt.xlabel('whether or not owns a car')
plt.ylabel('no.of customers')


# In[201]:


x = np.array(['Manu', 'Finance', 'Health', 'Retail', 'Property', 'IT', 'Entertainment', 'Agri', 'Telecom'])
len(df['JT'].unique())
df["Category"].value_counts()


# In[207]:


val = [203, 199, 152, 78, 64, 51, 37, 26, 25]
x = ['Manu', 'Finance', 'Health', 'Retail', 'Property', 'IT', 'Entertainment', 'Agri', 'Telecom']


# In[208]:


plt.figure()


# In[209]:


plt.bar(x,val)


# In[212]:


plt.xticks(rotation=45)


# In[213]:


plt.xlabel('Job category')
plt.ylabel('no.of customers')

