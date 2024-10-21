def solution(s) :
    num_list = list(map(int, list(s.split())))
    return ''.join(str(min(num_list))+' '+str(max(num_list)))
    