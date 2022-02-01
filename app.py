import core
from flask import Flask, g, render_template, request


app = Flask(__name__)

# index page
@app.route('/', methods=['POST', 'GET'])
def index():
    # check db and create if necessary
    core.get_message_db()

    # GET request
    if request.method == 'GET':
        return render_template("submit.html")
    else: # POST request
        try:
            # insert a record into messages table
            rc = core.insert_message(request)
            if rc:
                return render_template('success.html' )
            else:
                return render_template('fail.html')
        except:
            return render_template('fail.html')

# view page
@app.route('/view/')
def view_records():
    # check db and create if necessary
    core.get_message_db()
    # render template and call random_message
    return render_template('view.html', msg = core.random_messages(5))

# main
if __name__ == "__main__":
    app.run(debug = True)
