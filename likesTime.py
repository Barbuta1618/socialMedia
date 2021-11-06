import json
from datetime import datetime
 

def likesTime():
    # Opening JSON file
    f = open('./datasets/facebook.json', encoding="utf8")
    data = json.load(f)
    
    likes = []
    shares = []
    comms = []
    for i in range(24):
        likes.append(0)
        shares.append(0)
        comms.append(0)

    for post in data:
        ts = int(post['created_at'])
        date = int(datetime.utcfromtimestamp(ts).strftime('%H'))
        likes[date] = int(post['likes']) + likes[date]
        shares[date] = int(post['shares']) + shares[date]
        comms[date] = int(post['reactions']) + comms[date]
    

    
    # Closing file
    f.close()
    return (likes, shares, comms)