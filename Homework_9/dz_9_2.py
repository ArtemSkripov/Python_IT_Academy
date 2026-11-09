#d
words = [
"Python"
,
"java"
,
"C++"
,
"Rust"
,
"Go"
,
"Swift"
,
"PHP"
]

a = list(filter(lambda n:len(n)>=5, words))
lower_a = list(map(lambda n: n.lower(),a))
print(lower_a)