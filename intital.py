from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    param1 = request.form.get('param1')
    param2 = request.form.get('param2')
    # Perform calculations or call your existing Python script with the received parameters
    result = perform_calculations(param1, param2)
    return render_template('result.html', result=result)

def perform_calculations(param1, param2):
    # Your Python code that uses the input parameters
    # Return the result
    return param1 + param2

if __name__ == '__main__':
    app.run(debug=True)