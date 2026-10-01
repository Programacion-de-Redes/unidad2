'''
Mi primer servidor web con Flask y Python
Autor: Gabriel Barrón
Fecha: 30 septiembre
'''

from flask import Flask
app = Flask(__name__)

inventario = [ 
	{"hostname": "Core-SW01", "ip": "10.0.0.1", "status": "up"},
	{"hostname": "Dist-SW02", "ip": "10.0.0.2", "status": "down"},
	{"hostname": "Access-SW03", "ip": "10.0.0.3", "status": "up"},
	{"hostname": "Edge-R01", "ip": "172.16.1.1", "status": "down"} 
]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/<nombre>')
def saludo(nombre):
	return f"<h1>Hola {nombre}</h1>"

@app.route('/dispositivo/<device>')
def buscar_dispositivo(device):
	return f"{device}"	


if __name__ == "__main__":
	app.run(debug=True, port=5001)