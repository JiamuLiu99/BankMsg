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
            rc = core.insert_message(request)
            if rc:
                return render_template('success.html' )
            else:
                return render_template('fail.html')
        except:
            return render_template('fail.html')

@app.route('/view/')
def view_records():
    core.get_message_db()
    return render_template('view.html', msg = core.random_messages(5))

if __name__ == "__main__":
    app.run(debug = True)
