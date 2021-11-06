from flask import Flask, render_template, url_for, request
import likesTime 

app = Flask(__name__)

@app.route('/likestime', methods = ['GET'])
def index():
    likes = likesTime.likesTime()
    hours = []
    for i in range(23):
        hours.append(i)

    data = dict(zip(hours, likes)) 
    print(data)
    return data


if __name__ == "__main__":
    app.run(debug=True)


