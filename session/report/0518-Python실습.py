for num in range(1, 100+1):
    print(num, end=" ")

for num in range(1, 100+1):
    if(num%2 ==0):
        print(num)

for num in range(1, 100+1):
    if(num%5 == 0):
        print(num)

#1) 짝수이면서 동시에 5의 배수인 수를 출력
#2) 짝수를 모두 출력하면서 5의 배수인 짝수도 출력
#3) 짝수를 모두 출력하면서 5의 배수도 출력(홀수인 5의 배수 포함)

#1) 코딩
for num in range(1, 100+1):
    if(num % 2) == 0 and (num % 5) == 0:
        print(num, end='\t')

#2) 코딩
print()
for num in range(1, 100+1):
    if(num%2) ==0 or (num % 5) ==0:
        print(num, end='\t')

#3) 코딩
print()
for num in range(1, 100+1):
    if(num % 2) ==0 or (num % 5)==0:
        print(num, end='\t')
print()
#알파벳 'a'의 개수
prince = '''the fox said. I hunt chickens; men hunt'''
count =0
for char in prince:
    if(char =='a'):
        count = count +1
print(count)

#단어 개수
words =0
for char in prince:
    if(char == ' '):
        words +=1
print(words)