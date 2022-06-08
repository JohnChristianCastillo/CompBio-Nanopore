from collections import Counter
from typing import List

from Bio import SeqIO

# # used for translating a LEGO DNA sequence to the standard DNA sequence repr
# # e.g. sequence.translate(COLOUR_TO_BASE)
# COLOUR_TO_BASE = {
#     ord("B"): "T",
#     ord("G"): "A",
#     ord("Y"): "C",
#     ord("R"): "G",
# }
BASE_TO_SIGNAL = {
    "T": "2",
    "A": "3",
    "C": "4",
    "G": "5",
}

# TODO: calibrate this value by testing against the DNA sequences and CSV files we already have
NUM_SENSOR_VALUES_PER_BASE = 47


def generate_vector_from_sequence(sequence: str) -> List[int]:
    sensor_values = []
    for base in sequence:
        if base not in BASE_TO_SIGNAL:
            continue
        sensor_values.extend([BASE_TO_SIGNAL[base]] * NUM_SENSOR_VALUES_PER_BASE)
    return sensor_values


def apply_mutations():
    """
    apply to vector (of signals) or DNA sequence?
    :return:
    """
    return None


# num of 10s in a row, we want to see to ltrim
K: int = NUM_SENSOR_VALUES_PER_BASE


def get_sensor_values_from_file(path: str) -> list[int]:
    import csv

    with open(path) as file:
        reader = csv.DictReader(file)
        values = [int(float(row["Colour_p4_01"])) for row in reader]

    # split in halves, trim both sides
    def ltrim(values):
        counter = Counter(values[-K:])
        # not foolproof but should work for our usecases
        for index in reversed(range(0, len(values) - K)):
            if counter[6] == K:
                return values[index + K + 1:]
            counter[values[index + K]] -= 1
            counter[values[index]] += 1
        raise ValueError("unable to left trim white blocks from sequence of signals")

    midpoint = len(values) // 2  # FIXME: niet altijd een goede schatting van de midpoint
    left_half, right_half = values[:midpoint], [*reversed(values[midpoint:])]
    trimmed_left_half, trimmed_right_half = ltrim(left_half), ltrim(right_half)
    return trimmed_left_half + [*reversed(trimmed_right_half)]


def print_db():
    for record in SeqIO.parse("data/extraAnimalBlastMetNamen.fasta", "fasta"):
        name, binomen = record.description.split("|")
        sequence = record.seq
        print(
            f"{name},{binomen},{sequence},{''.join(generate_vector_from_sequence(sequence))}"
        )


if __name__ == "__main__":
    print_db()

    for sequence_index in range(1, 8):
        for reading_index in range(1, 4):
            sensor_values = get_sensor_values_from_file(f"data/{sequence_index}_{reading_index}.csv")
            print(f"{sequence_index}_{reading_index} --> {len(sensor_values)}")
            # print(sensor_values)
