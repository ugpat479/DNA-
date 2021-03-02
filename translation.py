#!/usr/bin/env python
import sys
#mRNA will have the shape/format: 'CCUUUUUUAAUGAGUCGUGGUUGAAUUCCU'
#codon table will have the shape/format: {'UUU':'Phe', 'UUC':'Phe', 'UUA':'Leu', 'AUG':'Met', 'UGA:STOP', .....}

def init_codon_table():
    bases = "UCAG"
    codons = [a + b + c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))
    return codon_table

def translate_mRNA(mRNA, codon_table):
    #find the position of the start codon
    start_index = mRNA.index('AUG')
    polypeptide = ''
    
    #need to find the position of the stop codon
    
    possible_stop_indices = []
    stop_index_UAA = mRNA.find('UAA')
    stop_index_UAG = mRNA.find('UAG')
    stop_index_UGA = mRNA.find('UGA')
    
    possible_stop_indices.append(stop_index_UAA)
    possible_stop_indices.append(stop_index_UAG)
    possible_stop_indices.append(stop_index_UGA)
    
    possible_stop_indices = [p for p in possible_stop_indices if p >= 0]
    #find the first stop codon that occurs in the mRNA
    stop_index = min(possible_stop_indices)
    
    #step through mRNA, looking at 3 characters at a time
    for i in range(start_index, stop_index, 3):
    
        #extract codon from mRNA string
        codon = mRNA[i:i+3]
        #find corresponding amino acid
        amino_acid = codon_table[codon]
        #add the amino acid to the polypeptide chain
        polypeptide = polypeptide+amino_acid
        
    return polypeptide
	
if __name__ == "__main__":
    mRNA = sys.argv[1]
    codon_table = init_codon_table()
    polypeptide = translate_mRNA(mRNA, codon_table)
    output_str = f'Polypeptide: {polypeptide}'
    print(output_str)
