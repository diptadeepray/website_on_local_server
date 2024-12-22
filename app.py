'''We can directly run the app buy python3 app.py
Or we can write flask run in the virtual environment'''


'''The app.py file is running as a development server.
To run your Flask app with a production-ready WSGI server,
 you can use tools like Gunicorn, uWSGI, or Waitress.'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
'''Along with calling index.html, we can also pass any value.
To display that value in HTML file. We can use {{variable_name}}inside any tag.
'''

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'Name: {name}, and Email: {email}'
    return render_template('index.html')

#debug=True restarts the server, everytime we change the code
if __name__ == '__main__':
    app.run(debug=True)

