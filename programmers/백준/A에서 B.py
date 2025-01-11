

#무조건 정수임, 거꾸로 생각해보자

a,b = map(int,input().split())

def change(a,b):
    cnt = 1

    while b != a:
        # B가 A보다 작아지면 변환 불가능
        if b < a:
            return -1
        
        if(b % 2 == 0):
            # //는 나눗셈을 의미하며 결과가 int
            # B = int(B/2)
            b = b // 2
        elif(b % 10 == 1):
            b = b // 10
            
        else:
            return -1

        cnt += 1
        

    return cnt 

print(change(a,b))
        