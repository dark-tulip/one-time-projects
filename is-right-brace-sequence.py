#  is right braces sequence

s = "(()[([][]())[()][()][][]])([])()"
"""


"""
cnt = 0
cnt2 = 0
for i in s:
    if i == "(":
        cnt += 1
    elif i == ")":
        cnt -= 1
        if cnt < 0: break
    elif i == "[":
        cnt2 += 1
    elif i == "]":
        cnt2 -= 1
        if cnt2 < 0: break

if cnt == 0 and cnt2 == 0: print("YES")
else: print("NO")
