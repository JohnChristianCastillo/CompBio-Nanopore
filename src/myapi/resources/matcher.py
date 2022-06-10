from flask_restful import Resource
from src.db import MUTATED_SIGNALS, rank_matches, db, Levenshtein

class SpeciesMatcher(Resource):
    def get(self, species: str):
        species.replace("%20", " ")
        matches = rank_matches(db, MUTATED_SIGNALS[species], scorer=Levenshtein.distance)
        return {"Description": "This is ordered from closest match to furthest match",
                "matches": [f"{match[0][0]} ({match[0][1]}): {match[1]}" for match in matches]}, 200


class SignalMatcher(Resource):
    def get(self, signal: str):
        signal.replace("%20", " ")
        matches = rank_matches(db, signal, scorer=Levenshtein.distance)
        return {"Description": "This is ordered from closest match to furthest match",
                "matches": [f"{match[0][0]} ({match[0][1]}): {match[1]}" for match in matches]}, 200
