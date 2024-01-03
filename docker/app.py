# app.py (Do not change the app name)
from flask import Flask, render_template
import requests

app = Flask(__name__)

graphql_endpoint = "https://api.tibber.com/v1-beta/gql"
access_token = "INSERT YOU API TOKEN HERE"

query = """
{
  viewer {
    homes {
      currentSubscription {
        status
        priceInfo {
          current {
            total
            energy
            tax
            startsAt
          }
        }
      }
    }
  }
}
"""

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

def get_strompreis():
    response = requests.post(graphql_endpoint, json={"query": query}, headers=headers)
    if response.status_code == 200:
        data = response.json()
        current_price = data["data"]["viewer"]["homes"][0]["currentSubscription"]["priceInfo"]["current"]
        cp = current_price['total'] * 100
        return cp
    else:
        return "Fehler bei der Anfrage: " + str(response.status_code)

@app.route('/')
def show_strompreis():
    cp = get_strompreis()
    return render_template('index.html', strompreis=cp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9945)
