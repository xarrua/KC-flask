#importar la libreria de flask
from flask import Flask

#inicializar la variable app con flask
app = Flask(__name__)

#inicializar el servidor de flask
# en mac: export FLASK_APP=main.py
# en windows: set FLASK_APP=main.py

#Comando para ejecutar el servidor:
#flask --app main run

#Comando para ejecutar el servidor en otro puerto diferente por default es el 5000
#flask --app main run -p 5002

#Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real
#flask --app main --debug run

@app.route("/hola")
def hola_mundo():
    return "Esto mola mucho"

#ejercicio una ruta que devuelva una lista de frutas el path seria /frutas
@app.route("/frutas")
def lista_frutas():
    list_fruta = ['Platano','Fresa','Piña','Melon','Naranja']
    return list_fruta

#ejemplo para enviar parametros en las rutas
@app.route("/nombre/<n>/apellido/<a>/edad/<int:e>")
def tunombre(n,a,e):
    return f"Eres {n} {a} y tienes {e} años de edad"

#ejercicio2 realizar una ruta que devuelva el cuadrado de un numero dado, /numero/<parametro>
@app.route("/numero/<int:parametro>")
def cuadrado(parametro):
    #parametro = int(parametro)
    return f"El cuadrado de {parametro} es {parametro*parametro}"

#ejercicio3, realizar una ruta, que dinamicamente pueda solicitar o realizar
#operaciones de suma,resta,multiplicacion y division segun los parametros pasados en la ruta