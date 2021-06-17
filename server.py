from flask import Flask, render_template, redirect, request,session
app = Flask(__name__)
from users import User


@app.route('/')
def index():
    result = User.get_all_users()
    return render_template('index.html', users = result)


@app.route('/users')
def form_users():
    return render_template('users.html')


@app.route('/delete-user/<int:id>')
def delete_user(id):
    id_to_str = str(id)
    User.delete_user(id_to_str)
    return redirect('/')


@app.route('/update-user-data', methods=[ 'POST'])
def update_user1():
    data = {
        "id" : request.form["id"],
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }

    User.update_user(data);
    return redirect('/')


@app.route('/update-user/<int:id>/<first_name>/<last_name>/<email>')
def update_user2(id,first_name,last_name,email):
    data = {
        "id" : str(id),
        "first_name":first_name,
        "last_name":last_name,
        "email":email
    }
    return render_template("updateusers.html",users = data)


@app.route('/create-user',methods=['GET','POST'])
def create_user():
    req = request.form
    User.add_user(req)
    return redirect('/')




if __name__ == '__main__':
  app.run(debug=True)
 