from data import db_session
from data.jobs import Jobs
import argparse

def p4(db_name:str):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()
    for job in db_sess.query(Jobs).all():
        if job.work_size < 20 and not (job.is_finished):
            print(job)

parser = argparse.ArgumentParser()

parser.add_argument('file')
args = parser.parse_args()

p4(args.file)