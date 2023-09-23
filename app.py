from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 + num2
    operation = request.form['operation']
    if operation == 'addition':
        result = num1 + num2
    elif operation == 'subtract':
            result = num1 - num2
    elif operation == 'multiply':
            result = num1 * num2
    elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return 'Error: Division by zero'
    else:
            return 'Error: Invalid operation'

    return render_template('result.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)