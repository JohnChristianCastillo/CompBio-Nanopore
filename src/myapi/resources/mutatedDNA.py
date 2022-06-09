from flask_restful import Resource
from src.db import MUTATED_SIGNALS


class MutatedDNA(Resource):
    def get(self):
        mutatedDNAList = []
        for name, signal in MUTATED_SIGNALS.items():
            mutatedDNAList.append(name)
        return {"MUTATED_DNA_SEQUENCES": mutatedDNAList}, 200

