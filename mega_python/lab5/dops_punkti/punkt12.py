from data import db_session
from data.jobs import Jobs
from data.users import User
from data.departament import Departament
import argparse
from num1 import add_jobs, add_departament

def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    add_departament("геологической разведки",1,"2;3;4","geolog@email.com")
    add_jobs(1,"testing punkt 12",25,"2;4")
    for dept in db_sess.query(Departament).filter(Departament.id == 1):
        w = dept.members.split(";")

    hours_work = dict()
    for job in db_sess.query(Jobs).all():
        j_workers = job.collaborators.split(";")
        for workers in j_workers:
            try:
                hours_work[workers] += job.work_size
            except:
                hours_work[workers] = job.work_size
    for i in hours_work.items():
        if i[1] > 25:
            for user in db_sess.query(User).filter(User.id == int(i[0])):
                if str(user.id) in w:
                    print(user)


if __name__ == '__main__':
    main()