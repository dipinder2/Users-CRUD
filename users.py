from mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.id = data["id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def get_all_users(cls):
        mysql = connectToMySQL("users")
        query = "SELECT * FROM users"
        results = mysql.query_db(query)
        res = []
        for result in results:    
            res.append(User(result))
        return res
    
    
    @classmethod
    def add_user(cls,formdata):
        query = 'INSERT INTO users VALUES(null, %(first_name)s,%(last_name)s,%(email)s,NOW(),NOW())'
        mysql = connectToMySQL('users')
        mysql.query_db(query,formdata)
    
    
    @classmethod
    def delete_user(cls,id):
        data = {"id":id}
        query = 'DELETE FROM users WHERE id = %(id)s'
        mysql = connectToMySQL('users')
        mysql.query_db(query,data)

        
        
    @classmethod
    def update_user(cls,data):
        print(data)
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at=NOW() WHERE id = %(id)s'
        mysql = connectToMySQL('users')
        mysql.query_db(query,data)
