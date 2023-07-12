from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def change_page():
    return render_template('simplepage.html')


@app.route('/change_trip', methods=['GET', 'POST'])
def change_trip():
    return render_template('simp.html')

# I have changed it
