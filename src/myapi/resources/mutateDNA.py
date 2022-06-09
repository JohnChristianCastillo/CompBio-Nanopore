from flask_restful import Resource
from db import apply_errors


class Mutator(Resource):
    def get(self, original_signal):
        """req = requests.get(f"{request.host_url}/api/sequence/{chosen_species}")
        response = req.json()
        for key, val in response.items():
            print(key, val)
        """
        mutated_sequence = "".join(
            apply_errors(
                    list(original_signal), duplicate=0.22, replace=0.10, delete=0.05
                )
            )
        return {"mutated_DNA": mutated_sequence}, 200

