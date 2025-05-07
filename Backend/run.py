from flask import Flask ,render_template,url_for,redirect,flash
from forms import RegistrationForm ,LoginForm
from email_validator import EmailSyntaxError,EmailNotValidError
app = Flask(__name__)
app.secret_key ='hello world'

#client
@app.route('/')
@app.route('/Home')
def Home():
    return render_template ('coffee.html',title='Home')


#register and login 
email =None
passwo =None
@app.route('/Register', methods=['GET','POST'])
def Register():
    mail = None
    passw = None

    reg= RegistrationForm()
    if reg.validate_on_submit():
        mail =reg.Email.data
        passw = reg.Password.data
        email =mail
        passwo =passw
        reg.Email.data=""
        reg.Password.data =""
        return redirect(url_for('Login'))
    
    return render_template('register.html',title='Register',reg =reg)

    
@app.route('/Login',methods=['GET','POST'])
def Login():
    log = LoginForm()
    if log.validate_on_submit():
        mails =log.Email.data
        passws = log.Password.data
        if email == mails and passws == passwo :
            flash('tu as connecter success','success')
            return redirect(url_for('Admin'))
            
    return render_template ('login.html',title='Login',log =log)

#admin
@app.route('/Admin')
def Admin():
    return render_template ('admin.html',title='Admin')


@app.route('/Add')
def Add():
    return render_template ('add.html',title='Add')

@app.route('/Profit')
def Profit():
    return render_template ('profit.html',title='Profit')





if __name__ == '__main__':
    app.run(debug=True)
