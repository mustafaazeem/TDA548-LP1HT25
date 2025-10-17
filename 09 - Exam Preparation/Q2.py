def gene_match(gene, genome_file):
    with open(genome_file) as infile:
        genome = infile.read()
        for i in range(len(genome) - (len(gene) + 1)):
            print(i)
            if genome[i:i+len(gene)] == gene:
                print(f"gene found at {i}")  

def gene_match2(gene, genome_file):
    with open(genome_file) as infile:
        yield from infile
        
        # for line in infile: 
        #     yield line

def main():
    gene = 'ACA'
    genome_file = 'genome.txt'
    # gene_match(gene, genome_file)
    file_gen = gene_match2(gene, genome_file)
    print(next(file_gen))

    # print(gene_match2(gene, genome_file))

main()