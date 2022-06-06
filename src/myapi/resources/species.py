from flask_restful import Resource
from db import *


class Species(Resource):
    def get(self):
        """
        """
        species = []
        for record in SeqIO.parse("data/animalBlast.fasta", "fasta"):
            species_name, scientific_name = record.id.split('|')
            species.append(species_name)
        return {"species": species}, 200

