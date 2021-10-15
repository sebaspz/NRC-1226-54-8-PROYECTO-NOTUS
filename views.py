from flask import Flask, render_template, blueprints, request, jsonify, redirect, url_for
from mensaje import mensajes


#creo el objeto que representa la aplicacion 
main = blueprints.Blueprint('main', __name__) #esto es un constructor - , url_prefix='/home'

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

    if(request.method == 'POST'): 

        usuario= request.form['username']
        clave = request.form['userPassword']
        Accion = request.form['Boton']

        if(Accion == 'login'):      # Boton iniciar sesion pulsado -> me direcciona al index de la app
            
            # return redirect(url_for('main.index'))
            if(usuario =='notus' and clave =='notus'):
                # return redirect(url_for('main.listadoMensajes')) # Aquise programa lo que debe hacer cuando el login sea exitoso
                return redirect(url_for('main.index'))
        
        '''if(Accion == 'Cancelar'):
            return redirect(url_for('main.home'))

        if(Accion == 'resetPassword'):
            return redirect(url_for('main.resetPassword'))'''

    return render_template('login.html')

@main.route('/signUp/', methods=['GET', 'POST'])
def signUp():

    if(request.method == 'POST'):

        Accion = request.form['Boton']

        if(Accion == 'newRegister'):      # Boton Enviar pulsado -> redirecciona al formulario de home

            print(request.form['nombre']) 
            print(request.form['sexo'])
            print(request.form['condiciones'])
            print(request.form['username'])
            print(request.form['userPassword'])
            print(request.form['correo'])

            return redirect(url_for('main.registerOK')) # Debe redireccional a una pagina de confirmacion y enviar un correo electornico de confirmacion

        if(Accion == 'Cancelar'):
            return redirect(url_for('main.home'))

    return render_template('signUp.html')

@main.route('/registerOK/', methods=['GET', 'POST'])
def registerOK():

    if(request.method == 'POST'):
        
        Accion = request.form['Boton']

        if(Accion == 'Aceptar'):
            return redirect(url_for('main.home'))

    return render_template('registerOK.html')

@main.route('/resetPassword/', methods=['GET', 'POST'])
def resetPassword():

    if(request.method == 'POST'):
        return redirect(url_for('main.resetPasswordOK'))

    return render_template('resetPassword.html')

@main.route('/resetPasswordOK/', methods=['GET', 'POST'])
def resetPasswordOK():

    if(request.method == 'POST'):
            return redirect(url_for('main.home'))

    return render_template('resetPasswordOK.html')

@main.route('/listado_Mensajes/')
def listadoMensajes():
    return jsonify(mensajes)

@main.route('/testAjax/')
def testAjax():
    return render_template('testAjax.html')

@main.route('/index/', methods=['GET', 'POST'])
def index():
    return render_template('index2.html')

@main.route('/index/usuario/', methods=['GET', 'POST'])
def usuario():
        
    return render_template('usuario.html')

@main.route('/index/crearUsuario/', methods=['GET', 'POST'])
def crearUsuario():
    if(request.method == 'POST'):
        
        Accion = request.form['Boton']

        if(Accion == 'Create'):
            return redirect(url_for('main.usuario'))

    return render_template('usuario_Crear.html')

@main.route('/index/buscarUsuario/', methods=['GET', 'POST'])
def buscarUsuario():
    return render_template('usuario_Buscar.html')

@main.route('/index/editarUsuario/', methods=['GET', 'POST'])
def editarUsuario():
    return render_template('usuario_Editar.html')

@main.route('/index/eliminarUsuario/', methods=['GET', 'POST'])
def eliminarUsuario():
    return render_template('usuario_Eliminar.html')

@main.route('/index/cursos/', methods=['GET', 'POST'])
def cursos():
    return render_template('cursos.html')

@main.route('/index/materias/', methods=['GET', 'POST'])
def materias():
    return render_template('materias.html')

@main.route('/index/crear_materias/', methods=['GET', 'POST'])
def crear_materias():
    return render_template('crear_materias.html')

@main.route('/index/editar_materias/', methods=['GET', 'POST'])
def editar_materias():
    return render_template('editar_materias.html')

@main.route('/index/eliminar_materias/', methods=['GET', 'POST'])
def eliminar_materias():
    return render_template('eliminar_materias.html')

@main.route('/index/buscar_materias/', methods=['GET', 'POST'])
def buscar_materias():
    return render_template('buscar_materias.html')

@main.route('/index/actividades/', methods=['GET', 'POST'])
def actividades():
    return render_template('actividades.html')

@main.route('/index/comentarios/', methods=['GET', 'POST'])
def comentarios():
    return render_template('comentarios.html')