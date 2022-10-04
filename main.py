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


"""
    비밀번호 조합 과정은 크게 4단계로 나눔
    1. 조합에 필요한 단어, 글자 등을 입력받아 list에 저장
    2. separator를 입력받아 list 값을 하나의 문자열로 조합 (여러번 시행)
    3. 조합된 값의 길이가 max_len 값을 초과하는지 확인
    4. 만들어진 값을 모아서 출력
    4`. 만약 만들어진 비밀번호에 좋고 나쁨을 수치화할 수 있다면 나타낸다
"""


