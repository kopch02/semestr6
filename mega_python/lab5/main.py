from flask import Flask, url_for, render_template, redirect, send_from_directory
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departament import Departament
from forms.user import RegisterForm
from forms.job import JobsForm
from forms.deportament import DeportamentForm
from num1 import add_user, add_departament, add_jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


@app.route('/')
@app.route('/index')
def index():
    param = {}
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    param["jobs"] = jobs
    return render_template('index.html', **param)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html',
                                   title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        add_user(form.surname.data,
                 form.name.data,
                 form.age.data,
                 form.position.data,
                 form.speciality.data,
                 form.addres.data,
                 form.email.data,
                 passworld=form.password.data)
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    db_sess = db_session.create_session()
    form = JobsForm()
    team_list = db_sess.query(User).all()
    form.team_leader.choices = team_list
    form.collaborators.choices = team_list
    if form.validate_on_submit():
        collaborators = ""
        for i in form.collaborators.data:
            collaborators += str(int(i[11:13])) + ";"
        add_jobs(int(form.team_leader.data[11:13]),
                 form.job.data,
                 form.work_size.data,
                 collaborators
                 )
        
        return redirect('/login')
    return render_template('add_job.html', title='Опять работать? ', form=form)


@app.route('/add_deportament', methods=['GET', 'POST'])
def add_departaments():
    db_sess = db_session.create_session()
    form = DeportamentForm()
    team_list = db_sess.query(User).all()
    form.chief.choices = team_list
    form.members.choices = team_list
    if form.validate_on_submit():
        members = ""
        for i in form.members.data:
            members += str(int(i[11:13])) + ";"
        add_departament(form.title.data,
                        int(form.chief.data[11:13]),
                        members,
                        form.email.data)
        return redirect('/login')
    return render_template('add_deportament.html', title='Новый депортамент? ', form=form)


if __name__ == '__main__':
    main()