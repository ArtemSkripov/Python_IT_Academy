#d
text = 'Functional programming'
clear_text = text.replace(' ','')
dict_text = {}

for key in clear_text:
    if key not in dict_text:
        dict_text[key] = 1
    else:
        dict_text[key] += 1
print(dict_text)