from bottle import route, run, request, template, debug, static_file
from time import *
from gps import *
def getspeed():
		
	g = gps(mode=WATCH_ENABLE)
	g.poll()
        if PACKET_SET:
               	g.stream()
	speed = str(g.fix.speed)

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

@route('/gps')
def loc():
	speed = 0
	click = 0
	speed = speed+1
		
	
	
	
	return template('location.tpl',speed=speed,click=click)
	bottle.TEMPLATES.clear()
	sleep(2)
	loc()
	
	
	

debug()       
run(reloader=True)
