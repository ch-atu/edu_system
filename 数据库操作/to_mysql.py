import pandas as pd
import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', password='1234', port=3306, db='schoolnew')
cursor = db.cursor()
print(cursor)
print('开始初始化数据库信息...')


# todo 初始化用户信息表
file_name = 'tables/用户信息表.xls'
df = pd.read_excel(file_name)
# print(df.values)
for i in df.values:
    sql = f"""
    insert into User (password, user_id, user_name, user_type, is_admin, is_active) 
    values ('{i[0]}', '{i[2]}', '{i[3]}', '{i[4]}', {i[5]}, {i[6]})
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print('初始化用户信息表错误', e)


# todo 初始化院系信息表
file_name = 'tables/院系信息表.xls'
df = pd.read_excel(file_name)
# print(df)
# print(df.values)
# print(df.columns)
for key, i in enumerate(df.values):
    # print(key, i)
    sql = f"""insert into CollegeTable values ('{i[0]}','{i[1]}')"""
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print('初始化院系信息表错误', e)

# todo 初始化学生信息表
file_name = 'tables/学生信息表.xls'
df = pd.read_excel(file_name)
# print(df)
# print(df.values)
# print(df.columns)
for i in df.values:
    sql = f"""insert into StudentTable values ('{i[0]}','{i[1]}', '{i[2]}')"""
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print('初始化学生信息表错误', e)

# todo 初始化教师信息表
file_name = 'tables/教师信息表.xls'
df = pd.read_excel(file_name)
# print(df)
# print(df.values)
# print(df.columns)
for i in df.values:
    sql = f"""insert into TeacherTable values ('{i[0]}','{i[1]}', '{i[2]}')"""
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print('初始化教师信息表错误', e)

# todo 初始化课程信息表
file_name = 'tables/课程信息表.xls'
df = pd.read_excel(file_name)
# print(df)
# print(df.values)
# print(df.columns)
for i in df.values:
    # print(i[1], type(i[1]))
    # course_id = '0' + str(i[0])
    # print(course_id, type(course_id))
    sql = f"""insert into CourseTable values ('{i[0]}','{i[1]}', {i[2]})"""
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print('初始化课程信息表错误', e)

# todo 初始化开课表
file_name = 'tables/开课信息表.xls'
df = pd.read_excel(file_name)
# print(df)
# print(df.values)
# print(df.columns)
for key, i in enumerate(df.values):
    # print(key, i)
    # course_id = '0' + str(i[0])
    # print(course_id, type(course_id))
    sql = f"""insert into OpenTable values ({key}, '{i[0]}','{i[1]}', '{i[2]}', '{i[3]}')"""
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print('初始化开课表错误', e)

print('数据库初始完成')











