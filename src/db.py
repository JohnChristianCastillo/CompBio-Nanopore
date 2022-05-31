from typing import List

from Bio import SeqIO

BASE_TO_SENSOR_VALUE = {
    "B": "2",
    "G": "3",
    "Y": "4",
    "R": "5",
    # TODO: hoe weten we welke base tot een bepaalde base behoort?
    # alle combinaties testen??
    # "B": "2",
    # "G": "3",
    # "Y": "4",
    # "R": "5",
}

NUM_SENSOR_VALUES_PER_BASE = 47
NUM_STRINGS_PER_SEQUENCE = 5


def generate_vector_from_sequence(sequence: str) -> List[int]:
    sensor_values = []
    for base in sequence:
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


if __name__ == '__main__':
    for record in SeqIO.parse("data/animalBlast.fasta", "fasta"):
        name, binomen = record.id.split('|')
        sequence = record.seq
        print(f"{name} ({binomen}): {sequence}")
        print(generate_vector_from_sequence(sequence))
