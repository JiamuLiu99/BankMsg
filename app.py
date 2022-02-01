import core
from flask import Flask, g, render_template, request


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    core.get_message_db()
    if request.method == 'GET':
        return render_template("submit.html")
    else:
        try:
            core.insert_message(request)
            return render_template('submit.html', msg=request.form['message'], hdl=request.form['handle'])
        except:
            return render_template('error.html')

@app.route('/view/')
def view_records():
    core.get_message_db()
    return render_template('view.html')


if __name__ == "__main__":
    app.run(debug = True)
