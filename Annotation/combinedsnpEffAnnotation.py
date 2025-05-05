import pandas as pd
import os

# Step 1: Load the metadata file
metadata_path = os.path.expanduser("~/covseq/sarscov2_genome_nepal/metadata/metadata_curated/master_design_table.tsv")
metadata = pd.read_csv(metadata_path, sep="\t")

# Step 2: Get the list of SampleIDs
sample_ids = metadata['Accession_ID'].tolist()

# Step 3: Base path for snpEff files
base_path = os.path.expanduser("~/covseq/sarscov2_genome_nepal/processed/covseq")

# Step 4–7: Loop through samples and load snpEff files
combined_data = []

for sample_id in sample_ids:
    file_path = os.path.join(base_path, sample_id, f"{sample_id}.snpEff.tsv")
    
    if os.path.isfile(file_path):
        try:
            df = pd.read_csv(file_path, sep="\t")
            df["Accession_ID"] = sample_id
            combined_data.append(df)
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
    else:
        print(f"⚠️ File not found: {file_path}")

# Step 8–9: Combine and export
if combined_data:
    final_df = pd.concat(combined_data, ignore_index=True)
    final_df.to_csv("combined_snpEff.tsv", sep="\t", index=False)
    print("✅ combined_snpEff.tsv created successfully.")
else:
    print("🚫 No files loaded. Check file paths and metadata.")


