from flask import *
app = Flask("__name__")

# Showing HTML page
@app.route('/Flask_based_calculator')
def cal_page():
    return render_template('calculator.html')


@app.route('/math', methods = ['POST'])
def calculator_test():
    #Taking data from the HTML file
    ops = request.form['operation']
    first_number = int(request.form['num1'])
    secound_number = int(request.form['num2'])

    if ops == 'add':
        result = first_number + secound_number
        return f"Addition of {first_number} and {secound_number} is {result}"

    if ops == 'subtract':
        result = first_number - secound_number
        return f"Subtraction of {first_number} and {secound_number} is {result}"

    if ops == 'multiply':
        result = first_number * secound_number
        return f"Multiplication of {first_number} and {secound_number} is {result}"

    if ops == 'divide':
        result = first_number / secound_number
        return f"Divide of {first_number} and {secound_number} is {result}"

if __name__ == '__main__':
    app.run(host="0.0.0.0")