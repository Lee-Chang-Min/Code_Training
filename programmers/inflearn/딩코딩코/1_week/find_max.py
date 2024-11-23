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