from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstcrud.db'
db = SQLAlchemy(app)

class FirstApp(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.sno} - {self.fname}"

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        entry = FirstApp(fname=fname, lname=lname, email=email)
        db.session.add(entry)
        db.session.commit()
    allrecord = FirstApp.query.all()
    return render_template('Index.html', allrecord=allrecord)

@app.route('/delete/<int:sno>')
def delete(sno):
    record = FirstApp.query.get_or_404(sno)
    db.session.delete(record)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    record = FirstApp.query.get_or_404(sno)
    if request.method == 'POST':
        record.fname = request.form['fname']
        record.lname = request.form['lname']
        record.email = request.form['email']
        db.session.commit()
        return redirect('/')
    return render_template('update.html', record=record)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
