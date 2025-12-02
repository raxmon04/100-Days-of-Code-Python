from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function

def maeke_underlined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
    '<p>This is a paragraph.</p>' \
    '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTRvaW9vcGFoaHYxcTBxMTJvZnk0bGV4eGVhZ3V0dTlvNng1Y3l3aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dRcMsUUrnR8He/giphy.gif" width="300">'

@app.route('/bye')
@make_bold
@make_emphasis
@maeke_underlined
def bye():
    return 'Bye!'

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello there {name}, you are {number} years old!'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f'This is {user.name}\'s blog post')

new_user = User('Ramon')
new_user.is_logged_in = True
create_blog_post(new_user)
            