import random
import re
from fractions import Fraction
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import io
from Dictionary.html_function import *
import itertools
from Dictionary.reference import *
from itertools import combinations
import math
from math import gcd
from fractions import Fraction
import pandas as pd
import random


# Reference class initialization
ref = Reference()


# 이미지 파일 불러오는 함수
def load_img(file_path):
    # Load the image using Matplotlib
    img = mpimg.imread(file_path)
    return img

def save_svg_resize(ratio):
    # ratio : 그림 확대 / 축소를 위한 파라미터, 기본값 100      
    file = io.StringIO()
    plt.savefig(file, format='svg', dpi=300, bbox_inches='tight', pad_inches=0.1) # Additional option to remove the rest parts
    file.seek(0)
    svg_data = file.getvalue()
    svg_data = svg_data.replace('<svg ', f'<svg width="{ratio}%" height="{ratio}%"  ') # style="display: block; margin: auto;"

    return svg_data


'''#######################################################################

#  QSNO 101220 71047

#######################################################################'''

def intandrationalM112_Stem_07_001():
	'''
	1. 정수-정수, 소수-소수, 분수-분수, 정수-소수, 정수-분수
	2. 문제(stem), 정답(answer), 해설(comment)을 *tuple type*으로 반환
	3. 내부 함수에는 난수(random), 분수(Fraction), 최대공약수(gcd) 등을 활용하여 계산 문제를 생성하고, MathJax 표기 형식으로 반환	
	'''

	###########################################################
	# 약분이 불가능한 분수를 생성하는 헬퍼 함수
	###########################################################
	def generate_non_simplifiable_fraction():
		while True:
			numerator = random.randint(1, 9) # 분자 1~9 사이의 난수 생성
			denominator = random.randint(2, 9) # 분모 2~9 사이의 난수 생성
			if math.gcd(numerator, denominator) == 1:  # 약분되지 않는 경우만 선택
				return Fraction(numerator, denominator) # 조건 만족시 Fraction 객체로 변환
			

	###########################################################
	# Fraction 객체의 부호를 포함하여 MathJax 형식으로 표기하는 헬퍼 함수
	###########################################################
	def format_fraction_with_sign(fraction):
		sign = "-" if fraction.numerator < 0 else "+" # Fraction.numerator가 음수면 '-'부호 포함, 양수면 '+'부호
		return f"{sign}\\frac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"
			
	###########################################################
	# 정수-정수 계산 함수
	###########################################################
	def integer_integer_calculation():
		while True:
			num1 = random.randint(-10, 10) # 첫 번째 정수 -10~10 사이의 난수 생성
			num2 = random.randint(-10, 10) # 두 번째 정수 -10~10 사이의 난수 생성
			if num1 != 0 and num2 != 0: # 두 정수 모두 0이 아닐 경우 조건 만족
				break

		result = num1 - num2 # 두 정수의 차 계산
		result_str = str(result) if result >= 0 else str(result) # 결과값 정수형으로 변환

		num1_str = str(num1) if num1 < 0 else str(abs(num1)) # 첫 번째 정수 음수면 그대로, 양수면 부호 없이
		num2_str = f"({num2})" if num2 < 0 else str(abs(num2)) # 두 번째 정수 음수면 괄호 포함, 양수면 부호 없이
		expression = f"{num1_str} - {num2_str}" # 문제 표기식
		neg_num2_str = f"({-num2})" if -num2 < 0 else str(abs(-num2)) # 두 번째 정수 음수면 괄호 포함, 양수면 부호 없이
		calculation = f"{num1_str} - {num2_str} = {num1_str} + {neg_num2_str} = {result_str}" # 계산 과정 표기식
		
		return f"\\({expression}\\)", f"\\({result_str}\\)", f"\\({calculation}\\)" # 문제, 정답, 해설 MathJax 문자열을 반환

	###########################################################
	# 소수 - 소수 계산 함수
	###########################################################
	def decimal_decimal_calculation():
		while True:
			num1 = round(random.uniform(-10, 10), 1) # 첫 번째 소수 -10~10 사이의 난수 생성
			num2 = round(random.uniform(-10, 10), 1) # 두 번째 소수 -10~10 사이의 난수 생성
			if num1 != 0 and num2 != 0 and int(num1 * 10) % 10 != 0 and int(num2 * 10) % 10 != 0: # 두 소수 모두 0이 아니고, 소수점 첫째 자리가 0이 아닐 경우 조건 만족
				break
		result = num1 + (-num2) # 결과 result = num1-num2를 구하되, 내부적으로 num1 + (-num2)로 처리

		result_str = (
			"0" if result == 0  # 결과값이 0일 때는 "0"
			else f"{int(result)}" if result % 1 == 0  # 정수일 때는 정수형으로 변환
			else f"{round(result, 1)}" if result > 0  # 양수일 경우 부호 제거
			else f"{round(result, 1):+}"  # 음수일 경우 부호 포함
		)
		# 첫 번째 숫자: 음수면 그대로, 양수면 부호 없이
		num1_str = str(num1) if num1 < 0 else str(abs(num1))
		# 두 번째 숫자: 음수면 괄호 안에, 양수면 부호 없이
		num2_str = f"({num2})" if num2 < 0 else str(abs(num2))

		expression = f"{num1_str} - {num2_str}"
		neg_num2_str = f"({-num2})" if -num2 < 0 else str(abs(-num2))
		calculation = f"{num1_str} - {num2_str} = {num1_str} + {neg_num2_str} = {result_str}"
		return f"\\({expression}\\)", f"\\({result_str}\\)", f"\\({calculation}\\)"

	###########################################################
	# 분수-분수 계산을 위한 임의의 부호(양/음) 분수 생성 함수
	###########################################################
	def generate_random_sign_fraction():
		
		fraction = generate_non_simplifiable_fraction()
		sign = random.choice([-1, 1])
		return Fraction(sign * fraction.numerator, fraction.denominator)
	
	##################################################################
	# 분수-분수 계산 함수 (뺄셈을 덧셈으로 전환해서, 공통분모 작업 후 최종 결과 도출)
	##################################################################
	def fraction_fraction_calculation_with_proper_parentheses_corrected():
		'''
		1. 무작위 분수 fraction1, fraction2를 생성( 약분x )
		2. 절댓값이 같은 분수는 다시 뽑고, 서로 다른 크기를 갖도록 보장
		3. " - "  연산이므로 fraction1 - fraction2를 fraction1 + (-fraction2) 형태로 변환
		4. 분모가 같지 않을 경우, 최소공배수 형태로 공통분모를 구한다.
		5. 두 분수를 공통분모로 통일하고, 분자 합을 낸 뒤 Fraction을 통해 약분(simplify) 여부를 체크

		'''
		fraction1 = generate_random_sign_fraction()
		fraction2 = generate_random_sign_fraction()

		# 두 분수의 절대값이 같으면 다시 생성
		while abs(fraction1) == abs(fraction2):
			fraction2 = generate_random_sign_fraction()

		# 분수 표기
		def format_fraction_with_sign(numerator, denominator):
			sign = "-" if numerator < 0 else ""
			return f"{sign}\\dfrac{{{abs(numerator)}}}{{{denominator}}}"
		

		def format_fraction_with_sign_answer(numerator, denominator):
			'''
			
			1. "-" 분모가 1이면 정수 형태로 변환
			2. "-"분모가 1이 아니면 분수 형태로 변환
			
			'''
			sign = "-" if numerator < 0 else ""
			if denominator == 1:
				return f"{sign}{abs(numerator)}"	
			else :
				return f"{sign}\\dfrac{{{abs(numerator)}}}{{{denominator}}}"

		#fraction1,fraction2를 각각 mathjax 문자열로 변환
		fraction1_str = format_fraction_with_sign(fraction1.numerator, fraction1.denominator)
		
		#fraction2가 음수일 경우 괄호로 감싸야 하므로 조건 분기
		fraction2_str = (f"(-\\dfrac{{{abs(fraction2.numerator)}}}{{{fraction2.denominator}}})" 
                if fraction2.numerator < 0 
                else f"\\dfrac{{{abs(fraction2.numerator)}}}{{{fraction2.denominator}}}")

		# -fraction2를 mathjax로 표기 (뺄셈->덧셈 변환에서 필요)
		neg_fraction2_str = (f"(-\\dfrac{{{abs(-fraction2.numerator)}}}{{{fraction2.denominator}}})" 
                    if -fraction2.numerator < 0 
                    else f"\\dfrac{{{abs(-fraction2.numerator)}}}{{{fraction2.denominator}}}")
		# 최종 표기 예시 : fraction1 - fraction2
		expression = f"{fraction1_str} - {fraction2_str}"
		# 중간 해설 단계에서 fraction1 + (-fraction2) 형태로 표기
		calculation = f"{fraction1_str} + {neg_fraction2_str}"  # Updated expression content

		# 공통분모 작업
		if fraction1.denominator == fraction2.denominator:
			
			# 분모가 이미 동일한 경우
			common_denominator = fraction1.denominator
			fraction1_scaled_numerator = fraction1.numerator
			fraction2_scaled_numerator = -fraction2.numerator

		elif fraction2.denominator % fraction1.denominator == 0:
			
			# fraction2의 분모가 fraction1의 분모의 배수일 경우
			common_denominator = fraction2.denominator
			fraction1_scaled_numerator = fraction1.numerator * fraction2.denominator * (common_denominator // fraction1.denominator)
			fraction2_scaled_numerator = -fraction2.numerator  

		else:
			# 분모가 다르고, 배수가 아닐 경우
			# 최소공배수 형태로 공통분모를 구함.
			common_denominator = (fraction1.denominator * fraction2.denominator) // gcd(fraction1.denominator, fraction2.denominator)
			fraction1_scaled_numerator = fraction1.numerator * fraction2.denominator * (common_denominator // fraction1.denominator)
			fraction2_scaled_numerator = -fraction2.numerator * fraction1.denominator * (common_denominator // fraction2.denominator)



		# 새로 스케일링한 분수 객체 생성
		fraction1_new = Fraction(fraction1_scaled_numerator, common_denominator)
		fraction2_new = Fraction(fraction2_scaled_numerator, common_denominator)

		# MathJax 표기
		fraction1_new_str = format_fraction_with_sign(fraction1_new.numerator, common_denominator)
		fraction2_new_str = (f"(-\\dfrac{{{abs(fraction2_new.numerator)}}}{{{common_denominator}}})" 
                    if fraction2_new.numerator < 0 
                    else f"\\dfrac{{{abs(fraction2_new.numerator)}}}{{{common_denominator}}}")
		

		# 해설 업데이트: 공통분모가 된 형태의 분수 덧셈까지
		calculation += f" = {fraction1_new_str} + {fraction2_new_str}"

		# 분자 합 계산: fraction1_new + fraction2_new
		result_numerator = fraction1_new.numerator + fraction2_new.numerator
		result = Fraction(result_numerator, common_denominator)
		simplified_result = result.limit_denominator() # 약분 여부 체크

		# 결과를 MathJax 형태로 표기
		result_str = format_fraction_with_sign_answer(result.numerator, result.denominator)

		# 결과가 약분 가능하다면 약분 후 표시
		if result != simplified_result:
			simplified_result_str = format_fraction_with_sign(simplified_result.numerator, simplified_result.denominator)
			answer = simplified_result_str
		else:
			answer = result_str
		
		# 해설 마지막에 최종 결과까지 추가
		calculation += f" = {result_str}"
		return f"\\({expression}\\)", f"\\({answer}\\)", f"\\({calculation}\\)"

	###########################################################
	# 정수-소수(소수-정수) 계산
	###########################################################
	def integer_decimal_calculation_modified():
		'''
		1. 무작위 정수 num1, 소수 num2를 생성(모두 0이 아님)
		2. 소수는 한 자리 소수점으로, 소수점 한 자리가 0이 아닌 값으로 필터링
		'''
		
		while True:
			num1 = random.randint(-10, 10)
			num2 = round(random.uniform(-10, 10), 1)
			# num2가 0이 아니고, 소수점 첫째 자리가 0이 아닌 숫자만 허용
			if num1 != 0 and num2 != 0 and num2 * 10 % 10 != 0:
				break
		
		# True/False로 '정수-소수', '소수-정수' 랜덤 선택
		if random.choice([True, False]):
			# 정수-소수
			num1_str = str(num1) if num1 < 0 else str(abs(num1))
			num2_str = f"({num2})" if num2 < 0 else str(abs(num2))

			expression = f"{num1_str} - {num2_str}"
			neg_num2_str = f"({-num2})" if -num2 < 0 else str(abs(-num2))
			calculation = f"{num1_str} - {num2_str} = {num1_str} + {neg_num2_str}"
			result = num1 + (-num2)
		else:
			# 소수-정수
			num2_str = str(num2) if num2 < 0 else str(abs(num2))
			num1_str = f"({num1})" if num1 < 0 else str(abs(num1))

			expression = f"{num2_str} - {num1_str}"
			neg_num1_str = f"({-num1})" if -num1 < 0 else str(abs(-num1))
			calculation = f"{num2_str} - {num1_str} = {num2_str} + {neg_num1_str}"
			result = num2 + (-num1)
		
		# 결과 문자열 (0, 정수, 소수, 음수 처리)
		result_str = (
			"0" if result == 0 
			else f"{int(result)}" if result % 1 == 0 
			else f"{round(result, 1)}" if result > 0 
			else f"{round(result, 1):+}"
		)
		calculation += f" = {result_str}"
		
		return f"\\({expression}\\)", f"\\({result_str}\\)", f"\\({calculation}\\)"
	
	###########################################################
	# 정수 - 분수 , 분수 - 정수 계산 함수 (순서 랜덤)
	###########################################################
	def integer_fraction_calculation_with_multiplication():
		'''
		1. 정수 num1(0 제외), 약분 불가능한 분수 생성
		2. 중간과정: 정수를 분수로 바꾸어 (e.g.: 3->3*(분모)/분모) 같은 분모를 만들어서 계산
		3. 최종적으로 Fraction 객체의 limit_denominator()로 약분 여부 판단 후 답을 표시
		'''
		# fraction객체가 음수면, '-'를 붙여 반환
		def format_fraction_with_sign_answer2(fraction):
			sign = "-" if fraction.numerator < 0 else ""
			return f"{sign}\\dfrac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"			

		# 정수 num1 생성
		while True:
			num1 = random.randint(-10, 10)
			if num1 != 0:
				break

		# 분수 fraction 생성
		fraction = generate_non_simplifiable_fraction()

		# fraction을 +, - 부호와 함께 표시하는 헬퍼 함수를 사용하여 문자열화
		fraction_str = format_fraction_with_sign(fraction)

		if random.choice([True, False]):			
			''' 1) 정수 - 분수 '''
			num1_str = str(num1) if num1 < 0 else str(abs(num1))
			
			# 분수가 음수면 괄호, 양수면 그대로
			fraction_str = (f"(-\\dfrac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}})" 
                       if fraction.numerator < 0 
                       else f"\\dfrac{{{fraction.numerator}}}{{{fraction.denominator}}}")

			expression = f"{num1_str} - {fraction_str}"
			
			# 분수를 음수로 만들기
			neg_fraction = Fraction(-fraction.numerator, fraction.denominator)
			neg_fraction_str = (f"(-\\dfrac{{{abs(neg_fraction.numerator)}}}{{{neg_fraction.denominator}}})" 
                          if neg_fraction.numerator < 0 
                          else f"\\dfrac{{{neg_fraction.numerator}}}{{{neg_fraction.denominator}}}")
			sign_change = f"-\\dfrac{{{abs(num1)}}}{1} - {fraction_str}"
			
			# 정수를 같은 분모로 변환: num1 * fraction.denominator
			num1_as_fraction = Fraction(num1 * fraction.denominator, fraction.denominator)
			num1_as_fraction_str = (f"-\\dfrac{{{abs(num1 * fraction.denominator)}}}{{{fraction.denominator}}}" 
                               if num1 < 0
                               else f"\\dfrac{{{num1 * fraction.denominator}}}{{{fraction.denominator}}}")
			
			# 공통분모 맞추기 e.g. 3/1-2/3 -> 9/3 - 2/3
			fraction_addition = f"{num1_as_fraction_str} + {neg_fraction_str}"
			result = num1_as_fraction + neg_fraction
			
		else:
			'''2) 분수 - 정수'''
			fraction_str = f"-\\dfrac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}" if fraction.numerator < 0 else f"\\dfrac{{{fraction.numerator}}}{{{fraction.denominator}}}"
			num1_str = str(num1) if num1 > 0 else f"({str(num1)})"
			expression = f"{fraction_str} - {num1_str}"
			
			neg_num1 = -num1
			neg_num1_str = f"({neg_num1})" if neg_num1 < 0 else str(abs(neg_num1))
			sign_change = f"{fraction_str} + {neg_num1_str}"

			num1_as_fraction = Fraction(neg_num1 * fraction.denominator, fraction.denominator)
			num1_as_fraction_str = (f"(-\\dfrac{{{abs(neg_num1 * fraction.denominator)}}}{{{fraction.denominator}}})" 
                               if neg_num1 < 0 
                               else f"\\dfrac{{{neg_num1 * fraction.denominator}}}{{{fraction.denominator}}}")
			fraction_addition = f"{fraction_str} + {num1_as_fraction_str}"
			result = fraction + num1_as_fraction
			

		# 결과 약분 확인
		simplified_result = result.limit_denominator()

		result_str = format_fraction_with_sign_answer2(result)
		simplified_result_str = format_fraction_with_sign_answer2(simplified_result)
		
		'''약분 가능하면 약분된 결과로 표시'''
		if result != simplified_result:
			answer = simplified_result_str
		else:
			answer = result_str

		# 해설 구성( 뺄셈 -> 덧셈 전환, 분모 통일, 최종 결과)
		calculation = f"{expression} = {sign_change} = {fraction_addition} = {result_str}"
		return f"\\({expression}\\)", f"\\({answer}\\)", f"\\({calculation}\\)"

	###########################################################
	# 문제 생성 (stem)
	###########################################################
	stem = "다음을 계산하시오.\n"
	problem_type = random.choice(["정수-정수", "소수-소수", "분수-분수", "정수-소수", "정수-분수"])
	

	if problem_type == "정수-정수":
		exp, res, calc = integer_integer_calculation()
	elif problem_type == "소수-소수":
		exp, res, calc = decimal_decimal_calculation()
	elif problem_type == "분수-분수":
		exp, res, calc = fraction_fraction_calculation_with_proper_parentheses_corrected()
	elif problem_type == "정수-소수":
		exp, res, calc = integer_decimal_calculation_modified()
	elif problem_type == "정수-분수":
		exp, res, calc = integer_fraction_calculation_with_multiplication()
	
	stem += f"{exp}\n"
	
	answer = f"(정답) {res}\n"

	comment = f"(해설) {calc}\n"

	return stem, answer, comment


'''#############################################################################################

#  QSNO 101221 71048

#############################################################################################'''

def intandrationalM112_Stem_07_002():
 	
	def generate_non_simplifiable_fraction():
		"""약분되지 않는 분수를 생성하는 함수"""
		while True:
			numerator = random.randint(1, 9)
			denominator = random.randint(2, 9)
			if math.gcd(numerator, denominator) == 1:
				return Fraction(numerator, denominator)
	
	def format_with_sign(number, is_after_operation=False):
		"""숫자를 수학 표기법에 맞게 문자열로 변환"""
		if isinstance(number, (int, float)):
			formatted = str(int(number)) if float(number).is_integer() else f"{number:.1f}"
			
			if number < 0:
				if is_after_operation:
					return f"({formatted})"  # 연산자 뒤 음수: (-2)
				return formatted            # 첫 번째 음수: -2
			return formatted               # 양수: 2

	def format_fraction(fraction, is_after_operation=False):
		"""분수를 수학 표기법에 맞게 LaTeX 문자열로 변환"""
		if fraction.numerator < 0:
			if is_after_operation:
				# 연산자 뒤에 오는 음수에는 괄호
				return f"(-\\dfrac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}})"
			# 식 맨 앞이나, 연산자 앞의 움수인 경우 괄호 없이 e.g. -3/4 + ~~
			return f"-\\dfrac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"
		# 분수가 양수인 경우에는 그냥 기본 분수 형태로 출력
		return f"\\dfrac{{{fraction.numerator}}}{{{fraction.denominator}}}"

	def format_calculation(num1, operator, num2, result):
		"""계산 과정을 수학 표기법에 맞게 포맷팅"""
		if operator == '-':
			neg_num2 = -num2
			return (
				f"{format_with_sign(num1)} - {format_with_sign(num2, True)} = "
				f"{format_with_sign(num1)} + {format_with_sign(neg_num2, True)} = "
				f"{format_with_sign(result)}"
			)
		return (
			f"{format_with_sign(num1)} {operator} {format_with_sign(num2, True)} = "
			f"{format_with_sign(result)}"
		)

	def generate_random_sign_fraction():
		"""랜덤한 부호를 가진 분수 생성"""
		fraction = generate_non_simplifiable_fraction()
		sign = random.choice([-1, 1])
		return Fraction(sign * fraction.numerator, fraction.denominator)
	
	
	def integer_integer_calculation():
		"""정수-정수 뺄셈 계산 함수"""
		while True:
			num1 = random.randint(-10, 10)
			num2 = random.randint(-10, 10)
			if num1 != 0 and num2 != 0 and abs(num1) != abs(num2):  # 0 제외
				break
		
		result = num1 - num2
		
		# LaTeX 식 구성
		expression = f"{format_with_sign(num1)} - {format_with_sign(num2, True)}"
		
		# 계산 과정 (뺄셈을 덧셈으로 변환)
		calculation = format_calculation(num1, '-', num2, result)
		
		return (
			f"\\({expression}\\)",
			f"\\({format_with_sign(result)}\\)",
			f"\\({calculation}\\)"
		)

	def decimal_decimal_calculation():
		"""소수-소수 뺄셈 계산 함수"""
		while True:
			num1 = round(random.uniform(-10, 10), 1)
			num2 = round(random.uniform(-10, 10), 1)
			# 0이 아니고 소수점 첫째자리가 0이 아닌 값
			if (num1 != 0 and num2 != 0 and 
				int(num1 * 10) % 10 != 0 and 
				int(num2 * 10) % 10 != 0):
				break
		
		result = num1 - num2
		
		# LaTeX 식 구성
		expression = f"{format_with_sign(num1)} - {format_with_sign(num2, True)}"
		
		# 계산 과정 (뺄셈을 덧셈으로 변환)
		calculation = format_calculation(num1, '-', num2, result)
		
		return (
			f"\\({expression}\\)",
			f"\\({format_with_sign(result)}\\)",
			f"\\({calculation}\\)"
		)

	def integer_decimal_calculation():
		"""정수-소수 또는 소수-정수 뺄셈 계산 함수"""
		while True:
			num_int = random.randint(-10, 10)
			num_dec = round(random.uniform(-10, 10), 1)
			# 0이 아니고 소수점 첫째자리가 0이 아닌 수 선택
			if num_int != 0 and num_dec != 0 and int(num_dec * 10) % 10 != 0:
				break
		
		# 정수-소수 또는 소수-정수 순서 랜덤 선택
		if random.choice([True, False]):
			num1, num2 = num_int, num_dec
		else:
			num1, num2 = num_dec, num_int
		
		result = num1 - num2
		
		# LaTeX 식 구성
		expression = f"{format_with_sign(num1)} - {format_with_sign(num2, True)}"
		
		# 계산 과정 (뺄셈을 덧셈으로 변환)
		calculation = format_calculation(num1, '-', num2, result)
		
		return (
			f"\\({expression}\\)",
			f"\\({format_with_sign(result)}\\)",
			f"\\({calculation}\\)"
		)
	
	def fraction_fraction_calculation():
		"""분수-분수 계산 함수"""
		# 두 개의 랜덤 부호 분수 생성
		while True:
			fraction1 = generate_random_sign_fraction()
			fraction2 = generate_random_sign_fraction()
			if abs(fraction1.numerator) != abs(fraction2.numerator) or abs(fraction1.denominator) != abs(fraction2.denominator):
				break
		# LaTeX 식 구성
		expression = f"{format_fraction(fraction1)} - {format_fraction(fraction2, True)}"		
				
		# 통분 과정
		if fraction1.denominator == fraction2.denominator:
			common_denominator = fraction1.denominator  # 25.2.8일 1시 50분 수정 중. 통분 과정 추가 예정
			fraction1_numerator = fraction1.numerator
			fraction2_numerator = -fraction2.numerator
		else:
			common_denominator = fraction1.denominator * fraction2.denominator
			fraction1_numerator = fraction1.numerator * fraction2.denominator
			fraction2_numerator = -fraction2.numerator * fraction1.denominator
		

		neg_fraction2 = Fraction(-fraction2.numerator, fraction2.denominator)
		calculation = (
			f"{format_fraction(fraction1)} - {format_fraction(fraction2, True)} = "
			f"{format_fraction(fraction1)} + {format_fraction(neg_fraction2, True)} ="
		)
			
		
		# 분수 - 분수 계산의 경우
		if fraction1.numerator > 0 and fraction2.numerator > 0:
			# 양수 - 양수
			result_numerator = abs(fraction1.numerator*fraction2.denominator) - abs(fraction2.numerator*fraction1.denominator)
			calculation = (
				f"{expression} = "
				f"\\dfrac{{{abs(fraction1.numerator*fraction2.denominator)}}}{{{fraction1.denominator*fraction2.denominator}}} - "
				f"\\dfrac{{{abs(fraction2.numerator*fraction1.denominator)}}}{{{fraction2.denominator*fraction1.denominator}}} = "
				f"{'-' if result_numerator < 0 else ''}\\dfrac{{{abs(result_numerator)}}}{{{common_denominator}}}"
			)


		elif fraction2.numerator < 0:
			# 양수 - (-음수)
			neg_fraction2 = Fraction(abs(fraction2.numerator), fraction2.denominator)

			
			calculation += (

				f"\\dfrac{{{abs(fraction1.numerator*fraction2.denominator)}}}{{{fraction1.denominator*fraction2.denominator}}} + "
				f"\\dfrac{{{abs(fraction2.numerator*fraction1.denominator)}}}{{{fraction2.denominator*fraction1.denominator}}} = "
				f"\\dfrac{{{abs(fraction1.numerator*fraction2.denominator) + abs(fraction2.numerator*fraction1.denominator)}}}{{{common_denominator}}}"	

			)

			


		elif fraction1.numerator < 0 and fraction2.numerator < 0:
			# 음수 - (-)음수
			result_numerator = fraction1.numerator*fraction2.denominator - fraction2.numerator*fraction1.denominator
			calculation += (
				# f"{expression} = "
				f"{format_fraction(fraction1)} - {format_fraction(fraction2, True)} = 음-(-)음2"
				f"{format_fraction(fraction1)} + {format_fraction(neg_fraction2, True)} = 음-(-)음2"
				# f"{'-' if fraction1_numerator < 0 else ''}\\dfrac{{{abs(fraction1_numerator)}}}{{{common_denominator}}}"
    			# f"{'-' if fraction2_numerator < 0 else ''}\\dfrac{{{abs(fraction2_numerator)}}}{{{common_denominator}}} = "
    			# 최종 결과
				f"{'-' if (fraction1_numerator +fraction2_numerator) < 0 else ''}\\dfrac{{{abs(fraction1_numerator + fraction2_numerator)}}}{{{common_denominator}}}"
			)
		else:
			# 음수 + (-음수
			calculation += (
				f"{'-' if fraction1_numerator < 0 else ''}\\dfrac{{{abs(fraction1_numerator)}}}{{{common_denominator}}}"
				f"{'+' if fraction2_numerator < 0 else ''}(-\\dfrac{{{abs(fraction2_numerator)}}}{{{common_denominator}}}) = "
				f"{'-' if (fraction1_numerator +fraction2_numerator) < 0 else ''}\\dfrac{{{abs(fraction1_numerator + fraction2_numerator)}}}{{{common_denominator}}}"
			)


		result = Fraction(fraction1_numerator + fraction2_numerator, common_denominator)
		simplified_result = result.limit_denominator()

		if result != simplified_result:
			calculation += f" = {format_fraction(simplified_result)}"
			final_result = simplified_result
		else:
			final_result = result

		
		return (
			f"\\({expression}\\)",
			f"\\({format_fraction(final_result)}\\)",
			f"\\({calculation}\\)"
		)

	def integer_fraction_calculation():
		"""정수-분수 또는 분수-정수 뺄셈 계산 함수"""
		# 0이 아닌 정수 생성
		while True:
			num = random.randint(-10, 10)
			if num != 0:
				break
		
		# 약분되지 않는 분수 생성
		fraction = generate_random_sign_fraction()
		
		# 정수-분수 또는 분수-정수 순서 랜덤 결정
		is_integer_first = random.choice([True, False])
		
		if is_integer_first:
			# 정수 - 분수
			expression = f"{format_with_sign(num)} - {format_fraction(fraction, True)}"
			
			# 정수를 분수로 변환
			num_as_fraction = Fraction(num * fraction.denominator, fraction.denominator)
			# neg_fraction = Fraction(-fraction.numerator, fraction.denominator)
			
			if fraction.numerator < 0:
				neg_fraction = Fraction(abs(fraction.numerator), fraction.denominator)
				operation_symbol = "+"
				first_step = f"{format_fraction(num_as_fraction)} + {format_fraction(neg_fraction)}"
				# first_step = f"{format_fraction(num_as_fraction)} + \\dfrac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"
			else:
				neg_fraction = Fraction(-fraction.numerator, fraction.denominator)
				operation_symbol = "-"
				first_step = f"{format_fraction(num_as_fraction)} + ({format_fraction(neg_fraction)})"
				# first_step = f"{format_fraction(num_as_fraction)} - \\dfrac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"
	

			calculation = (
				f"{format_with_sign(num)} - {format_fraction(fraction, True)} = "
				f"{first_step} = "
				f"{'-' if num < 0 else ''}\\dfrac{{{abs(num * fraction.denominator)}}}{{{fraction.denominator}}} {operation_symbol} "
				f"\\dfrac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}} = "
				f"{format_fraction(num_as_fraction + neg_fraction)}"
			)
			
			result = num_as_fraction + neg_fraction
		else:
			# 분수 - 정수
			expression = f"{format_fraction(fraction)} - {format_with_sign(num, True)}"
			
			# 정수를 분수로 변환
			num_as_fraction = Fraction(num * fraction.denominator, fraction.denominator)
			neg_num_as_fraction = Fraction(-num * fraction.denominator, fraction.denominator)
			
			if num < 0: # 뒤의 수가 음수인 경우
				calculation = (
					f"{format_fraction(fraction)} - ({format_fraction(num_as_fraction)}) = "
					f"{format_fraction(fraction)} + {format_fraction(neg_num_as_fraction)} = "
					f"{'-' if fraction.numerator * num_as_fraction.denominator < 0 else ''}\\dfrac{{{abs(fraction.numerator * num_as_fraction.denominator)}}}{{{fraction.denominator * num_as_fraction.denominator}}} + "
					f"{'-' if neg_num_as_fraction.numerator * fraction.denominator < 0 else ''}\\dfrac{{{abs(neg_num_as_fraction.numerator * fraction.denominator)}}}{{{fraction.denominator * num_as_fraction.denominator}}} = "
					f"{format_fraction(fraction + neg_num_as_fraction)}"
				)
			else: # 뒤의 수가 양수인 경우
				calculation = (
					f"{format_fraction(fraction)} - {format_fraction(num_as_fraction)} = "
					f"{format_fraction(fraction)} + ({format_fraction(neg_num_as_fraction)}) = "
					f"{'-' if fraction.numerator * num_as_fraction.denominator < 0 else ''}\\dfrac{{{abs(fraction.numerator * num_as_fraction.denominator)}}}{{{fraction.denominator * num_as_fraction.denominator}}} + "
					f"{'-' if neg_num_as_fraction.numerator * fraction.denominator < 0 else ''}\\dfrac{{{abs(neg_num_as_fraction.numerator * fraction.denominator)}}}{{{fraction.denominator * num_as_fraction.denominator}}} = "
					f"{format_fraction(fraction + neg_num_as_fraction)}"
				)
			
			
			result = fraction + neg_num_as_fraction
		
		# 결과 약분
		simplified_result = result.limit_denominator()
		if result != simplified_result:
			calculation += f" = {format_fraction(simplified_result)}"
			result = simplified_result
		
		return (
			f"\\({expression}\\)",
			f"\\({format_fraction(result)}\\)",
			f"\\({calculation}\\)"
		)


	"""5가지 유형의 뺄셈 계산 문제를 생성하고, 결과가 가장 큰 것을 찾는 선택형 문제 생성"""
	# 5가지 유형의 계산 수행
	calculations = [
		integer_integer_calculation(),      # 정수-정수
		decimal_decimal_calculation(),      # 소수-소수
		integer_decimal_calculation(),      # 정수-소수
		fraction_fraction_calculation(),    # 분수-분수
		integer_fraction_calculation()      # 정수-분수
	]
	
	# 결과를 섞어서 보기 생성
	random.shuffle(calculations)
	
	# 문제 생성
	stem = "다음 중 계산 결과가 가장 큰 것은?\n"
	labels = ['①', '②', '③', '④', '⑤']
	
	for label, (expr, _, _) in zip(labels, calculations):
		stem += f"{label} {expr}\n"
	
	# 각 계산 결과를 숫자로 변환하여 비교
	results = []
	for _, result_str, _ in calculations:
		clean_str = (result_str.replace('\\(', '')
							  .replace('\\)', '')
							  .replace('\\dfrac', '')
							  .replace('{', '')
							  .replace('}', '')
							  .replace('\\', '')
							  .strip())
		
		# 분수 형태인 경우
		if '/' in clean_str:
			num, denom = map(int, clean_str.split('/'))
			results.append(num / denom)
		else:
			# 정수 또는 소수인 경우
			results.append(float(clean_str))
	
	# 가장 큰 값의 인덱스 찾기
	max_index = results.index(max(results))
	
	# 정답 및 해설 생성
	answer = f"(정답) {labels[max_index]}\n"
	
	comment = "(해설)\n"
	for label, (_, _, calc) in zip(labels, calculations):
		comment += f"{label} {calc}\n"
	comment += f"따라서 계산 결과가 가장 큰 것은 {labels[max_index]}이다.\n"
	
	return stem, answer, comment

'''#############################################################################

# QSNO 101222 71049 #회사에서 수정

#############################################################################'''

def intandrationalM112_Stem_07_003():
	
	def generate_non_simplifiable_fraction():
		while True:
			numerator = random.randint(1, 9)
			denominator = random.randint(2, 9)
			if math.gcd(numerator, denominator) == 1:  # 약분되지 않는 경우만 선택
				return Fraction(numerator, denominator)

	# +/- 기호가 분수 좌측으로 위치하도록 하는 함수
	def format_fraction_with_sign(numerator, denominator):
		sign = "-" if numerator < 0 else ""
		return f"{sign}\\dfrac{{{abs(numerator)}}}{{{denominator}}}"


	# 정수 - 정수 계산 함수
	def integer_integer_calculation():
		while True:
			num1 = random.randint(-10, 10)
			num2 = random.randint(-10, 10)
			if num1 != 0 and num2 != 0:  # Exclude 0 for both integers
				break
		
		correct_result = num1 - num2
		correct_result_str = str(correct_result)

		num1_str = str(num1) if num1 < 0 else str(abs(num1))
		num2_str = f"({num2})" if num2 < 0 else str(abs(num2))

		correct_expression = f"{num1_str} - {num2_str}"

		neg_num2_str = f"({-num2})" if -num2 < 0 else str(abs(-num2))
		correct_calc = f"{num1_str} - {num2_str} = {num1_str} + {neg_num2_str} = {correct_result_str}"

		incorrect_result = num1 + num2
		incorrect_result_str = str(incorrect_result)
		incorrect_calc = f"{num1_str} - {num2_str} = {incorrect_result_str}"

		return f"\\({correct_expression}\\)", f"\\({correct_result_str}\\)", f"\\({correct_calc}\\)", f"\\({incorrect_calc}\\)"


	# 소수 - 소수 계산 함수
	def decimal_decimal_calculation():
		while True:
			num1 = round(random.uniform(-10, 10), 1)
			num2 = round(random.uniform(-10, 10), 1)
			if num1 != 0 and num2 != 0 and int(num1 * 10) % 10 != 0 and int(num2 * 10) % 10 != 0:  # Ensure first decimal place isn't 0
				break
		correct_result = num1 + (-num2)
		
		correct_result_str = (
			"0" if correct_result == 0 
			else f"{int(correct_result)}" if correct_result % 1 == 0  # Handles all whole numbers
			else f"{round(correct_result, 1)}"  # Handles non-whole numbers (negative and positive)
		)
		
		num1_str = str(num1) if num1 < 0 else str(abs(num1))
		num2_str = f"(-{abs(num2)})" if num2 < 0 else str(abs(num2))

		correct_expression = f"{num1_str} - {num2_str}"

		# neg_num2 = -num2
		neg_num2_str = f"(-{abs(num2)})" if num2 > 0 else str(abs(num2))
		correct_calculation = f"{num1_str} - {num2_str} = {num1_str} + {neg_num2_str} = {correct_result_str}"

		# Incorrect calculation (using addition instead of subtraction)
		incorrect_result = num1 + num2
		incorrect_result_str = f"{round(incorrect_result, 1)}"
		incorrect_calc = f"{num1_str} - {num2_str} = {incorrect_result_str}"
		return f"\\({correct_expression}\\)", f"\\({correct_result_str}\\)", f"\\({correct_calculation}\\)", f"\\({incorrect_calc}\\)"


	#분수 계산
	def generate_random_sign_fraction():
		# Randomly generate a fraction with a random sign
		fraction = generate_non_simplifiable_fraction()
		sign = random.choice([-1, 1])
		return Fraction(sign * fraction.numerator, fraction.denominator)

	# 분수-분수 함수 계산
	
	def fraction_fraction_calculation_with_proper_parentheses_corrected():
		fraction1 = generate_random_sign_fraction()
		fraction2 = generate_random_sign_fraction()

		while abs(fraction1) == abs(fraction2):
			fraction2 = generate_random_sign_fraction()
		
		common_denominator = fraction1.denominator
		fraction1_scaled_numerator = fraction1.numerator
		fraction2_scaled_numerator = fraction2.numerator

		# Define a function to format fractions with the sign in front
		def format_fraction_with_sign(numerator, denominator, is_second_term=False):
			if numerator > 0:
				return f"\\dfrac{{{numerator}}}{{{denominator}}}"
			else:
				if is_second_term:
					return f"\\left(-\\dfrac{{{abs(numerator)}}}{{{denominator}}}\\right)"
				else:
					return f"-\\dfrac{{{abs(numerator)}}}{{{denominator}}}"

		
		# 보인 변경(2024.12.17) - 등호 우변 기호 제거
		def format_fraction_with_sign_answer(numerator, denominator):
			if numerator > 0:
				if denominator == 1:
					return f"{numerator}"
				return f"\\dfrac{{{numerator}}}{{{denominator}}}"
			else:
				if denominator == 1:
					return f"-{abs(numerator)}"
				return f"-\\dfrac{{{abs(numerator)}}}{{{denominator}}}"

		# MathJax format for fractions with parentheses
		fraction1_str = format_fraction_with_sign(fraction1.numerator, fraction1.denominator)
		fraction2_str = format_fraction_with_sign(fraction2.numerator, fraction2.denominator, is_second_term=True)		
		expression = f"{fraction1_str} - {fraction2_str}"

		# Sign conversion and negate the numerator of the second fraction
		neg_fraction2 = Fraction(-fraction2.numerator, fraction2.denominator)
		neg_fraction2_str = format_fraction_with_sign(neg_fraction2.numerator, neg_fraction2.denominator, is_second_term=True)
		
		calculation = f"{fraction1_str} + {neg_fraction2_str}"

		
		if fraction1.denominator == fraction2.denominator:
			common_denominator = fraction1.denominator
			fraction1_scaled_numerator = fraction1.numerator
			fraction2_scaled_numerator = -fraction2.numerator

		else:
			common_denominator = (fraction1.denominator * fraction2.denominator) // gcd(fraction1.denominator, fraction2.denominator)
			multiplier1 = common_denominator // fraction1.denominator
			multiplier2 = common_denominator // fraction2.denominator
			fraction1_scaled_numerator = fraction1.numerator * multiplier1
			fraction2_scaled_numerator = -fraction2.numerator * multiplier2
		

		calculation += f" = \\dfrac{{{fraction1_scaled_numerator}}}{{{common_denominator}}} + \\dfrac{{{fraction2_scaled_numerator}}}{{{common_denominator}}}"
		result_numerator = fraction1_scaled_numerator + fraction2_scaled_numerator
		result = Fraction(result_numerator, common_denominator)
		simplified_result = result.limit_denominator()

		result_str = format_fraction_with_sign_answer(result.numerator, result.denominator)
		
		if result != simplified_result:
			answer = format_fraction_with_sign_answer(simplified_result.numerator, simplified_result.denominator)
		else:
			answer = result_str

		# calculation += f" = {fraction1_str} + {neg_fraction2_str}"

		# if fraction1.denominator != fraction2.denominator:
		# 	calculation += f" = \\dfrac{{{fraction1_scaled_numerator}}}{{{common_denominator}}} + \\dfrac{{{fraction2_scaled_numerator}}}{{{common_denominator}}} = {result_str}"
		# else:
		# 	calculation += f" = {result_str}"
		
		# calculation += f" = {result_str}"
		# # Represent the fractions with the scaled numerators and common denominator
		# fraction1_new = Fraction(fraction1_scaled_numerator, common_denominator)
		# fraction2_new = Fraction(fraction2_scaled_numerator, common_denominator)

		# # Format the new fractions
		# fraction1_new_str = format_fraction_with_sign(fraction1_new.numerator, common_denominator)
		# fraction2_new_str = format_fraction_with_sign(fraction2_new.numerator, common_denominator, is_second_term=True)
		

		# # Calculation steps showing the fractions with the common denominator
		# calculation += f" = {fraction1_new_str} + {fraction2_new_str}"

		# # Perform the addition of numerators and simplify the result
		# result_numerator = fraction1_scaled_numerator + fraction2_scaled_numerator
		# result = Fraction(result_numerator, common_denominator)
		# simplified_result = result.limit_denominator()

		# # Ensure MathJax formatting for final results
		# result_str = format_fraction_with_sign_answer(result.numerator, result.denominator)

		# if result != simplified_result:
		# 	answer = format_fraction_with_sign_answer(simplified_result.numerator, simplified_result.denominator)
		# else:
		# 	answer = result_str

		# # Append the final result to the calculation string
		calculation += f" = {result_str}"

		incorrect_numerator = result_numerator + 3
		incorrect_result = Fraction(incorrect_numerator, common_denominator) 
		incorrect_result_str = f"\\dfrac{{{incorrect_result.numerator}}}{{{incorrect_result.denominator}}}" if incorrect_result.numerator >= 0 else f"\\dfrac{{{incorrect_result.numerator:+}}}{{{incorrect_result.denominator}}}"
		incorrect_calc = f"{fraction1_str} - {fraction2_str} = {incorrect_result_str}"

		return f"\\({expression}\\)", f"\\({answer}\\)", f"\\({calculation}\\)", f"\\({incorrect_calc}\\)"


	def format_integer(num):
		if num > 0:
			return str(num)
		else:
			return f"({num})"
	
	# 정수 - 분수/분수 - 정수 계산 함수 (순서 랜덤화)
	def integer_fraction_calculation_with_multiplication():
		while True:
			num1 = random.randint(-10, 10)
			if num1 != 0:  # Exclude 0 for both integers
				break
		fraction = generate_non_simplifiable_fraction()

		# 보인 변경(2024/12/06) - +/- 기호가 분수 좌측으로 위치하도록 하는 함수 (기존: +/-기호가 분자에 있었음)
		def format_fraction_with_sign(fraction):
			sign = "-" if fraction.numerator < 0 else "+"
			return f"{sign}\\dfrac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"

		# Format the fraction string
		fraction_str = format_fraction_with_sign(fraction)

		if fraction.numerator > 0:
			fraction_str = f"\\dfrac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"


		if random.choice([True, False]):
			# Integer - Fraction
			expression = f"{format_integer(num1)} - {fraction_str}"

			# Negating the fraction
			neg_fraction = Fraction(-fraction.numerator, fraction.denominator)
			neg_fraction_str = format_fraction_with_sign(neg_fraction)
			if neg_fraction.numerator > 0:
				neg_fraction_str = f"\\dfrac{{{abs(neg_fraction.numerator)}}}{{{neg_fraction.denominator}}}"
			sign_change = f"({num1:+}) + ({neg_fraction_str})"

			# Convert integer to a fraction with the same denominator and multiply the numerator
			num1_as_fraction = Fraction(num1 * fraction.denominator, fraction.denominator)  # Multiply by denominator
			num1_as_fraction_str = format_fraction_with_sign(num1_as_fraction) # 보인 변경(2024/12/06) - {format_fraction_with_sign} 사용
			fraction_addition = f"({num1_as_fraction_str}) + ({neg_fraction_str})"

			# Final result
			result = num1_as_fraction + neg_fraction
		else:
			# Fraction - Integer
			expression = f"{fraction_str} - {format_integer(num1)}"

			# Negating the integer
			neg_num1 = -num1
			neg_num1_as_fraction = Fraction(neg_num1 * fraction.denominator, fraction.denominator)
			neg_num1_as_fraction_str = format_fraction_with_sign(neg_num1_as_fraction)
			if neg_num1_as_fraction.numerator > 0:
				neg_num1_as_fraction_str = f"\\dfrac{{{abs(neg_num1_as_fraction.numerator)}}}{{{neg_num1_as_fraction.denominator}}}"
			sign_change = f"{fraction_str} + {format_integer(neg_num1)}"
			fraction_addition = f"{fraction_str} + {neg_num1_as_fraction_str}"

			# Final result
			result = fraction + neg_num1_as_fraction

		# Simplify the result
		simplified_result = result.limit_denominator()

		# Format the final result
		result_str = format_fraction_with_sign(result)

		if result.numerator > 0:
			result_str = f"\\dfrac{{{abs(result.numerator)}}}{{{result.denominator}}}"
		
		if result != simplified_result:
			simplified_result_str = format_fraction_with_sign(simplified_result)

			if simplified_result.numerator > 0:
				simplified_result_str = f"\\dfrac{{{abs(simplified_result.numerator)}}}{{{simplified_result.denominator}}}"
			answer = simplified_result_str
		else:
			answer = result_str

		# Connect all calculation steps
		calculation = f"{expression} = {sign_change} = {fraction_addition} = {result_str}"


		return f"\\({expression}\\)", f"\\({answer}\\)", f"\\({calculation}\\)"	


	


	# 문제 생성 및 해설
	expr1, res1, correct_calc1, incorrect_calc1 = integer_integer_calculation()
	expr2, res2, correct_calc2, incorrect_calc2 = decimal_decimal_calculation()
	expr3, res3, correct_calc3, incorrect_calc3 = fraction_fraction_calculation_with_proper_parentheses_corrected()
	expr4, res4, correct_calc4 = integer_fraction_calculation_with_multiplication()

	# 옳은 옵션들을 리스트로 저장
	options = [(expr1, res1, correct_calc1), (expr2, res2, correct_calc2), (expr3, res3, correct_calc3), (expr4, res4, correct_calc4)]

	# 옳지 않은 옵션 생성
	incorrect_expr1, incorrect_res1, incorrect_correct_calc1, incorrect_incorrect_calc1 = integer_integer_calculation()
	incorrect_expr2, incorrect_res2, incorrect_correct_calc2, incorrect_incorrect_calc2 = decimal_decimal_calculation()
	incorrect_expr3, incorrect_res3, incorrect_correct_calc3, incorrect_incorrect_calc3 = fraction_fraction_calculation_with_proper_parentheses_corrected()

	# 옳지 않은 옵션들 리스트로 저장
	incorrect_options = [(incorrect_expr1, incorrect_res1, incorrect_correct_calc1, incorrect_incorrect_calc1), 
						(incorrect_expr2, incorrect_res2, incorrect_correct_calc2, incorrect_incorrect_calc2), 
						(incorrect_expr3, incorrect_res3, incorrect_correct_calc3, incorrect_incorrect_calc3)]

	# 무작위로 하나의 옳지 않은 옵션 선택
	incorrect_expr, incorrect_res, correct_calc, incorrect_calc = random.choice(incorrect_options)

	# 옳지 않은 옵션을 무작위로 삽입
	random_index = random.randint(0, 4)
	options.insert(random_index, (incorrect_expr, incorrect_res, correct_calc, incorrect_calc))

	labels = ['①', '②', '③', '④', '⑤']

	# 문제 본문 생성 (옳지 않은 선지는 option[3], 나머지는 option[2])
	stem = f"다음 중 옳지 않은 것은?\n"
	for i, (label, option) in enumerate(zip(labels, options)):
		if i == random_index:
			stem += f"{label} {option[3]}\n"  # 옳지 않은 선지는 incorrect_calc 사용
		else:
			stem += f"{label} {option[0]} = {option[1]}\n"  # 옳은 선지는 correct_calc 사용

	# 옳지 않은 정답의 위치 표시
	answer = f"(정답) {labels[random_index]}\n"

	# 해설 생성 (random_index를 기반으로 옳지 않은 정답을 표시)
	comment = "(해설) "
	for i, (label, option) in enumerate(zip(labels, options)):
		comment += f"{label} {option[2]}\n"  # 옳은 계산 과정 표시

	return stem, answer, comment



#################################################################################

# QSNO 101223 71050

##################################################################################

def intandrationalM112_Stem_07_004():
	def generate_non_simplifiable_fraction():
		while True:
			numerator = random.randint(1, 9)
			denominator = random.randint(2, 9)
			if math.gcd(numerator, denominator) == 1:  
				return Fraction(numerator, denominator)
			
	
	def format_fraction_with_sign(numerator, denominator):
		sign = "-" if numerator < 0 else ""
		return f"{sign}\\dfrac{{{abs(numerator)}}}{{{denominator}}}"

	# 정수 - 정수 계산 함수
	def integer_integer_calculation():
		while True:
			num1 = random.randint(-10, 10)
			num2 = random.randint(-10, 10)
			if num1 != 0 and num2 != 0:  # Exclude 0 for both integers
				break
		
		correct_result = num1 - num2
		correct_result_str = str(correct_result)
		# correct_result_str = str(correct_result) if correct_result >= 0 else f"{correct_result:+}"
		
		num1_str = str(num1) if num1 < 0 else str(abs(num1))
		num2_str = f"({num2})" if num2 < 0 else str(abs(num2))

		expression = f"{num1_str} - {num2_str}"
		correct_expression = f"{num1_str} - {num2_str} = {correct_result_str}"


		return f"\\({expression}\\)", f'\\({correct_result_str}\\)', f"\\({correct_expression}\\)"

	# 소수 - 소수 계산 함수
	def decimal_decimal_calculation():
		while True:
			num1 = round(random.uniform(-10, 10), 1)
			num2 = round(random.uniform(-10, 10), 1)
			if num1 != 0 and num2 != 0 and int(num1 * 10) % 10 != 0 and int(num2 * 10) % 10 != 0:  # Ensure first decimal place isn't 0
				break
		correct_result = num1 + (-num2)
		# 보인 변경(2024/12/06) - 정수형 결과에 소숫점 이하 .0 삭제
		correct_result_str = (
			"0" if correct_result == 0 
			else f"{int(correct_result)}" if correct_result % 1 == 0  # Handles all whole numbers
			# else f"{round(correct_result, 1):+}" if correct_result < 0  # Handles non-whole numbers (negative and positive)
			else f"{round(correct_result, 1)}" # 보인 변경(2024.12.17) : 우변에 양수, 0 일경우 부호 생략
		)

		num1_str = str(num1) if num1 < 0 else str(abs(num1))
		num2_str = f"({num2})" if num2 < 0 else str(abs(num2))
		expression = f"{num1_str} - {num2_str}"
		correct_expression = f"{num1_str} - {num2_str} = {correct_result_str}"
		# correct_calculation = f"({num1:+}) - ({num2:+}) = ({num1:+}) + ({-num2:+}) = {correct_result_str}"



		return f"\\({expression}\\)", f"\\({correct_result_str}\\)", f"\\({correct_expression}\\)"


	#분수 계산
	def generate_random_sign_fraction():
		# Randomly generate a fraction with a random sign
		fraction = generate_non_simplifiable_fraction()
		sign = random.choice([-1, 1])
		return Fraction(sign * fraction.numerator, fraction.denominator)

	# 분수-분수 함수 계산

	def fraction_fraction_calculation_with_proper_parentheses_corrected():
		fraction1 = generate_random_sign_fraction()
		fraction2 = generate_random_sign_fraction()

		while abs(fraction1) == abs(fraction2):  # Check for both absolute and signed equality
			fraction2 = generate_random_sign_fraction()

		# Define a function to format fractions with the sign in front
		def format_fraction_with_sign(numerator, denominator):
			sign = "-" if numerator < 0 else ""
			return f"{sign}\\dfrac{{{abs(numerator)}}}{{{denominator}}}"
		
		def format_fraction_with_sign_answer(numerator, denominator):
			sign = "-" if numerator < 0 else ""
			if denominator == 1:
				return f"{sign}{abs(numerator)}"
			else :
				return f"{sign}\\dfrac{{{abs(numerator)}}}{{{denominator}}}"

		# MathJax format for fractions with parentheses
		fraction1_str = format_fraction_with_sign(fraction1.numerator, fraction1.denominator)
		fraction2_str = (f"(-\\dfrac{{{abs(fraction2.numerator)}}}{{{fraction2.denominator}}})" 
                   if fraction2.numerator < 0 
                   else f"\\dfrac{{{fraction2.numerator}}}{{{fraction2.denominator}}}")

		# Sign conversion and negate the numerator of the second fraction
		neg_fraction2_str = f"\\left({format_fraction_with_sign(-fraction2.numerator, fraction2.denominator)}\\right)"

		expression = f"{fraction1_str} - {fraction2_str}"

		#통분
		if fraction1.denominator == fraction2.denominator:
			common_denominator = fraction1.denominator
			fraction1_scaled_numerator = fraction1.numerator
			fraction2_scaled_numerator = -fraction2.numerator

		elif fraction2.denominator % fraction1.denominator == 0:
			common_denominator = fraction2.denominator
			fraction1_scaled_numerator = fraction1.numerator * (common_denominator // fraction1.denominator)
			fraction2_scaled_numerator = -fraction2.numerator * (common_denominator // fraction2.denominator)
			#fraction1_scaled_numerator = fraction1.numerator * fraction2.denominator * (common_denominator // fraction1.denominator)
			#fraction2_scaled_numerator = -fraction2.numerator

		else:
			common_denominator = (fraction1.denominator * fraction2.denominator) // gcd(fraction1.denominator, fraction2.denominator)
			fraction1_scaled_numerator = fraction1.numerator * (common_denominator // fraction1.denominator)
			fraction2_scaled_numerator = -fraction2.numerator * (common_denominator // fraction2.denominator)
			#  fraction1_scaled_numerator = fraction1.numerator * fraction2.denominator * (common_denominator // fraction1.denominator)
			# fraction2_scaled_numerator = -fraction2.numerator * fraction1.denominator * (common_denominator // fraction2.denominator)

		result_numerator = fraction1_scaled_numerator + fraction2_scaled_numerator# 보인 변경(2024/12/06) - 결과값 에러 수정
		result = Fraction(result_numerator, common_denominator)
		simplified_result = result.limit_denominator()

		# Ensure MathJax formatting for final results
		result_str = format_fraction_with_sign_answer(result.numerator, result.denominator)

		if result != simplified_result:
			simplified_result_str = format_fraction_with_sign_answer(simplified_result.numerator, simplified_result.denominator)
			answer = simplified_result_str
		else:
			answer = result_str

		# Append the final result to the calculation string
		# calculation += f" = {result_str}"
		return f"\\({expression}\\)", f"\\({answer}\\)", f"\\({expression} = {answer}\\)"


	# ##### ORIGINAL
	# # 정수 - 분수/분수 - 정수 계산 함수 (순서 랜덤화)
	def format_fraction_for_addition(fraction_str, is_second_term=False):
		if fraction_str.startswith('-') and is_second_term:
			return f"\\left({fraction_str}\\right)"
		else:
			return fraction_str

	def integer_fraction_calculation_with_multiplication():
		fraction_addition = None
		while True:
			num1 = random.randint(-10, 10)
			if num1 != 0:  # Exclude 0 for both integers
				break
		fraction = generate_non_simplifiable_fraction()

				# Define a function to format fractions with the sign in front
		def format_fraction_with_sign(numerator, denominator):
			sign = "-" if numerator < 0 else ""
			return f"{sign}\\dfrac{{{abs(numerator)}}}{{{denominator}}}"
		
		def format_fraction_with_sign_answer(numerator, denominator):
			sign = "-" if numerator < 0 else ""
			if denominator == 0:
				return f"{sign}{abs(numerator)}"
			else :
				return f"{sign}\\dfrac{{{abs(numerator)}}}{{{denominator}}}"

		# Always display '+' for positive numerators and denominators in intermediate steps
		# 보인 변경(2024/12/09) - +/- 기호가 분수 좌측 위치로 수정 (기존: 분자 옆)
		# fraction_str = f"\\frac{{{fraction.numerator:+}}}{{{fraction.denominator}}}"
		fraction_str = format_fraction_with_sign(fraction.numerator, fraction.denominator)

		if random.choice([True, False]):
			# Integer - Fraction
			num1_str = str(num1) if num1 > 0 else f"-{abs(num1)}"
			expression = f"{num1_str} - \\dfrac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"
			
			# Negating the fraction
			neg_fraction = Fraction(-fraction.numerator, fraction.denominator)
			# 보인 변경(2024/12/09) - +/- 기호가 분수 좌측 위치로 수정 (기존: 분자 옆)
			
			neg_fraction_str = format_fraction_with_sign(neg_fraction.numerator, neg_fraction.denominator)
			neg_fraction_str_with_parens = format_fraction_for_addition(neg_fraction_str, True)
			sign_change = f"{num1_str} + {neg_fraction_str_with_parens}"
			
			# Convert integer to a fraction with the same denominator and multiply the numerator
			## # 보인 변경(2024/12/06) - +/- 기호 수정 (format_fraction_with_sign이 적용 안되서 {sign} 사용 )
			num1_as_fraction = Fraction(num1 * fraction.denominator, fraction.denominator)  # Multiply by denominator
			sign = "-" if num1 * fraction.denominator < 0 else ""
			num1_as_fraction_str = f"{sign}\\dfrac{{{abs(num1 * fraction.denominator)}}}{{{fraction.denominator}}}"
			neg_fraction_str_with_parens = format_fraction_for_addition(neg_fraction_str, True)
			fraction_addition = f"{num1_as_fraction_str} + {neg_fraction_str_with_parens}"

			# Combine with the negated fraction string
			# fraction_addition = f"({num1_as_fraction_str}) + ({neg_fraction_str})"


			# Final result
			result = num1_as_fraction + neg_fraction
		else:
			# Fraction - Integer
			num1_str = f"({num1})" if num1 < 0 else str(num1)
			expression = f"{fraction_str} - {num1_str}"
			
			# Negating the integer
			neg_num1 = -num1
			neg_num1_str = f"({neg_num1})" if neg_num1 < 0 else str(neg_num1)
			sign_change = f"{fraction_str} + {neg_num1_str}"
			
			# Convert integer to a fraction with the same denominator and multiply the numerator
			## # 보인 변경(2024/12/06) - +/- 기호 수정 (format_fraction_with_sign이 적용 안되서 {sign} 사용 )
			num1_as_fraction = Fraction(neg_num1 * fraction.denominator, fraction.denominator)  # Multiply by denominator
			sign = "-" if neg_num1 * fraction.denominator < 0 else "" # 보인 변경(2024/12/06) - +/- 기호를 분수 옆으로 붙임 (기존:분자 옆에 있었음)
			num1_as_fraction_str = f"{sign}\\dfrac{{{abs(neg_num1 * fraction.denominator)}}}{{{fraction.denominator}}}"  # Show '+/-' on numerator
			fraction_addition = f"{fraction_str} + {num1_as_fraction_str}"

			
			# Final result
			result = fraction + num1_as_fraction

		simplified_result = result.limit_denominator()
		
		# Only display signs in the intermediate steps, but remove the '+' sign for positive results in the final answer
		result_str = format_fraction_with_sign(result.numerator, result.denominator)
		
		if result != simplified_result:
			# simplified_result_str = f"\\frac{{{simplified_result.numerator}}}{{{simplified_result.denominator}}}" if simplified_result.numerator > 0 else f"\\frac{{{simplified_result.numerator:+}}}{{{simplified_result.denominator}}}"
			#mine
			# sign = "0" if num1 * simplified_result.denominator >= 0 else "-"
			simplified_result_str = f"{sign}\\dfrac{{{abs(simplified_result.numerator)}}}{{{simplified_result.denominator}}}" if simplified_result.numerator > 0 else f"-\\frac{{{simplified_result.numerator}}}{{{simplified_result.denominator}}}"
			answer = simplified_result_str
		else:
			answer = result_str

		# Connect all calculation steps
		if fraction_addition :
			calculation = f"{expression} = {sign_change} = {fraction_addition} = {result_str}"
		else :
			calculation = f"{expression} = {sign_change} = {result_str}"

		return f"\\({expression}\\)", f"\\({answer}\\)", f"\\({calculation}\\)"

	# 4개의 선택지를 위한 랜덤한 식 생성
	expressions = [
		integer_integer_calculation(),  # 정수 - 정수
		decimal_decimal_calculation(),  # 소수 - 소수
		fraction_fraction_calculation_with_proper_parentheses_corrected(),  # 분수 - 분수
		# fraction_fraction_calculation_with_proper_parentheses_corrected(),  # 분수 - 분수
		integer_fraction_calculation_with_multiplication()  # 정수 - 분수/분수 - 정수
	]

	# 각 식의 결과 계산
	selected_expressions = random.sample(expressions, 4)

	# 라벨 붙이기
	labels = ['(ㄱ)', '(ㄴ)', '(ㄷ)', '(ㄹ)']
	labeled_options = list(zip(labels, selected_expressions))

	# 결과가 음수인 것 찾기
	correct_labels = [label for label, (expr, result, calc) in labeled_options if '-' in result]
	correct_labels_sorted = sorted(correct_labels)

	correct_answer = ", ".join(correct_labels_sorted)

	# 가능한 모든 선택지 생성
	possible_choices = []
	for i in range(1, 5):
		for combo in combinations(labels, i):
			choice = ", ".join(sorted(combo))
			possible_choices.append(choice)

	possible_choices = list(set(possible_choices))  # 중복 제거

	# 정답을 제외한 선택지에서 랜덤하게 선택
	if correct_answer in possible_choices:
		possible_choices.remove(correct_answer)
	random.shuffle(possible_choices)
	answer_choices_list = [correct_answer] + possible_choices[:4]
	answer_choices_list = answer_choices_list[:5]

	# 선택지를 항목 개수와 알파벳 순으로 정렬
	answer_choices_list = sorted(answer_choices_list, key=lambda x: (len(x.split(',')), x))

	# 정답 인덱스 갱신
	choices_symbols = ['①', '②', '③', '④', '⑤']
	correct_index = answer_choices_list.index(correct_answer)

	# 문제 지문 생성
	stem = "계산 결과가 음수인 것을 보기에서 모두 고른 것은?\n\n"
	text_list = [f"{label}  {expr}" for label, (expr, result, calc) in labeled_options]

	box_stem = make_box_stem(text_list, type = 1, mark_title= True, col_count=2)
	stem += insert_html_code(box_stem)

	stem += "\n\n" + "\n".join([f"{choices_symbols[idx]} {choice}" for idx, choice in enumerate(answer_choices_list)]) + "\n"

	# 정답 및 해설 생성
	answer = f"(정답) {choices_symbols[correct_index]}\n"
	comment = '(해설)\n'
	for label, (expr, result, calc) in labeled_options:
		comment += f"{label} {calc}\n"
	comment += f"\n이상에서 음수인 것은 {correct_answer}이다.\n"

	return stem, answer, comment

#############################################################################################

# QSNO 101224 71051

#############################################################################################

def intandrationalM112_Stem_07_005():    
    def generate_non_simplifiable_fraction():
        while True:
            numerator = random.randint(1, 9)
            denominator = random.randint(2, 9)
            if math.gcd(numerator, denominator) == 1:  # 약분되지 않는 경우만 선택
                return Fraction(numerator, denominator)
    
    #분수 출력 포맷 함수
    def format_fraction_with_sign(numerator, denominator):
        sign = "-" if numerator < 0 else ""
        return f"{sign}\\dfrac{{{abs(numerator)}}}{{{denominator}}}"
    
    # 정수 - 정수 계산 함수
    def integer_integer_calculation():
        while True:
            num1 = random.randint(-10, 10)
            num2 = random.randint(-10, 10)
            if num1 != 0 and num2 != 0:
                break
        num1_str = str(num1) if num1 > 0 else f"-{abs(num1)}"
        num2_str = f"({num2})" if num2 < 0 else str(num2)

        result = num1 - num2
        result_str = str(result) if result >= 0 else f"{result:+}"
        expression = f"{num1_str} - {num2_str}"
        neg_num2_str = f"({-num2})" if -num2 < 0 else str(-num2)
        calculation = f"{num1_str} - {num2_str} = {num1_str} + {neg_num2_str} = {result_str}"
        return f"\\({expression}\\)", f"{result_str}" if result >= 0 else result_str, f"\\({calculation}\\)"
    
    # 소수 - 소수 계산 함수
    def decimal_decimal_calculation():
        while True:
            num1 = round(random.uniform(-10, 10),1)
            num2 = round(random.uniform(-10, 10),1)

            print(f"num1: {num1}, num2: {num2}")

            if num1 != 0 and num2 != 0 and int(num1 * 10) % 10 != 0 and int(num2 * 10) % 10 != 0:
                break
        
        result = num1 - num2

        result_str = (
            "0" if result == 0
            else f"{int(result)}" if result % 1 == 0
            else f"{round(result, 1)}"
        )

        num1_str = str(num1) if num1 > 0 else f"-{abs(num1)}"
        num2_str = f"({num2})" if num2 < 0 else str(num2)
        expression = f"{num1_str} - {num2_str}"
        neg_num2_str = f"({-num2})" if - num2 < 0 else str(-num2)
        calculation = f"{num1_str} - {num2_str} = {num1_str} + {neg_num2_str} = {result_str}"
        return f"\\({expression}\\)", f"{result_str}" if result >= 0 else result_str, f"\\({calculation}\\)"
    
    # 분수 - 분수 계산 함수
    def generate_random_sign_fraction():
        fraction = generate_non_simplifiable_fraction()
        sign = random.choice([-1, 1])
        return Fraction(sign * fraction.numerator, fraction.denominator)
    
    def fraction_fraction_calculation_with_proper_parentheses_corrected():
        # 2 개의 랜덤 분수 생성
        fraction1 = generate_random_sign_fraction()
        fraction2 = generate_random_sign_fraction()
        
        print(f"\n=== 초기 분수 ===")
        print(f"분수1: {fraction1} ({fraction1.numerator}/{fraction1.denominator})")
        print(f"분수2: {fraction2} ({fraction2.numerator}/{fraction2.denominator})")
    
        # 두 분수의 절대값이 같으면 다시 생성
        while abs(fraction1) == abs(fraction2):
            fraction2 = generate_random_sign_fraction()
            print(f"재생성된 분수2: {fraction2}")
        
        # LaTeX 포맷팅 함수 수정
        def format_fraction_with_sign(numerator, denominator, is_first=True):
            if numerator < 0:
                if not is_first:
                    return f"(-\\dfrac{{{abs(numerator)}}}{{{denominator}}})"
                return f"-\\dfrac{{{abs(numerator)}}}{{{denominator}}}"
            return f"\\dfrac{{{numerator}}}{{{denominator}}}"
            # # 양수일 때는 괄호 없이
            # return f"\\dfrac{{{numerator}}}{{{denominator}}}"
        
        # 초기 분수 표현
        fraction1_str = format_fraction_with_sign(fraction1.numerator, fraction1.denominator)
        fraction2_str = format_fraction_with_sign(fraction2.numerator, fraction2.denominator, is_first=False)
    
        print(f"\n=== 뺄셈을 덧셈으로 변환 ===")
        # 원래 식: 두 번째 항이 음수일 때만 괄호
        original_fraction2_str = f"({fraction2})" if fraction2.numerator < 0 else str(fraction2)
        print(f"원래 식: {fraction1} - {original_fraction2_str}")
        
        # 변환 식: 음수일 때만 괄호
        converted_fraction2 = -fraction2
        converted_fraction2_str = f"({converted_fraction2})" if converted_fraction2.numerator < 0 else str(converted_fraction2)
        print(f"변환 식: {fraction1} + {converted_fraction2_str}")
    
        # 통분 및 분자 계산
        common_denominator = (fraction1.denominator * fraction2.denominator) // gcd(fraction1.denominator, fraction2.denominator)
        fraction1_scaled_numerator = fraction1.numerator * (common_denominator // fraction1.denominator)
        fraction2_scaled_numerator = fraction2.numerator * (common_denominator // fraction2.denominator)
        
        fraction1_scaled_str = format_fraction_with_sign(fraction1_scaled_numerator, common_denominator)
        fraction2_scaled_str = format_fraction_with_sign(fraction2_scaled_numerator, common_denominator, is_first=False)

        if fraction1.numerator < 0:
            fraction1_scaled_numerator = -fraction1_scaled_numerator
        if fraction2.numerator < 0:
            fraction2_scaled_numerator = -fraction2_scaled_numerator
        print(f"\n=== 통분 과정 ===")
        print(f"통분된 분모: {common_denominator}")
        print(f"통분된 분수1: {fraction1_scaled_numerator}/{common_denominator}")
        print(f"통분된 분수2(부호 변환 후): {fraction2_scaled_numerator}/{common_denominator}")
        # 덧셈 수행 (이미 부호가 바뀌었으므로 덧셈으로 처리)
        result_numerator = fraction1_scaled_numerator + fraction2_scaled_numerator
        result = Fraction(result_numerator, common_denominator)
        
        print(f"\n=== 계산 과정 ===")
        print(f"계산식: {fraction1_scaled_numerator}/{common_denominator} + {fraction2_scaled_numerator}/{common_denominator}")
        print(f"결과: {result_numerator}/{common_denominator}")
        
        simplified_result = result.limit_denominator()
        print(f"약분된 결과: {simplified_result}")
    
        # 결과 포맷팅
        result_str = format_fraction_with_sign(result.numerator, result.denominator)
        if result != simplified_result:
            simplified_result_str = format_fraction_with_sign(simplified_result.numerator, simplified_result.denominator)
            answer = simplified_result_str
        else:
            answer = result_str
        
        calculation = f"{fraction1_str} + {fraction2_str}"
        calculation_a = f"{fraction1_str} + {fraction2_str} = {fraction1_scaled_str} + {fraction2_scaled_str} = {result_str}"
        #calculation_a = f"{fraction1_str} + {fraction2_str} = \\dfrac{{{fraction1_scaled_numerator}}}{{{common_denominator}}} + \\dfrac{{{fraction2_scaled_numerator}}}{{{common_denominator}}} = {result_str}"

    
        return f"\\({calculation}\\)", f"\\({answer}\\)", f"\\({calculation_a}\\)"
    
    def integer_decimal_calculation_modified():
        while True:
            num1 = random.randint(-10, 10)
            num2 = round(random.uniform(-10, 10),1)
            print(f"\n=== 생성된 숫자 ===")
            print(f"num1(정수): {num1}")
            print(f"num2(소수): {num2}")
            
            if num1 != 0 and num2 != 0 and int(num2 * 10) % 10 != 0:
                break
    
        if random.choice([True, False]):  # 정수 - 소수 또는 소수 - 정수 순서 랜덤화
            # 정수 - 소수
            num1_str = str(num1) if num1 > 0 else f"-{abs(num1)}"
            num2_str = f"({num2})" if num2 < 0 else str(num2)
            expression = f"{num1_str} - {num2_str}"
            
            print(f"\n=== 뺄셈을 덧셈으로 변환 ===")
            print(f"원래 식: {num1} - {num2_str}")
            
            neg_num2 = -num2
            neg_num2_str = f"({neg_num2})" if neg_num2 < 0 else str(neg_num2)
            print(f"변환 식: {num1} + {neg_num2_str}")
            
            calculation = f"{num1_str} - {num2_str} = {num1_str} + {neg_num2_str}"
            result = num1 + neg_num2
        else:
            # 소수 - 정수
            num2_str = str(num2) if num2 > 0 else f"-{abs(num2)}"
            num1_str = f"({num1})" if num1 < 0 else str(num1)
            expression = f"{num2_str} - {num1_str}"
            
            print(f"\n=== 뺄셈을 덧셈으로 변환 ===")
            print(f"원래 식: {num2} - {num1_str}")
            
            neg_num1 = -num1
            neg_num1_str = f"({neg_num1})" if neg_num1 < 0 else str(neg_num1)
            print(f"변환 식: {num2} + {neg_num1_str}")
            
            calculation = f"{num2_str} - {num1_str} = {num2_str} + {neg_num1_str}"
            result = num2 + neg_num1
        
        print(f"\n=== 계산 결과 ===")
        result_str = (
            "0" if result == 0
            else f"{int(result)}" if result % 1 == 0  # 정수로 변환 가능한 경우
            else f"{round(result, 1)}"  # 소수인 경우
        )
        print(f"최종 결과: {result_str}")
    
        calculation += f" = {result_str}"
        return f"\\({expression}\\)", f"{result_str}", f"\\({calculation}\\)"
    
    def integer_fraction_calculation_with_multiplication():
        print("\n=== integer_fraction_calculation_with_multiplication 함수 시작 ===")
        try:
            while True:
                num1 = random.randint(-10, 10)
                if num1 != 0:  # 0은 제외
                    break
            print(f"\n=== 생성된 정수 ===")
            print(f"num1(정수): {num1}")

            fraction = generate_non_simplifiable_fraction()
            print(f"생성된 분수: {fraction.numerator}/{fraction.denominator}")

            def format_fraction_with_sign(numerator, denominator, is_first=True):
                sign = "-" if numerator < 0 else ""
                return f"{sign}\\dfrac{{{abs(numerator)}}}{{{denominator}}}"

            fraction_str = format_fraction_with_sign(fraction.numerator, fraction.denominator)
            
            if random.choice([True, False]):  # 정수 - 분수 또는 분수 - 정수 순서 랜덤화
                # 정수 - 분수
                print("\n=== 계산 유형: 정수 - 분수 ===")
                num1_str = str(num1) if num1 > 0 else f"-{abs(num1)}"
                expression = f"{num1_str} - {fraction_str}"
                print(f"식: {expression}")
                
                neg_fraction = Fraction(-fraction.numerator, fraction.denominator)
                print(f"부호 변환된 분수: {neg_fraction}")
                neg_fraction_str = format_fraction_with_sign(neg_fraction.numerator, neg_fraction.denominator)
                sign_change = f"{num1_str} + {neg_fraction_str}"

                # 정수를 같은 분모를 가진 분수로 변환
                num1_as_fraction = Fraction(num1 * fraction.denominator, fraction.denominator)
                print(f"분수로 변환된 정수: {num1_as_fraction}")
                num1_as_fraction_str = format_fraction_with_sign(num1_as_fraction.numerator, fraction.denominator)

                # 통분된 형태로 더하기
                fraction_addition = f"{num1_as_fraction_str} + {neg_fraction_str}"
                result = num1_as_fraction + neg_fraction
                print(f"계산 결과: {result}")
            else:
                # 분수 - 정수
                print("\n=== 계산 유형: 분수 - 정수 ===")
                num1_str = f"({num1})" if num1 < 0 else str(num1)
                expression = f"{fraction_str} - {num1_str}"
                print(f"식: {expression}")
                
                neg_num1 = -num1
                print(f"부호 변환된 정수: {neg_num1}")
                neg_num1_str = f"({neg_num1})" if neg_num1 < 0 else str(neg_num1)
                sign_change = f"{fraction_str} + {neg_num1_str}"

                # 정수를 분수로 변환 후 더하기
                num1_as_fraction = Fraction(neg_num1 * fraction.denominator, fraction.denominator)
                print(f"분수로 변환된 정수: {num1_as_fraction}")
                num1_as_fraction_str = format_fraction_with_sign(num1_as_fraction.numerator, fraction.denominator)

                fraction_addition = f"{fraction_str} + {num1_as_fraction_str}"
                result = fraction + num1_as_fraction
                print(f"계산 결과: {result}")

            simplified_result = result.limit_denominator()
            if result != simplified_result:
                print(f"약분된 결과: {simplified_result}")

            # 결과 포맷
            result_str = format_fraction_with_sign(result.numerator, result.denominator)
            simplified_result_str = format_fraction_with_sign(simplified_result.numerator, simplified_result.denominator)

            if result != simplified_result:
                answer = simplified_result_str
            else:
                answer = result_str

            # 계산 과정
            calculation = f"{expression} = {sign_change} = {fraction_addition} = {result_str}"
            print("\n=== 함수 반환값 ===")
            print(f"expression: {expression}")
            print(f"answer: {answer}")
            print(f"calculation: {calculation}")
            
            return f"\\({expression}\\)", f"\\({answer}\\)", f"\\({calculation}\\)"
            
        except Exception as e:
            print(f"에러 발생: {str(e)}")
            raise e
    def parse_fraction(fraction_str):
        try:
            cleaned = re.sub(r"\\\\\(|\\\\\)", "", fraction_str)
            cleaned = re.sub(r"\\dfrac{", "", cleaned).replace("}", "")
            
            is_negative = cleaned.startswith("-")
            
            if is_negative:
                cleaned = cleaned[1:]
            
            numerator, denominator = cleaned.split("/")
            result = int(numerator) / int(denominator)
            
            return -result if is_negative else result
        except Exception as e:
            raise ValueError(f"분수 파싱 오류: {fraction_str}")
    
    expr1, res1, calc1 = integer_integer_calculation()
    expr2, res2, calc2 = decimal_decimal_calculation()
    expr3, res3, calc3 = integer_decimal_calculation_modified()
    expr4, res4, calc4 = integer_fraction_calculation_with_multiplication()
    expr5, res5, calc5 = fraction_fraction_calculation_with_proper_parentheses_corrected()
    
	# 문제 옵션 리스트 생성
    options = [
        (expr1, res1, calc1),
        (expr2, res2, calc2),
        (expr3, res3, calc3),
        (expr4, res4, calc4),
        (expr5, res5, calc5),
    ]
    
	# 문제 순서 랜덤화
    random.shuffle(options)
    
	# 문제 본문 생성
    labels = ['①', '②', '③', '④', '⑤']
    stem = "다음 중 계산 결과가 가장 작은 것은?\n"
    for label, option in zip(labels, options):
        stem += f"{label}{option[0]}\n"
    
	# 결과 리스트 생성 및 분수 파싱 포함
    results = []
    for i, option in enumerate(options):
        try:
            if 'frac' in option[1]:
                parsed_value = parse_fraction(option[1])
                results.append((parsed_value, i))
            else:
                value = float(option[1].replace("+", ""))
                results.append((value, i))
        except ValueError as e:
            print(f"결과 처리 오류 {i+1}번째 문제: {e}")
            continue
    
	# 가장 작은 값 찾기
    min_value, min_index = min(results, key=lambda x: x[0])
    
	# 정답 및 해설 생성
    answer = f"(정답) {labels[min_index]}\n"
    comment = "(해설)\n"
    for label, option in zip(labels, options):
        comment += f"{label}{option[2]}\n"
    comment += f"따라서 계산 결과가 가장 작은 것은 {labels[min_index]}이다.\n"
    
    return stem, answer, comment





#################################################################################

# QSNO 101225 71052

#################################################################################

# 보인 변경 (24/12/11) - [메모] 수정 사항 많아서, 우선 서비스 제외
def intandrationalM112_Stem_07_006():
	def generate_random_number(existing_numbers):
		while True:
			number_type = random.choice(['integer', 'decimal', 'fraction'])

			if number_type == 'integer':
				num = random.randint(-10, 10)
				if num != 0 and num not in existing_numbers:  # Exclude 0 for both integers
					return num

			elif number_type == 'decimal':
				num = round(random.uniform(-10, 10), 1)
				if num % 1 != 0 and num not in existing_numbers:  # Ensure no decimals like 0.0, 1.0
					return num

			elif number_type == 'fraction':
				while True:
					numerator = random.randint(1, 4)  # 보인 변경(2024/12/11) - 결과값 제한 (기존: 1, 10)
					denominator = random.randint(2, 6) # 보인 변경(2024/12/11) - 결과값 제한 (기존: 1, 10)
					if math.gcd(numerator, denominator) == 1:  # 약분되지 않는 경우만 선택
						fraction_num = Fraction(numerator, denominator) * random.choice([1, -1])
						if fraction_num not in existing_numbers and fraction_num not in [Fraction(1), Fraction(0)]:
							return fraction_num

	
	def format_fraction_with_sign(numerator, denominator):
		if numerator < 0:
			return f"-\\dfrac{{{abs(numerator)}}}{{{denominator}}}"
		return f"\\dfrac{{{numerator}}}{{{denominator}}}"
	


	generated_numbers = []
	while len(generated_numbers) < 5:
		new_number = generate_random_number(generated_numbers)
		generated_numbers.append(new_number)

	sorted_numbers_list = sorted(generated_numbers)

	def format_number(num):
		if num == 0:
			return "0"  

		if isinstance(num, Fraction):
			
			if num.denominator == 1:
				return str(num.numerator)
			return format_fraction_with_sign(num.numerator, num.denominator)
			
		elif isinstance(num, float):
			return str(num)
		else:
			return str(num)
			#return f"\\left({num}\\right)"
	def format_final_calculation(expression, result):
		formatted_result = f"({result})" if isinstance(result, (int, float)) and result < 0 else str(result)
		return f"{expression} = {formatted_result}"

		

	random_numbers = [f'\\({format_number(num)}\\)' for num in generated_numbers]
	sorted_numbers_str = " \\(\\lt\\) ".join([f'\\({format_number(num)}\\)' for num in sorted_numbers_list])

	a = sorted_numbers_list[-1]
	b = sorted_numbers_list[0]

	# operations = ['a - b', 'a + b', 'a * b']
	# mine - for test
	operations = ['a + b']
	selected_operation = random.choice(operations)

	def format_result(result):
		if isinstance(result, Fraction):
			# return f"\\frac{{{result.numerator}}}{{{result.denominator}}}"
			return format_fraction_with_sign(result.numerator, result.denominator)
			
		elif isinstance(result, float):
			return f"{round(result, 1)}"
		else:
			return f"{int(result)}"



	def format_decimal_result(result):
		if result == 0:
			return "0"
		if isinstance(result, float) or isinstance(result, int):
			return f"{round(result, 1)}" if result % 1 != 0 else f"{int(result)}"
		else:
			return str(result)

	fraction_addition = ""

	if selected_operation == 'a - b' or selected_operation == 'a + b':
		if isinstance(a, float) and isinstance(b, Fraction):
			a_as_fraction = Fraction(a).limit_denominator(10)
			
			# 음수일 경우 괄호 추가
			b_str = f"({format_fraction_with_sign(b.numerator, b.denominator)})" if b.numerator < 0 else f"{format_fraction_with_sign(b.numerator, b.denominator)}"
			
			# 연산자에 따라 표현식 생성
			if selected_operation == 'a - b':
				expression = f"{a} - {b_str}"
				result = a_as_fraction - b
			else:
				expression = f"{a} + {b_str}"
				result = a_as_fraction + b

			# 중간 과정에서 부호 반영
			sign_change_b = f"({format_fraction_with_sign(b.numerator, b.denominator)})" if b.numerator < 0 else f"{format_fraction_with_sign(b.numerator, b.denominator)}"
			sign_change = f"{format_fraction_with_sign(a_as_fraction.numerator, a_as_fraction.denominator)} - {sign_change_b}" if selected_operation == 'a - b' else f"{format_fraction_with_sign(a_as_fraction.numerator, a_as_fraction.denominator)} + {sign_change_b}"			
			# 공통 분모 계산 과정
			common_denominator = a_as_fraction.denominator * b.denominator
			numerator_a = a_as_fraction.numerator * b.denominator
			numerator_b = b.numerator * a_as_fraction.denominator

			if (selected_operation == 'a - b' and numerator_b > 0) or (selected_operation == 'a + b' and numerator_b < 0):
				detailed_step = f"{format_fraction_with_sign(numerator_a, common_denominator)} - {format_fraction_with_sign(abs(numerator_b), common_denominator)}"
			else:
				detailed_step = f"{format_fraction_with_sign(numerator_a, common_denominator)} + {format_fraction_with_sign(abs(numerator_b), common_denominator)}"

			
			# if b.numerator < 0:
			# 	detailed_step = f"{format_fraction_with_sign(numerator_a, common_denominator)} - {format_fraction_with_sign(numerator_b, common_denominator)}"
			# else:
			# 	detailed_step = f"{format_fraction_with_sign(numerator_a, common_denominator)} + {format_fraction_with_sign(numerator_b, common_denominator)}"

			# detailed_step = f"\\dfrac{{{numerator_a}}}{{{common_denominator}}} + \\dfrac{{{numerator_b}}}{{{common_denominator}}}"
			
			result_str = format_fraction_with_sign(result.numerator, result.denominator)
			calculation = f"{expression} = {sign_change} = {detailed_step} = {result_str}"





		elif isinstance(a, Fraction) and isinstance(b, float):
			b_as_fraction = Fraction(b).limit_denominator(10)			
			b_str =f"{b}" if b <0 else str(b)

			if selected_operation == 'a - b':
				expression = f"{format_fraction_with_sign(a.numerator, a.denominator)} - {b_str}"
				result = a - b_as_fraction
			else:
				expression = f"{format_fraction_with_sign(a.numerator, a.denominator)} + {b_str}"
				result = a + b_as_fraction
					

			# 중간 과정에서 부호 반영
			b_mid_str = f"({format_fraction_with_sign(b_as_fraction.numerator, b_as_fraction.denominator)})" if b_as_fraction.numerator < 0 else f"{format_fraction_with_sign(b_as_fraction.numerator, b_as_fraction.denominator)}"		
			sign_change = f"{format_fraction_with_sign(a.numerator, a.denominator)} - {b_mid_str}" if selected_operation == 'a - b' else f"{format_fraction_with_sign(a.numerator, a.denominator)} + {b_mid_str}"
			
			# 공통 분모 계산 과정
			common_denominator = a.denominator * b_as_fraction.denominator
			numerator_a = a.numerator * b_as_fraction.denominator
			numerator_b = abs(b_as_fraction.numerator * a.denominator)

			# 통분된 형태 추가
			if (selected_operation == 'a - b' and b > 0) or (selected_operation == 'a + b' and b < 0):
				detailed_step = f"{format_fraction_with_sign(numerator_a, common_denominator)} - {format_fraction_with_sign(numerator_b, common_denominator)}"
			else:
				detailed_step = f"{format_fraction_with_sign(numerator_a, common_denominator)} + {format_fraction_with_sign(numerator_b, common_denominator)}"

			
			result_str = format_fraction_with_sign(result.numerator, result.denominator)			
			calculation = f"{expression} = {sign_change} = {detailed_step} = {result_str}"

		elif isinstance(a, int) and isinstance(b, Fraction):
			a_as_fraction = Fraction(a * b.denominator, b.denominator)  # 3을 5분의 15로 변환
			
			
			if selected_operation == 'a - b':
				b_str = f"({format_fraction_with_sign(b.numerator, b.denominator)})" if b.numerator < 0 else format_fraction_with_sign(b.numerator, b.denominator)
				expression = f"{a} - {b_str}"
				
				# 중간 과정에서 부호 반영
				if b.numerator < 0:
					sign_change = f"{format_fraction_with_sign(a_as_fraction.numerator, a_as_fraction.denominator)} + {format_fraction_with_sign(abs(b.numerator), b.denominator)}"
				else:
					sign_change = f"{format_fraction_with_sign(a_as_fraction.numerator, a_as_fraction.denominator)} - {format_fraction_with_sign(b.numerator, b.denominator)}"
					
			
			else:
				b_str = f"({format_fraction_with_sign(b.numerator, b.denominator)})" if b <0 else str(b)
				expression = f"{a} + {b_str}"

				if b.numerator < 0:
					sign_change = f"{format_fraction_with_sign(a_as_fraction.numerator, a_as_fraction.denominator)} - {format_fraction_with_sign(abs(b.numerator), b.denominator)}"
				else:
					sign_change = f"{format_fraction_with_sign(a_as_fraction.numerator, a_as_fraction.denominator)} + {format_fraction_with_sign(b.numerator, b.denominator)}"

				# sign_change = f"\\dfrac{{{a * b.denominator}}}{{{b.denominator}}} + \\dfrac{{{abs(b.numerator)}}}{{{b.denominator}}}"
			# expression = f"\\left({a}\\right) - \\left({format_fraction_with_sign(b.numerator, b.denominator)}\\right)"
			# fraction_addition = f"{format_fraction_with_sign(a_as_fraction.numerator, b.denominator)} + {format_fraction_with_sign(neg_fraction.numerator, neg_fraction.denominator)}"
						
			result = a_as_fraction - b if selected_operation == 'a - b' else a_as_fraction + b
			result_str = format_fraction_with_sign(result.numerator, result.denominator)
			calculation = f"{expression} = {sign_change} = {result_str}"

		elif isinstance(a, Fraction) and isinstance(b, int):
			b_as_fraction = Fraction(b * a.denominator, a.denominator)
			
			if selected_operation == 'a - b':
				b_str = f"({b})" if b <0 else str(b)
				# expression = f"{format_fraction_with_sign(a.numerator, a.denominator)} - {b_str}"
				expression = f"{format_fraction_with_sign(a.numerator, a.denominator)} - {b_str}"


				if b < 0:
					sign_change = f"{format_fraction_with_sign(a.numerator, a.denominator)} + {format_fraction_with_sign(abs(b_as_fraction.numerator), b_as_fraction.denominator)}"
				else:
					sign_change = f"{format_fraction_with_sign(a.numerator, a.denominator)} - {format_fraction_with_sign(b_as_fraction.numerator, b_as_fraction.denominator)}"
			else:
				b_str = f"({b})" if b < 0 else str(b)
				expression = f"{format_fraction_with_sign(a.numerator, a.denominator)} + {b_str}"

				if b < 0:
					sign_change = f"{format_fraction_with_sign(a.numerator, a.denominator)} - {format_fraction_with_sign(abs(b_as_fraction.numerator), b_as_fraction.denominator)}"
				else:
					sign_change = f"{format_fraction_with_sign(a.numerator, a.denominator)} + {format_fraction_with_sign(b_as_fraction.numerator, b_as_fraction.denominator)}"
			#sign_change = f"\\left(\\dfrac{{{a.numerator}}}{{{a.denominator}}}\\right) + \\left(\\dfrac{{{-b * a.denominator}}}{{{a.denominator}}}\\right)"
			result = a - b_as_fraction if selected_operation == 'a - b' else a + b_as_fraction
			result_str = format_fraction_with_sign(result.numerator, result.denominator)
			calculation = f"{expression} = {sign_change} = {result_str}"

		elif isinstance(a, Fraction) and isinstance(b, Fraction):
			numerator_a = a.numerator * b.denominator
			numerator_b = b.numerator * a.denominator
			common_denominator = a.denominator * b.denominator

			# 음수일 때 괄호 추가
			b_str = f"({format_fraction_with_sign(b.numerator, b.denominator)})" if b.numerator < 0 else f"{format_fraction_with_sign(b.numerator, b.denominator)}"

			if selected_operation == 'a - b':
				expression = f"{format_fraction_with_sign(a.numerator, a.denominator)} - {b_str}"
			else:
				expression = f"{format_fraction_with_sign(a.numerator, a.denominator)} + {b_str}"
			
			# 통분 과정에서도 음수는 괄호로 처리
			if (selected_operation == 'a - b' and b.numerator > 0) or (selected_operation == 'a + b' and b.numerator < 0):
				detailed_addition = f"{format_fraction_with_sign(numerator_a, common_denominator)} - {format_fraction_with_sign(abs(numerator_b), common_denominator)}"
			else:
				detailed_addition = f"{format_fraction_with_sign(numerator_a, common_denominator)} + {format_fraction_with_sign(numerator_b, common_denominator)}"



			# expression = f"\\dfrac{{{a.numerator}}}{{{a.denominator}}} + \\dfrac{{{b.numerator}}}{{{b.denominator}}}"
			# detailed_addition = f"\\dfrac{{{numerator_a}}}{{{common_denominator}}} + \\dfrac{{{numerator_b}}}{{{common_denominator}}}"
			result = Fraction(numerator_a + numerator_b, common_denominator)
			result_str = format_fraction_with_sign(result.numerator, result.denominator)
			calculation = f"{expression} = {detailed_addition} = {result_str}"

		else:
			if selected_operation == 'a - b':
				expression = f"{a} - {b}"
			else:
				b_str = f"({b})" if b < 0 else f"{b}"
				expression = f"{a} + {b_str}"
			result = a - b if selected_operation == 'a - b' else a + b
			result_str = format_decimal_result(result) if isinstance(a, (int, float)) and isinstance(b, (int, float)) else format_result(result)
			calculation = f"{expression} = {result_str}"
			

	elif selected_operation == 'a * b':
		expression = f"\\left({format_fraction_with_sign(a)}\\right) * \\left({format_fraction_with_sign(b)}\\right)"
		result = a * b
		result_str = format_decimal_result(result) if isinstance(a, (int, float)) and isinstance(b, (int, float)) else format_result(result)
		calculation = f"{expression} = {result_str}"




	# 보인 변경(2024.12.17) - a+b / a*b mathjax적용
	stem = f"다음 중 가장 큰 수를 \\(a\\), 가장 작은 수를 \\(b\\)라 할 때, \\({selected_operation}\\)의 값을 구하시오.\n"
	text_list = random_numbers
	# box_stem 함수 사용을 위한 placeholder
	box_stem = make_box_stem(text_list, type = 1, mark_title= True, col_count=7)
	stem += insert_html_code(box_stem)

	answer = f"(정답) \\({result_str}\\)\n"
	comment = f"(해설) {sorted_numbers_str}이므로\n\\(a = {format_number(a)}\\),  \\(b = {format_number(b)}\\)\n"

	if fraction_addition:
		comment += f"\\({selected_operation} = {expression} = {fraction_addition} = {result_str}\\)\n"

	comment += f"\\(∴ {calculation}\\)\n"

	return stem, answer, comment

####################################################################################

# QSNO 101226 71053

####################################################################################

def intandrationalM112_Stem_07_007():
	def generate_expression():
		while True:
			num1 = random.randint(-10, 10)
			num2 = random.randint(-10, 10)
			if num1 != 0 and num2 != 0:  # Exclude 0 for both integers
				break
		if num2 < 0:
			expr = f"{num1} - ({num2})"
		else:
			expr = f"{num1} - {num2}"
		result = num1 - num2
		return num1, num2, expr, result
		# expr = f"({num1:+}) - ({num2:+})"
		# result = num1 - num2
		# return num1, num2, expr, result



	# 먼저 -5인 문제 하나 생성
	correct_num1, correct_num2, correct_expr, correct_result = None, None, None, None
	while correct_result != -5:
		correct_num1, correct_num2, correct_expr, correct_result = generate_expression()

	# -5가 아닌 문제 4개 생성
	incorrect_problems = []
	while len(incorrect_problems) < 4:
		num1, num2, expr, result = generate_expression()
		if result != -5:
			incorrect_problems.append((num1, num2, expr, result))

	# 정답을 포함한 모든 문제를 섞기
	problems = incorrect_problems + [(correct_num1, correct_num2, correct_expr, correct_result)]
	random.shuffle(problems)  # 문제의 순서를 섞음

	# 보인 변경(24.12.17) : 보기 mathjax 적용
	# 보기 형식으로 출력
	options = [f"① \\( {problems[0][2]} \\)", 
			f"② \\( {problems[1][2]} \\)",
			f"③ \\( {problems[2][2]} \\)",
			f"④ \\( {problems[3][2]} \\)",
			f"⑤ \\( {problems[4][2]} \\)"]
	# 문제 스템 생성
	stem = f"다음 중 계산 결과가 \\(-5\\)인 것은?\n"
	# 문제 스템에 보기를 추가
	stem += "\n".join(options)

	# 정답 인덱스 찾기
	correct_index = problems.index((correct_num1, correct_num2, correct_expr, correct_result)) + 1
	answer = f"(정답) {'①②③④⑤'[correct_index-1]}\n"
	def format_number(n):
		return f"({n})" if n < 0 else str(abs(n))
	# 해설 작성 (부호 변환 과정 포함, 양수 처리)
	comment = "(해설) "
	for i, (num1, num2, expr, result) in enumerate(problems):
		# 부호 변환 과정 (양수일 경우 + 표시, 정답이 맞으면 그대로 계산)
		sign_conversion = f"\\({format_number(num1)} - {format_number(num2)}\\) \\(= {format_number(num1)} + {format_number(-num2)}\\) \\(= {num1 + (-num2)}\\)"
		comment += f"{['①', '②', '③', '④', '⑤'][i]} {sign_conversion}\n"
	return stem, answer, comment




########################################################################################

# QSNO 101227 71054

########################################################################################
# 보인 변경(24/12/11) - 문항 생성 에러 확인


def intandrationalM112_Stem_07_008():
	def generate_random_number(existing_numbers):
		while True:
			number_type = random.choice(['integer', 'decimal', 'fraction'])

			if number_type == 'integer':
				num = random.randint(-10, 10)
				if num != 0 and num not in existing_numbers:  # Exclude 0 for both integers
					return num

			elif number_type == 'decimal':
				num = round(random.uniform(-10, 10), 1)
				if num % 1 != 0 and num not in existing_numbers:  # Ensure no decimals like 0.0, 1.0
					return num

			elif number_type == 'fraction':
				while True:
					numerator = random.randint(1, 9)
					denominator = random.randint(2, 9)
					if math.gcd(numerator, denominator) == 1:  # Ensure no simplifiable fractions
						fraction_num = Fraction(numerator, denominator) * random.choice([1, -1])
						if fraction_num not in existing_numbers and fraction_num != Fraction(1):
							return fraction_num

	# Generate 5 random numbers
	generated_numbers = []
	while len(generated_numbers) < 5:
		new_number = generate_random_number(generated_numbers)
		generated_numbers.append(new_number)

	# Compare absolute values and sort the numbers
	sorted_numbers_list = sorted(generated_numbers, key=lambda x: abs(x))

	def format_number(num):
		if isinstance(num, Fraction):
			return f"\\frac{{{abs(num.numerator)}}}{{{num.denominator}}}" if num >= 0 else f"-\\frac{{{abs(num.numerator)}}}{{{num.denominator}}}"
		else:
			return f"{abs(num)}" if num >= 0 else f"-{abs(num)}"

	# List the absolute values for the explanation
	absolute_values_list = " < ".join([f"|{format_number(num)}|" for num in sorted_numbers_list])

	# Select the largest and smallest numbers based on absolute values
	min_val = sorted_numbers_list[0]  # Smallest based on absolute value
	max_val = sorted_numbers_list[-1]  # Largest based on absolute value

	# Calculate B - A
	result = max_val - min_val

	def format_result(result):
		if isinstance(result, Fraction):
			return f"\\frac{{{result.numerator}}}{{{result.denominator}}}"
		elif isinstance(result, float):
			return f"{round(result, 1)}"
		else:
			return f"{int(result)}"

	# Prepare the problem text and explanation
	stem = f"다음 수 중에서 절댓값이 가장 큰 수를 \\(A\\), 절댓값이 가장 작은 수를 \\(B\\)라 할 때, \\(B - A\\)의 값을 구하시오.\n"
	numbers_list = ", ".join([f"\\({format_number(num)}\\)" for num in generated_numbers])
	# box_stem = make_box_stem(numbers_list, type = 1, mark_title= True, col_count=7)
	box_stem = make_box_stem(numbers_list, type = 1, mark_title= True)
	stem += insert_html_code(box_stem)

	stem += f"\n"

	# The final result and detailed explanation
	answer = f"(정답) \\({format_result(result)}\\)\n"
	
	comment = f"(해설) \\(|{format_number(max_val)}| > {absolute_values_list} > |{format_number(min_val)}|\\) 이므로\nA = {format_number(max_val)}, B = {format_number(min_val)}\n따라서 \\(B - A = {format_number(min_val)} - {format_number(max_val)} = {format_result(result)}\\)\n"

	# answer = f"(정답) answer"
	# comment = f"(해설) comment"

	return stem, answer, comment


# QSNO 101228
# 보인 변경(2024/12/11) 
# 1. 기존 문항의 표 글씨가 흐림 -> 이유: Type 3, 표를 이미지로 생성
# 2. 수정: Type2로 문제 새로 생성함
def intandrationalM112_Stem_07_009():

	# Reference class initialization
	ref.places()  # Call the places() method to initialize the city lists

	# Use cities from the 'place_city_korea' list
	cities = random.sample(ref.place_city_korea, 5)  # Randomly select 5 cities

	# 온도를 문자열로 변환하고 양수일 경우 + 기호를 붙이며 소수점 첫째 자리가 0이면 정수로 표시하는 함수
	# 보인 변경(2024.12.17) : 0값의 경우 부호 제거
	def convert_to_str_with_sign(temp):
		if temp.is_integer():  # 소수점 첫째 자리가 0인 경우 정수로 변환
			if temp > 0:
				return f"+{int(temp)}"  # 양수일 경우
			else:
				return f"{int(temp)}"   # 음수일 경우
		else:
			if temp > 0:
				return f"+{temp:.1f}"  # 양수일 경우 소수 표시
			else:
				return f"{temp:.1f}"   # 음수일 경우 소수 표시

	def convert_to_str_with_sign_answer(temp):
		if temp.is_integer():  # 소수점 첫째 자리가 0인 경우 정수로 변환
			if temp >= 0:
				return f"{int(temp)}"  # 양수일 경우
			else:
				return f"{int(temp)}"   # 음수일 경우
		else:
			if temp >= 0:
				return f"{temp:.1f}"  # 양수일 경우 소수 표시
			else:
				return f"{temp:.1f}"   # 음수일 경우 소수 표시


	# 도시와 랜덤 기온 생성
	max_temperatures = [round(random.uniform(0, 15), 1) for _ in range(5)]
	min_temperatures = [round(random.uniform(-10, 0), 1) for _ in range(5)]

	# 도시별 일교차 계산
	temperature_differences = [max_temp - min_temp for max_temp, min_temp in zip(max_temperatures, min_temperatures)]
	max_difference_index = temperature_differences.index(max(temperature_differences))
	max_difference_city = cities[max_difference_index]

	# HTML 표 생성
	# 보인 변경(2024.12.17) - 온도 기호 조정
	table_stem = "<table style='border: 1px solid black; border-collapse: collapse; text-align: center; margin: 0 auto;'>"
	table_stem += "<tr style='background-color: lightgray;'>"
	table_stem += "<th style='padding: 5px;'>도시</th>"
	for city in cities:
		table_stem += f"<td style='padding: 5px;'>{city}</td>"
	table_stem += "</tr>"

	table_stem += "<tr>"
	table_stem += "<th style='padding: 5px;'>최고 기온 \\((°C)\\)</th>"
	for max_temp in max_temperatures:
		table_stem += f"<td style='padding: 5px;'>\\({convert_to_str_with_sign(max_temp)}\\)</td>"
	table_stem += "</tr>"

	table_stem += "<tr>"
	table_stem += "<th style='padding: 5px;'>최저 기온 \\((°C)\\)</th>"
	for min_temp in min_temperatures:
		table_stem += f"<td style='padding: 5px;'>\\({convert_to_str_with_sign(min_temp)}\\)</td>"
	table_stem += "</tr>"
	table_stem += "</table>"

	# 문제 본문
	stem = (
		"다음 표는 어느 날 5개의 도시의 최고 기온과 최저 기온을 나타낸 것이다. "
		"5개의 도시 중 일교차가 가장 큰 도시는?\n\n"
		f"{insert_html_code(table_stem)}\n"
		f"① {cities[0]}  ② {cities[1]}  ③ {cities[2]}  \n④ {cities[3]}  ⑤ {cities[4]}"
	)

	# 정답 생성
	circled_numbers = ["①", "②", "③", "④", "⑤"]
	correct_answer = circled_numbers[max_difference_index]
	answer = f"(정답) {correct_answer}"

	# 해설 생성
	comment = "(해설) \n"
	for i, city in enumerate(cities):
		comment += (
			f"{city}: \\( ({convert_to_str_with_sign(max_temperatures[i])}) - ({convert_to_str_with_sign(min_temperatures[i])}) \\)"
			f"\\( = ({convert_to_str_with_sign(max_temperatures[i])}) + ({convert_to_str_with_sign(-min_temperatures[i])}) \\) "			
			f"\\( = {convert_to_str_with_sign_answer(temperature_differences[i])} (°C)\\)\n"
		)
	comment += f"\n따라서 {max_difference_city}의 일교차가 가장 큽니다."

	return stem, answer, comment




# 문항 오류: 문항 교체 후, 검수파일 제출 시 생성하여 제출하겠습니다.
# QSNO 101229
def intandrationalM112_Stem_07_010():

	# 문제
	stem = (f"\n")
	stem += 'intandrationalM112_Stem_07_010'
	# 정답
	answer = "(정답) \n "

	# 해설
	comment = "(해설) \n "

	# 이미지 부분
	svg = "이미지 부분"

	return stem, answer, comment, svg

