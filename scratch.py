import pandas as pd
import json
import re
import requests

# pay dashboard https://medium.com/me/partner/dashboard?format=json&limit=5000
# stats page https://medium.com/@doug-foo/stats?format=json&limit=5000000000000

stats = open('data.txt', 'r', encoding='utf-8').read()
paystats = open('paydata.txt', 'r', encoding='utf-8').read()

# Remove unnecessary preceding characters and save as DataFrame
dfs=pd.DataFrame(json.loads(re.sub(r'^.*?{', '{', stats)))
dfps=pd.DataFrame(json.loads(re.sub(r'^.*?{', '{', paystats)))

# Extract story stats
df_stats=pd.json_normalize(dfs.loc['value', 'payload'], sep='_')
df_paystats=pd.json_normalize(dfps.loc['postAmounts','payload'], sep='_')

publishers = {}  # publisherId:name
pubs = dfs.loc['references', 'payload']['Collection']
for p in pubs.values():
    publishers[p['id']] = p['name']
df_publishers = pd.DataFrame.from_dict(publishers, orient='index', columns=['name'])
df_publishers.index.name = 'id'

print(df_stats[['title','views','reads','upvotes','firstPublishedAtBucket','readingTime']])
print(df_paystats[['post_title','amount','weeklyAmounts']])
print(df_publishers)

print ('stop')