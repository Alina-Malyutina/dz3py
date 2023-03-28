word = (input('Enter your word on EN or RU: ').upper())
score_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
score_2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
score_3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
score_4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
score_5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
score_8 = ['J', 'X', 'Ш', 'Э', 'Ю']
score_10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
count = 0
for i in word:
    for k in score_1:
        if k == i:
            count += 1
    for j in score_2:
        if j == i:
            count += 2
    for l in score_3:
        if l == i:
            count += 3
    for n in score_4:
        if n == i:
            count += 4
    for r in score_5:
        if r == i:
            count += 5
    for d in score_8:
        if d == i:
            count += 8
    for s in score_10:
        if s == i:
            count += 10
print(count)