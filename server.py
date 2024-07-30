import os
from flask import Flask, render_template
import main  # Ensure this module is correctly imported and implemented

app = Flask(__name__)

@app.route('/')
def default():
    return 'Routing Algorithms <br><a href="/Dijkstras">Dijkstras Algorithm</a>'

@app.route('/Dijkstras1')
def webInterface():
    input_file = os.getenv('INPUT_FILE', 'in.in')  # Default to 'in.in' if not set
    result = main.result(input_file)
    input_graph = result[-1]
    result = result[:-1]
    return render_template('Dijkstras.html', result=result, input_graph=input_graph)

@app.route('/Dijkstras')
def webInterface1():
    input_file = os.getenv('INPUT_FILE_1', 'in1.in')  # Default to 'in1.in' if not set
    result = main.result(input_file)
    input_graph = result[-1]
    result = result[:-1]
    return render_template('Dijkstras.html', result=result, input_graph=input_graph)

if __name__ == "__main__":
    app.run("127.0.0.1", 4200, debug=True)