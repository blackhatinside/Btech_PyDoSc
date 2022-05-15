import pandas as pd
# from urllib.request import Request, urlopen

# link = 'https://www.studentsdatabases.com/wp-content/uploads/2021/11/JEE-Applicants-Samples-2021.xlsx'
link = input("Enter the .xlsx url to scrap: ").strip()

# worksheet = urllib.urlopen(link)
# with urllib.request.urlopen(link) as worksheet:
# 	xd = pd.ExcelFile(worksheet)
# 	print(xd.sheet_names)
# 	df = xd.parse(xd.sheet_names[-1], header=None)
# 	print(df)

# OR

# df = pd.read_excel(link,'sheetname')

# OR

# req = Request(link)
# req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
# content = urlopen(req)

# df = pd.read_csv(content, sep='|', encoding='latin-1', on_bad_lines='skip', lineterminator='\n')

# OR

# https://simplernerd.com/python-pandas-read-excel-from-url/
import requests
r = requests.get(link)
open('temp.xls', 'wb').write(r.content)
df = pd.read_excel('temp.xls')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)		# throws FUTUREWARNING

res = df[df.apply(lambda row: row.astype(str).str.contains('samyuktha', case=False).any(), axis=1)]
res.style.set_table_styles([{'selector' : '',
                            'props' : [('border',
                                        '10px solid yellow')]}])

# OR

# res = df[df.isin(['SAMYUKTHA']).any()]

arr = res.values.tolist()

print()
print(res)
print()
print(*arr, sep = "\n")