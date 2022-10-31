from flask import Flask, request,jsonify ,url_for, render_template, redirect, session
from database import db
from flask_migrate import Migrate
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from models import Automovil, Empleado,Locales,Cliente,Gerente
from forms import EmpleadoForm, ClienteForm

app = Flask(__name__)

#Configuracion de la base de datos
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'examen2'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACE_MODIFICATION'] = False

app.config['SECRET_KEY'] = 'algofacil'

#logging.basicConfig(filename='error.log',level=logging.DEBUG)

db.init_app(app)

#Configurar migracion
migrate = Migrate()
migrate.init_app(app,db)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        usuario = request.form['username']
        session['username'] = usuario
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/empleado')
def empleados():
    if 'username' in session:
        empleados = Empleado.query.all()
        return render_template('/empleado/empleados.html',empleados = empleados)
    else:
        return redirect(url_for('login'))

@app.route('/empleados/<int:id>')
def verEmpleado(id):
    if 'username' in session:
        empleado = Empleado.query.get_or_404(id)
        return render_template('/empleado/detalleEmpleado.html',empleado = empleado)
    else:
        return redirect(url_for('login'))

@app.route('/empleados/agregar', methods=["GET","POST"])
def agregarEmpleado():
    if 'username' in session:
        empleado = Empleado()
        empleadoForm = EmpleadoForm(obj=empleado)
        if request.method == "POST":
            if empleadoForm.validate_on_submit():
                empleadoForm.populate_obj(empleado)
                db.session.add(empleado)
                db.session.commit()
                return redirect(url_for("empleados"))
        return render_template('/empleado/agregarEmpleado.html', forma = empleadoForm)
    else:
        return redirect(url_for('login'))

@app.route('/empleados/editar/<int:id>', methods=["GET","POST"])
def editarEmpleado(id):
    if 'username' in session:
        app.logger.debug(request.headers.get('token'))
        empleado = Empleado.query.get_or_404(id)
        empleadoForm = EmpleadoForm(obj=empleado)
        if request.method == "POST":
            if empleadoForm.validate_on_submit():
                empleadoForm.populate_obj(empleado)
                db.session.commit()
                return redirect(url_for("empleados"))
        return render_template('/empleado/editarEmpleado.html', forma = empleadoForm)
    else:
        return redirect(url_for('login'))


@app.route('/empleados/eliminar/<int:id>')
def eliminarEmpleado(id):
    if 'username' in session:
        app.logger.debug(request.headers.get('token'))
        empleado = Empleado.query.get_or_404(id)
        db.session.delete(empleado)
        db.session.commit()
        return redirect(url_for('empleados'))
    else:
        return redirect(url_for('login'))

@app.route('/cliente')
def clientes():
    if 'username' in session:
        clientes = Cliente.query.all()
        return render_template('/cliente/clientes.html',clientes = clientes)
    else:
        return redirect(url_for('login'))

@app.route('/clientes/<int:id>')
def verCliente(id):
    if 'username' in session:
        cliente = Cliente.query.get_or_404(id)
        return render_template('/cliente/detalleCliente.html',cliente = cliente)
    else:
        return redirect(url_for('login'))

@app.route('/clientes/agregar', methods=["GET","POST"])
def agregarCliente():
    if 'username' in session:
        cliente = Cliente()
        clienteForm = ClienteForm(obj=cliente)
        if request.method == "POST":
            if clienteForm.validate_on_submit():
                clienteForm.populate_obj(cliente)
                db.session.add(cliente)
                db.session.commit()
                return redirect(url_for("clientes"))
        return render_template('/cliente/agregarCliente.html', forma = clienteForm)
    else:
        return redirect(url_for('login'))

@app.route('/clientes/editar/<int:id>', methods=["GET","POST"])
def editarCliente(id):
    if 'username' in session:
        app.logger.debug(request.headers.get('token'))
        cliente = Cliente.query.get_or_404(id)
        clienteForm = ClienteForm(obj=cliente)
        if request.method == "POST":
            if clienteForm.validate_on_submit():
                clienteForm.populate_obj(cliente)
                db.session.commit()
                return redirect(url_for("clientes"))
        return render_template('/cliente/editarCliente.html', forma = clienteForm)
    else:
        return redirect(url_for('login'))


@app.route('/clientes/eliminar/<int:id>')
def eliminarCliente(id):
    if 'username' in session:
        app.logger.debug(request.headers.get('token'))
        cliente = Cliente.query.get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return redirect(url_for('clientes'))
    else:
        return redirect(url_for('login'))

@app.route('/automovil',methods=["GET","POST"])
def getAutomovils():
    if request.method == "GET":
        automovils = Automovil.query.all()
        return jsonify(automovils = Automovil.serialize_list(automovils))
    elif request.method == "POST":
        info = request.json
        automovil = Automovil(modelo=info["modelo"], costo = info["costo"])
        db.session.add(automovil)
        db.session.commit()
        return "Automovil agregado"

@app.route('/automovil/<int:id>',methods=["GET"])
def getAutomovil(id):
    if request.method == "GET":
        automovil = Automovil.query.get_or_404(id)
        return jsonify(Automovil.serialize(automovil))

@app.route('/automovil/eliminar',methods=["DELETE"])
def eliminarAutomovil():
    if request.method == "DELETE":
        id = request.headers.get('id')
        automovil = Automovil.query.get_or_404(id)
        db.session.delete(automovil)
        db.session.commit()
        return f"Automovil con ID: {id} eliminado"

@app.route('/local',methods=["GET","POST"])
def getLocales():
    if request.method == "GET":
        locals = Locales.query.all()
        return jsonify(locals = Locales.serialize_list(locals))
    elif request.method == "POST":
        info = request.json
        local = Locales(direccion=info["direccion"], ciudad = info["ciudad"])
        db.session.add(local)
        db.session.commit()
        return "Local agregado"

@app.route('/local/<int:id>',methods=["GET"])
def getLocals(id):
    if request.method == "GET":
        local = Locales.query.get_or_404(id)
        return jsonify(Locales.serialize(local))

@app.route('/local/eliminar',methods=["DELETE"])
def eliminarLocales():
    if request.method == "DELETE":
        id = request.headers.get('id')
        local = Locales.query.get_or_404(id)
        db.session.delete(local)
        db.session.commit()
        return f"Locales con ID: {id} eliminado"
    
@app.route('/gerente',methods=["GET","POST"])
def getGerentes():
    if request.method == "GET":
        gerentes = Gerente.query.all()
        return jsonify(gerentes = Gerente.serialize_list(gerentes))
    elif request.method == "POST":
        info = request.json
        gerente = Gerente(direccion=info["direccion"], nombre = info["nombre"])
        db.session.add(gerente)
        db.session.commit()
        return "Gerente agregado"

@app.route('/gerente/<int:id>',methods=["GET"])
def getGerente(id):
    if request.method == "GET":
        gerente = Gerente.query.get_or_404(id)
        return jsonify(Gerente.serialize(gerente))

@app.route('/gerente/eliminar',methods=["DELETE"])
def eliminarGerente():
    if request.method == "DELETE":
        id = request.headers.get('id')
        gerente = Gerente.query.get_or_404(id)
        db.session.delete(gerente)
        db.session.commit()
        return f"Gerente con ID: {id} eliminado"


@app.errorhandler(404)
def noEncontrado(error):
    return render_template('404.html',error=error),404