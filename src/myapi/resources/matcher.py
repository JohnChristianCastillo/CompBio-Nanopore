from flask_restful import Resource
from db import MUTATED_SIGNALS, rank_matches, db, Levenshtein


class Matcher(Resource):
    def get(self, dna_sequence: str):
        dna_sequence.replace("%20", " ")
        matches = rank_matches(db, MUTATED_SIGNALS[dna_sequence], scorer=Levenshtein.distance)
        return {"matches": [f"{match[0][0]} ({match[0][1]}): {match[1]}" for match in matches]}, 200

