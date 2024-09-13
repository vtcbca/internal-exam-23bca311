#!/usr/bin/env python
# coding: utf-8

# ### Create python.txt file . Take input from user till user choise and write it into python.txt. Take start and end line number from user and print only those line.

# In[14]:


f=open("D:\\23bca311\\sqlite-tools-win-x64-3460000(1)\\database\\python01.txt",'w')


# In[15]:


line=[]
while True:
    l=input("enter any value:")
    if l:
        line.append(l+"\n")
    else:
        break
text="\n".join(line) 


# In[16]:


start_line=int(input("enter start line number:"))


# In[18]:


end_line=int(input("enter end line number:"))


# In[19]:


f.close()


# In[33]:


f=open("D:\\23bca311\\sqlite-tools-win-x64-3460000(1)\\database\\python01.txt",'r')


# In[34]:


f.read()


# In[35]:


line=f.readlines()
for i in range(start_line-1,end_line):
   print(i)


# In[ ]:




