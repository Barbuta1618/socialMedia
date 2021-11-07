from flask import Flask, request
from flask_cors import CORS, cross_origin
import likesTime 
from comparePosts import compare_posts
from objDetection import getElements

app = Flask(__name__)

def comparePosts(firstText, secondText):
    return (len(firstText), len(secondText))

CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/likestime', methods = ['GET'])
def getLikes():
    (likes, shares, comms) = likesTime.likesTime()

    data = {
        "likes": likes,
        "shares": shares,
        "comms": comms
    }
    
    return data


@app.route('/postcompare', methods = ['GET', 'POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def comparePostsHTTP():
    if request.method == "POST":
        data = request.get_json()

        firstText = data['firstText']
        secondText = data['secondText']

        (firstPrcFb, secondPrcFb) = compare_posts(firstText, secondText, 'facebook')
        (firstPrcIg, secondPrcIg) = compare_posts(firstText, secondText, 'instagram')
        (firstPrcTw, secondPrcTw) = compare_posts(firstText, secondText, 'twitter')
        (firstPrcLi, secondPrcLi) = compare_posts(firstText, secondText, 'linkedin')

        myDict = {
            'facebook': {
                'firstPrc': firstPrcFb,
                'secondPrc': secondPrcFb 
            },
            'instagram': {
                'firstPrc': firstPrcIg,
                'secondPrc': secondPrcIg 
            },
            'twitter': {
                'firstPrc': firstPrcTw,
                'secondPrc': secondPrcTw 
            },
            'linkedin': {
                'firstPrc': firstPrcLi,
                'secondPrc': secondPrcLi 
            }
        }
        return myDict

#@app.route('/', methods = ['GET', 'POST'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization'])
#def ():


if __name__ == "__main__":
    app.run(debug=True)


