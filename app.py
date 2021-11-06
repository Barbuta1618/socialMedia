from flask import Flask, render_template, url_for, request
import likesTime 

app = Flask(__name__)

@app.route('/likestime', methods = ['GET'])
def index():
    (likes, shares, comms) = likesTime.likesTime()

    data = {
        "likes": likes,
        "shares": shares,
        "comms": comms
    }
    
    return data


if __name__ == "__main__":
    app.run(debug=True)


