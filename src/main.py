from typing import List
import csv

import editdistance

DNA_SEQUENCES = [
    "YGYBBGGRGGBRGRGGYBGGGBGGRRB",
    "RBYBYBGBYBRRBBGRRGBBBYYRB",
    "RRGRBGYGGRBYBGBBYRBRRB",
    "BGRYGRBGRRGBRYRBBYYG",
    "BRGYYGGBBGBGBYYYBGRGYYY",
    "YYBRBBRBYRGGYYGYGRBGG",
    "RBRBRBYBBGYGGGBBYRRGRR",
]

BASE_TO_SENSOR_VALUE = {
    "B": "2",
    "G": "3",
    "Y": "4",
    "R": "5",
}

NUM_SENSOR_VALUES_PER_BASE = 47
NUM_STRINGS_PER_SEQUENCE = 5


def generate_fake_reading_from_dna(dna: str) -> List:
    sensor_values: List[int] = []
    for base in dna:
        if base not in BASE_TO_SENSOR_VALUE:
            continue
        sensor_values.extend([BASE_TO_SENSOR_VALUE[base]] * NUM_SENSOR_VALUES_PER_BASE)
    return sensor_values


def apply_mutations():
    """
    apply to vector (of signals) or DNA sequence?
    :return:
    """
    return None


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
            inverse_score = editdistance.distance(
                reading, generated_sensor_readings
            )  # FIXME: use a passed in scoring function param
            results.append((sequence_index, inverse_score))
    results.sort(key=lambda result: result[1])
    return [result[0] for result in results]
    # return results


if __name__ == "__main__":
    for i in range(len(DNA_SEQUENCES)):
        print(f"sequence {i + 1} matches (closest to furthest): {test_sequence(i)}")
