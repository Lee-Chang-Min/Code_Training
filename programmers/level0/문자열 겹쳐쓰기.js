function solution(my_string, overwrite_string, s) {
    var answer = "He11oWor1d";
    var end = overwrite_string.length 
    
    answer = my_string.slice(0,s) + overwrite_string + my_string.slice(s+end)
    console.log(answer);
    
    return answer;
}