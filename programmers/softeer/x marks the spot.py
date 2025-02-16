import sys

n = int(input())

result = []
for _ in range(n):
    word1, word2 = map(str, input().split())
    # word = input()
    word2 = list(word2)
    # print(word)
    index = word1.lower().find("x")
    if index != -1:
        if word2[index].isalpha():  # 문자인 경우
            result.append(word2[index].upper())
        else:  # 숫자나 특수문자는 그대로 추가
            result.append(word2[index])

print("".join(result))