from flask import Flask
from flask_restful import Api
from myapi.resources.sequences import Sequencer
from myapi.resources.species import Species
from flask import render_template

app = Flask(__name__)
api = Api(app)

api.add_resource(Sequencer, '/api/sequence/<string:species_name>')
api.add_resource(Species, '/api/species')


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)