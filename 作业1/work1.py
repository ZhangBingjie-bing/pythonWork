
class SQL:
    def __init__(self,host,database,username,password,port):
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self.port = port
        self.flag = 0


    # 连接数据库
    def connect(self):
        config = {
            host: '0.0.0.0',
            database: 'user',
            username: 'zbj',
            password: '123456',
            port: '3306',
        }
        if self.host == config.get(host) and self.database == config.get(database) and self.username == config.get(username) and self.password == config.get(password) and self.port == config.get(port):
            print('connect is successed!')
            self.flag = 1
        else:
            print('connect is failed!')
            self.flag = 0

    def select(self, *args, **kwargs):
        # 判断是否链接数据库
        if not self.flag:
            print('数据库未连接!')
            exit(-1)

        if args:
            print(args)
            print('不符合条件')
        if kwargs:

            # print('Select {} from {} where {}={}'.format(kwargs['column'], kwargs['tablename'], kwargs['condation']))
            print('Select {} from {} where {}'.format(kwargs['column'], kwargs['tablename'], kwargs['condation']))

if __name__ == '__main__':
    # p = {'query': 'student', 'method': 'age,name', 'age': '12','name':'li'} # Select name FROM Student where age=12
    host = input("请输入数据库地址(建议输入0.0.0.0)：")
    database = input("请输入数据库名称(建议输入user)：")
    username = input("请输入用户名(建议输入zbj)：")
    password = input("请输入密码(建议输入123456)：")
    port = input("请输入端口号(建议输入3306)：")

    sql = SQL(host,database,username,password,port)
    sql.connect()
    if(sql.flag):
        tablename = input("请输入要查询的表名(建议输入user)：")
        column = input("请输入要查询的列名(比如输入no,name)：")
        condation = input("请输入要查询的条件(比如输入no = 1 and name = 1)：")
        sql.select(tablename=tablename, column=column, condation=condation)










