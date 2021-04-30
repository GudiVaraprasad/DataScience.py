#!/usr/bin/env python
# coding: utf-8

# # IPL Data Analysis and Data Visualization Using Python

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Load Data

# In[2]:


data = pd.read_csv("./IPL_Matches_2008_2020.csv")


# In[3]:


data.head()


# In[4]:


data.head(-5)


# In[5]:


data.tail()


# In[6]:


data.info()


# In[7]:


# drop the method feature
data.drop(['method'], axis=1)


# In[8]:


data.info()


# In[9]:


# drop the method feature
data.drop(['method'], axis=1)


# In[10]:


# drop the method feature and update dataframe
data.drop(['method'], axis=1, inplace=True)


# In[11]:


data


# ### Most Wins in IPL

# In[12]:


temp = pd.DataFrame({"Winner": data['winner']})
count_wins = temp.value_counts()
print(count_wins)


# In[13]:


labels = [X[0] for X in count_wins.keys()]

bar, ax = plt.subplots(figsize=(20,12))
ax = plt.pie(x = count_wins, autopct = "%.2f", labels=labels)
plt.title("Most wins in IPL",  fontsize=21)
plt.show()


# ### Most Wins in Eliminator

# In[14]:


sns.countplot(data['winner'][data['eliminator']=='Y'], data = data)
plt.title("Most wins in Eliminator", fontsize = 21)
plt.xticks(rotation = 90)
plt.show()


# ### Toss Decision

# In[15]:


teams = data['toss_winner'].unique()
teams


# In[16]:


teams = data['toss_winner'].unique()

decision_making = pd.DataFrame([], columns = ['Toss Winner', 'Decision', 'Times'])

for id, element in enumerate(teams):
    temp_bat = data[(data['toss_winner']==element)& (data['toss_decision']=='bat')]
    temp_field = data[(data['toss_winner']==element)& (data['toss_decision']=='field')]
    
    # append to decison making
    decision_making = decision_making.append({'Toss Winner': element,
                                            'Decision':'bat', 'Times': temp_bat['toss_winner'].count()}, ignore_index = True)
    decision_making = decision_making.append({'Toss Winner': element,
                                            'Decision':'field', 'Times': temp_field['toss_winner'].count()}, ignore_index = True)


# In[17]:


decision_making


# In[18]:


sns.catplot(x="Toss Winner", y="Times", hue="Decision", data=decision_making, kind='bar', height=5, aspect=2)

plt.xticks(rotation=90)
plt.title("Toss Decision of Teams")
plt.xlabel("IPL Teams")
plt.ylabel("Toss Decision")
plt.show()


# ### Famous Venue

# In[19]:


sns.barplot(x=data['venue'].value_counts().head(8).values,
           y=data['venue'].value_counts().head(8).index,
           data = data)
plt.title("Famous Venue")
plt.xlabel("Venue Count")
plt.ylabel("Venue")


# ### Top 10 Famous Venues

# In[20]:


sns.barplot(x=data['venue'].value_counts().head(10).values,
           y=data['venue'].value_counts().head(10).index,
           data = data)
plt.title("Famous Venue")
plt.xlabel("Venue Count")
plt.ylabel("Venue")
plt.show()


# ### All Venues played

# In[21]:


sns.barplot(x=data['venue'].value_counts().values,
           y=data['venue'].value_counts().index,
           data = data)
plt.title("Famous Venue")
plt.xlabel("Venue Count")
plt.ylabel("Venue")


# ### Top 5 Umpires1

# In[22]:


sns.barplot(x=data['umpire1'].value_counts().head(5).values,
           y=data['umpire1'].value_counts().head(5).index,
           data = data)
plt.title("Top 5 Umpires 1")
plt.xlabel("Umpire 1")
plt.ylabel("Match count")
plt.show()


# ### Top 5 Umpires2

# In[23]:


sns.barplot(x=data['umpire2'].value_counts().head(5).values,
           y=data['umpire2'].value_counts().head(5).index,
           data = data)
plt.title("Top 5 Umpires 2")
plt.xlabel("Umpire 2")
plt.ylabel("Match count")
plt.show()


# ### References :

# 1. Dataset downloaded from kaggle - [Click Here to download](https://www.kaggle.com/patrickb1912/ipl-complete-dataset-20082020)
# 2. Pandas References - [Click Here](https://pandas.pydata.org/docs/user_guide/index.html)
# 3. Matplotlib References - [Click Here](https://www.tutorialspoint.com/matplotlib/index.htm)
# 4. Seaborn Help - [Click Here](https://www.tutorialspoint.com/seaborn/index.htm)
# 5. Project Idea - [Click Here](https://github.com/GudiVaraprasad)

# ## End of Analysis by Gudi Varaprasad
