# https://www.lintcode.com/problem/659/

def encode(strs):

    res = ''
    for s in strs:
        res += str(len(s)) + '#' + s
    return res




def decode(str):

    res = []
    idx = 0
    while idx < len(str):
        num = ''
        while str[idx].isnumeric():
            num += str[idx]
            idx += 1
        if str[idx] == '#':
            res.append(str[idx+1:int(num) + idx + 1])
        idx = int(num) + idx + 1

    return res
        




e = encode(["we", "say", "-", '-',"5#", '#100', "100#", "yes"])
print(e)
d = decode(e)
print(d)