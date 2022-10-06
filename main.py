from math import factorial
from random import shuffle


fragments = [] #인풋값의 모음, fragments
max_len = 0 #Default

max_len = input("비밀번호 생성이 가능한 최대 글자수를 입력 :")
while True:
    value = input("비밀번호 생성에 이용하실 단어를 입력 :")
    if value == "":
        break
    else:
        fragments.append(value)
frag_len = len(fragments) #비밀번호 조합에 사용되는 단어, 글자 등과 같은 조각 갯수

for elmt in frag_len:
    total_len =+ len(elmt)
if total_len < max_len:
    print("Err: Exceed of lettercount")
    raise Exception("Err: Exceed of lettercount")

combinations = [] #완성된 비밀번호 조합들을 저장한 list

## len(combination)은 반드시 max_len를 초과해선 안됩니다


def combinate(separator):
    #중복 없이 조합 가능한 경우의 수(순열)
    permutation = int(factorial(2*frag_len-1)/factorial(frag_len-1)) #순열 = 분자/분모
    for idx in range(permutation):      
        shuffle(combinations)
        combination = separator.join(fragments)                                    
        combinations.append(combination)
combinate("")
combinate("_")
com_rearranged = set(combinations) #중복제거
print(com_rearranged)
