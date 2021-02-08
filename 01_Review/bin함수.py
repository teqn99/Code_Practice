"""
파이썬에서는 기본적으로 10 진수 형태로 숫자를 표현하기 때문에, 다른 진수 형태로 숫자를 표현하려면 다음과 같이 숫자 앞에 접두어를 붙여줘야 한다.
2진수: 0b
8진수: 0o
16진수: 0x
"""

# bin(number)
# -> 전달받은 number의 값(integer 혹은 long integer 자료형)을 이진수(bin) 문자열로 돌려준다.

bin(10)
# 결과: '0b1010'
bin(42)
# 결과: '0b101010'



# oct(number)
# -> 전달받은 number의 값(integer 혹은 long integer 자료형)을 8진수(oct) 문자열로 돌려준다.

oct(42)
# 결과: '0o52'



# hex(number)
# -> 전달받은 number의 값(integer 혹은 long integer 자료형)을 16진수(hex) 문자열로 돌려준다.

hex(42)
# 결과: '0x2a'



