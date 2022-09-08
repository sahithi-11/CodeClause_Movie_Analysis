#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Code Clause\IMDB-Movie-Data.csv")


# In[3]:


data.head(10)


# In[4]:


data.tail(10)


# In[5]:


data.shape


# In[6]:


print("Number of Rows in the Dataset",data.shape[0])
print("Number of Columns in the Dataset",data.shape[1])


# In[7]:


data.info()


# In[10]:


print("Any Missing values",data.isnull().values.any())


# In[13]:


data.isnull().sum()


# In[14]:


data.dropna(axis=0,inplace=True)


# In[15]:


data


# In[19]:


print("Any duplicate values",data.duplicated().any())


# In[21]:


data.describe(include="all")


# In[22]:


data.columns


# In[27]:


#Title of the movie which has runtime more than 180 minutes


# In[30]:


data[data["Runtime (Minutes)"]>=180][["Title","Runtime (Minutes)"]]


# In[ ]:


# In which year there was the highest average voting


# In[32]:


data.groupby("Year")["Votes"].mean().sort_values(ascending=False)


# In[37]:


sns.barplot(x="Year",y="Votes",data=data)
plt.title("Votes by year")
plt.show()


# In[38]:


#in which year there was highest average revenue


# In[39]:


data.groupby("Year")["Revenue (Millions)"].mean().sort_values(ascending=False)


# In[41]:


sns.barplot(x="Year",y="Revenue (Millions)",data=data)
plt.title("Revenue by Year")
plt.show()


# In[42]:


#finding the average rating for each director


# In[44]:


data.groupby("Director")["Rating"].mean().sort_values(ascending=False)


# In[45]:


sns.barplot(x="Director",y="Rating",data=data)
plt.title("Rating for directors")
plt.show()


# In[46]:


#displaying top 10 lengthy movies title and runtime


# In[48]:


top10_len=data.nlargest(10,"Runtime (Minutes)")[["Title","Runtime (Minutes)"]].set_index("Title")


# In[49]:


top10_len


# In[52]:


sns.barplot(x="Runtime (Minutes)",y=top10_len.index,data=top10_len)


# In[53]:


#Display number of movies per year


# In[54]:


data["Year"].value_counts()


# In[56]:


sns.countplot(x="Year",data=data)
plt.title("Number of movies per year")
plt.show()


# In[57]:


#Find most popular Movie Title


# In[65]:


data[data["Revenue (Millions)"].max()==data["Revenue (Millions)"]]["Title"]


# In[66]:


#Finding top 10 rating movie Titles and Directors


# In[81]:


top10_rat=data.nlargest(10,"Rating")[["Title","Rating","Director"]].set_index("Title")


# In[82]:


top10_rat


# In[83]:


sns.barplot(x="Rating",y=top10_rat.index,data=top10_rat)
plt.title("Highest rating")
plt.show()


# In[86]:


#Display top 10 highest revenue movie titles


# In[87]:


top10_rev=data.nlargest(10,"Revenue (Millions)")[["Title","Revenue (Millions)"]].set_index("Title")


# In[88]:


top10_rev


# In[93]:


sns.barplot(x="Revenue (Millions)",y=top10_rev.index,data=top10_rev)
plt.title("Highest revenue movies")
plt.show()


# In[94]:


#Finding avearae rating of movie year wise


# In[96]:


data.groupby("Year")["Rating"].mean().sort_values(ascending=False)


# In[97]:


#Does rating effect Revenue


# In[98]:


sns.scatterplot(x="Revenue (Millions)",y="Rating",data=data)
plt.title("rating vs revenue")
plt.show()


# In[99]:


#classifying movies based as rating


# In[100]:


def rating(rating):
    if rating>=7.0:
        return "Excellent"
    elif rating>=6.0:
        return "Good"
    else:
        return "Average"


# In[103]:


data["data_categories"]=data["Rating"].apply(rating)


# In[104]:


data


# In[105]:


#count number of action movies


# In[109]:


len(data[data["Genre"].str.contains("Action",case=False)])


# In[110]:


#Find unique values from Genre


# In[111]:


data["Genre"]


# In[122]:


list1=[]
for i in data["Genre"]:
    list1.append(i.split(","))
   


# In[123]:


list1


# In[126]:


oned=[]
for i in list1:
    for j in i:
        oned.append(j)


# In[127]:


oned


# In[130]:


uni=[]
for i in oned:
    if i not in uni:
        uni.append(i)


# In[131]:


uni


# In[132]:


len(uni)


# In[133]:


#How many films of each genre


# In[135]:


from collections import Counter


# In[141]:


Counter(oned)


# In[ ]:




