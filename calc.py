from flask import Flask, render_template, jsonify,flash,request,redirect, url_for, session
from flask import Flask,jsonify, make_response
import flask_monitoringdashboard as dashboard
from auk import Ackermann,fib,factorial
import logging
import json
from logging import Formatter, FileHandler
from datetime import datetime
import sys





#sys.setrecursionlimit(50000)

#dashboard.bind(app)
app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
dashboard.bind(app)
@app.route('/')
def hello():
	return "welcome to the flask Implementation by Muthu"

@app.route('/login', methods = ['GET', 'POST'])
def login():
	'''Admin login page'''
	#Check if admin is already login
	if 'session_data' in session:
		if session['session_data']['admin_logged_in'] == True:
			return render_template('select.html')
	#Fetch post value from login form   
	if request.method == "POST":
                name = request.form.get("name")
                password = request.form.get("password")
                print(name,password)
		#Check user name and password is match to db details
                try:
                        #checklogin = model.check_login(name, password)
                        #checklogin = [element for tupl in checklogin for element in tupl]
                        checklogin = check_login(name, password)
                        session_data = dict(name=checklogin[1], email=checklogin[2], id=checklogin[0], admin_logged_in=True)
                        session['session_data'] = session_data
                        print("loggin success ful")
                        return render_template('select.html')
                except Exception as e:
                    print(str(e))
                    return redirect('/login')       
	return render_template('login.html')

@app.route("/logout")
def logout():
	'''Logout the session'''
	clear_session = [session.pop(key) for key in list(session.keys())]	
	return redirect("/login")

def check_login(name, password):
    d={'name':'admin','email':'muthu55@mail.com','id':1,'pw':'admin123'}

    if d['name'] == name and d['pw']==password:
        return [d['id'],d['name'],d['email']]
@app.route("/feb",methods = ['GET'])
def febnocci():
    try:
        
        app.logger.info("Started Febnocci....")
        n = request.args.get("n")
        if int(n) <0:
            d={'input':n,'Message':'Input less than 0, invalid input'}
            app.logger.error("Output {}".format(json.dumps(d)))
            return make_response(jsonify(d), 400)
        nth=fib(int(n))
        d={'input':n,'ouput':nth,'Message':"Success"}
        print(d)
        app.logger.info("Output :{}".format(json.dumps(d)))
        return make_response(jsonify(d), 200)
    except Exception as e:
        d={'input':n,'Message':"Error due to {}".format(str(e))}
        app.logger.error("Output {}".format(json.dumps(d)))
        return make_response(jsonify(d), 400)

@app.route("/ack",methods = ['GET'])
def ackerman():
    try: 
        app.logger.info("Started Auckerman....")
        n = request.args.get("n")  
        m = request.args.get("m")
        if m is None or n is None:
            d={'input':[n,m],'Message':'We need two numbers as input, one missing'}
            app.logger.error("Output {}".format(json.dumps(d)))
            return make_response(jsonify(d), 400)
        n,m =int(n),int(m)
        if n<0 or m < 0:
            d={'input':[n,m],'Message':'Input less than 0, invalid input'}
            app.logger.error("Output {}".format(json.dumps(d)))
            return make_response(jsonify(d), 400)
        if (m==3 and n > 13) or (m==4 and n > 1) or (m==5 and n>0) or (m>5):
            d={'input':{"n":n,"m":m},'Message':"For this input, calculation is not psossible due to memory constrains,will get memory error, enter correct data"}
            print(d)
            app.logger.error("Output for Auckerman :{}".format(json.dumps(d)))
            return make_response(jsonify(d), 200)
        start_time = datetime.now()
        ackermann = Ackermann()
        v=ackermann.run(int(m),int(n))
        app.logger.info('ackermann(%d,%d): %d' % (m, n,v ))
        end_time = datetime.now()
        time_diff = end_time - start_time
        app.logger.info('execution time: %s' % time_diff)
        app.logger.info('Number of calls: %d' % ackermann.count)
        if ackermann.cache != {}:
            app.logger.info('Cache Hit count: %d' % ackermann.cache_hit)
            app.logger.info('Cache Miss count: %d' % ackermann.cache_miss)
            #app.logger.info('Cache Hit ratio: %.2f' % ((float)(ackermann.cache_hit) / ackermann.cache_miss * 100))        
        d={'input':{"n":n,"m":m},'ouput':v,'Message':"Success"}
        print(d)
        app.logger.info("Output :{}".format(json.dumps(d)))
        return make_response(jsonify(d), 200)
    except Exception as e:
        d={'input':{"n":n,"m":m},'Message':"Error due to {}".format(str(e))}
        app.logger.error("Output {}".format(json.dumps(d)))
        return make_response(jsonify(d), 400)

@app.route("/fac",methods = ['GET'])
def fact():
    try:
        app.logger.info("started webservice factorial...")
        n = request.args.get("n")
        f = factorial(int(n))
        d={'input':n,'ouput':f,'Message':"Success"}
        print(d)
        app.logger.info("Output :{}".format(d))
        return make_response(jsonify(d), 200)
    except Exception as e:
        d={'input':n,'Message':"Error due to {}".format(str(e))}
        app.logger.error("Output {}".format(json.dumps(d)))
        return make_response(jsonify(d), 400)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)
