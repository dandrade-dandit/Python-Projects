
n = 9
m = 27
txt = ''
mid = (n // 2) + 1
cont = 1

for i in range(0, n):
    pos = i + 1
    if pos < mid:
        txt_line = '.|.' * cont
        tam_comp = m - len(txt_line)
        mid_comp = int(tam_comp / 2)
        comp = '-' * mid_comp
        txt += comp + txt_line + comp + '\n'
        cont += 2
    elif pos == mid:
        txt_line = 'WELCOME'
        tam_comp = m - len(txt_line)
        mid_comp = int(tam_comp / 2)
        comp = '-' * mid_comp
        txt += comp + txt_line + comp + '\n'
        cont -= 2
    elif pos > mid:
        txt_line = '.|.' * cont
        tam_comp = m - len(txt_line)
        mid_comp = int(tam_comp / 2)
        comp = '-' * mid_comp
        txt += comp + txt_line + comp + '\n'
        cont -= 2

print(txt)