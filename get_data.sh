# Prepare directory structure
mkdir -p data
mkdir -p results

# Download GO-slims from pombase
curl -o data/mf_goslim_pombe_ids_and_names.tsv https://www.pombase.org/data/releases/latest/misc/mf_goslim_pombe_ids_and_names.tsv
curl -o data/cc_goslim_pombe_ids_and_names.tsv https://www.pombase.org/data/releases/latest/misc/cc_goslim_pombe_ids_and_names.tsv
curl -o data/bp_goslim_pombe_ids_and_names.tsv https://www.pombase.org/data/releases/latest/misc/bp_goslim_pombe_ids_and_names.tsv

# Add a timestamp
date > data/timestamp.txt