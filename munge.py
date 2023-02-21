import csv    

f = open('data/laligaStats.csv', 'r')
g = open('data/clean_data.csv', 'w')

reader = csv.reader(f)
writer = csv.writer(g)

header = next(reader)[:-1] # Skip the last column

new_header = [] 
for col in header: # This was used to remove spaces from header names
    new_header.append(col.replace(' ', ''))

writer.writerow(new_header)

values = list(reader)

fourth_col = []
for row in values:
    if (row[4] == ''):
        continue
    fourth_col.append(float(row[4]))
avg = sum(fourth_col) / len(fourth_col) # This was used to replace the missing value of passes for Celta De Vigo

for row in values:
    new_row = [row[0]]
    for data in row[1:-1]:
        if (data == ''):
            data = avg
        new_data = round(float(data), 2) # Round every data value to 2 decimal places
        new_row.append(new_data)
    writer.writerow(new_row)

f.close()
g.close()