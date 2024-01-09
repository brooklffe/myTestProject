from flask import Flask,render_template
from flask import request

app = Flask(__name__)

@app.route("/show/info")
def index():
    # return"测试文本 hello world"
    return render_template("index2.html")
    
@app.route("/register", methods = ["GET"])
def register():
    return render_template("register.html")

@app.route("/do/reg", methods = ["GET","POST"])
def do_register():
    if request.method == "GET":
        print(request.args)
        return"注册成功 get"
    else:
        print(request.form)
        return"注册成功 post"

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        print(request.args)
        return render_template("login.html")
    else:
        print(request.form)
        return render_template("login.html")
    
    

# @app.route("/post/reg", methods = ["POST"])
# def post_register():
#     print(request.form)
#     return"注册成功 post"
    

if __name__ == '__main__':
#    app.run(host='0.0.0.0',debug=True,port=8080)
    app.run()
    

