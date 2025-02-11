import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import io
from Dictionary.html_function import *
import itertools
from Dictionary.reference import *
from itertools import combinations
import math
import random
from fractions import Fraction

# QSNO 105300
def coordinatesM114_Stem_11_001():
    # 기본 설정
	machines_initial  = random.randint(3, 9)  # 전체 쪽수 (100에서 300 사이의 랜덤 값)
	time_initial = random.randint(10, 20)  # 기간 (5에서 15일 사이의 랜덤 값)
	total_work = machines_initial * time_initial  # 전체 작업량 (36으로 고정)

	# x의 값은 2~6 사이에서 무작위 선택
	machines_x = random.randint(2, 6)

	# `(2)`에서 결과가 정수로 나오도록 새로운 기계 대수를 선택
	possible_new_machines = [i for i in range(2, 10) if total_work % i == 0]
	machines_new = random.choice(possible_new_machines)

	# 문제 생성
	stem= f"같은 기계 \\({machines_initial}\\)대를 \\({time_initial}\\)시간 동안 가동해야 끝나는 작업이 있다. 같은 기계 \\({machines_new}\\)대를 가동하여 이 작업을 끝내려면 몇 시간이 걸리는지 구하시오.\n"

	# 해설 및 계산
	y_calculated = total_work // machines_new  # 항상 정수 결과

	# 정답
	answer = f"(정답) \\({y_calculated}\\)시간\n"
	# 해설
	comment = f"(해설) \\({machines_initial} \\times {time_initial} = x \\times y\\) 이므로    \\(y = \\frac{{{total_work}}}{{x}}\\)\n\\(y = \\frac{{{total_work}}}{{x}}\\)에 \\(x={machines_new}\\)를 대입하면    \\(y =  \\frac{{{total_work}}}{{{machines_new}}} = {y_calculated}\\)\n따라서 \\({y_calculated}\\)시간이 걸린다.\n"


	return stem, answer, comment

# QSNO 105301
def coordinatesM114_Stem_11_002():

	# 문제 설정
	days = random.randint(5, 15)  # 기간 (5에서 15일 사이의 랜덤 값)
	multiplier = random.randint(10, 20)  # 전체 페이지 수를 결정하는 배수 (10에서 20 사이의 랜덤 값)
	total_pages = days * multiplier  # 전체 쪽수는 항상 days의 배수로 설정

	# 문제 생성
	stem = f"전체 쪽수가 \\({total_pages}\\)인 책을 하루에 \\(x\\)쪽씩 읽으면 \\(y\\)일 동안 모두 읽을 수 있다고 한다. 이 책을 \\({days}\\)일 동안 다 읽으려면 하루에 몇 쪽씩 읽어야 하는지 구하시오.\n"

	# (2) 계산
	pages_per_day = total_pages // days

	# 정답
	answer = f"(정답) \\({pages_per_day}\\)쪽\n"
	# 해설
	comment = f"(해설) \\(x \\times y = {total_pages}\\)이므로   \\(y = \\frac{{{total_pages}}}{{x}}\\)\n\\(y = \\frac{{{total_pages}}}{{x}}\\)에 \\(y = {days}\\)을 대입하면\n" \
					f"\\({days} = \\frac{{{total_pages}}}{{x}}\\)    ∴ \\(x = {pages_per_day}\\)\n" \
					f"따라서 하루에 \\({pages_per_day}\\)쪽씩 읽어야 한다.\n"

	return stem, answer, comment

# QSNO 105302
def coordinatesM114_Stem_11_003():

	while True:
		# 랜덤 값 설정
		initial_pressure = random.randint(9, 20)  # 초기 압력 (9~20 사이의 랜덤 값)
		initial_volume = random.randint(5, 12)    # 초기 부피 (5~12 사이의 랜덤 값)
		new_volume = random.randint(9, 15)        # 새로운 부피 (9~15 사이의 랜덤 값)

		# 반비례 상수 a 계산
		a = initial_pressure * initial_volume

		# 나누어 떨어지는지 확인
		if a % new_volume == 0:
			# 새로운 부피에서 압력 계산
			new_pressure = a // new_volume
			break  # 조건을 만족하면 반복 종료

	# 오답 목록 생성 (정답과 다른 값들로 구성)
	wrong_answers = [
		new_pressure + random.randint(5, 9),
		new_pressure - random.randint(1, 2),
		new_pressure * random.randint(2, 3),
		new_pressure + random.randint(1, 4)
	]

	# 객관식 선택지 생성 및 오름차순 정렬
	choices = sorted(wrong_answers + [new_pressure])

	# 정답 위치 결정
	correct_index = choices.index(new_pressure)
	answer_symbol = ["①", "②", "③", "④", "⑤"][correct_index]

	# 문제 생성
	stem = (
		f"온도가 일정할 때, 기체의 부피는 압력에 반비례한다. "
		f"부피가 \\({initial_volume}\\; \\mathrm{{cm}}^3\\)인 기체의 압력이 \\({initial_pressure}\\)기압일 때, "
		f"부피가 \\({new_volume}\\; \\mathrm{{cm}}^3\\)인 기체의 압력은? (단, 온도는 일정하다.)\n"
		f"① \\({choices[0]}\\)기압\n② \\({choices[1]}\\)기압\n③ \\({choices[2]}\\)기압\n④ \\({choices[3]}\\)기압\n⑤ \\({choices[4]}\\)기압\n"
	)

	# 정답
	answer = f"(정답) {answer_symbol}\n"

	# 해설
	comment = (
		f"(해설) 기체의 압력을 \\(x\\)기압, 부피를 \\(y\\; \\mathrm{{cm}}^3\\)라 하고\n"
		f"\\(y = \\frac{{a}}{{x}}\\) \\((a ≠ 0)\\)에 \\(x = {initial_pressure}\\), \\(y = {initial_volume}\\)를 대입하면"
		f"\\({initial_volume} = \\frac{{a}}{{{initial_pressure}}}\\)    ∴ \\(a = {a}\\)\n"
		f"∴ \\(y = \\frac{{{a}}}{{x}}\\)\n\\(y = \\frac{{{a}}}{{x}}\\)에 \\(y = {new_volume}\\)을 대입하면\n\\({new_volume} = \\frac{{{a}}}{{x}}\\)    ∴ \\(x = {new_pressure}\\)\n"
		f"따라서 기체의 압력은 \\({new_pressure}\\)기압이다.\n"
	)
	return stem, answer, comment

# QSNO 105303
def coordinatesM114_Stem_11_004():

	while True:
		# 파장의 랜덤 값 생성 (1m에서 10m 사이, 정수)
		wavelength1 = random.randint(2, 7)
		wavelength2 = random.randint(2, 7)

		# 첫 번째 파장의 진동수는 50 Hz에서 300 Hz 사이에서 랜덤 생성 (정수)
		frequency1 = random.randint(50, 400)

		# a 값 계산 (a = wavelength1 * frequency1)
		a = wavelength1 * frequency1

		# 두 번째 파장의 진동수 계산 (반비례 관계식 사용)
		if a % wavelength2 == 0:
			correct_frequency = a // wavelength2  # 정수로 계산
			break  # 조건을 만족하면 반복 종료

	# 오답 보기 생성 (정수형 오답 생성)
	choices = [correct_frequency]
	while len(choices) < 5:
		# 10 Hz에서 500 Hz 사이에서 랜덤 정수 생성
		fake_frequency = random.randint(10, 500)
		# 정답과 너무 비슷하거나 이미 존재하는 값은 제외
		if abs(fake_frequency - correct_frequency) > 5 and fake_frequency not in choices:
			choices.append(fake_frequency)

	# 보기 순서를 섞음
	random.shuffle(choices)

	# stem: 문제 생성
	stem = (
		f"속력이 일정한 음파의 진동수는 파장에 반비례한다. 파장이 \\({wavelength1}\\) \\(m\\)인 음파의 진동수가 \\({frequency1}\\) \\(Hz\\)일 때, 파장이 \\({wavelength2}\\) \\(m\\)인 음파의 진동수는?\n\n"
		f"① \\({choices[0]}\\) \\(Hz\\)   ② \\({choices[1]}\\) \\(Hz\\)   ③ \\({choices[2]}\\) \\(Hz\\)   "
		f"④ \\({choices[3]}\\) \\(Hz\\)   ⑤ \\({choices[4]}\\) \\(Hz\\)\n"
	)

	# answer: 정답 (정답이 몇 번째인지 찾음)
	correct_index = choices.index(correct_frequency) + 1
	answer = f"(정답) ①\n" if correct_index == 1 else \
				f"(정답) ②\n" if correct_index == 2 else \
				f"(정답) ③\n" if correct_index == 3 else \
				f"(정답) ④\n" if correct_index == 4 else \
				f"(정답) ⑤\n"

	# comment: 해설
	comment = (
		f"(해설) 파장이 \\(x\\) \\(m\\)인 음파의 진동수를 \\(y\\) \\(Hz\\)라 하고\n\\(y = \\frac{{a}}{{x}}\\) \\((a ≠ 0)\\)에 \\(x = {wavelength1}\\), \\(y = {frequency1}\\)을 대입하면\n"
		f"\\({frequency1} = \\frac{{a}}{{{wavelength1}}}\\)    \\(∴ a = {a}\\)\n"
		f"\\(∴ y = \\frac{{{a}}}{{x}}\\)\n"
		f"\\(y = \\frac{{{a}}}{{x}}\\)에 \\(x = {wavelength2}\\)를 대입하면\n"
		f"\\(y = \\frac{{{a}}}{{{wavelength2}}} = {correct_frequency}\\)\n따라서 음파의 진동수는 \\({correct_frequency}\\) \\(Hz\\)이다.\n"
	)

	return stem, answer, comment

# QSNO 105304
def coordinatesM114_Stem_11_005():

	# 톱니바퀴 1의 톱니 개수와 회전수 설정 (랜덤 값 생성)
	teeth1 = random.randint(20, 40)  # 톱니 개수 (20에서 40 사이)
	rotations1 = random.randint(2, 6)  # 회전수 (1에서 5 사이)

	# 톱니바퀴 2의 톱니 개수 설정 (변수로 사용)
	teeth2 = random.randint(10, 60)  # 톱니 개수 (10에서 60 사이)

	# 톱니바퀴 2의 회전수 계산
	a = teeth1 * rotations1
	correct_expression = f"y = \\frac{{{a}}}{{x}}"

	# 오답 목록 생성 (정답과 다른 값들로 구성)
	wrong_answers = [
		f"y = \\frac{{{a // 2}}}{{x}}",
		f"y = \\frac{{{a * 2}}}{{x}}",
		f"y = \\frac{{{a + random.randint(10, 20)}}}{{x}}",
		f"y = \\frac{{{a - random.randint(5, 10)}}}{{x}}"
	]

	# 객관식 선택지 생성 및 섞기
	choices = wrong_answers + [correct_expression]
	random.shuffle(choices)

	# 정답 위치 결정
	correct_index = choices.index(correct_expression)
	answer_symbol = ["①", "②", "③", "④", "⑤"][correct_index]

	# 문제 생성
	stem = (
		f"두 톱니바퀴가 서로 맞물려 회전하고 있다. "
		f"톱니가 \\({teeth1}\\)개인 톱니바퀴가 \\({rotations1}\\)번 회전할 때, "
		f"톱니가 \\(x\\)개인 다른 톱니바퀴는 \\(y\\)번 회전한다. "
		f"이때 \\(y\\)를 \\(x\\)에 대한 식으로 나타내면?\n\n"
		f"① \\({choices[0]}\\)      ② \\({choices[1]}\\)      ③ \\({choices[2]}\\)\n④ \\({choices[3]}\\)      ⑤ \\({choices[4]}\\)\n"
	)

	# 정답
	answer = f"(정답) {answer_symbol}\n"

	# 해설
	comment = (
		f"(해설) 일정한 시간 동안 맞물린 톱니의 개수는 같으므로\n"
		f"\\({teeth1} \\times {rotations1} = x \\times y\\)\n"
		f"\\(∴ y = \\frac{{{a}}}{{x}}\\)\n"
	)

	return stem, answer, comment

# QSNO 105305
def coordinatesM114_Stem_11_006():
	
	while True:
		# 랜덤 값 설정
		length = random.randint(40, 60)  # 가로 길이 (40에서 60 사이)
		width = random.randint(20, 40)   # 세로 길이 (20에서 40 사이)
		height = random.randint(10, 50)  # 높이 (10에서 50 사이)

		# 부피 계산
		volume = length * width * height
		

		# 높이가 항상 정수로 나누어 떨어지도록 조건 확인
		if volume % (length * width) == 0:
			break


	# 문제 생성
	stem = (
		f"가로의 길이가 \\({length}\\) \\(cm\\)이고 부피가 \\({volume}\\) \\(cm³\\)인 직육면체 모양의 상자를 만들려고 한다. "
		f"세로의 길이가 \\({width}\\) \\(cm\\)일 때, 상자의 높이는 몇 \\(cm\\)이어야 하는지 구하시오.\n"
	)

	# 정답
	answer = f"(정답) \\({height}\\) \\(cm\\)\n"

	# 해설
	comment = (
		f"(해설) \\( y = \\frac{{{width*height}}}{{x}} \\)에 \\( x = {width}\\)을 대입하면\n"
        f"\\( y = \\frac{{{width*height}}}{{{width}}} = {height} \\)\n"
        f"따라서, 상자의 높이는 \\({height}\\) \\(cm\\)이어야 한다."
    )


	return stem, answer, comment

# QSNO 105306
def coordinatesM114_Stem_11_007():
    while True:
        # Random values generation
        fill_rate = random.randint(8, 15)  # Amount of water filled per hour (8 to 15 tons)
        total_time_hours = random.randint(2, 4)  # Total time to fill the tank (2 to 4 hours)
        additional_time_minutes = random.choice([30, 45])  # Additional time (30, 45 minutes)
        new_fill_time_minutes = random.randint(100, 150)  # New fill time in minutes (100 to 150 minutes)

        # Total time in minutes
        total_time_minutes = total_time_hours * 60 + additional_time_minutes

        # Total volume of the tank
        total_volume = fill_rate * total_time_minutes / 60  # Total volume filled in tons

        # Calculate the required fill rate for the new time
        numerator = total_volume * new_fill_time_minutes
        denominator = total_time_minutes

        # Ensure valid integer results for required fill rate
        if denominator == 0 or numerator % denominator != 0:
            continue  # Skip if division would not yield an integer

        required_fill_rate = int(numerator // denominator)

        # Validate total_volume as an integer by rounding
        rounded_total_volume = round(total_volume)
        if abs(total_volume - rounded_total_volume) > 1e-6:
            continue  # Skip if total_volume is not effectively an integer

        total_volume = rounded_total_volume
        break  # Break the loop if all conditions are satisfied

    # Simplify the fraction
    gcd = math.gcd(new_fill_time_minutes, 60)
    simplified_numerator = new_fill_time_minutes // gcd
    simplified_denominator = 60 // gcd

    # Check if simplified denominator is 1 to display y as an integer
    if simplified_denominator == 1:
        fraction_text = f"\\({simplified_numerator}\\)"
    else:
        fraction_text = f"\\(\\frac{{{simplified_numerator}}}{{{simplified_denominator}}}\\)"

    # Handle phrasing of new fill time
    if new_fill_time_minutes % 60 == 0:
        new_fill_time_text = f"\\({new_fill_time_minutes // 60}\\)시간"
    else:
        new_fill_time_text = f"\\({new_fill_time_minutes // 60}\\)시간 \\({new_fill_time_minutes % 60}\\)분"

    # Generate answer choices
    choices = list(set([
        required_fill_rate - 1, 
        required_fill_rate, 
        required_fill_rate + 1, 
        required_fill_rate + 2, 
        required_fill_rate - 2
    ]))

    # Ensure the correct answer is in the choices
    if required_fill_rate not in choices:
        choices[random.randint(0, 4)] = required_fill_rate
    # random.shuffle(choices)

    # Find the index of the correct answer
    correct_index = choices.index(required_fill_rate)

    # Question stem
    stem = (
        f"\\(1\\)시간에 \\({fill_rate}\\)톤의 물을 넣는 속도로 물을 채우면 "
        f"\\({total_time_hours}\\)시간 \\({additional_time_minutes}\\)분 만에 가득 차는 수조관이 있다. "
        f"이 수조관에 {new_fill_time_text} 만에 물을 가득 채우려고 할 때, "
        f"\\(1\\)시간당 넣어야 하는 물의 양은?\n\n"
        f"① \\({choices[0]}\\)톤  ② \\({choices[1]}\\)톤  ③ \\({choices[2]}\\)톤  ④ \\({choices[3]}\\)톤  ⑤ \\({choices[4]}\\)톤\n"
    )

    # Correct answer
    answer = f"(정답) {['①', '②', '③', '④', '⑤'][correct_index]}\n"

    # Explanation
    comment = (
        f"(해설) \\(1\\)시간당 \\(x\\)톤의 물을 넣어 \\(y\\)시간 만에 수조관에 물을 가득 채운다고 하자.\n"
                f"이미 알고 있는 정보인 \\({total_time_hours}\\)시간 \\({additional_time_minutes}\\)분을 대입하여 공식을 만들면\n"
        f"\\(x \\times y = {fill_rate} \\times \\frac{{{total_time_minutes}}}{{60}}\\)"
        f"\\(\\therefore y = \\frac{{{total_volume}}}{{x}}\\)\n"
        f"\\(y = \\frac{{{total_volume}}}{{x}}\\)에 {new_fill_time_text}인 "
        f"\\(y = \\frac{{{new_fill_time_minutes}}}{{60}} =\\) {fraction_text}을 대입하면\n"
        f"{fraction_text} \\(= \\frac{{{total_volume}}}{{x}}\\)\n"
        f"\\(\\therefore x = {required_fill_rate}\\)\n"
        f"따라서 \\(1\\)시간당 넣어야 하는 물의 양은 \\({required_fill_rate}\\)톤이다.\n"
    )

    return stem, answer, comment


# QSNO 105307
def coordinatesM114_Stem_11_008():
	
	def to_frac(value, with_a=False):
		"""Fraction을 LaTeX의 분수 형태로 변환. 분모에 'a'를 포함할지 여부를 조절."""
		if with_a:
			return rf"\frac{{{value.numerator}}}{{{value.denominator}a}}" if value.denominator != 1 else rf"\frac{{{value.numerator}}}{{a}}"
		return rf"\frac{{{value.numerator}}}{{{value.denominator}}}" if value.denominator != 1 else str(value.numerator)

	# 1부터 6까지 숫자 중 무작위로 선택
	num1 = random.choice([1, 3, 5, 7, 9])
	num2 = random.choice([1, 3, 5, 7, 9])
	eps_value = Fraction((num2 + 2 * num1), 2)
	eps1_value = Fraction(1 * 3 * (num2 + 2 * num1), 4)
	eps2_value = Fraction(num2, 2) + Fraction(num1, 2)
	result = eps1_value - eps2_value


	# 문제 생성
	stem = (f"반비례 관계 \\(y = \\frac{{{num1}}}{{x}}\\)의 그래프에서 제\\(3\\)사분면 위의 임의의 한 점을 \\(P\\)라 하고, "
			f"반비례 관계 \\(y = -\\frac{{{num2}}}{{x}}\\)의 그래프 위의 한 점을 \\(Q\\)라 하자. "
			f"점 \\(Q\\)의 \\(x\\)좌표는 점 \\(P\\)의 \\(x\\)좌표의 \\(2\\)배일 때, \\(\\triangle OPQ\\)의 넓이를 구하시오. (단, \\(O\\)는 원점)")

	# 정답 예시
	answer = f"(정답) \\({to_frac(result)}\\)"

	# 해설 작성
	comment = (f"(해설) \n "
			f"점 \\(P\\)는 제\\(3\\)사분면 위의 점이므로 점 \\(P\\)의 \\(x\\)좌표를 \\(a\\)라 하면 \\(a \\lt 0\\)이다. \n "
			f"점 \\(P\\)의 좌표는 \\((a, \\frac{{{num1}}}{{a}})\\)이고 점 \\(Q\\)의 좌표는 \\((2a, -\\frac{{{num2}}}{{2a}})\\)이다. \n "
			f"\\(\\triangle OPQ =\\)"
			f"\\(\\frac{{1}}{{2}} \\times (-2a - a) \\times ( -\\frac{{{num2}}}{{2a}} - \\frac{{{num1}}}{{a}})\\)\n "
			f"\\(-\\frac{{1}}{{2}} \\times (-2a) \\times (-\\frac{{{num2}}}{{2a}}) -\\frac{{1}}{{2}} \\times (-a) \\times (-\\frac{{{num1}}}{{a}})\\)\n"
			f"=\\(\\frac{{1}}{{2}} \\times (-3a) \\times (-{to_frac(eps_value, with_a=True)}) - \\frac{{{num2}}}{{2}} - \\frac{{{num1}}}{{2}}\\)\n"
			f"= \\({to_frac(eps1_value)} - {to_frac(eps2_value)} = {to_frac(result)}\\)")
	return stem, answer, comment