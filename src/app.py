from flask import Flask
from flask_restful import Api
from myapi.resources.sequences import Sequencer
from myapi.resources.species import Species
from myapi.resources.dna import DNA
from myapi.resources.matcher import Matcher
from myapi.resources.mutatedDNA import MutatedDNA
from myapi.resources.mutateDNA import Mutator

from flask import render_template

app = Flask(__name__)
api = Api(app)

api.add_resource(Sequencer, '/api/sequence/<string:species_name>')
api.add_resource(DNA, '/api/dna')
api.add_resource(Species, '/api/species')
api.add_resource(Matcher, '/api/matcher/<string:dna_sequence>')
api.add_resource(MutatedDNA, '/api/mutatedDNA')
api.add_resource(Mutator, '/api/mutator/<string:original_signal>')


#todo: project is handig
@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)

