from flask_restful import Resource
from main import DNA_SEQUENCES, test_sequence


class Matcher(Resource):
    def get(self, dna_sequence):
        if dna_sequence in DNA_SEQUENCES:
            return {"matches": test_sequence(dna_sequence)}, 200
        return {}, 400

