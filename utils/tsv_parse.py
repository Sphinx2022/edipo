import csv

def _get_variables_from_header(tsv_stream):
    header = next(tsv_stream)
    input_vars = header[:-1]
    output_vars = header[-1]
    return (input_vars, output_vars)

def parse_tsv(tsv_path: str):
    with open(tsv_path) as tsv_file:
        csv_stream = csv.reader(tsv_file, delimiter='\t')
        (input_vars, output_vars) = _get_variables_from_header(csv_stream)
        data = list(csv_stream)
        return (input_vars, output_vars, data)