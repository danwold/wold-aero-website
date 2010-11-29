from bottle import route, run, request, template, debug, static_file,redirect
##from time import *
import urllib
import pickle
from logweb import *
global authenticated
authenticated = False

@route('/:filename')
def send_image(filename):
	return static_file(filename,root='./')
@route('/')
def mainpage():
	return template('main.tpl')
@route('/service')
def service():
	return template('service.tpl')

@route('/contact')
def contact():
	return template('contact.tpl')

@route('/portfolio')
def portfolio():
	return template('portfolio.tpl')

@route('/tide')
def tide():
	connection = urllib.urlopen('http://danwold:llbk123@api.pachube.com/v2/feeds/12634.csv')
	
	tidefeet = connection.read().split(',')[2]

	return template('tides.tpl',tidefeet=tidefeet)

@route('/admin',method='GET')
def admin():
	if (request.GET.get('save','')):
		
		username = request.GET.get('username','')
		password = request.GET.get('password','')
		if (username == 'dano' and password == 'dano'):
			auth.state = True
			redirect("/add") 
										

		else:
			return template('login.tpl')
		
	else:
			
		return template('login.tpl')

@route('/add',method='GET')	
def add():	
	reply = ''
	if (request.GET.get('save2','')):
		inblogpost = request.GET.get('blogpost')
		indate = request.GET.get('date')
		if inblogpost and indate :
		
			blog.append(post(indate,inblogpost))
			saveblogfile()
			reply = 'submission submitted'
			return template('admin.tpl',reply=reply)
		else:	
			
			reply = 'non valid submission'
			return template('admin.tpl',reply=reply)
	if (request.GET.get('logoff','')):
		auth.state = False
		redirect('/')
	if auth.state == True:
		return template('admin.tpl',reply=reply)

@route('/blog')
def blogthing():
	return template('blog.tpl',blog=blog) 

##@route('/extractor')	
##def ex():
##	return logweb.mainpage()


class post:
	def __init__(self,date,text):
		self.date = date
		self.text = text
class auth:
	def __init__(self):
		self.state = False


try:
	blogfile = open('blogfile','r')
	blog = pickle.load(blogfile)
	blogfile.close()
except:	
	blogfile = open('blogfile','w')
	blog = []
	pickle.dump(blog,blogfile)
	blogfile.close()

def saveblogfile():	
	blogfile = open('blogfile','w')
	pickle.dump(blog,blogfile)
	blogfile.close()

auth = auth()		


debug()       
run(reloader=True)
