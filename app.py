from flask import Flask, render_template, request
import requests
import random
import time

app = Flask(__name__)

@app.route("/")
def home():
  color = random.choice(["red", "yellow", "blue "])

  panels = [
    {
      "title": "SuperHi API",
      "url": "https://api.superhi.com"
    },
    {
      "title": "SuperHi Editor",
      "url": "https://editor.superhi.com"
    },
    {
      "title": "SuperHi",
      "url": "https://www.superhi.com"
    },
    {
      "title": "BBC News",
      "url": "https://www.bbc.com/"
    }
  ]

  return render_template("home.html", color=color, panels=panels)

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/ping")
def ping():
  url = request.args.get("url")

  start_time = time.time()
  r = requests.get(url)
  end_time = time.time()

  diff_time = int((end_time - start_time) * 1000)

  return {
    "url": url,
    "code": r.status_code,
    "speed": diff_time
  }