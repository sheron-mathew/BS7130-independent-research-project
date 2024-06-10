import requests
import pandas as pd
import gzip
import shutil
import os

###downloading escape gene data###

#read the csv file
df = pd.read_csv("escape_data.csv")

#make a list of the gene names
gene_names = df['Gencode.v19'].tolist()

counter = 0
for gene in gene_names:
#parse through the list and get each fasta file from ensembl
#what were the settings that were used???????
    url = f"https://grch37.ensembl.org/Homo_sapiens/Export/Output/Gene?db=core;flank3_display=500;flank5_display=500;g={gene};output=fasta;r=X;192989-220023;strand=feature;param=cdna;param=coding;param=utr5;param=utr3;param=exon;param=intron;genomic=5_3_flanking;_format=TextGz"

    response = requests.get(url, headers={"Content-Type": "application/json"})

    #Check if the request was successful
    if response.status_code == 200:
        #Define the filename to save the downloaded content
        gz_filename = f"escape_genes/{gene}.fasta.gz"
    
    #Save the response content to a file
        with open(gz_filename, "wb") as file:
            file.write(response.content)

        #define the filename for the unzipped gene
        fasta_filename = f"escape_genes/{gene}.fasta"
        print(f"File downloaded successfully and saved as {fasta_filename}")
        with gzip.open(gz_filename, 'rb') as f_in:
            with open(fasta_filename, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(f"escape_genes/{gene}.fasta.gz")
        print(f"File downloaded successfully and saved as {gz_filename}")
        counter = counter + 1
    else:
        print(f"Failed to download the file. HTTP Status Code: {response.status_code}")

print(str(counter) " escape genes downloaded")

###downloading inactive gene data###

#read the csv file
df = pd.read_csv("inactive_data_cropped.csv")

#make a list of the gene names
gene_names = df['Gencode.v19'].tolist()

counter = 0
for gene in gene_names:
#parse through the list and get each fasta file from ensembl
#what were the settings that were used???????
    url = f"https://grch37.ensembl.org/Homo_sapiens/Export/Output/Gene?db=core;flank3_display=500;flank5_display=500;g={gene};output=fasta;r=X;192989-220023;strand=feature;param=cdna;param=coding;param=utr5;param=utr3;param=exon;param=intron;genomic=5_3_flanking;_format=TextGz"

    response = requests.get(url, headers={"Content-Type": "application/json"})

    #Check if the request was successful
    if response.status_code == 200:
        #Define the filename to save the downloaded content
        gz_filename = f"inactive_genes/{gene}.fasta.gz"
    
    #Save the response content to a file
        with open(gz_filename, "wb") as file:
            file.write(response.content)

        #define the filename for the unzipped gene
        fasta_filename = f"inactive_genes/{gene}.fasta"
        print(f"File downloaded successfully and saved as {fasta_filename}")
        with gzip.open(gz_filename, 'rb') as f_in:
            with open(fasta_filename, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(f"inactive_genes/{gene}.fasta.gz")
        print(f"File downloaded successfully and saved as {gz_filename}")
        counter = counter + 1
    else:
        print(f"Failed to download the file. HTTP Status Code: {response.status_code}")

print(str(counter) + " inactive genes downloaded")


###downloading escape gene data###

#read the csv file
df = pd.read_csv("variable_data.csv")

#make a list of the gene names
gene_names = df['Gencode.v19'].tolist()

counter = 0
for gene in gene_names:
#parse through the list and get each fasta file from ensembl
#what were the settings that were used???????
    url = f"https://grch37.ensembl.org/Homo_sapiens/Export/Output/Gene?db=core;flank3_display=500;flank5_display=500;g={gene};output=fasta;r=X;192989-220023;strand=feature;param=cdna;param=coding;param=utr5;param=utr3;param=exon;param=intron;genomic=5_3_flanking;_format=TextGz"

    response = requests.get(url, headers={"Content-Type": "application/json"})

    #Check if the request was successful
    if response.status_code == 200:
        #Define the filename to save the downloaded content
        gz_filename = f"variable_genes/{gene}.fasta.gz"
    
    #Save the response content to a file
        with open(gz_filename, "wb") as file:
            file.write(response.content)

        #define the filename for the unzipped gene
        fasta_filename = f"variable_genes/{gene}.fasta"
        print(f"File downloaded successfully and saved as {fasta_filename}")
        with gzip.open(gz_filename, 'rb') as f_in:
            with open(fasta_filename, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(f"variable_genes/{gene}.fasta.gz")
        print(f"File downloaded successfully and saved as {gz_filename}")
        counter = counter + 1
    else:
        print(f"Failed to download the file. HTTP Status Code: {response.status_code}")

print(str(counter) + " variable genes downloaded")
