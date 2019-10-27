import mysql.connector


class DbHelper:

    def __init__(self):
        self.my_db = mysql.connector.connect(host="localhost", user="root", password="shamsad@123",  database="employee_db")
        self.my_cursor = self. my_db.cursor()

    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        self.my_cursor.execute("select max(emp_salary) from employee")
        return self.my_cursor.fetchone()[0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        self.my_cursor.execute("select min(emp_salary) from employee")
        return self.my_cursor.fetchone()[0]

    def close_db_connection(self):
        ''''
        Closing db_connection
        '''
        self.my_cursor.close()
        self.my_db.close()


if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
    db_helper.close_db_connection()
