from data import db_session
from data.jobs import Jobs
from data.users import User
import argparse

def p4(db_name:str):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()
    max_workers = 0
    for job in db_sess.query(Jobs).all():
        if len(job.collaborators.split(";")) > max_workers:
            max_workers = len(job.collaborators.split(";"))

    for job in db_sess.query(Jobs).all():
        if len(job.collaborators.split(";")) == max_workers:
            for user in db_sess.query(User).filter(User.id == job.team_leader):
                print(user)

parser = argparse.ArgumentParser()

parser.add_argument('file')
args = parser.parse_args()

p4(args.file)