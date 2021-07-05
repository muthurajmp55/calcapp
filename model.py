#db model for employee
import pymysql
# Import datetime class from datetime module
from datetime import datetime 

#Connect db 
#Database config
db = pymysql.connect(host='localhost', user='root', password='muthurajmp55',db='automate_recruitment')
cursor  = db.cursor()

def list_form():
	"""List the records form db"""
	sql = "SELECT id, name, role, team, status FROM cba_employee ORDER BY created_date desc"
	cursor.execute(sql)
	form_result = cursor.fetchall()
	return form_result

def create_form(args):
	"""Create form"""
	if(args):
		name = args['name']
		role = args['role']
		team = args['team']
		status = args['status']
		cursor.execute("INSERT INTO cba_employee(name, role, team, status) VALUES (%s, %s, %s, %s)", (name, role, team, status))
		db.commit() 
		return True

def edit_form(id):
	"""List the records form db"""
	sql = "SELECT id, name, role, team, status FROM cba_employee where id = {}".format(id)
	cursor.execute(sql)
	edit_result = cursor.fetchall()
	return edit_result

def update_form(args, id):
	""" Update records to db based id"""			  
	name = args['name']
	role = args['role']
	team = args['team']
	status = args['status']
	updated_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	sql = "UPDATE cba_employee SET name={},role={},team={}, status={}, updated_date={} WHERE id = {}".format("'"+name+"'","'"+role+"'","'"+team+"'","'"+status+"'","'"+updated_date+"'",id)
	cursor.execute(sql)
	db.commit()
	return True

def check_login(name, password):
	"""Check the login credentials"""
	sql = "SELECT * FROM cba_admin WHERE name = {} AND password = {}".format("'"+name+"'", "'"+password+"'")
	cursor.execute(sql)
	result = cursor.fetchall()
	if result:
		return result