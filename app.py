from flask import Flask,redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/') 
def calculator():
    return render_template("index.html")

@app.route('/calculate', methods = ['POST']) 
def calculate():
    data1 = float(request.form['num1'])
    data2 = float(request.form['num2'])
    op = request.form['operation']

    if op == '+' :
        result = data1 + data2
    elif op == '-' :
        result = data1 - data2
    elif op == '*' :
        result = data1 * data2
    elif op == '/' :
        result = data1 / data2
    else :
        result = "Error : Invalid operation"
    
    return render_template('output.html', result = result)

if __name__ == "__main__" :
    app.run(debug = True)