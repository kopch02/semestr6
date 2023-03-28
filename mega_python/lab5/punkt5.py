from data import db_session
from data.users import User
import argparse

def p4(db_name:str):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()
    for user in db_sess.query(User).all():
        if user.addres == "module_1":
            if not("engineer" in user.speciality) and not("engineer" in user.position):
                print(user)

parser = argparse.ArgumentParser()

parser.add_argument('file')
args = parser.parse_args()

p4(args.file)