from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

inscritos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lista')
def lista():
    return render_template('lista.html', inscritos=inscritos)

@app.route('/registrar', methods=['POST'])
def registrar():
    
    nuevo_inscrito = {
        'id': len(inscritos) + 1,
        'fecha': request.form['fecha'],
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'turno': request.form['turno'],
        'seminarios': request.form.getlist('seminarios')
    }
    inscritos.append(nuevo_inscrito)
    return redirect(url_for('lista'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    inscrito = next((i for i in inscritos if i['id'] == id), None)
    
    if request.method == 'POST':
        inscrito['fecha'] = request.form['fecha']
        inscrito['nombre'] = request.form['nombre']
        inscrito['apellido'] = request.form['apellido']
        inscrito['turno'] = request.form['turno']
        inscrito['seminarios'] = request.form.getlist('seminarios')
        return redirect(url_for('lista'))

    return render_template('editar.html', inscrito=inscrito)

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    global inscritos
    inscritos = [i for i in inscritos if i['id'] != id]
    return redirect(url_for('lista'))

if __name__ == '__main__':
    app.run(debug=True)