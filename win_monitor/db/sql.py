import pymysql
from controller import windows_obj
from db import log
import datetime

LOGGER = log.LOGGER

####################################user######################################
# 通过工号查找用户
FIND_USER_BY_JOB_NUM = "select * from user where job_num = %s"
# 通过id查找用户
FIND_USER_BY_ID = "select * from user where id = %s"
# 通过姓名查找用户
FIND_USER_BY_NAME = "select * from user where name = %s"
# 通过姓名工号查找用户
FIND_USER_BY_NAME_AND_JOB_NUM = "select * from user where name = %s and job_num = %s"
# 通过姓名 工号查找用户id
FIND_USER_ID_BY_NAME_AND_JOB_NUM = "select id from user where name = %s and job_num = %s"
# 插入用户信息
INSERT_USER = "insert into user(name, job_num, email, tenant, start, end,description) values(%s, %s, %s, %s, %s, %s, %s)"
# 更新用户信息
UPDATE_USER = "update user set email = %s, tenant = %s, start = %s, end = %s, description = %s where name = %s and job_num = %s"

####################################record######################################
# 插入打卡数据
INSERT_RECORD = "insert into record(user, date, start, end, overtime, exchange_time, reason, handled, description) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
# 更新下班时间
UPDATE_START_TIME = "update record set start = %s where user = %s and date = %s"
# 更新下班时间
UPDATE_END_TIME = "update record set end = %s where user = %s and date = %s"
# 更新加班时间
UPDATE_OVER_EXCHANGE_TIME = "update record set overtime = %s, exchange_time = %s where user = %s and date = %s"
# 更新加班理由
UPDATE_REASON = "update record set reason = %s where user = %s and date = %s"
# 更新加班处理结果
UPDATE_HANDLED = "update record set handled = %s where user = %s and date = %s"
# 更新描述
UPDATE_DESCRIPTION = "update record set description = %s where user = %s and date = %s"
# 用户更新加班数据
USER_UPDATE_SQL = "update record set overtime = %s, exchange_time = %s, reason = %s, description = %s where user = %s and date = %s"
# 管理员更新加班数据
ADMIN_UPDATE_SQL = "update record set overtime = %s, exchange_time = %s, handled = %s, description = %s where user = %s and date = %s"
# 根据用户和日期查找数据库数据行数
SUM_RECORD_COUNT = "select count(1) from record where user = %s and date = %s"
# 根据日期查找数据库数据
FIND_RECORDS_BY_DATE_DELTA = "select * from record where user = %s and date >= %s and date <= %s"
# 根据日期查找数据库数据
FIND_RECORD_BY_USER_AND_DATE = "select * from record where user = %s and date = %s"
# 查询上班时间
FIND_START_BY_USER_AND_DATE = "select start from record  where user = %s and date = %s"
# 查询下班时间
FIND_END_BY_USER_AND_DATE = "select end from record where user = %s and date = %s"

#####################Tenant#########################################
# 插入租户
INSERT_TENANT = "insert into tenant(name, owner, description) values(%s, %s, %s)"
# 查找所有租户
FIND_TENANTS = "select name from tenant"
# 查找租户
FIND_TENANT_BY_NAME = "select * from tenant where name = %s"


# 测试数据库是否能正常连接
def test_connect(database, user):
    db = None
    try:
        db = pymysql.connect(host=database.host,
                             port=int(database.port),
                             user=database.username,
                             password=database.password,
                             database=database.database,
                             charset='utf8')
        return True
    except Exception as e:
        LOGGER.error("测试数据库是否能正常连接 Exception = " + str(e))
    finally:
        # 关闭db
        if db is not None:
            db.close()

    return False


# 根据名字和工号查找用户
def find_user_by_name_and_num(database, user):
    result = None
    db = None
    cursor = None

    try:
        db = pymysql.connect(host=database.host,
                             port=int(database.port),
                             user=database.username,
                             password=database.password,
                             database=database.database,
                             charset='utf8')
        cursor = db.cursor()
        # 查找所有租户
        cursor.execute(FIND_USER_BY_NAME_AND_JOB_NUM, [user.user_name, user.job_number])
        result = cursor.fetchone()
        if result is None:
            LOGGER.debug(
                "查找用户不存在 : " + user.user_name + ": " + user.job_number)
    except Exception as e:
        # 数据库回滚
        if db is not None:
            db.rollback()

        LOGGER.error("查找用户异常 Exception = " + str(e))
    finally:
        # 关闭数据库连接
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

    return result


# 插入用户
def insert_user(database, user):
    result = None
    db = None
    cursor = None

    try:
        db = pymysql.connect(host=database.host,
                             port=int(database.port),
                             user=database.username,
                             password=database.password,
                             database=database.database,
                             charset='utf8')
        cursor = db.cursor()
        # 插入用户
        result = cursor.execute(INSERT_USER,
                                [user.user_name, user.job_number, user.email, user.tenant, user.attendance.startTime,
                                 user.attendance.endTime, user.description])
        db.commit()

    except Exception as e:
        # 数据库回滚
        if db is not None:
            db.rollback()

        LOGGER.error("插入用户异常 Exception = " + str(e))
    finally:
        # 关闭数据库连接
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

    return result


# 更新新用户 数据
def update_user(database, user):
    result = 0
    db = None
    cursor = None

    try:
        db = pymysql.connect(host=database.host,
                             port=int(database.port),
                             user=database.username,
                             password=database.password,
                             database=database.database,
                             charset='utf8')
        cursor = db.cursor()
        # 插入用户
        result = cursor.execute(UPDATE_USER,
                                [user.email, user.tenant, user.attendance.startTime, user.attendance.endTime,
                                 user.description,
                                 user.user_name, user.job_number])
        db.commit()

    except Exception as e:
        # 数据库回滚
        if db is not None:
            db.rollback()

        LOGGER.error("更新用户数据异常 Exception = " + str(e))
    finally:
        # 关闭数据库连接
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

    return result


# 查找用户id
def find_user_id_by_name_and_num(database, user):
    user_id = None
    db = None
    cursor = None
    try:
        db = pymysql.connect(host=database.host,
                             port=int(database.port),
                             user=database.username,
                             password=database.password,
                             database=database.database,
                             charset='utf8')
        cursor = db.cursor()
        # 查找所有租户
        cursor.execute(FIND_USER_ID_BY_NAME_AND_JOB_NUM, [user.user_name, user.job_number])
        result = cursor.fetchone()

        if result is None:
            LOGGER.debug(
                "查找用户不存在 : " + user.user_name + ": " + user.job_number)
        else:
            user_id = result[0]
    except Exception as e:
        # 数据库回滚
        if db is not None:
            db.rollback()

        LOGGER.error("查找用户异常 Exception = " + str(e))
    finally:
        # 关闭数据库连接
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

    return user_id


# 注册新用户 （已废弃）
def user_regist(win_obj):
    if win_obj.mode == windows_obj.Mode.OFFLINE.name:
        LOGGER.debug("离线模式，不使用远程数据库")
        return

    user = win_obj.user
    attendance = win_obj.attendance
    one = None

    db = None
    cursor = None

    try:
        db = pymysql.connect(host=win_obj.database.host,
                             port=int(win_obj.database.port),
                             user=win_obj.database.username,
                             password=win_obj.database.password,
                             database=win_obj.database.database,
                             charset='utf8')
        cursor = db.cursor()
        cursor.execute(FIND_USER_BY_JOB_NUM, user.job_number)
        one = cursor.fetchone()
        if one is None:
            LOGGER.debug("判断用户为 新用户")
            cursor.execute(INSERT_USER,
                           [user.user_name, user.job_number, user.email, user.tenant, attendance.startTime,
                            attendance.endTime, user.description])
            db.commit()
            cursor.execute(FIND_USER_ID_BY_NAME_AND_JOB_NUM, [user.user_name, user.job_number])
            one = cursor.fetchone()
        else:
            LOGGER.debug("判断用户为 老用户")

    except Exception as e:
        # 数据库回滚
        if db is not None:
            db.rollback()

        LOGGER.error("新用户插入异常 Exception = " + str(e))
    finally:
        # 关闭数据库连接
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

    # 返回user_id 主键
    LOGGER.debug("用户信息 = " + str(one))
    user.id = one[0]
    return one[0]


# 追加屏幕登录记录
def addUNLockRecord(database, user_id):
    LOGGER.debug("追加屏幕登录记录:  user_id: " + str(user_id) + ", Time: " + str(
        datetime.datetime.now()))
    db = None
    cursor = None

    try:
        db = pymysql.connect(host=database.host,
                             port=int(database.port),
                             user=database.username,
                             password=database.password,
                             database=database.database,
                             charset='utf8')
        cursor = db.cursor()
        # 查找今天的上班时间
        cursor.execute(FIND_RECORD_BY_USER_AND_DATE, [user_id, datetime.date.today()])
        one = cursor.fetchone()
        # 今天没有上班记录
        if one is None:
            # 插入新的上班记录
            cursor.execute(INSERT_RECORD,
                           [user_id, datetime.date.today(), datetime.datetime.now().time(), None, None, None, None, 0,
                            None])
            db.commit()
        else:
            # 如果有上班记录，并且记录时间比现在晚，更新上班时间
            if one[3] > (datetime.datetime.now() - datetime.datetime(year=datetime.date.today().year,
                                                                     month=datetime.date.today().month,
                                                                     day=datetime.date.today().day)):
                cursor.execute(UPDATE_START_TIME, [datetime.datetime.now().time(), user_id, datetime.date.today()])
                db.commit()
                LOGGER.debug("上班时间更新 原上班时间: " + str(one[3]) + ", 新上班时间: " + str(
                    datetime.datetime.now() - datetime.datetime(year=datetime.date.today().year,
                                                                month=datetime.date.today().month,
                                                                day=datetime.date.today().day)))
            else:
                # 如果有上班记录，并且记录时间比现在早，不更新上班时间
                LOGGER.debug("上班时间不更新 原上班时间: " + str(one[3]) + ", 新上班时间: " + str(
                    datetime.datetime.now() - datetime.datetime(year=datetime.date.today().year,
                                                                month=datetime.date.today().month,
                                                                day=datetime.date.today().day)))

    except Exception as e:
        # 数据库回滚
        if db is not None:
            db.rollback()

        LOGGER.error("上班时间插入异常 Exception = " + str(e))
        LOGGER.error("上班时间插入异常  当前时间 " + str(
            datetime.datetime.now() - datetime.datetime(year=datetime.date.today().year,
                                                        month=datetime.date.today().month,
                                                        day=datetime.date.today().day)))
    finally:
        # 关闭数据库连接
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


# 追加屏幕锁定记录
def addLockRecord(database, user_id):
    LOGGER.debug("追加屏幕锁定记录: user_id: " + str(user_id) + ", Time: " + str(
        datetime.datetime.now()))
    db = None
    cursor = None

    try:
        db = pymysql.connect(host=database.host,
                             port=int(database.port),
                             user=database.username,
                             password=database.password,
                             database=database.database,
                             charset='utf8')
        cursor = db.cursor()
        # 查找今天的上班班记录
        cursor.execute(FIND_RECORD_BY_USER_AND_DATE, [user_id, datetime.date.today()])
        one = cursor.fetchone()
        # 今天没有上班记录（昨天通宵了？）
        if one is None:
            cursor.execute(INSERT_RECORD,
                           [user_id, datetime.date.today(), None, datetime.datetime.now().time(), None,
                            None, None, 0,
                            None])
            db.commit()
        else:
            # 如果没有下班记录，或者下班时间比当前时间早，更新下班时间
            if one[4] is None or one[4] < (datetime.datetime.now() - datetime.datetime(year=datetime.date.today().year,
                                                                                       month=datetime.date.today().month,
                                                                                       day=datetime.date.today().day)):
                cursor.execute(UPDATE_END_TIME, [datetime.datetime.now().time(), user_id, datetime.date.today()])
                db.commit()
                LOGGER.debug("下班时间更新 原下班时间: " + str(one[4]) + ", 新下班时间: " + str(
                    datetime.datetime.now() - datetime.datetime(year=datetime.date.today().year,
                                                                month=datetime.date.today().month,
                                                                day=datetime.date.today().day)))
            else:
                LOGGER.debug("下班时间不更新 原下班时间: " + str(one[4]) + ", 新下班时间: " + str(
                    datetime.datetime.now() - datetime.datetime(year=datetime.date.today().year,
                                                                month=datetime.date.today().month,
                                                                day=datetime.date.today().day)))

    except Exception as e:
        # 数据库回滚
        if db is not None:
            db.rollback()

        LOGGER.error("下班记录更新异常 Exception = " + str(e))
        LOGGER.error("下班记录更新异常  当前时间 " + str(
            datetime.datetime.now() - datetime.datetime(year=datetime.date.today().year,
                                                        month=datetime.date.today().month,
                                                        day=datetime.date.today().day)))
    finally:
        # 关闭数据库连接
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


# 插入tenant
def insert_tenant(database, user):
    tenants = []

    db = None
    cursor = None

    try:
        db = pymysql.connect(host=database.host,
                             port=int(database.port),
                             user=database.username,
                             password=database.password,
                             database=database.database,
                             charset='utf8')
        cursor = db.cursor()
        # 查找所有租户
        cursor.execute(INSERT_TENANT, [user.tenant, user.id, None])
        db.commit()
        LOGGER.error("插入新租户 租户 ： " + user.tenant)

    except Exception as e:
        # 数据库回滚
        if db is not None:
            db.rollback()

        LOGGER.error("插入新租户异常 Exception = " + str(e))
    finally:
        # 关闭数据库连接
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

    return tenants


# 查找所有tenant
def find_tenants(database):
    tenants = []

    db = None
    cursor = None

    try:
        db = pymysql.connect(host=database.host,
                             port=int(database.port),
                             user=database.username,
                             password=database.password,
                             database=database.database,
                             charset='utf8')
        cursor = db.cursor()
        # 查找所有租户
        cursor.execute(FIND_TENANTS)
        result = cursor.fetchall()

        for one in result:
            tenants.append(one[0])
        LOGGER.debug("查找所有租户 : " + str(tenants))
    except Exception as e:
        # 数据库回滚
        if db is not None:
            db.rollback()

        LOGGER.error("查找所有租户异常 Exception = " + str(e))
    finally:
        # 关闭数据库连接
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

    return tenants


# 根据租户查找数据
def find_tenant_by_name(database, name):
    tenant = None

    db = None
    cursor = None

    try:
        db = pymysql.connect(host=database.host,
                             port=int(database.port),
                             user=database.username,
                             password=database.password,
                             database=database.database,
                             charset='utf8')
        cursor = db.cursor()
        # 查找所有租户
        cursor.execute(FIND_TENANT_BY_NAME, name)
        tenant = cursor.fetchone()

        if tenant is None:
            LOGGER.debug("查找租户不存在 : " + name)
    except Exception as e:
        # 数据库回滚
        if db is not None:
            db.rollback()

        LOGGER.error("查找租户异常 Exception = " + str(e))
    finally:
        # 关闭数据库连接
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

    return tenant
