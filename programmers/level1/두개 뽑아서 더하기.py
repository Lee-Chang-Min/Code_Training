def solution(numbers):
    answer = []
    return answer

numbers = [2,1,3,4,1]
numbers.sort()

anwer = set()

# for idx, val in enumerate(numbers):
#     print(idx, val)


for idx, val in enumerate(numbers):
    for i in range(len(numbers)):
        #i=> 0 1 2 3 4
        # print(f'후자: {numbers[i+idx+1]}')
        idxs = idx+1
        # print(f'ggg: {len(numbers)}')
        # print(numbers[5])
        print('---------------')
        # print(val+numbers[i+idxs])
        
        if(idxs+i > len(numbers)-1): 
            break;
        else:
            anwer.add(val+numbers[i+idxs])

print(anwer)