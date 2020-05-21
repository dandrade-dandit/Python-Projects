def print_formatted(number):
    txt = ''
    for i in range(0, number):
        d = i + 1
        o = oct(d)[2:]
        h = hex(d)[2:].upper()
        b = bin(d)[2:]
        max_bin_size = len(b)
        txt += str(d) + '*' + o + '*' + h + '*' + b + '*'

    cnt = 0
    final = ''
    txt_split = txt[:len(txt) - 1].split('*')
    for s in txt_split:
        final += s.rjust(max_bin_size, ' ') + ' '
        cnt += 1
        if cnt == 4:
            final += '\n'
            cnt = 0

    print(final[:len(final) - 1])


if __name__ == '__main__':
    n = 63
    print_formatted(n)