from utils.tsv_parse import parse_tsv

x, y, z = parse_tsv('./datasets/period.tsv')
print(z)