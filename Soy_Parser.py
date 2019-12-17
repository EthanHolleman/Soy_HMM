import os
from itertools import chain
import csv

# constants
TE_DIR = '/media/ethan/EH_DATA/Gypsy_Seperated'
ASSEMBLY = '/media/ethan/EH_DATA/GMax2.1_assembly/completeGM.fna'
TRANS = '/home/ethan/Desktop/HMM/Transitions.csv'
EMMS = '/home/ethan/Desktop/HMM/Emissions.csv'


def fasta_content(assembly):
    bases = [0]*5 # by index a, t, g, c, n
    with open(assembly) as asmb:
        for line in asmb:
            if line[0] == '>':
                continue  # line is a header, no seq
            else:
                counts = count_bases(line)
                bases = [total + line for total, line in zip(bases, counts)]
    return bases


def TE_content(TE_dir, type='INTACT'):
    dir = os.listdir(TE_dir)
    dir = [os.path.join(TE_dir, TE_file) for TE_file in dir]
    total_base_content = [0]*5
    for TE_file in dir:
        if type in TE_file:
            bases = fasta_content(TE_file)
            total_base_content = [tb + b for tb, b in zip(total_base_content, bases)]

    return total_base_content


def base_content(base_counts):
    s = sum(base_counts)
    return [count / s for count in base_counts]


def count_bases(seq):
    bases = [0]*5
    temp = seq.strip()
    bases[0] += temp.count('A')
    bases[1] += temp.count('T')
    bases[2] += temp.count('G')
    bases[3] += temp.count('C')
    bases[4] += temp.count('N')

    return bases


def adjust_count(count_a, count_b):
    return [a-b for a, b in zip(count_a, count_b)]


def calculate_transitions(asbl_count, solo_count, intact_count):

    pro_assembly = sum(adjust_count(adjust_count(asbl_count, solo_count), intact_count)) / sum(asbl_count)
    pro_solo_in_assbl = sum(solo_count) / sum(asbl_count)
    pro_intact_in_assbl = sum(intact_count) / sum(asbl_count)
    # adjust count by removing bases in solo and intact counts from assembly
    # counts. Taking sum of all bases with adjusted assembly value and dividing
    # it by the total bases in the assembly
    return [[pro_assembly, pro_solo_in_assbl, pro_intact_in_assbl],
             [0.90, 0.10, 0], [0.85, 0, 0.15]]
    #           Assembly,           Solo,       Intact
    # Assebmly  prob_assembly       prob_solo   prob_intact
    # Solo      1 - prob_solo              0
    # Intact                       0

def calculate_emissions(asbl_count, solo_count, intact_count):
    return [base_content(counts) for counts in [asbl_count, solo_count, intact_count]]


def write_files(trans_matrix, emm_matrix):
    filenames = [TRANS, EMMS]
    with open(filenames[0], 'w') as f:
        writer = csv.writer(f)
        writer.writerows(trans_matrix)
    with open(filenames[1], 'w') as g:
        writer = csv.writer(g)
        writer.writerows(emm_matrix)


def __main__():
    assembly_content = fasta_content(ASSEMBLY)
    TE_intact_content = TE_content(TE_DIR)
    TE_solo_content = TE_content(TE_DIR, type='SOLO')
    transitions = calculate_transitions(assembly_content, TE_solo_content, TE_intact_content)
    emm = calculate_emissions(assembly_content, TE_solo_content, TE_intact_content)
    write_files(transitions, emm)


if __name__ == '__main__':
    __main__()
