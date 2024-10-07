def linear_search(target: int, search_list: list) -> list:
    to_return = []
    for i in range(len(search_list)):
        if search_list[i] == target:
            to_return.append(i)
    if len(to_return) == 0:
        return [-1]
    return to_return


'''inp_file = open("input")
search_list = list(map(int, inp_file.readline().split()))
target = int(inp_file.readline())
inp_file.close()
out_file = open("output", 'w')
try:
    ans = linear_search(target, search_list)
    out = ''
    for e in ans:
        out = out + str(e) + ' '
    out_file.write(out)
except:
    print('we have egor :(')

out_file.close()'''