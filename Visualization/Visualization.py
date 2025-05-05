import matplotlib.pyplot as plt
import pandas as pd
#LOADING THE TSV FILE WHICH CONTAINS FREQUENCY OF UNIQUE MUTATIONS(SUBSTITUION) ACROSS ALL THE SAMPLES.

mutation_freq = pd.read_csv("/home/himanshu/mutation_frequency_table_S.tsv", sep='\t')
mutation_freq = mutation_freq.head(50)

#PLOTTING THE BARPLOT FOR THE FIRST 50 Mutations

plt.figure(figsize = (14, 6))
plt.bar(mutation_freq['Mutation'], mutation_freq['Frequency'], color = 'skyblue')
plt.xticks(rotation = 90, fontsize = 8)
plt.xlabel('Mutation')
plt.ylabel('Frequency')
plt.title('Mutation Frequence Table')
plt.tight_layout()
pdf_path = "spike_mutation_frequency_barplot.pdf"
plt.savefig(pdf_path, format='pdf')

pdf_path
