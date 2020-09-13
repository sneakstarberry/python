#문제6. 한 번만 실행되는 슬롯머신
# import random

# slot1 = random.randint(1, 6)
# slot2 = random.randint(1, 6)
# slot3 = random.randint(1, 6)

# score = 0

# print(slot1, ":", slot2, ":", slot3)

# if(slot1 == slot2 == slot3):
#     score = score + 300
# elif((slot1 == slot2) or (slot2 == slot3) or (slot1 == slot3)):
#     score = score + 200
# else:
#     score = score - 100

# print("점수:", score)

# 문제7. 계속 실행 여부를 선택하는 슬롯머신
# import random
# score = 0
# while(True):
#     print("#################")
#     print("# 슬롯머신 v1.0 #")
#     print("#################")


#     slot1 = random.randint(1, 6)
#     slot2 = random.randint(1, 6)
#     slot3 = random.randint(1, 6)


#     print(slot1, ":", slot2, ":", slot3)

#     if(slot1 == slot2 == slot3):
#         score = score + 300
#     elif((slot1 == slot2) or (slot2 == slot3) or (slot1 == slot3)):
#         score = score + 200
#     else:
#         score = score - 100

#     print("\n", "점수:", score)

#     key = input("\n계속?(n/N = quit)")

#     if(key == "n") or (key == "N"):
#         break
#     else:
#         continue

# 문제8. 숫자 대신 문자가 출력되는 슬롯머신

# import random
# score = 0
# SlotName = ["사과", "바나나", "귤", "망고", "배", "황금향"]
# while(True):
#     print("#################")
#     print("# 슬롯머신 v1.5 #")
#     print("#################")


#     slot1 = random.randint(0, 5)
#     slot2 = random.randint(0, 5)
#     slot3 = random.randint(0, 5)


#     print("\n", SlotName[slot1], ":", SlotName[slot2], ":", SlotName[slot3])

#     if(slot1 == slot2 == slot3):
#         score = score + 300
#     elif((slot1 == slot2) or (slot2 == slot3) or (slot1 == slot3)):
#         score = score + 200
#     else:
#         score = score - 100

#     print("\n", "점수:", score)

#     key = input("\n계속?(n/N = quit)")

#     if(key == "n") or (key == "N"):
#         break
#     else:
#         continue

# 문제9. 슬롯머신에서 다음과 같이 메뉴를 사용하자.

import random
import time

score = 0
SlotName = ["사과", "바나나", "귤", "망고", "배", "황금향"]
MenuString = ["1.게임시작", "2.점수조회", "3.종료"]
while(True):
    print("#################")
    print("# 슬롯머신 v2.0 #")
    print("#################")
    print(MenuString[0])
    print(MenuString[1])
    print(MenuString[2])

    MenuSelect = input("메뉴 선택:_?")
    if(MenuSelect == "1"):
        slot1 = random.randint(0, 5)
        slot2 = random.randint(0, 5)
        slot3 = random.randint(0, 5)

        # print("\n", SlotName[slot1], ":", SlotName[slot2], ":", SlotName[slot3])
        print("\n", SlotName[slot1], ":", end=""); time.sleep(1)
        print("\n", SlotName[slot2], ":", end=""); time.sleep(1)
        print("\n", SlotName[slot3])

        if(slot1 == slot2 == slot3):
            score = score + 300
            print("\n300 점 획득!!!\n")
        elif((slot1 == slot2) or (slot2 == slot3) or (slot1 == slot3)):
            score = score + 200
            print("\n200 점 획득!!!\n")
        else:
            score = score - 100
            print("\n-100 점 감점~~\n")

    elif(MenuSelect == "2"):
        print("\n", "현재 점수:", score)
        print()
        print()

    elif(MenuSelect=="3"):
        print("\n\n~~~게임 종료~~~")
        break;

#프로그램 끝