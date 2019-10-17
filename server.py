from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.TipoSensores import TipoSensor

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'api':  {
                                'nombre': 'Tipo de Sensores EverGreen',
                                'version':'v1',
                                'colecciones': ['tipoSensores','cultivos']
                            }
                    })

@app.route('/tipoSensores',methods=['GET'])
def getAll():
    return (TipoSensor.list())

@app.route('/tipoSensores',methods=['POST'])
def postOne():
    body = request.json
    return (TipoSensor.create(body))

app.run(port=5000,debug=True)