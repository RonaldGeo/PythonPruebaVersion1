from flask import Flask

app = Flask(__name__) #nuevo objeto

@app.route('http://35.196.160.196:8080/') #wrap o un decorador

def index():
	return 'HOla mundo' #regresa un string

app.run() #ejecuta el servidor en puerto 5000


