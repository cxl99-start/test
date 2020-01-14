# region 使用web框架
# from flask import Flask
# from flask import request
# app=Flask(__name__)   #app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递(name)
#
# @app.route('/',methods=['GET','POST'])
# def home():
#     return '<h1>Home</h1>'
#
# @app.route('/signin',methods=['GET'])
# def signin_from():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form> '''
#
# @app.route('/signin',methods=['POST'])
# def signin():
#     if request.form['username']=='admin' and request.form['password']=='123456':
#         return '<h3>Welocme admin!</h3>'
#     return '<h3>对不起，您输入的密码有误！</h3>'
#
# if __name__=='__main__':
#     app.run()
# endregion

#使用模板
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='账号密码有误！', username=username)

if __name__ == '__main__':
    app.run()