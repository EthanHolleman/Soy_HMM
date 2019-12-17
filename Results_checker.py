import csv

SUMM = '/home/ethan/Desktop/HMM/IILTRGypsy.txt'
VIT = '/home/ethan/Desktop/HMM/Viterbi.txt'

def get_element_locations(summary_file, chr='01'):
    els = []
    with open(summary_file) as sf:
        reader = csv.reader(sf, delimiter='\t')
        reader.next()
        for row in reader:
            try:
                if row[8][2:] == chr:
                    descrip, start, end = row[7], row[10], row[11]
                    if descrip == 'SOLO':
                        descrip = 'S'
                    if descrip == 'INTACT':
                        descript = 'I'
                    els.append((descrip, int(start), int(end)))
            except IndexError as e:
                continue

    return els

def compare(viterbi_file, elements):
    elements = sorted(elements, key=lambda x: x[1], reverse=True)
    # sort by position reverse to use pop
    correct, incorrect, total = 0, 0, 0
    current_el = elements.pop()
    with open(viterbi_file) as vf:
        for i, line in enumerate(vf):
            if i+1 < current_el[1]:
                if line == 'G':
                    correct += 1
                else:
                    incorrect += 1
            elif i+1 >= current_el[1] and i+1 <= current_el[2]:
                if line == current_el[0]:
                    correct += 1
                else:
                    incorrect += 1
            else:
                if line == 'G':
                    corrent += 1
                else:
                    incorrect += 1
                if i+1 > current_el[2] and elements != []:
                    current_el = elements.pop()
            total+= 1
    return (correct, incorrect, total)

print(compare(VIT, get_element_locations(SUMM)))
