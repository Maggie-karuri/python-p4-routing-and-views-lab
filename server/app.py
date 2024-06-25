from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(num) for num in range(parameter))
    return f"{numbers}\n"  # Return numbers separated by newline and end with newline

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return jsonify(error="Invalid input. Please provide integers for num1 and num2."), 400

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':  # Changed operation name from '/' to 'div'
        if num2 == 0:
            return jsonify(error="Division by zero is not allowed"), 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return jsonify(error="Operation not supported"), 400

    return jsonify(num1=num1, num2=num2, operation=operation, result=result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
