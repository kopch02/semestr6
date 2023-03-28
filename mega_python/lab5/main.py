from flask import Flask, url_for, render_template, redirect, send_from_directory
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'



def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()

@app.route('/')
def index():
    param = {}
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    param["jobs"] = jobs
    return render_template('index.html', **param)

if __name__ == '__main__':
    main()