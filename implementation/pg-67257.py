import re
from itertools import permutations
import copy
    
def solution(expression):
    answers = []
    operators_list = ['*', '+', '-']
    numbers = re.split('[*+-]', expression)
    operators = re.split('[0-9]+', expression)[1:-1]

    combs = list(permutations(operators_list, 3))
    
    for comb in combs:
        n = copy.deepcopy(numbers)
        o = copy.deepcopy(operators)
        for operator in comb:
            while operator in o:
                i = o.index(operator)
                n[i] = str(eval(n[i] + operator + n[i + 1]))
                
                del n[i + 1]
                del o[i]
        answers.append(abs(int(n[0])))
    return max(answers)