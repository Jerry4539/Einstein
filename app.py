from flask import Flask, render_template, request
import wolframalpha

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/', methods=['POST'])
def process():
    client = wolframalpha.Client("EAWW8U-EVPXRVXUWA")
    query = request.form['query']
    res = client.query(query)
    answer = next(res.results).text
    return render_template('index2.html', query=query, answer=answer)

if __name__ == '__main__':
    app.run()
