"""
Return a gmt file from a go_slim table file from pombase (tsv, no headers, first column is go term id, second 
column is term name).

The args are input and output file, e.g.:

python make_gmt_file.py data/bp_goslim_pombe_ids_and_names.tsv results/bp_goslim.gmt
"""

import requests
import sys
import pandas

def main(input_file, output_file):
    # Load the table downloaded from pombase
    go_slims_data = pandas.read_csv(input_file, sep='\t', names=['go_slim_id', 'go_slim_description'])

    # For each of the go_slims, do a request to pombase API to get all the associated ids
    with open(output_file,'w') as out:
        # Iterate over the lines in the data
        for i, row in go_slims_data.iterrows():
            # Request to pombase API
            response_data = requests.get(f'https://www.pombase.org/api/v1/dataset/latest/data/term/{row["go_slim_id"]}').json()

            # This is missing from obsoleted terms (e.g. obsolete metal ion homeostasis (obsolete GO:0055065))
            if 'annotated_genes' in response_data:
                print(row["go_slim_id"], len(response_data['annotated_genes']))
                # Format response
                line2write = [row["go_slim_id"], row["go_slim_description"], '\t'.join(response_data['annotated_genes'])]
                out.write('\t'.join(line2write) + '\n')

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
