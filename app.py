from flask import Flask
from flask import render_template
from flask import request

# I know that this shouldn't be done, but it's a small and limited project.
# in another case, you should import one by one just what you need.
from src.resolver import *

app = Flask(__name__)


@app.route('/')
def home_page():
    """
    This method renders the base html template that shows user a button
    for the backend challenge.
    :return:
    """
    return render_template('base.html')


@app.route('/backend')
def backend():
    """
    This method let you enter in the backend challenge part of this program
    once there you have 4 more options, that is the 4 questions that are going
    to be answered.
    :return:
    """
    return render_template('template_backend.html')


@app.route('/backend/q1', methods=['GET', 'POST'])
def backend_q1():
    """
    This is the first question route that calls first question resolver and
    shows on html the result to the user
    :return:
    """
    if request.method == 'POST':
        try:
            answer = question_1(request.form.get('array'))
            return render_template('backend_q1.html',
                                   context={'result': answer})
        except Exception:
            return render_template('backend_q1.html', context={
                'message': '* Please, enter a valid array'})
    elif request.method == 'GET':
        return render_template('backend_q1.html')


@app.route('/backend/q2', methods=['GET', 'POST'])
def backend_q2():
    """
    This is the second question route that calls second question resolver and
    shows on html the result to the user
    :return:
    """
    if request.method == 'POST':
        try:
            answer = question_2(request.form.get('brackets'))
            return render_template('backend_q2.html', context={
                'result': 'SIM' if answer else 'NÃO'})
        except Exception:
            return render_template('backend_q2.html', context={
                'message': '* Please, enter a valid bracket sequence'})
    elif request.method == 'GET':
        return render_template('backend_q2.html')


@app.route('/backend/q3', methods=['GET', 'POST'])
def backend_q3():
    """
    This is the third question route that calls third question resolver and
    shows on html the result to the user
    :return:
    """
    if request.method == 'POST':
        try:
            answer = question_3(request.form.get('quote'))
            return render_template('backend_q3.html',
                                   context={'result': answer})
        except Exception:
            return render_template('backend_q3.html', context={
                'message': '* Please, enter a valid array'})
    elif request.method == 'GET':
        return render_template('backend_q3.html')


@app.route('/backend/q4', methods=['GET', 'POST'])
def backend_q4():
    """
    This is the fourth question route that calls fourth question resolver and
    shows on html the result to the user
    :return:
    """
    if request.method == 'POST':
        try:
            answer = question_4(request.form.get('graph_array'))
            return render_template('backend_q4.html',
                                   context={'result': answer})
        except Exception:
            return render_template('backend_q4.html', context={
                'message': '* Please, enter a valid array'})
    elif request.method == 'GET':
        return render_template('backend_q4.html')


if __name__ == '__main__':
    app.run()
