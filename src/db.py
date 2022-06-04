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


if __name__ == '__main__':
    for record in SeqIO.parse("../data/animalBlast.fasta", "fasta"):
        name, binomen = record.id.split('|')
        sequence = record.seq
        print(f"{name},{binomen},{sequence},{''.join(generate_vector_from_sequence(sequence))}")
