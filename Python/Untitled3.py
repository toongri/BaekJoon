#!/usr/bin/env python
# coding: utf-8

# ##  실습
# - riot api grandmaster 구간 데이터 가져오기
# - 첫번째 df는 gameId, matches, timelines
# - matches 컬럼을 이용해서 새로운 match_df 생성
# - match_df 컬럼은 gameId, gameDuration, gameVersion,summonerName, summonerLevel. participantId, championName, champExperience, teamPosition, teamId, vin...
# ('gameId','gameDuration','gameVersion','summonerName','summonerLevel','participantId',
#                                    'championName','champExperience','teamPosition','teamId','win','kills','deaths','assists',
#                                   'totalDamageDealtToChampions','totalDamageTaken'
# 
# - table 생성하고 insert 
# - api 사용 부분에서는 limit 유의하여 랜덤 또는 순차적 20개씩 수집 
# - table 생성ㅇ하고 insert까지

# In[5]:


import my_utils as mu
import pandas as pd
import requests
from tqdm import tqdm
tqdm.pandas()


# In[3]:


riot_api_key='RGAPI-6f742a17-a269-4b78-8c67-377019093a99'


# In[7]:


url='https://kr.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key='+riot_api_key


# In[12]:


url


# In[8]:


res=requests.get(url).json()


# In[9]:


res


# In[10]:


res.keys()


# In[11]:


res['entries']


# In[14]:


summonerName_lst=list(map(lambda x: x['summonerName'], res['entries']))
summonerName_lst


# In[15]:


len(summonerName_lst)


# In[16]:


puuid_lst=[]
for n in summonerName_lst[:20]:
    try:
        puuid_lst.append(mu.get_puuid(n))
    except:
        continue


# In[21]:


matchId_lst=[]
for p in puuid_lst:
    matchId_lst=matchId_lst+mu.get_matchId(p, 5)


# In[22]:


len(puuid_lst)


# In[23]:


len(matchId_lst)


# In[24]:


matchId_lst


# In[26]:


from random import sample


# In[27]:


matchIds=sample(matchId_lst, 20)
matchIds


# In[48]:


tmp=[]
for m_id in tqdm(matchIds):
    tmp_lst= []
    tmp_lst.append(m_id)
    matches, timelines=mu.get_matches_timelines(m_id)
    tmp_lst.append(matches)
    tmp_lst.append(timelines)
    tmp.append(tmp_lst)


# In[49]:


df=pd.DataFrame(tmp, columns=['gameId', 'match', 'timeline'])
df.head()


# In[ ]:


df[]


# In[60]:


lst=[]
for i in range(len(df)):
    for j in range(10):
        tmp=[]
        tmp.append(df.iloc[i].gameId)
        tmp.append(df.iloc[i].match['info']['gameDuration'])
        tmp.append(df.iloc[i].match['info']['gameVersion'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['summonerName'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['summonerLevel'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['participantId'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['championName'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['champExperience'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['teamPosition'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['teamId'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['win'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['kills'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['deaths'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['assists'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['totalDamageDealtToChampions'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['totalDamageTaken'])
        lst.append(tmp)


# In[61]:


my_df=pd.DataFrame(lst, columns=['gameId','gameDuration','gameVersion','summonerName','summonerLevel','participantId',
                                   'championName','champExperience','teamPosition','teamId','win','kills','deaths','assists',
                                  'totalDamageDealtToChampions','totalDamageTaken'])


# In[62]:


my_df[:20]


# In[63]:


query = """
create table matches(gameId varchar(20), gameDuration number(20), gameVersion varchar(50), summonerName varchar(50),
summonerLevel number(20), participantId number(20), championName varchar(50), champExperience number(20),
teamPosition varchar(50), teamId number(20), win varchar(50), kills number(20), deaths number(20), assists number(20),
totalDamageDealtToChampions number(20), totalDamageTaken number(20))
"""


# In[64]:


query2='select*from matches'


# In[30]:


mu.db_open()


# In[65]:


res=mu.sql_excute(query)
res


# In[66]:


res=mu.sql_excute(query2 )
res


# In[ ]:


query=(f'insert into matches(game))


# In[83]:


def insert(row):
    query=(
        f'insert into matches(gameId, gameDuration, gameVersion, summonerName, summonerLevel, participantId, championName, champExperience, '
        f'teamPosition,teamId, win, kills, deaths, assists, totalDamageDealtToChampions, totalDamageTaken)'
        f'values(\'{row.gameId}\', {row.gameDuration}, '
        f'\'{row.gameVersion}\', \'{row.summonerName}\', {row.summonerLevel}, {row.participantId},'
        f'\'{row.championName}\', {row.champExperience}, \'{row.teamPosition}\', {row.teamId},'
        f'\'{row.win}\', {row.kills}, {row.deaths},{row.assists},'
        f'{row.totalDamageDealtToChampions},{row.totalDamageTaken})')
    mu.sql_excute(query)


# In[84]:


my_df.progress_apply(lambda x: insert(x), axis=1)


# In[85]:


res=mu.sql_excute('select*from matches')
res


# In[88]:


df.timeline.iloc[0]['info']


# In[86]:


df.timeline.iloc[0]['info']['frames'][14]['participantFrames']['2']


# - timeline 
# - gameId, participantId, g.5, g.6, ~ 10분까지  

# In[108]:


res


# In[95]:


lst=[]
for i in range(len(df)):
    for j in range(10):
        tmp=[]
        tmp.append(df.iloc[i].gameId)
        #for i in range(5,11):
            #tmp.append(df.iloc[i]['timeline'][info]['participants'][j]['participantId'])
        tmp.append(df.iloc[i]['timeline']['info']['participants'][j]['participantId'])
        tmp.append(df.iloc[i]['timeline']['info']['frames'][5]['participantFrames'][str(j+1)]['totalGold'])
        tmp.append(df.iloc[i]['timeline']['info']['frames'][6]['participantFrames'][str(j+1)]['totalGold'])
        tmp.append(df.iloc[i]['timeline']['info']['frames'][7]['participantFrames'][str(j+1)]['totalGold'])
        tmp.append(df.iloc[i]['timeline']['info']['frames'][8]['participantFrames'][str(j+1)]['totalGold'])
        tmp.append(df.iloc[i]['timeline']['info']['frames'][9]['participantFrames'][str(j+1)]['totalGold'])
        tmp.append(df.iloc[i]['timeline']['info']['frames'][10]['participantFrames'][str(j+1)]['totalGold'])
        lst.append(tmp)


# In[96]:


lst


# In[114]:


tier_lst=['I', 'II', 'III', 'IV']


# In[115]:


url='https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/GOLD/'+t+'?page=1&api_key='+riot_api_key
res=requests.get(url).json()


# In[119]:


res


# In[117]:


lst=[]
for t in tier_lst:
    url='https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/GOLD/'+t+'?page=1&api_key='+riot_api_key
    res=requests.get(url).json()
    lst=lst+sample(list(map(lambda x: x['summonerName'], res)), 5)


# In[118]:


len(lst)


# In[ ]:





# In[97]:


url='https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/GOLD/III?page=1&api_key='+riot_api_key


# In[98]:


url


# In[99]:


res=requests.get(url).json()


# In[100]:


res


# In[101]:


len(res)


# In[42]:


from random import sample
import random
from tqdm import tqdm
import my_utils as mu
import pandas as pd
import requests
tqdm.pandas()


# In[4]:


riot_api_key='RGAPI-6f742a17-a269-4b78-8c67-377019093a99'


# In[2]:


tier_lst=['I', 'II', 'III', 'IV']


# In[ ]:





# In[43]:


lst=[]
p=random.randrange(1,10)
for t in tqdm(tier_lst):
    url='https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/GOLD/'+t+'?page='+str(p)+'&api_key='+riot_api_key
    res=requests.get(url).json()
    lst=lst+sample(res, 5)


# In[7]:


url='https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/GOLD/'+t+'?page=1&api_key='+riot_api_key
res=requests.get(url).json()


# In[8]:


res


# In[11]:


lst=[]
for t in tqdm(tier_lst):
    url='https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/GOLD/'+t+'?page=1&api_key='+riot_api_key
    res=requests.get(url).json()
    lst=lst+sample(res,5)


# In[13]:


summonerName_lst=list(map(lambda x: x['summonerName'], lst))
summonerName_lst


# In[29]:


puuId_lst=[]
for n in tqdm(summonerName_lst):
    try:
        puuId_lst.append(mu.get_puuid(n))
    except:
        continue


# In[30]:


len(puuId_lst)


# In[31]:


matchId_lst=[]
for p in tqdm(puuId_lst):
    matchId_lst=matchId_lst+mu.get_matchId(p,3)


# In[32]:


import time


# In[33]:


time.sleep(5)
print('test')


# In[35]:


tmp=[]
for m_id in tqdm(matchId_lst):
    tmp_lst=[]
    tmp_lst.append(m_id)
    matches, timelines=mu.get_matches_timelines(m_id)
    tmp_lst.append(matches)
    tmp_lst.append(timelines)
    tmp.append(tmp_lst)


# In[ ]:


# tmp=[]
# for m_id in tqdm(matches):
#     tmp_lst=[]
#     tmp_lst.append(m_Id)
#     matches, timelines= mu.get_matches_timelines(m_Id)
#     tmp_lst.append(matches)
#     tmp_lst.append(timelines)
#     tmp.append(tmp_lst)


# In[38]:


df=pd.DataFrame(tmp, columns=['gameId', 'match', 'timeline'])
df.head()


# In[ ]:


# list(map(lambda x: [mu.get_matches_timelines(x)], matchId_lst))


# ### 데이터 수집 함수화
# - gameId, match, timeline으로 구성된 원시데이터 df 만드는 함수 (인자값으로 티어 ex.gold~)
# 
# - 원시데이터 df를 인풋으로 넣어서  아웃풋으로 match_df, timeline_df (인자값이 원시데이터 df)
# - match_df['~~~
# - timeline_df[ 'gameId', 'participantId', 'g5', 'g6', -'g25']
# -3) db에 insert (인자값이 전처리를 진행한 match_df, timeline_df
# - match_pk timelike_pk=gameId, participantId
# -insert하기 전에 dataframe 중복 제거 
# - match_df, timeline_df컬럼값 임의로 추천해드린 것. -추후 프로젝트에 개인적으로 필요한 데이터가 있으면 추가해서 수집 가능 

# In[44]:


#cycle
tier='gold'
data=source_data(tier)

match_df, timeline_df=preprocessing(data)

mu.db_open()
match_insert(match_df)
timeline_insert(timeline_df)
#400개 insert


# In[ ]:


import time
for i in range(10):
    print(i)
    time.sleep(2)


# In[ ]:


mu.db_open()
match_df=mu.sql_excute('select*from matdh~')
timeline_df=mu.sql_excute('select *from timeline~')
mu.db_close()


# In[45]:


def tier='gold'
data=source_data(tier)

match_df, timeline_df=preprocessing(data)
mu.db_open()
match_insert(match_df)
timeline 


# In[ ]:


def my_df()
    


    my_df=pd.DataFrame[lst, columns=['gameId', 'match', 'timeline']]


# In[ ]:





# In[ ]:


tmp=[]
for m_id in tqdm(matchIds):
    tmp_lst= []
    tmp_lst.append(m_id)
    matches, timelines=mu.get_matches_timelines(m_id)
    tmp_lst.append(matches)
    tmp_lst.append(timelines)
    tmp.append(tmp_lst)


# In[ ]:


lst=[]
for i in range(len(df)):
    for j in range(10):
        tmp=[]
        tmp.append(df.iloc[i].gameId)
        tmp.append(df.iloc[i].match['info']['gameDuration'])
        tmp.append(df.iloc[i].match['info']['gameVersion'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['summonerName'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['summonerLevel'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['participantId'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['championName'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['champExperience'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['teamPosition'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['teamId'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['win'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['kills'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['deaths'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['assists'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['totalDamageDealtToChampions'])
        tmp.append(df.iloc[i].match['info']['participants'][j]['totalDamageTaken'])
        lst.append(tmp)


# In[ ]:


def tier_lst=[]
    for i in range(len(df)):
        for j in r


# In[ ]:


q

