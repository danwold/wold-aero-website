from bottle import route, run, request, template, debug, static_file

@route('/:filename')
def send_image(filename):
	return static_file(filename,root='./')
@route('/')
def anotherpage():
	return template('main.tpl')

debug()       
run(reloader=True)
