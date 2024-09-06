from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "welcome to docker comisión A"


if __name__ == "__main__":
    app.run(
host="0.0.0.0",
port=5000,
debug=True,
)

# from flask import Flask, render_template, redirect, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/vehiculos_db' #coneccion a la base de datos 
# # (despues del @ es el ip) en el ultimo / de la linea 6 nombre base de datos
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# from models import Marca, Tipo, Vehiculo

# listado_nombres = ['Juan', 'Ana', 'Luis']
# listado_personas = [
#     dict(
#         name=dict(
#             first="Pablo",
#             last="Amedey"    
#         ),
#         location=dict(
#             city="Rio Cuarto"
#         ),
#         email="pablito1166@hotmail.com"
#     ),
#     dict(
#         name=dict(
#             first="Esteban",
#             last="Quito"    
#         ),
#         location=dict(
#             city="Antofagasta"
#         ),
#         email="quitoesteban@yahoo.com"
#     ),
# ]

# @app.route('/') # app es la instancia, route el metodo, '/' es el disparador
# def index():
#     return render_template(
#         'index.html',
#     )

# @app.route('/info') # app es la instancia, route el metodo, '/' es el disparador
# def informacion():
#     return render_template(
#         'informacion.html',
#     )

# @app.route('/bienvenido/<nombre>')
# def bienvenida(nombre):
#     return render_template(
#         'bienvenida.html',
#     )

# @app.route('/personas')
# def personas():
#      listado = listado_personas
#      return render_template(
#          'personas.html',
#          listado = listado
#     )

# @app.route('/personas_add', methods=['POST', 'GET'])
# def agregar_personas():
#     if request.method == 'POST':
#         first_name = request.form['nombre']
#         last_name = request.form['apellido']
#         email = request.form['email']
#         city = request.form['ciudad']
        
#         persona=dict(
#             name=dict(
#                 first=first_name,
#                 last=last_name    
#             ),
#             location=dict(
#                 city=city
#             ),
#             email=email
#         )
#         listado_personas.append(persona)
#     return render_template(
#         'add_personas.html',
#     )