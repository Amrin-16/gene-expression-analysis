import csv

genes = []

with open("gene_expression.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        genes.append((row["Gene"], float(row["Expression"])))

genes.sort(key=lambda x: x[1], reverse=True)

print("Top 10 Expressed Genes")
print("----------------------")

for gene, expression in genes[:10]:
    print(gene, ":", expression)
