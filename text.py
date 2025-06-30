from flask import Flask
app=Flask(__name__)
@app.route('/admin')
def admin():
    return 'this is admin'
@app.route('/harsha')
def harsha():
    return 'this is harsha'
@app.route('/cmrcollege')
def cmrcollege():
    return 'this is cmrcollege'


def hello():
    return 'Hello,World!'
if __name__ =="__main__":
    app.run(debug=True) 