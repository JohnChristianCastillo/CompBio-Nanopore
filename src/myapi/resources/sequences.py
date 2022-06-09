from flask_restful import Resource, reqparse
from src.db import *


class Sequencer(Resource):
    def get(self, species_name):
        for record in SeqIO.parse("data/animalBlast.fasta", "fasta"):
            name, scientific_name = record.id.split('|')
            scientific_name = scientific_name.capitalize()
            scientific_name = scientific_name.replace('_', ' ')
            if name == species_name:
                sequence = str(record.seq)
                return {
                    "species": name,
                    "scientific_name": scientific_name,
                    "sequence": sequence,
                    "signal": ''.join(str(e) for e in (generate_vector_from_sequence(sequence)))
                }, 200
        return {}, 400

