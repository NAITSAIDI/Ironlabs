#!/usr/bin/env python
# coding: utf-8

# # [Rr]eg[Ee]xp? Lab
# 
# # Challenge 1- Regular Expressions
# 
# Sometimes, we would like to perform more complex manipulations of our string. This is where regular expressions come in handy. In the cell below, return all characters that are upper case from the string specified below.

# In[15]:


import re


# In[16]:




poem = """The apparition of these faces in the crowd;
Petals on a wet, black bough."""


# Your code here:
pattern = '[A-Z]'
list=re.findall(pattern, poem )
print(list)


# In the cell below, filter the list provided and return all elements of the list containing a number. To filter the list, use the `re.search` function. Check if the function does not return `None`. You can read more about the `re.search` function [here](https://docs.python.org/3/library/re.html).

# In[20]:


data = ['123abc', 'abc123', 'JohnSmith1', 'ABBY4', 'JANE']
for item in data:
    if re.search('[0-9]', item) == None:
        data.remove(item)
print(data)


# # Challenge 2 - Regular Expressions II
# 
# In the cell below, filter the list provided to keep only strings containing at least one digit and at least one lower case letter. As in the previous question, use the `re.search` function and check that the result is not `None`.
# 
# To read more about regular expressions, check out [this link](https://developers.google.com/edu/python/regular-expressions).

# In[21]:


data = ['123abc', 'abc123', 'JohnSmith1', 'ABBY4', 'JANE']
data_list=[]
for i in range(0,len(data)):
    if re.search(r'\d', data[i]) != None and re.search(r'[a-z]', data[i]):
        data_list.append(data[i])
print(data_list)              


# In[12]:



Regex=("^(?=.*[a-z])(?=.*\\d)" .+$")
       
     


# In[22]:


re.search ("c.+", "abcmdj").group()


# # Challenge 3 -  Advanced Regular Expressions
# 
# Complete the following set of exercises to solidify your knowledge of regular expressions.

# In[20]:


import re


# In[ ]:





# ### 1. Use a regular expression to find and extract all vowels in the following text.

# In[27]:


text = "This is going to be a sentence with a good number of vowels in it."


# In[32]:


vowels = ["a","e","i","o","u"]
for i in text:
    if i in vowels:
        text=text.replace(i,"")
print(text)


# ### 2. Use a regular expression to find and extract all occurrences and tenses (singular and plural) of the word "puppy" in the text below.

# In[33]:


text = "The puppy saw all the rest of the puppies playing and wanted to join them. I saw this and wanted a puppy of my own!"


# In[34]:


p= re.findall(r'puppy|puppies', text)
p


# ### 3. Use a regular expression to find and extract all tenses (present and past) of the word "run" in the text below.

# In[41]:


text = "I ran the relay race the only way I knew how to run it."


# In[59]:


import re


# In[47]:


t=re.findall(r'r.n',text)
t


# ### 4. Use a regular expression to find and extract all words that begin with the letter "r" from the previous text.

# In[60]:


text = "I ran the relay race the only way I knew how to run it."


# In[62]:


x = re.findall(r'[r]\w+', text)
print (x)


# ### 5. Use a regular expression to find and substitute the letter "i" for the exclamation marks in the text below.

# In[42]:


text = "Th!s !s a sentence w!th spec!al characters !n !t."


# In[43]:


text.replace("!","i")


# ### 6. Use a regular expression to find and extract words longer than 4 characters in the text below.

# In[23]:


text = "This sentence has words of varying lengths."


# In[24]:


words= x=re.findall("\w{5,}", text)
print(words)


# ### 7. Use a regular expression to find and extract all occurrences of the letter "b", some letter(s), and then the letter "t" in the sentence below.

# In[31]:


text = "I bet the robot couldn't beat the other bot with a bat, but instead it bit me."


# In[32]:



words=re.findall("b[a-z]t", text)
print (words)


# ### 8. Use a regular expression to find and extract all words that contain either "ea" or "eo" in them.

# In[33]:


text = "During many of the peaks and troughs of history, the people living it didn't fully realize what was unfolding. But we all know we're navigating breathtaking history: Nearly every day could be — maybe will be — a book."


# In[34]:


words=re.findall("[a-zA-Z]+e[ao][a-z]+", text)
print(words)


# ### 9. Use a regular expression to find and extract all the capitalized words in the text below individually.

# In[35]:


text = "Teddy Roosevelt and Abraham Lincoln walk into a bar."


# In[37]:


words=re.findall("[A-Z]+[a-z]+", text)
print(x)


# ### 10. Use a regular expression to find and extract all the sets of consecutive capitalized words in the text above.

# In[38]:


words=re.findall("[A-Z]+[a-z]+\s+[A-Z]+[a-z]+", text)
print(x)


# ### 11. Use a regular expression to find and extract all the quotes from the text below.
# 
# *Hint: This one is a little more complex than the single quote example in the lesson because there are multiple quotes in the text.*

# In[39]:


text = 'Roosevelt says to Lincoln, "I will bet you $50 I can get the bartender to give me a free drink." Lincoln says, "I am in!"'


# In[43]:


x= re.findall('"[^"]+"',text)
print (x)


# ### 12. Use a regular expression to find and extract all the numbers from the text below.

# In[44]:


text = "There were 0 students in the class. Of the 30 students, 14 were male and 16 were female. Only 10 students got A's on the exam."


# In[45]:


x= re.findall('[0-9]{1,}',text)
print (x)


# ### 13. Use a regular expression to find and extract all the social security numbers from the text below.

# In[46]:


text = """
Henry's social security number is 876-93-2289 and his phone number is (847)789-0984.
Darlene's social security number is 098-32-5295 and her phone number is (987)222-0901.
"""


# In[47]:


x= re.findall('[0-9]{3}-[0-9]{2}-[0-9]{4}',text)
print (x)


# ### 14. Use a regular expression to find and extract all the phone numbers from the text below.

# In[49]:


x=re.findall('\S[0-9]{3}\S[0-9]{3}-[0-9]{4}',text)
print (x)


# ### 15. Use a regular expression to find and extract all the formatted numbers (both social security and phone) from the text below.

# In[50]:


x=re.findall('\S{,1}[0-9]{3}\S{,1}[0-9]{2,3}-[0-9]{4}',text)
print(x)


# In[ ]:




