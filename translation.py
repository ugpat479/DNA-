
#mRNA will have the shape/format: 'CCUUUUUUAAUGAGUCGUGGUUGAAUUCCU'
#codon table will have the shape/format: {'UUU':'Phe', 'UUC':'Phe', 'UUA':'Leu', 'AUG':'Met', 'UGA:STOP', .....}

def translate_mRNA(mRNA, codon_table):
    
    #we find the position of the start codon
    start_index = mRNA.index('AUG')
    polypeptide = ''
    
    #we need to find the position of the stop codon
    
    possible_stop_indices = []
    stop_index_UAA = mRNA.index('UAA')
    stop_index_UAG = mRNA.index('UAG')
    stop_index_UGA = mRNA.index('UGA')
    
    possible_stop_indices.append(stop_index_UAA)
    possible_stop_indices.append(stop_index_UAG)
    possible_stop_indices.append(stop_index_UGA)
    
    #find the first stop codon that occurs in the mRNA
    stop_index = min(possible_stop_indices)
    
    #then we need to step through mRNA, looking at 3 characters at a time
    for i in range(start_index, stop_index, 3):
    
        #extract codon from mRNA string
        codon = mRNA[i:i+3]
        #find corresponding amino acid
        amino_acid = codon_table[codon]
        #add the amino acid to the polypeptide chain
        polypeptide = polypeptide+amino_acid
        
    return polypeptide
	