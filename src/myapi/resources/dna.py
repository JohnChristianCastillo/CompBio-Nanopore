from flask_restful import Resource
from main import DNA_SEQUENCES


class DNA(Resource):
    def get(self):
        dnaList = []
        for dna in DNA_SEQUENCES:
            dnaList.append(dna)
        return {"DNA_SEQUENCES": dnaList}, 200

