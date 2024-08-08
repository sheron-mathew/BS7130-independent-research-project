import os
import pandas as pd
from Bio import SeqIO

escape_dir = '/home/sm1073/Documents/independent_project/escape_genes'
inactive_dir = '/home/sm1073/Documents/independent_project/inactive_genes'

data = []

def read_fasta_files(directory, label):
    for filename in os.listdir(directory):
        if filename.endswith('.fasta'):
            filepath = os.path.join(directory, filename)
            # Extract gene name from the filename
            gene_name = os.path.splitext(filename)[0]
            for record in SeqIO.parse(filepath, "fasta"):
                sequence = str(record.seq)
                data.append([gene_name, sequence, label])
                break  # Only take the first sequence

# Read escaping sequences
read_fasta_files(escape_dir, 1)

# Read non-escaping sequences
read_fasta_files(inactive_dir, 0)

# Create DataFrame
df = pd.DataFrame(data, columns=['GeneName','Sequence', 'Label'])

# Save to CSV
df.to_csv('x_inactivation_genes.csv', index=False)
