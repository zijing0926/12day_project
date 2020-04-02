from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hist')
def hist():
  return render_template('hist.html')

@app.route('/price')
def price():
  return render_template('close.html')


if __name__ == '__main__':
  app.run(port=33507)
