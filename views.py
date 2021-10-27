import functools
# from formularios import formularioMensaje
from flask import Flask, abort, render_template, blueprints, request, jsonify, redirect, url_for,session, flash, send_file
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db
from markupsafe import escape
from mensaje import mensajes


#creo el objeto que representa la aplicacion 
main = blueprints.Blueprint('main', __name__) #esto es un constructor - , url_prefix='/home'

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'usuario' not in session: #puedes hacer otro tipo de validación 
            return redirect(url_for('main.home'))
        return view(**kwargs)

    return wrapped_view

# creo las rutas - con cualquiera de estos alias voy a acceder a la pagima principal del sitio 

@main.route('/')    # Aqui aterriza el usuario cuando se dirige a la app, y es redireccionado al home
def site():         # desde aqui puede ser redireccionado donde se desee y puede ejecutarse el codigo que se 
    return redirect(url_for('main.home'))   # requiera a modo de setup

@main.route('/home/', methods=['GET', 'POST'])
def home():

    '''if(request.method == 'POST'):

        Accion = request.form['Boton']

        if(Accion == 'login'):      # Boton login pulsado -> redirecciona al formulario de login
            return redirect(url_for('main.login'))

        if(Accion == 'signUp'):      # Boton login pulsado -> redirecciona al formulario de login
            return redirect(url_for('main.signUp'))'''

    return render_template('home.html')

@main.route('/login/', methods=['GET', 'POST'])
def login():

    '''if(request.method == 'POST'): 

        usuario= request.form['username']
        clave = request.form['userPassword']
        Accion = request.form['Boton']

        if(Accion == 'login'):      # Boton iniciar sesion pulsado -> me direcciona al index de la app
            
            # return redirect(url_for('main.index'))
            if(usuario =='notus' and clave =='notus'):
                # return redirect(url_for('main.listadoMensajes')) # Aquise programa lo que debe hacer cuando el login sea exitoso
                return redirect(url_for('main.index'))

    return render_template('login.html') '''

    if request.method =='POST':

        usuario = escape(request.form['username'])
        clave = escape(request.form['userPassword'])

        db = get_db()
        #sql = "select * from usuario where usuario = '{0}' and clave= '{1}'".format(usuario, clave)

        # numUsers = db.execute('SELECT count(*) FROM Persona').fetchone()
        # if(numUsers == 0):
        # print(numUsers)

        user = db.execute('select * from Persona where username = ? ', (usuario,)).fetchone()
        db.commit()
        db.close()

        if user is not None:

            clave = clave + usuario
            
            sw = check_password_hash(user[9], clave)
            if(sw):

                session['nombre'] = user[3]
                session['apellido'] = user[4]
                session['usuario'] = user[8]
                session['role'] = user[12]

                return redirect(url_for('main.index'))
        flash('Usuario o clave incorrecto.', 'errorLogin') 
    return render_template('login.html')

@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))

@main.route('/resetPassword/', methods=['GET', 'POST'])
def resetPassword():

    if(request.method == 'POST'):
        return redirect(url_for('main.resetPasswordOK'))

    return render_template('password_reset.html')

@main.route('/resetPasswordOK/', methods=['GET', 'POST'])
def resetPasswordOK():

    if(request.method == 'POST'):
            return redirect(url_for('main.home'))

    return render_template('password_reset_OK.html')

@main.route('/listado_Mensajes/')
def listadoMensajes():
    return jsonify(mensajes)

@main.route('/testAjax/')
def testAjax():
    return render_template('testAjax.html')

@main.route('/index/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index2.html')

@main.route('/index/usuario/', methods=['GET', 'POST'])
@login_required
def usuario():
    return render_template('usuario.html')

@main.route('/index/crearUsuario/', methods=['GET', 'POST'])
@login_required
def crearUsuario():

    # Accion = request.form['Boton']
    # print(Accion)
    if (request.method == 'POST'): # and request.form['Boton'] == 'Create'):

        nombresUsuario = escape(request.form['nombresUsuario'])
        apellidosUsuario = escape(request.form['apellidosUsuario'])
        tipoDocumento = escape(request.form['tipoDocumento'])
        numeroDocumento = escape(request.form['numeroDocumento'])
        fechaNacimiento = escape(request.form['fechaNacimiento'])
        sexo = escape(request.form['sexo'])
        telefonoUsuario = escape(request.form['telefonoUsuario'])
        mailUsuario = escape(request.form['mailUsuario'])
        userName = escape(request.form['userName'])
        userPassword = escape(request.form['userPassword'])
        roll = escape(request.form['roll'])
        condiciones = escape(request.form['condiciones'])

        print(userName)
        print(userPassword)

        db = get_db()
        #agregar SALT
        #clave = SALT + clave + usuario
        userPassword = userPassword + userName 
        userPassword = generate_password_hash(userPassword)
        db.execute("INSERT into Persona ( numeroDocumento, tipoDocumento, nombres, apellidos, telefono, sexo, correo, username, password, estadoPersona, fechaNacimiento, roll) values( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(numeroDocumento, tipoDocumento, nombresUsuario, apellidosUsuario, telefonoUsuario, sexo, mailUsuario, userName, userPassword, 'True', fechaNacimiento, roll))
        db.commit()
        db.close()

        return redirect(url_for('main.usuario'))
        
    return render_template('usuario_crear.html')

@main.route('/index/buscarUsuario/', methods=['GET', 'POST'])
@login_required
def buscarUsuario():
    return render_template('usuario_buscar.html')

@main.route('/index/editarUsuario/', methods=['GET', 'POST'])
@login_required
def editarUsuario():
    return render_template('usuario_editar.html')

@main.route('/index/eliminarUsuario/', methods=['GET', 'POST'])
@login_required
def eliminarUsuario():
    return render_template('usuario_eliminar.html')

@main.route('/index/cursos/', methods=['GET', 'POST'])
@login_required
def cursos():
    return render_template('cursos.html')

@main.route('/index/cursos/crearCurso/', methods=['GET', 'POST'])
@login_required
def crearCurso():
    return render_template('cursos_crear.html')

@main.route('/index/cursos/buscarCurso/', methods=['GET', 'POST'])
@login_required
def buscarCurso():
    return render_template('cursos_buscar.html')

@main.route('/index/cursos/consultarCurso/', methods=['GET', 'POST'])
@login_required
def consultarCurso():
    return render_template('cursos_consultar.html')

@main.route('/index/cursos/editarCurso/', methods=['GET', 'POST'])
@login_required
def editarCurso():
    return render_template('cursos_editar.html')

@main.route('/index/cursos/eliminarCurso/', methods=['GET', 'POST'])
@login_required
def eliminarCurso():
    return render_template('cursos_eliminar.html')

@main.route('/index/cursos/calificarCurso/', methods=['GET', 'POST'])
@login_required
def calificarCurso():
    return render_template('cursos_calificar.html')

@main.route('/index/cursos/consultarCalificaciones/', methods=['GET', 'POST'])
@login_required
def consultarCalificaciones():
    return render_template('calificaciones_consultar.html')

@main.route('/index/materias/', methods=['GET', 'POST'])
@login_required
def materias():
    return render_template('materias.html')

@main.route('/index/crear_materias/', methods=['GET', 'POST'])
@login_required
def crear_materias():
    return render_template('materias_crear.html')

@main.route('/index/editar_materias/', methods=['GET', 'POST'])
@login_required
def editar_materias():
    return render_template('materias_editar.html')

@main.route('/index/eliminar_materias/', methods=['GET', 'POST'])
@login_required
def eliminar_materias():
    return render_template('materias_eliminar.html')

@main.route('/index/buscar_materias/', methods=['GET', 'POST'])
@login_required
def buscar_materias():
    return render_template('materias_buscar.html')

@main.route('/index/actividades/', methods=['GET', 'POST'])
@login_required
def actividades():
    return render_template('actividades.html')

@main.route('/index/comentarios/', methods=['GET', 'POST'])
@login_required
def comentarios():
    return render_template('comentarios.html')