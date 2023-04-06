

# 封装数据库
import pymysql


class CheckSql:

    def __init__(self,host,port,user,password,database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database


    def chSql(self,sql,size=0):
        # 创建连接
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                    password=self.password, database=self.database,
                                    charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()
        # self.sql = sql

        # startswith():
        # 方法用于检查字符串是否是以指定子字符串开头,如果是则返回True，否则返回False。如果参数beg和
        # end指定值，则在指定范围内检查。str.startswith(str, beg=0, end=len(string));
        # 参数:
        # str - -检测的字符串。
        # strbeg --可选参数用于设置字符串检测的起始位置。
        # strend --可选参数用于设置字符串检测的结束位置

        if sql.startswith('select'):
            try:
                self.cursor.execute(sql)
                # 统计查询结果的记录
                self.cnt = self.cursor.rowcount
                if size == 0:
                    self.res = self.cursor.fetchall()  #查询所有
                elif size == 1:
                    self.res = self.cursor.fetchone()  #查询一个
                else:
                    self.res = self.cursor.fetchmany(size)   #查询指定条数
            except Exception as e:
                print('查询失败',e)
        else:
            print("非查询语句")
        self.cursor.close()
        self.conn.close()
        return self.res,self.cnt

    def AddUpDel(self,sql):
        # 创建连接
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                    password=self.password, database=self.database,
                                    charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()

        if sql.startswith('insert'):
            try:
                self.cursor.execute(sql)
                print("添加成功")
            except Exception as e:
                self.conn.rollback()
                print("添加失败",e)
        elif sql.startswith('update'):
            try:
                self.cursor.execute(sql)
                print("修改成功")
            except Exception as e:
                self.conn.rollback()
                print("修改失败",e)
        else:
            try:
                self.cursor.execute(sql)
                print("删除成功")
            except Exception as e:
                self.conn.rollback()
                print("删除失败", e)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    # ck =CheckSql(host='localhost',port=3306,user='root',password='123456',database='student')
    # sql = 'select * from student.stu where id=15'
    # sql = 'select * from student.stu'
    # res = ck.chSql(sql,3)
    # print(res)
    # ck.AddUpDel("insert into stu(score,xueke) values(120,'测试')")
    # ck.AddUpDel("update stu set xueke='体育' where id =17")
    # ck.AddUpDel("delete from stu where id=17")

    ck = CheckSql(host="fat-bj-china-b2c-02.chfa9nngsipy.rds.cn-north-1.amazonaws.com.cn",
                  user="dml_user", password="tiens_123", port=3306, database="ruishi_core_service")
    sql = "select content from ruishi_core_service.base_sms_record where mobile = '18833333333' ORDER BY created_time desc limit 1"
    captcha = ck.chSql(sql, 1)[0][0]
    print(captcha)
    print(type(captcha))
    print(captcha[21:27])







