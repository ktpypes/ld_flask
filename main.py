import requests
import os
import ldclient
from ldclient.config import Config
from flask import Flask, jsonify

app = Flask(__name__)

user = {
    "key": "aa0ceb",
    "firstName": "Mara",
    "lastName": "Jade",
    "email": "mjade@coruscant.gov",
    "custom": {
      "groups": ["Jedi"]
    }
}

@app.route("/")
def get_feature():  
    ldclient.set_config(Config("sdk-ccb06a70-1a99-40b0-8fd0-9936de38354d"))
    show_feature = ldclient.get().variation("kptest", user, "No Data")
    if show_feature == True:
        r = requests.get("https://swapi.dev/api/people/1/").json()
        ldclient.get().close()
        return jsonify(r)
    else:
        text = "The app is up!"
        return text
        
if __name__ == '__main__':
    app.run(debug=True)