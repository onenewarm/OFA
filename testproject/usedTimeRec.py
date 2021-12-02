
def usedTimeRec(using_id) :
    #!/usr/bin/env python
    # coding: utf-8

    # In[1]:

    from IPython import get_ipython
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from ast import literal_eval
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity


    # In[124]:


    data = pd.read_csv('C:/Users/gao45/Desktop/OFA/one_for_all/testproject/usingtime.csv')
    tempdata=data
    userinput=str(using_id)
    tempdata=tempdata.astype({'id':'str'})
    tempdata=tempdata[tempdata['id']==userinput]
    tempdata=tempdata['usingtime'].values.tolist()
    tempdata=eval(tempdata[0])
    print(tempdata)
    frequency_serviece=max(tempdata,key=tempdata.get)


    # In[58]:


    split = data.usingtime.str.split(',')


    # In[59]:


    split


    # In[60]:


    split=split.apply(lambda x:pd.Series(x))


    # In[61]:


    split


    # In[62]:


    split.stack()


    # In[63]:


    split.stack().reset_index(level=1, drop=True)


    # In[64]:


    split = split.stack().reset_index(level=1, drop=True).to_frame('usingtime')


    # In[65]:


    split


    # In[66]:


    split['usingtime'] = split['usingtime'].str.replace(pat=r'[^A-Za-z0-9\s]', repl= r'', regex=True)


    # In[67]:


    split


    # In[68]:


    list_from_data = split['usingtime'].values.tolist()
    temp=[]


    # In[69]:


    for i in range(len(list_from_data)) :
            temp.append(list_from_data[i].split())


    # In[70]:


    temp2=[]
    for i in range(len(list_from_data)):
        if not temp[i]:
            temp2.append("")
        else:
            temp2.append(temp[i][-1])


    # In[71]:


    split['usingtime'] = split['usingtime'].str.replace(pat=r'[^A-Za-z]', repl= r'', regex=True)
    temp3=split['usingtime'].values.tolist()


    # In[72]:


    data = pd.DataFrame(index=range(0,len(temp2)), columns=[])
    data['user_id']=split.index+1
    data['sub_name']=temp3
    data['use_time']=temp2


    # In[73]:


    data


    # In[74]:


    data['use_time'] = pd.to_numeric(data['use_time'])


    # In[75]:


    data.pivot_table(index = 'user_id', columns='sub_name', values=['use_time'], aggfunc='first')
    data = data.pivot_table('use_time', index = 'user_id', columns = 'sub_name').fillna(0)


    # In[76]:


    data = data.transpose()


    # In[77]:


    data.head()


    # In[78]:


    sub_sim = cosine_similarity(data, data)
    print(sub_sim.shape)


    # In[79]:


    sub_sim_df = pd.DataFrame(data = sub_sim, index = data.index, columns = data.index)


    # In[80]:


    sub_sim_df.head(3)


    # In[125]:


    result=sub_sim_df[frequency_serviece].sort_values(ascending=False)[1:10]


    # In[126]:


    resultlist=[]
    resultlist=result.keys()
    return resultlist
