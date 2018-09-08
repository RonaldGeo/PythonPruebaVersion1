from flask import Flask

app = Flask(__name__) #nuevo objeto

@app.route('/') #wrap o un decorador

def index():
	return 'HOla mundo' #regresa un string

app.run() #ejecuta el servidor en puerto 5000


