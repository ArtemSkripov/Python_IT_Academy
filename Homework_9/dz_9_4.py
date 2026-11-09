cities = [
"Москва"
,
"Париж"
,
"Берлин"
,
"Рим"
,
"Токио"
]

sort_cities = sorted(cities, key=lambda x: x[::-1])
print(sort_cities)