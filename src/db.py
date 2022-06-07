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
# NUM_SENSOR_VALUES_PER_BASE = 47
NUM_SENSOR_VALUES_PER_BASE = 1


def generate_vector_from_sequence(sequence: str) -> List[int]:
    """
    FIXME: make customisable w.r.t. conversion dict
    :param sequence:
    :return:
    """
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
# TODO: better name
K: int = 50


def get_sensor_values_from_file(path: str) -> list[int]:
    import csv

    with open(path) as file:
        reader = csv.DictReader(file)
        values = [int(float(row["Colour_p4_01"])) for row in reader]
    # rtrim values
    # assumes it stops and continues reading 6 when the end of the LEGO sequence
    # has been reached
    for val in reversed(values):
        # if white
        if val == 6:
            del values[-1]
        else:
            break
    # run over list while reversed, once you encounter the first chunk of X 6's, slice from that index onwards
    counter = Counter(values[-K:])
    # not foolproof but should work for our usecases
    for index in reversed(range(0, len(values) - K)):
        if counter[6] == K:
            print(f"index broken @ {index}")
            return values[index + K + 1:]
        counter[values[index + K]] -= 1
        counter[values[index]] += 1
    raise ValueError("unable to left trim white blocks from sequence of signals")


if __name__ == "__main__":
    sensor_values = get_sensor_values_from_file("./standard.csv")
    print(len(sensor_values))
    print(sensor_values)

    # # for record in SeqIO.parse("data/animalBlast.fasta", "fasta"):
    # for record in SeqIO.parse("data/extraAnimalBlast.fasta", "fasta"):
    #     # name, binomen = record.id.split('|')
    #     name = record.id
    #     sequence = record.seq
    #     print(f"{name},{sequence},{''.join(generate_vector_from_sequence(sequence))}")
