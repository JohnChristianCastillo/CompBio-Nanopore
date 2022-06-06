import csv
from typing import List

import editdistance

from db import generate_vector_from_sequence

DNA_SEQUENCES = [
    # "YGYBBGGRGGBRGRGGYBGGGBGGRRB",
    # "RBYBYBGBYBRRBBGRRGBBBYYRB",
    # "RRGRBGYGGRBYBGBBYRBRRB",
    # "BGRYGRBGRRGBRYRBBYYG",
    # "BRGYYGGBBGBGBYYYBGRGYYY",
    # "YYBRBBRBYRGGYYGYGRBGG",
    # "RBRBRBYBBGYGGGBBYRRGRR",

    "CACTTAAGAATGAGAACTAAATAAGGT",
    "GTCTCTATCTGGTTAGGATTTCCGT",
    "GGAGTACAAGTCTATTCGTGGT",
    "TAGCAGTAGGATGCGTTCCA",
    "TGACCAATTATATCCCTAGACCC",
    "CCTGTTGTCGAACCACAGTAA",
    "GTGTGTCTTACAAATTCGGAGG",
]


def get_sensor_values_from_file(path: str) -> List[str]:
    with open(path) as file:
        reader = csv.DictReader(file)
        return [row["Colour"] for row in reader]


def test_sequence(sequence):
    # sequence we'll generate a fake signal from compare against our other signals
    dna_sequence = sequence
    generated_sensor_readings = "".join(generate_vector_from_sequence(dna_sequence))
    # print(generated_sensor_readings)

    results = []
    for sequence_index in range(1, len(DNA_SEQUENCES) + 1):
        for reading_index in range(1, 4):
            reading = "".join(
                get_sensor_values_from_file(
                    f"data/{sequence_index}_{reading_index}.csv"
                )
            )
            # print(reading)
            inverse_score = editdistance.distance(
                reading, generated_sensor_readings
            )  # FIXME: use a passed in scoring function param
            results.append((sequence_index, inverse_score))
    results.sort(key=lambda result: result[1])
    # return results
    return [result[0] for result in results]


if __name__ == "__main__":
    for sequence in DNA_SEQUENCES:
        print(f"sequence {sequence} matches (closest to furthest): {test_sequence(sequence)}")
