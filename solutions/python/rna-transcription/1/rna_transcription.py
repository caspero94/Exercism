def to_rna(dna):
    return dna.replace("G","c").replace("C","g").replace("T","a").replace("A","u").upper()
        
