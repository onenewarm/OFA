def profileRec(using_id) :

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


    # In[2]:


    data=pd.read_csv('C:/Users/gao45/Desktop/OFA/one_for_all/testproject/user_data.csv')


    # In[3]:


    cols=['gender','age','job','MBTI']
    data['user_profile']=data[cols].apply(lambda row : " ".join(row.values.astype(str)), axis=1)
    data.drop(['gender','age','job','MBTI'], axis=1, inplace=True)
    data.head()


    # In[4]:


    tfidf_vector = TfidfVectorizer()


    # In[5]:


    tfidf_matrix = tfidf_vector.fit_transform(data['user_profile']).toarray()


    # In[6]:


    tfidf_matrix_feature = tfidf_vector.get_feature_names()


    # In[7]:


    tfidf_matrix.shape


    # In[8]:


    tfidf_matrix = pd.DataFrame(tfidf_matrix, columns=tfidf_matrix_feature, index = data.id)


    # In[9]:


    print(tfidf_matrix.shape)


    # In[10]:


    tfidf_matrix.head()


    # In[11]:


    cosine_sim = cosine_similarity(tfidf_matrix)


    # In[13]:


    cosine_sim.shape


    # In[16]:


    cosine_sim_df = pd.DataFrame(cosine_sim, index = data.id, columns = data.id)
    print(cosine_sim_df.shape)
    cosine_sim_df.head()


    # In[17]:


    def profile_recommendations(target_id, matrix, items, k=10):
        recom_idx = matrix.loc[:, target_id].values.reshape(1, -1).argsort()[:, ::-1].flatten()[1:k+1]
        recom_id = items.iloc[recom_idx, :].id.values
        recom_profile = items.iloc[recom_idx, :].user_profile.values
        target_id_list = np.full(len(range(k)), target_id)
        target_profile_list = np.full(len(range(k)), items[items.id == target_id].user_profile.values)
        d = {
            'target_id':target_id_list,
            'target_profile':target_profile_list,
            'recom_id' : recom_id,
            'recom_profile' : recom_profile
        }
        return pd.DataFrame(d)


    # In[18]:


    user_input=int(using_id)
    similar_users=profile_recommendations(user_input, cosine_sim_df, data)


    # In[24]:


    data2=pd.read_csv('C:/Users/gao45/Desktop/OFA/one_for_all/testproject/usingdata.csv')


    # In[25]:


    data2['subscriptionlist']=data2['subscriptionlist'].apply(literal_eval)
    data2.head()


    # In[26]:


    data2['subscriptionlist']=data2['subscriptionlist'].apply(lambda x : " ".join(x))
    data2=data2.rename(columns={'id':'recom_id'})


    # In[27]:


    data2=data2[['recom_id','subscriptionlist']]


    # In[28]:


    data2.head()


    # In[29]:


    result=pd.merge(similar_users,data2)
    result


    # In[30]:


    val_list=result['subscriptionlist'].values.tolist()


    # In[31]:


    subscription_list=[]
    for i in range(10):
        q=(val_list[i].split())
        length=len(q)
        for j in range(length):
            subscription_list.append(q[j])


    # In[32]:


    import collections

    counts=collections.Counter(subscription_list)


    # In[33]:


    end_result=counts.most_common(5)


    # In[34]:

    resultlist=[]
    for i in range(5):
        resultlist.append(end_result[i][0])

    return resultlist
    # In[ ]:
