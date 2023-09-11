from flask import Flask, request, render_template, redirect, session
from api import get_overview_data, get_sentiment_data

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        session['data'] = data
        return redirect('/analyze')
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        return redirect('/sentiments')
    data = session['data']
    symbol1 = data.get('Symbol1')
    symbol2 = data.get('Symbol2')
    overview_data1 = get_overview_data(symbol1)
    overview_data2 = get_overview_data(symbol2)
    return render_template("analyze.html", overview_data1=overview_data1, overview_data2=overview_data2)

@app.route('/sentiments', methods=['GET', 'POST'])
def sentiments():
  data = session['data']
  symbol1 = data.get('Symbol1')
  symbol2 = data.get('Symbol2')
  sentiment_data1 = get_sentiment_data(symbol1)
  sentiment_data2 = get_sentiment_data(symbol2)
  
  return render_template("sentiments.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)