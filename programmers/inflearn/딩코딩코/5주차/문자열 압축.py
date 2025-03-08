input = "abcabcabcabcdededededede"

n = len(input)
real = n

for split in range(1, n//2 + 1):
    splited = []
    for i in range(0, n, split):
        # print(i, input[i:i+split])
        # print(split)
        splited.append(input[i:i+split])
    # print("split", splited)
    result = ""

    count = 1
    for i in range(0, len(splited)-1):
        cur, next = splited[i], splited[i+1]

        if cur == next:
            count += 1
        else:
            if count == 1:
                result += cur
            else:
                result += f"{count}{cur}"
            count =1

    if count == 1:
        result += splited[-1]
    else:
        result += f"{count}{splited[-1]}"

    print("spliteds",splited)
    print(result)
    real = min(len(result), real)

print(real)

def string_compression(string):
    return


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))