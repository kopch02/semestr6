from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departament import Departament
import datetime


def add_user(surname:str, name:str, age:int, position:str, speciality:str, addres:str, email:str, passworld:str = None):
    user = User()

    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.addres = addres
    user.email = email

    db_sess = db_session.create_session()
    if passworld != None:
        user.set_password(passworld)
    db_sess.add(user)
    db_sess.commit()


def add_jobs(team_leader:int,job:str,work_size:float,collaborators:str,start_date:datetime.date = datetime.date.today(), is_finished:bool = False):
    new_job = Jobs()
    new_job.team_leader = team_leader
    new_job.job = job
    new_job.work_size = work_size
    new_job.collaborators = collaborators
    new_job.start_date = start_date
    new_job.is_finished = is_finished

    db_sess = db_session.create_session()
    db_sess.add(new_job)
    db_sess.commit()


def add_departament(title:str,chief:int,members:str,email:str):
    new_departament = Departament()
    new_departament.title = title
    new_departament.chief = chief
    new_departament.members = members
    new_departament.email = email

    db_sess = db_session.create_session()
    db_sess.add(new_departament)
    db_sess.commit()

def main():
    db_session.global_init("db/mars_explorer.db")
    add_user("Scott", "Ridley", 21, "captain", "research engineer", "module_1",
             "scott_chief@mars.org")
    
    add_user("Jhon", "Peters", 33, "помошник капитана", "пилот", "module_1",
             "jhon_chief@mars.org")
    
    add_user("Alex", "Gibson", 25, "chief", "строитель", "module_1",
             "gibson_chief@mars.org")
    
    add_user("Piter", "Grant", 17, "рядовой", "engineer по терраформированию", "module_1",
             "piter_grant@mars.org")
    
    add_user("Emely", "Gibson", 23, "рядовой", "оператор марсохода", "module_1",
             "gibson_lady@mars.org")
    
    add_user("Skot", "Davis", 17, "middle engineer", "киберинженер", "module_1",
             "scottttt@mars.org")
    
    add_jobs(1,"deployment of residential modules 1 and 2",15,"2;3")

if __name__ == '__main__':
    main()