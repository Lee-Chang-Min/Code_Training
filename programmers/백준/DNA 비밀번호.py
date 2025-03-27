
s, p = map(int, input().split())  ## s 총길이 4 p 만들 비밀번호 길이 2
DNA_string = list(input().rstrip()) #['G', 'A', 'T', 'A']

# print(DNA_string)

DNA = [0, 0, 0, 0]
min_num = list(map(int, input().split()))  ## A, C, G ,T
start = 0
end = p
count = 0

def DNA_count(start, end):
  global count
  global DNA
  for i in range(start, end):
    if DNA_string[i] == 'A':
      DNA[0] += 1
    elif DNA_string[i] == 'C':
      DNA[1] += 1
    elif DNA_string[i] == 'G':
      DNA[2] += 1
    else:
      DNA[3] += 1
  if (DNA[0] >= min_num[0]) and (DNA[1] >= min_num[1]) and (DNA[2] >= min_num[2]) and (DNA[3] >= min_num[3]):
    # 1 0 0 1
    count += 1

DNA_count(start, end)

for i in range(end, s):
  print(i,s)
  print("DNA_string[i]", DNA_string[i])
  if DNA_string[i] == 'A':
    DNA[0] += 1
  elif DNA_string[i] == 'C':
    DNA[1] += 1
  elif DNA_string[i] == 'G':
    DNA[2] += 1
  elif DNA_string[i] == 'T':
    DNA[3] += 1

  print("DNA_string[i-p]", DNA_string[i-p])
  if DNA_string[i-p] == 'A':
    DNA[0] -= 1
  elif DNA_string[i-p] == 'C':
    DNA[1] -= 1
  elif DNA_string[i-p] == 'G':
    DNA[2] -= 1
  elif DNA_string[i-p] == 'T':
    DNA[3] -= 1
  if (DNA[0] >= min_num[0]) and (DNA[1] >= min_num[1]) and (DNA[2] >= min_num[2]) and (DNA[3] >= min_num[3]):
    count += 1

print(count)