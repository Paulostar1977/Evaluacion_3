from flask import Flask, render_template, request

app = Flask(__name__)


# Ruta principal (Menú principal)
@app.route('/')
def home():
    return render_template('index.html')  # Asegúrate de tener el archivo index.html


# Ruta para el Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Obtener las notas y asistencia del formulario
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Calcular el promedio de las notas
        promedio = (nota1 + nota2 + nota3) / 3

        # Determinar si el estudiante está aprobado o reprobado
        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        # Pasar los resultados al template
        return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    # Si es un GET, solo se renderiza el formulario vacío
    return render_template('ejercicio1.html', promedio=None, estado=None)


# Ruta para el Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Obtener los 3 nombres del formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Calcular el nombre más largo
        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_largo)

        # Pasar los resultados al template
        return render_template('ejercicio2.html', nombre_largo=nombre_largo, cantidad_caracteres=cantidad_caracteres)

    # Si es un GET, solo se renderiza el formulario vacío
    return render_template('ejercicio2.html', nombre_largo=None, cantidad_caracteres=None)


if __name__ == '__main__':
    app.run(debug=True)
