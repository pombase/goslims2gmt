# Run for all slims
python make_gmt_file.py data/bp_goslim_pombe_ids_and_names.tsv results/bp_goslim.gmt
python make_gmt_file.py data/cc_goslim_pombe_ids_and_names.tsv results/cc_goslim.gmt
python make_gmt_file.py data/mf_goslim_pombe_ids_and_names.tsv results/mf_goslim.gmt

# Add a timestamp
date > results/timestamp.txt