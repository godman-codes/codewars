def DNA_strand(dna):
   dna = [x for x in dna]
   alt_dna = []
   for i in dna:
      if i == 'T':
         alt_dna.append('A')
      elif i == 'A':
         alt_dna.append('T')
      elif i == 'G':
         alt_dna.append('C')
      elif i == 'C':
         alt_dna.append('G')
   return ''.join(alt_dna)