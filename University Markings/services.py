# Imports
from flask import Flask, redirect, url_for, render_template, request

# WSGI(Web server gateway interface) Application
app = Flask(__name__)


@app.route('/')  # decorator which binds the endpoint to the function calls
def _print():
    return render_template('index.html')


@app.route('/default')
def _default():
    return 'A default endpoint has been called.'


@app.route('/_pass/<int:score>')
def _pass(score):
    # return 'Passed :'+str(score)
    result = "with an average score of " + str(score) + " marks."
    return render_template('success.html', response=result, res=score)


@app.route('/_fail/<int:score>')
def _fail(score):
    # return 'Failed :'+str(score)
    result = "with an average score of " + str(score) + " marks."
    return render_template('failure.html', response=result)


# Checking the result by building URL's dynamically
@app.route('/result/<int:marks>')
def _result(marks):
    if marks >= 37:
        return redirect(url_for('_pass', score=marks))
    else:
        return redirect(url_for('_fail', score=marks))


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    com_score = 0
    if request.method == 'POST':
        computer_science = float(request.form['computer_science'])
        business_communication = float(request.form['business_communication'])
        com_score = (computer_science + business_communication)/2
        if computer_science >= 37 and business_communication >= 37 and com_score >= 37: return redirect(url_for('_pass', score=com_score))
        else: return redirect(url_for('_fail', score=com_score))


if __name__ == '__main__':
    # app.run(host='DESKTOP-BSGQRP6', port=3030, debug=True)
    # debug=True makes sure if any changes are made in the page, will be refreshed in the Web application.
    app.run(port=3030, debug=True)
