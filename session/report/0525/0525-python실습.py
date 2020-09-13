# 실습 1
# num = 0
# while True:
#     num = num + 1
#     print(str(num)+'\t', end="")

# 실습 2
# select = 999
# while select !=0:
#     print("1. 사이다")
#     print("2. 환타")
#     print("3. 파워에이드")
#     print("0. 종료")
#     select = int(input("메뉴 선택: _"))
#     print("선택 메뉴는 " + str(select) +" 입니다.\n\n")

# 실습 3
# for a in range(1, 10+1):
#     print(a)
#     if a % 2 == 0:
#         print("O")
#     if a % 3 == 0:
#         print("x")
#         if (a % 2 ==0) and (a % 3 == 0):
#             print("△")

# 실습 4
# for num in range(1, 100+1):
#     if (num % 5 ==0):
#         continue
#     else:
#         print(num)
# for num in range(1, 100+1):
#     if (num == 20):
#         break
#     else:
#         print(num)
# for num in range(1, 100+1):
#     if (num % 2 == 0 and num % 5 == 0):
#         pass
#     else:
#         print(num)

# 실습 5
select = 999
menu = ["1.사이다", "2.환타", "3.파워에이드", "0.종료"]

while select != 0:
    for m in range(4):
        print(menu[m])
    select = int(input("메뉴 선택:_"))
    print("\n선택 메뉴는" + menu[select-1]+"입니다.\n\n")# 색인은 0부터
