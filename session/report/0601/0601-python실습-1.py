# 주민등록번호를 입력 성별 출력
# jumin = input()
# if(jumin[7] == "1"):
#     print("남자")
# elif(jumin[7] == "2"):
#     print("여자")
# else:
#     print("뭘까요??")

# 문자의 개수를 세어보자.
# prince =''' "My life is very monotonous,"the fox said. "I hunt chickens; men hunt me. All the chickens are just alike, and all the men are just alike. And, in consequence, I am a little bored.But if you fame me, it will be as if the sun came to shine on my life." '''

# count_a =0
# count_b =0
# for char in prince:
#     if(char == "a"):
#         count_a = count_a + 1
#     if(char == "b"):
#         count_b = count_b + 1
# print(count_a)
# print(count_b)

# 문제1. 대문자 변경
# string = input('문장 입력: ')
# print(string.upper())

# 문제2. 공백있는 문자열에서 공백을 제거하고 비교
# name = input("name?")
# name = name.strip()

# if(name == "hong"):
#     print("ok")
# else:
#     print("error")

# 문제3. 화면에 출력된 별의 개수 맞추기
# import random

# star = random.randint(1, 10)

# for n in range(1, star+1):
#     print('* ', end='')
# print()

# count = int(input('몇 개 일까요?'))
# if(count == star):
#     print('참 잘했어요.')
# else:
#     print("틀렸습니다.")

# 문제4. 화면에 출력된 별의 개수를 맞추자
# import random

# star = random.randint(1, 5)
# for num in range(star):
#     print("*", end="")
# print()
# count = int(input("몇 개 일까요?"))
# if(count == star):
#     print('참 잘했어요')
# else:
#     print('틀렸습니다.')

# 문제5. 컴퓨터가 가지고 있는 숫자를 맞추자
import random
com = random.randint(1,5)
user = int(input("com은 1~5 중 얼마를 가지고 있을까요?"))
if(com == user):
    print("맞았습니다.")
else:
    print("틀렸습니다.")

print("com:", com, "user:", user)