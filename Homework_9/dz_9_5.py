#d
files = [
"main.py"
,
"test.py"
,
"README.md"
,
"data.csv"
,
"notes.txt"
]

files_filtered = list(filter(lambda x: '.py' in x, files))
print(files_filtered)