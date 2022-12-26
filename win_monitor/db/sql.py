import pymysql
from controller import windows_obj
from db import log


LOGGER = log.LOGGER

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
        LOGGER.debug("Method = sql#user_regist : 离线模式，不使用远程数据库")
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
            LOGGER.debug("Method = sql#user_regist : 在线模式，判断用户为 新用户")
            cursor.execute(INSERT_USER,[win_obj.user_name, win_obj.job_number, win_obj.email, win_obj.start, win_obj.end, win_obj.description])
            db.commit()
    except Exception as e:
        db.rollback()
        LOGGER.error("Method = sql#user_regist : 在线模式，新用户插入异常 Exception = " + str(e))
    finally:
        cursor.close()
        db.close()


def addRecord(user_id, status):
    pass

