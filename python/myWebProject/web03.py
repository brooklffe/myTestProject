import pymysql

# 数据库连接参数
host = '127.0.0.1'
port = 3306
user = 'root'
password = 'root@1234'
database = 'my_database01'

# 创建数据库连接
connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

try:
    # 创建游标对象
    with connection.cursor() as cursor:
        # 创建表（如果不存在）
        create_table_query = """
        CREATE TABLE IF NOT EXISTS tb7 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            mobil VARCHAR(15),
            email VARCHAR(255)
        )
        """
        cursor.execute(create_table_query)

        # 插入数据
        insert_data_query = """
        INSERT INTO tb7 (name, password,age, salary, email)
        VALUES (%s, %s, %s, %s,%s)
        """
        data_to_insert = ('John Doe', 'hehe',25, '1234', 'john.doe@example.com')
        cursor.execute(insert_data_query, data_to_insert)

    # 提交更改
    connection.commit()

except Exception as e:
    # 如果发生错误，回滚更改
    connection.rollback()
    print(f"Error: {e}")

finally:
    # 关闭连接
    connection.close()
