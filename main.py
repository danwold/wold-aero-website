from bottle import route, run, request, template, debug, static_file

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

debug()       
run(reloader=True)
