# def find_max_num(array):

#     for number in array:
#         is_max_num = True
#         for compare_number in array:
#             if number < compare_number:
#                 is_max_num = False
#         if is_max_num:
#             return number
            
#         print(number)

# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
# print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))


def find_max_num(array):

    max_number = array[0]
    for number in array:
        if number > max_number:
            max_number = number
    return max_number
 

# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))




#######################################################################
#######################################################################

def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurrence

    return max_alphabet

result = find_max_occurred_alphabet
# print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
# print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
# print("정답 = b 현재 풀이 값 =", result("best of best youtube"))


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet
# print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
# print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
# print("정답 = b 현재 풀이 값 =", result("best of best youtube"))


#######################################################################
#######################################################################

def is_number_exist(number, array):
    
    for a in array:
        if a == number:
            return True
    return False


result = is_number_exist
# print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
# print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
# print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))


def find_max_plus_or_multiply(array):
    plus_or_multiply_sum = 0
    for number in array:
        if number <= 1 or plus_or_multiply_sum <= 1:
            plus_or_multiply_sum += number
        else:
            plus_or_multiply_sum *= number
    return plus_or_multiply_sum


result = find_max_plus_or_multiply
# print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
# print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
# print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))




#######################################################################
#######################################################################

# input = "abadabac"

# def find_not_repeating_first_character(string):
    
#     for s in string:
        


# result = find_not_repeating_first_character
# print("정답 = d 현재 풀이 값 =", result("abadabac"))
# print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
# print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))



#소수 나열하기
# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.

input = 20


def find_prime_list_under_number(number):
    prime_list = []
    # N의 제곱근 보다 크지 앟은 어떤 소수로도 나누어 떨어지지 않는다.

    for n in range(2, number + 1):
        # 이것들이 소수인가? 소수라면 prime_list에 넣어라
        for i in prime_list: # 2 부터 n-1까지를 i 에 들어가는 것을 반복한다
            if i * i <= n and n % i == 0:
                break
        else:
            prime_list.append(n)
     
    return prime_list


result = find_prime_list_under_number(input)
# print(result)



# 문자열 뒤집기
input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_zero = 0
    count_to_one = 0

    if string[0] == '0':
        count_to_one += 1
    elif string[0] == '1':
        count_to_zero += 1

    for i in range(len(string) - 1):
        print(i)
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_one += 1
            if string[i + 1] == '1':
                count_to_zero += 1
    # return min(count_to_zero, count_to_one)






result = find_count_to_turn_out_to_all_zero_or_all_one(input)
# print("정답",result)


def summarize_string(input_str):
    # 이 부분을 채워보세요!
    result = ""
    alphabet = [0] * 26

    for i in input_str:
        alphabet[ord(i) - 97] += 1

    print(alphabet)

    for i in range(len(alphabet)):
        if alphabet[i] > 0:
            result += chr(i+97)+str(alphabet[i])+"/"
    return result[:-1]


    


input_str = "acccdeee"

print(summarize_string(input_str))