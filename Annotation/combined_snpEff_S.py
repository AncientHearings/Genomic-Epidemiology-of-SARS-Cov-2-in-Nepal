import pandas as pd

# Step 1: Load the combined snpEff annotation file
df = pd.read_csv("/home/himanshu/combined_snpEff.tsv", sep="\t")

# Step 2: Filter rows where the gene is 'S' (Spike)
# Check if 'Gene_Name' or similar column exists, adjust if column is named differently
if 'GENE' in df.columns:
    spike_df = df[df['GENE'] == 'S']
elif 'GENE' in df.columns:
    spike_df = df[df['GENE'] == 'S']
else:
    raise ValueError("❌ Column for gene name not found. Check column headers in 'combined_snpEff.tsv'.")

# Step 3: Save the filtered data to a new TSV file
spike_df.to_csv("combined_snpEff_S.tsv", sep="\t", index=False)
print("✅ Spike gene data saved to combined_snpEff_S.tsv")

