import json
from requests_oauthlib import OAuth1Session
import key

CK = key.consumer_key
CS = key.consumer_secret
AT = key.token
ATS = key.token_secret
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

params ={'count':5}
res = twitter.get(url, params = params)

if res.status_code == 200:
    timelines = json.loads(res.text)
    for line in timelines:
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('--------------------------------------------------------------------')
else: #正常通信出来なかった場合
    print("Failed: %d" % res.status_code)