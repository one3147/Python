"""animal = "고양이"
name  = "Chu"
age = 4
hobby = "츄르"
hobby = "참치"
is_adult = age >= 4
print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 ",age,"살이며, " + hobby + "를 좋아해요.")
print(name + "는 어른일까요? " + str(is_adult))"""
#주석 : 텍스트형식으로 존재하는 메모의 일종으로, 프로그램 실행에 전혀 영향을
#끼치지 않는다.

"""
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")
"""
#print(not(5 > 4 > 3))

#print('s','e','p',sep='@')

#print(round(3.49)) 반올림

#print(abs(-5)) 절댓값

#print(pow(5,2)) 제곱

#print(max(1,10)) 최대
from math import *
#print(floor(4.99)) #내림 floor : 바닥
#print(ceil(3.14)) #올림 ceil : 천장
#print(sqrt(5)) #제곱근
import random
#print(int(random() * 10))

"""a = 1
for x in range(1, 100):
    a = a * x
    print(a)
"""
#print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
#print("오프라인 스터디 모임 날짜는 매월",random.randint(4,28),"일입니다.")
sen = """
사랑하긴 했었나요
스쳐가는 인연이었나요
짧지않은 우리 함께 했던 시간들이
자꾸 내 마음을 가둬두네."""
#print(sen)
"""
jumin = "060306-3456789"
print("성별 : " + jumin[7])
print("생년월일 : 20" + jumin[0:6],sep='')
print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 (뒤부터) : " + jumin[-7:])
print(jumin)"""

#대소문자 변경
sen = "Python is Amazing"
#print(sen.lower()) #소문자로 변경
#print(sen.upper()) #대문자로 변경
#print(sen.replace("Amazing", "PyPy")) #문자열 대체
#index = sen.index("P") #문자가 몇번째에 있는지 알려줌
#print(index)

#a,b = map(int, input().split()) #다중 입력
#print(a + b)
c = [input() for _ in range(5)] #5번 입력
print(c)

#d = [list(map(int, input().split())) for _ in range(5)] #2차원배열
#print(d)
#sen = "Python is Amazing"
#index = sen.index("n") #n이 몇번째인지 찾아줌.
#index = sen.index("n",index + 1)
#print(sen.find("n")) #sen.index와 차이를 모르겠음.
"""a = int(input())
for x in range(1,a):
    for y in range(1, x):
        print("*",sep='',end='')
    print() 
"""
#print("나는 %d살입니다."%20)
#print("나는 %s을 좋아합니다." %"파이썬")
#print("나는 {}살입니다.".format(20))
#print("나는 {1}과 {0}을 좋아합니다.".format("Python", "C Language"))
#print("나는 {1}색과 {0}색을 좋아해요.".format("하얀", "검은"))
#print("1 과 5 사이의 수는 {0}, {2}, {1}, {3} 등이 있습니다.".format("1" , "3", "2" ,"4"))
#print(" 나는 {age}살이며, {color}색을 좋아한다.".format(age = 17, color = "BLACK"))
#print("Python\nC Language")
#print("나는 '\Python\\'을 좋아합니다.")
#print("C:\\Users\Linux\pwn\B0F\\b0f.py")
#print("Language : Python \r PyScript \r PyPy3")
#print("Language : Python\nLangauge : C Langauge")
#print("Pythonp\b") #원래 BackSpace의 역할인데, python3를 오면서 역할이 바뀜
#print("Python\nC Language")

"""
url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
"""


