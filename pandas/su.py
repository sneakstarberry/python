import pandas as pd
from datetime import datetime

class Doctor():
    name = ""
    class_num = 0
    class_name = []
    dept = ""
    minute = 0
    participant = 0
    def __init__(self, name, class_num, class_name, dept, length, participant):
        self.class_name=[]
        self.name = name
        self.class_num = class_num
        self.class_name.append(class_name)
        self.dept = dept
        self.minute = length.hour*60 + length.minute
        self.participant = participant

    def cl_plus(self, class_name, length, participant):
        self.class_num += 1
        self.class_name.append(class_name)
        self.minute += length.hour*60 + length.minute
        self.participant += participant

    def plus(self, length, participant):
        self.class_num += 1
        self.minute += length.hour*60 + length.minute
        self.participant += participant

df = pd.read_excel('./meetings2020-04-23-2020-05-23.xlsx', sheet_name='meetings2020-04-23-2020-05-23')
arr = [] # 객체를 담는 곳
check1 = [] # 객체가 들어있는지 확인하는 배열
check2 = [] # 과목이 들어가 있는지 확인하는 배열
for i in range(3035):
    lenth = df.loc[i]["기간(hh:mm:ss)"]
    name = df.loc[i]["호스트"]
    class_name = df.loc[i]["주제"]
    dept = df.loc[i]["부서"]
    participant = df.loc[i]["참가자"]

    # print(lenth.hour*60 + lenth.minute)
    if df.loc[i]["호스트"] not in check1:
        check1.append(name)
        check2.append(class_name)
        arr.append(Doctor(name, 1, class_name, dept, lenth, participant))

    elif df.loc[i]["주제"] not in check2:
        num = check1.index(name)
        check2.append(class_name)
        arr[num].cl_plus(class_name, lenth, participant)

    else:
        num = check1.index(name)
        arr[num].plus(lenth, participant)

print(arr[7].name)
print(arr[7].class_num)
print(arr[7].class_name)
print(arr[7].minute)

columns_format = ["교수명", '화상수업 개설 횟수', '과목명', '부서', '기간(분)', '누적 참가자(명)']
index_format = []
for i in range(1, len(arr)+1):
    index_format.append(i)
df2 = pd.DataFrame(columns=columns_format, index=index_format)
# print(df2)
for i in range(df2.shape[0]):
    df2.iloc[i, 0] = arr[i].name
    df2.iloc[i, 1] = arr[i].class_num
    df2.iloc[i, 2] = arr[i].class_name
    df2.iloc[i, 3] = arr[i].dept
    df2.iloc[i, 4] = arr[i].minute
    df2.iloc[i, 5] = arr[i].participant

# print(df2)

df2.to_excel('./complete.xlsx',
    sheet_name='Sheet1',
    columns=columns_format,
    header=True,
    startrow=1,
    startcol=0,
)
print("완료")