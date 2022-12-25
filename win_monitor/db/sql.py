import pymysql
from controller import windows_obj


FIND_USER_BY_JOB_NUM = "select * from user where job_num = %s"

FIND_USER_BY_ID = "select * from user where id = %s"

FIND_USER_BY_NAME = "select * from user where name = %s"

INSERT_USER = "insert into user(name, job_num, email, start, end,description) values(%s, %s, %s, %s, %s, %s)"


def db_connect(databse):
    # db = pymysql.connect(host='127.0.0.1',
    #                      port=3306,
    #                      user='root',
    #                      password='venus',
    #                      database='monitor',
    #                      charset='utf8')
    # db = pymysql.connect(host='192.168.2.54',
    #                      port=3306,
    #                      user='root',
    #                      password='password',
    #                      database='monitor',
    #                      charset='utf8')
    db = pymysql.connect(host=databse.host,
                         port=databse.port,
                         user=databse.username,
                         password=databse.password,
                         database=databse.database,
                         charset='utf8')

    return db


def user_regist(win_obj):
    if win_obj.mode == windows_obj.Mode.OFFLINE.name:
        print("offLine")
        return

    userId = None
    db = pymysql.connect(host=win_obj.database.host,
                         port=int(win_obj.database.port),
                         user=win_obj.database.username,
                         password=win_obj.database.password,
                         database=win_obj.database.database,
                         charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(FIND_USER_BY_JOB_NUM,win_obj.job_number)
        one = cursor.fetchone()
        if one is None:
            cursor.execute(INSERT_USER,[win_obj.user_name, win_obj.job_number, win_obj.email, win_obj.start, win_obj.end, win_obj.description])
            db.commit()
    except Exception as e:
        print("user_regist err: " + str(e))
        db.rollback()
    finally:
        cursor.close()
        db.close()


def addRecord(user_id, status):
    pass

