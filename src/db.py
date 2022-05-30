"""
'Database'
"""
import enum
from typing import List

DNA_SEQUENCES = [
    "YGYBBGGRGGBRGRGGYBGGGBGGRRB",
    "RBYBYBGBYBRRBBGRRGBBBYYRB",
    "RRGRBGYGGRBYBGBBYRBRRB",
    "BGRYGRBGRRGBRYRBBYYG",
    "BRGYYGGBBGBGBYYYBGRGYYY",
    "YYBRBBRBYRGGYYGYGRBGG",
    "RBRBRBYBBGYGGGBBYRRGRR",
    # "BRYBBYRGRR",
]

BASE_TO_SENSOR_VALUE = {
    "B": "2",
    "G": "3",
    "Y": "4",
    "R": "5",
}


class Error(enum.Enum):
    DUPLICATE = 0.05
    REPLACE = 0.05
    DELETE = 0.05


ERROR_LIKELIHOOD = {
    Error.DELETE: 0.05,
    Error.DUPLICATE: 0.05,
    Error.REPLACE: 0.05,
}

NUM_SENSOR_VALUES_PER_BASE = 47
# NUM_SENSOR_VALUES_PER_BASE = 3
NUM_STRINGS_PER_SEQUENCE = 5

import random


def generate_fake_reading_from_dna(dna: str) -> List:
    sensor_values: List[int] = []
    for base in dna:
        if base not in BASE_TO_SENSOR_VALUE:
            continue
        sensor_values.extend([BASE_TO_SENSOR_VALUE[base]] * NUM_SENSOR_VALUES_PER_BASE)
    return sensor_values
    duplicate_at = []
    for index, value in enumerate(sensor_values):
        roll = random.random()
        if 0.0 <= roll <= Error.DELETE.value:
            sensor_values[index] = "-"
        elif Error.DELETE.value < roll <= Error.DELETE.value + Error.DUPLICATE.value:
            duplicate_at.append(index)
        elif (
            Error.DELETE.value + Error.DUPLICATE.value
            < roll
            <= Error.DELETE.value + Error.DUPLICATE.value + Error.REPLACE.value
        ):
            sensor_values[index] = random.choice(list(BASE_TO_SENSOR_VALUE.values()))
    offset = 0
    for index in duplicate_at:
        sensor_values.insert(index, sensor_values[index + offset])
    return [*filter(lambda x: x != "-", sensor_values)]


import csv

import editdistance


def get_sensor_values_from_file(path: str) -> List[str]:
    with open(path) as file:
        reader = csv.DictReader(file)
        return [row["Colour"] for row in reader]


def test_sequence(index):
    # sequence we'll generate a fake signal from compare against our other signals
    dna_sequence = DNA_SEQUENCES[index]
    generated_sensor_readings = "".join(generate_fake_reading_from_dna(dna_sequence))
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
            inverse_score = editdistance.distance(reading, generated_sensor_readings) # FIXME: use a passed in scoring function param
            results.append((sequence_index, inverse_score))
    results.sort(key=lambda result: result[1])
    return [result[0] for result in results]
    # return results


if __name__ == "__main__":
    for i in range(len(DNA_SEQUENCES)):
        print(f"sequence {i + 1} has results: {test_sequence(i)}")
