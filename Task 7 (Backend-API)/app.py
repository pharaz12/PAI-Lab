from flask import Flask, render_template
import requests

app = Flask(__name__)

NASA_API = "TJ1PWoiFFSOFdWIsbVH55QNBr9pT9LjHVWsb5VsL"
APOD_URL = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"

@app.route("/", methods=["GET"])
def index():
    par = {"api_key" : NASA_API}
    response = requests.get(APOD_URL, params=par)
    apod_data = response.json()
    return render_template("index.html", apod = apod_data)

if __name__ == "__main__":
    app.run(debug=False)