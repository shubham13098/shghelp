
from flask import *
app = Flask(__name__)

app.secret_key="rhytgefdwfgtrerthref"

@app.route('/')
def rootef():
	if('user_name' not in session):
		session['user_name']='none'
	if('logged_in' not in session):
		session['logged_in']=False
	return render_template('home.html',logged_in=session['logged_in'],user_name=session['user_name'])
@app.route('/h')
def home():
	if('user_name' not in session):
		session['user_name']='none'
	if('logged_in' not in session):
		session['logged_in']=False
	return render_template('home.html',logged_in=session['logged_in'],user_name=session['user_name'])
@app.route('/p')
def popular():
	if('user_name' not in session):
		session['user_name']='none'
	if('logged_in' not in session):
		session['logged_in']=False
	return render_template('popular.html',logged_in=session['logged_in'],user_name=session['user_name'])
@app.route('/a')
def about():
	if('user_name' not in session):
		session['user_name']='none'
	if('logged_in' not in session):
		session['logged_in']=False
	return render_template('about.html',logged_in=session['logged_in'],user_name=session['user_name'])
@app.route('/w1')
def Hunger():
	if('user_name' not in session):
		session['user_name']='none'
	if('logged_in' not in session):
		session['logged_in']=False
	return render_template('webpage_1.html',logged_in=session['logged_in'],user_name=session['user_name'])
@app.route('/w2')
def Soft():
	if('user_name' not in session):
		session['user_name']='none'
	if('logged_in' not in session):
		session['logged_in']=False
	return render_template('webpage_2.html', logged_in=session['logged_in'],user_name=session['user_name'])
@app.route('/w3')
def Costmetics():
	if('user_name' not in session):
		session['user_name']='none'
	if('logged_in' not in session):
		session['logged_in']=False
	return render_template('webpage_3.html', logged_in=session['logged_in'],user_name=session['user_name'])
@app.route('/w4')
def Others():
	if('user_name' not in session):
		session['user_name']='none'
	if('logged_in' not in session):
		session['logged_in']=False
	return render_template('webpage_4.html',logged_in=session['logged_in'],user_name=session['user_name'])
@app.route('/help')
def Help():
	if('user_name' not in session):
		session['user_name']='none'
	if('logged_in' not in session):
		session['logged_in']=False
	return render_template('feedback.html',logged_in=session['logged_in'],user_name=session['user_name'])
@app.route('/f1', methods=['GET' , 'POST'])
def log():
	validuser=0
	error = None
	if request.method=='POST':
		data = open('data.txt','r')
		for line in data:
			a=line.split()
			user=a[0]
			passw=a[1]
			if request.form['username'] == user:
				if request.form['password'] == passw:
					validuser=1
					session['logged_in']=True
					session['user_name']=user
					break
		data.close()
		# if(request.form['username']!='admin' and request.form['password']!="admin"):
		# 	error = 'Invalid Crdedentials. Please try again.'
		# else:
		# 	return redirect(url_for('home'))
		if validuser==0:
			error = 'Invalid Credentials. Please try again.'
			return render_template("log.html", error=error,logged_in=session['logged_in'],user_name=session['user_name'])
		else:
			return render_template("home.html", logged_in=session['logged_in'],user_name=session['user_name'])
	return render_template("log.html", error=error,logged_in=session['logged_in'],user_name=session['user_name'])

@app.route("/logout")
def logout():
    session['logged_in']=False
    session['user_name']=None
    return redirect(url_for('home'))

@app.route('/f2', methods=['GET' , 'POST'])		 
def signup():
	error = None
	validuser=1
	if request.method == 'POST':
		data = open('data.txt','r')
		for line in data:
			a=line.split()
			user=a[0]
			if request.form['username'] == user:
				validuser=0
		data.close()
		if validuser==0:
			error = 'user already exist'
			return render_template("signup.html",error=error)
		else:
			data = open('data.txt','a')
			data.write(request.form['username'])
			data.write(' ')
			data.write(request.form['password'])
			data.write("\r\n")
			data.close()
			return render_template("congo.html",logged_in=session['logged_in'],user_name=session['user_name'])
	return render_template("signup.html",error=error )

if __name__ == '__main__' :
         app.run(debug=True)
