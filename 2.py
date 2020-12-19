import pyarrow.csv as pv
import pyarrow.parquet as pq

file='filename.csv'
table = pv.read_csv(file)
pq.write_table(table, file.replace('csv', 'parquet'))
print('Converted to Parquet')