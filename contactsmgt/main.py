from flask import flash,redirect,Flask, render_template, url_for,request
from datetime import datetime
from form import New,Box
from flask_sqlalchemy import SQLAlchemy


year=datetime.now().year
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///contactlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    num=db.Column(db.Integer)

app.secret_key='christian'

with app.app_context():
    db.create_all()
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home',year=year)
@app.route('/Add', methods=['POST', 'GET'])
def add():
    my_form=New()
    form=my_form
    if form.validate_on_submit():
        username=form.name.data
        usercontacts=form.contacts.data
        new_contact=Contact(name=username,num=usercontacts)
        flash (f'contact {new_contact.name} succefully created')
        with app.app_context():
            db.session.add(new_contact)
            db.session.commit()
        
        return redirect(url_for('all'))
    return render_template('user.html', title='Add contact',year=year, form=form)
@app.route('/All')
def all():
    allcontacts=Contact.query.all()
    return render_template('all.html', title='All Contacts',year=year,allcontacts=allcontacts)

@app.route('/edit/<id>', methods=['POST','GET'])
def edit(id):
    editcontact=Contact.query.get(id)
    if request.method=='POST':
        editcontact.name=request.form['name']
        editcontact.num=request.form['contact']
        db.session.commit()
        return redirect(url_for('all'))
    else:
        return render_template('edit.html', editcontact=editcontact)

@app.route('/delete/<id>')
def delete(id):
    move=Contact.query.get(id)
    deletecontact=Contact.query.get(id)
    db.session.delete(deletecontact)
    db.session.commit()
    return redirect(url_for('all'))
    


if __name__=='__main__':
    app.run(debug=True)
    
