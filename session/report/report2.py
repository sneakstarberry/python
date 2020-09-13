# 국어, 수학, 영어, 과학 변수 선언
kor = 0
mat = 0
eng = 0
sci = 0
# 성적을 입력받는 부분
kor = int(input('국어 점수:'))
mat = int(input('수학 점수:'))
eng = int(input('영어 점수:'))
sci = int(input('과학 점수:'))
# 국어, 수학, 영어, 과학 테이블 출력
print('국어\t수학\t영어\t과학')
# 테이블 구분자 출력
print('-----------------------------')
# 국어, 수학, 영어, 과학 성적 출력
print('%03d\t%03d\t%03d\t%03d' % (kor, mat, eng, sci))