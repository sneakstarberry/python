from time import sleep
# 자판기 내용물 객체
class Item():
    price = 0
    name = ""
    stock = 0

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
# 음료수 선
select = 0
# 넣는 순간의 돈
insertMoney = 0
# 자판기에 들어 있는 돈
remainMoney = 0
# 자판기 내용물들 배열
items = [Item("포카리스웨트", 800, 5), Item("코카콜라", 1000, 5), Item("네쓰비", 500, 5)]

# 계속 반복해준다.
while(True):
    # 자판기 이름 출력
    print("#####################")
    print("# 음료수 자판기 v2.7 #")
    print("#####################")
    # 돈을 넣는다.
    insertMoney = int(input("돈을 넣으시오.\n"))
    remainMoney += insertMoney
    # 메뉴를 선택한다.
    select = int(input("음료를 선택하시오. \n 1.포카리스웨트 800 2.코카콜라 1000 네쓰비 500\n"))
    select = select-1
    # 돈이 부족한지 확인한다.
    if (remainMoney - items[select].price < 0):
        print("잔액이 부족합니다.")
        continue
    # 재고가 부족한지 확인한다.
    elif (items[select].stock == 0):
        print(items[select].name+"의 재고가 부족합니다. 다른 메뉴를 선택해 주세요.")
        continue
    # 문제가 없을 경우 돈을 줄이고 재고를 감소시킨다.
    else:
        remainMoney = remainMoney - items[select].price
        items[select].stock -= 1

    print("나오는 중")
    print()
    sleep(2)
    # 음료수 출력
    print(items[select].name +"(이)가 나왔습니다.")
    print(str(items[select].stock) +"개 남았습니다.")
    print(str(remainMoney)+"원 남았습니다.")
    print()
    # 잔액이 있을 경우 잔액은 반환 할 것인지
    if (remainMoney > 0):
        sel = input("잔액 반환을 합니까?\nYes or No\n")
        sel = sel.capitalize()
        # 잔액 반환 시 프로그램 종료
        if (sel == "Yes"):
            print(str(remainMoney)+"원을 반환하였습니다.")
            remainMoney = 0
            break
        # 아니면 계속
        else:
            continue


