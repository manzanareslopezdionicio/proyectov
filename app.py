from flask import Flask 

app=Flask(__name__)

@app.route('/') # Decorador para la ruta principal
def home(): # Función para la ruta principal
    return "¡Hola, mundo!"

@app.route('/contacto')
def contacto(): # Función para la ruta de contacto
    return "Esta es la pagina de contactos"

@app.route('/about')
def about(): # Función para la ruta de acerca de
    return "Esta es la pagina de acerca de"

@app.route('/servicios/<nombre>')
def servicios(nombre): # Función para la ruta de servicios
    return 'El nombre del servicio es: %s' % nombre

@app.route('/edad/<edad>')
def edad(edad): # Función para la ruta de edad
    return 'La edad es: {} años'.format(edad)
@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1,num2):
    resultado=num1+num2
    return 'La suma de {} y {} es: {}'.format(num1,num2,resultado)

if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Ejecuta la aplicación en modo de depuración
