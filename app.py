from flask import *
from requestDatabase import requestDatabase

app=Flask(__name__)
db=requestDatabase()

@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        name = request.form['name']
        message = request.form['message']
        db.add(name, message)
        return redirect('/')
    else:
        msg=db.getAll()
        no=str(db.len())
        return render_template('index.html', msg=msg, no=no)
        
@app.route('/consolemaster', methods=['POST','GET'])
def delete():
    if request.method=='POST':
        id = request.form['id']
        db.delete(id)
        return redirect('/consolemaster')
    else:
        js=db.getAll()
        return render_template('master.html', js=js)
if __name__ == '__main__':
    app.run()