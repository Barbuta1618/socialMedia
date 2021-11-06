import json
from datetime import datetime
 

def likesTime():
    # Opening JSON file
    f = open('./datasets/facebook.json', encoding="utf8")
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    # for i in data["likes"]:
    # print(data)
    
    ts = int(data[0]['created_at'])
    print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
    
    likesList = []
    for post in data:
        likesList.append(post["likes"])
    
    # sort likesList
    likesList.sort()
    
    
    likes = []
    for i in range(24):
        likes.append(0)
    
    for post in data:
        ts = int(post['created_at'])
        date = int(datetime.utcfromtimestamp(ts).strftime('%H'))
        likes[date] = int(post['likes']) + likes[date]
    
    
    # Closing file
    f.close()
    return likes