import random
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from Dictionary.html_function import *
from Dictionary.reference import Reference, answer_dict
from fractions import Fraction
from math import gcd
import io
import re
from itertools import groupby


html_img_url_demo = "https://aig.boinit.com:8080/resources/img"
html_img_url = html_img_url


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

# QSNO 105280
def coordinatesM114_Stem_10_001():
	# 틀린 것
	incorrect_conditions = {
		'\\(y\\)는 \\(x\\)에 정비례한다.': '\\(y\\)는 \\(x\\)에 반비례한다.',
		'\\(x\\)의 값이 \\(4\\)일 때, \\(y\\)의 값은 \\(\\frac{1}{4}\\)이다.': '\\(x = 4\\)일 때, \\(y = \\frac{2}{4} = \\frac{1}{2}\\)',
		'\\(x\\)가 증가하면 \\(y\\)도 증가한다.': '\\(x\\)가 증가하면 \\(y\\)는 감소한다.',
		'\\(x\\)가 감소하면 \\(y\\)도 감소한다.': '\\(x\\)가 감소하면 \\(y\\)는 증가한다.',
	}

	# 옳은 것
	correct_conditions = [
		'\\(y\\)는 \\(x\\)에 반비례한다.',
		'\\(x\\)가 증가하면 \\(y\\)는 감소한다.',
		'\\(x\\)가 감소하면 \\(y\\)는 증가한다.',
		'\\(x\\)와 \\(y\\)의 곱은 항상 2이다.',
		'\\(x\\)의 값이 \\(2\\)배가 되면 \\(y\\)의 값은 \\(\\frac{1}{2}\\)배가 된다.'
	]


	# 중복되지 않도록 올바른 선택지 필터링
	filtered_correct_conditions = [
		condition for condition in correct_conditions
		if condition not in incorrect_conditions.values()
	]

	# 옳은 조건에서 1개 이상, 최대 2개 선택
	num_correct = random.randint(1, 2)
	selected_correct = random.sample(filtered_correct_conditions, k=num_correct)

	# 틀린 조건에서 3 - num_correct 만큼 선택
	selected_incorrect = random.sample(list(incorrect_conditions.keys()), k=3 - num_correct)

	# 선택된 문장들 섞기
	all_conditions = selected_incorrect + selected_correct
	random.shuffle(all_conditions)

	# 보기 생성
	text_list = []
	markers = ["(ㄱ)", "(ㄴ)", "(ㄷ)"]
	for i, condition in enumerate(all_conditions):
		text_list.append(f"{markers[i]} {condition}\n")

	# 문제 생성
	stem = "\\(y = \\frac{2}{x}\\)에 대한 설명으로 옳은 것을 보기에서 모두 고르시오.\n"

	# box_stem 생성 (HTML 변환 함수 사용)
	box_stem = make_box_stem(text_list, type=1, mark_title=True, col_count=1)
	stem += insert_html_code(box_stem)

	# 정답 생성
    # 정답 생성
	correct_answers = [markers[i] for i, condition in enumerate(all_conditions) if condition in selected_correct]
	answer = "(정답) " + ", ".join(correct_answers) + "\n"

	# 해설 생성 (틀린 경우에만 추가)
	comment_list = [
		f"({['ㄱ', 'ㄴ', 'ㄷ'][i]}) {incorrect_conditions[condition]}\n"
		for i, condition in enumerate(all_conditions) if condition in incorrect_conditions
	]
	comment = "(해설) " + ''.join(comment_list) if comment_list else ""
	comment += f"이상에서 옳은 것은 {', '.join(correct_answers)}이다."

	
	return stem, answer, comment

# QSNO 105281
def coordinatesM114_Stem_10_002():
	# 객관식 문제 번호
	answer_dict = {
		0: "①",
		1: "②",
		2: "③",
		3: "④",
		4: "⑤"
	}

	# 랜덤한 정수 x1 선택
	x1 = random.choice(list(range(2, 21)))
	
	# y1은 항상 정수 (1~10 중 선택)
	y1_candidates = list(range(2, 11))
	y1 = random.choice(y1_candidates)
	
	# 반비례 상수 a 계산 (항상 정수)
	a = x1 * y1

	# a의 약수 중에서 y1이 아닌 값만 선택
	y2_candidates = [y for y in range(1, 21) if a % y == 0 and y != y1]

	y2 = random.choice(y2_candidates)

	# x2를 계산하여 항상 정수로 설정
	x2 = a // y2  # 나눗셈 결과가 정수여야 하므로 정수 나눗셈(//) 사용

	# 정답 계산 (항상 정수)
	correct_answer = y2

	# 오답 선택지 생성 (정수만 포함)
	choices = {correct_answer}
	while len(choices) < 5:
		fake_y2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
		if fake_y2 != correct_answer:
			choices.add(fake_y2)

	choices = list(choices)
	# 선택지를 오름차순으로 정렬
	choices = sorted(choices)

	# 문제 출력 (MathJax 적용)
	stem = f"\\(y\\)가 \\(x\\)에 반비례하고 \\(x = {x1}\\)일 때 \\(y = {y1}\\)이다. " \
		f"\\(x = {x2}\\)일 때 \\(y\\)의 값은?\n\n"

	for idx, choice in enumerate(choices):
		stem += f"{answer_dict[idx]} \\({choice}\\)\n"

	# 정답 찾기
	correct_index = choices.index(correct_answer)

	# 정답 출력
	answer = f"(정답) {answer_dict[correct_index]}\n"

	# 해설 출력 (MathJax 적용)
	comment = "(해설)\n"
	comment += f"\\( y = \\frac{{a}}{{x}} \\) (\\( a \\neq 0 \\)) 라 하고 \\( x = {x1}, y = {y1} \\)를 대입하면\n\n"
	comment += f"\\( {y1} = \\frac{{a}}{{{x1}}} \\)  ∴ \\( a = {a} \\)\n\n"
	comment += f"따라서 \\( y = \\frac{{{a}}}{{x}} \\) 이므로 \\( x = {x2} \\)일 때,\n\n"
	comment += f"\\( y = \\frac{{{a}}}{{{x2}}} = {correct_answer} \\)\n"

	return stem, answer, comment


# QSNO 105282
def coordinatesM114_Stem_10_003():
	"""
	y가 x에 반비례하는 문제를 랜덤하게 생성하며, 항상 5개의 선택지(①~⑤)를 제공합니다.
	"""
	# 올바른 선택지와 해설
	correct_condition = {
		'소금 \\(10\;g\\)이 들어 있는 소금물 \\(x\;g\\)의 농도 \\(y\;%\\)': (
			'\\( (소금물의 농도) = \\frac{\\text{소금의 양}}{\\text{소금물의 양}} \\times 100(\\%) \\)이므로\n'
			'\\( y = \\frac{10}{x} \\times 100 = \\frac{1000}{x} \\)\n'
		),
		'\\(36\;cm\\)인 끈을 \\(x\\)개로 나누었을 때 나뉜 끈 한 개의 길이 \\(y\;cm\\)': (
			'\\( (끈 한 개의 길이) = \\frac{\\text{전체 끈의 길이}}{\\text{끈의 개수}} \\)이므로\n'
			'\\( y = \\frac{36}{x} \\)\n'
			),
		'넓이가 \\(10\; \\text{cm}^2\\)인 마름모의 두 대각선의 길이가 \\(x\; \\text{cm}^2,\;y\; \\text{cm}^2\\)': (
		'\\( \\frac{1}{2}xy = 10 \\)이므로\n'
		'\\( y = \\frac{20}{x} \\)\n'
)
	}
	
	# 틀린 선택지와 해설
	incorrect_conditions = {
		'한 변의 길이가 \\(x\;cm\\)인 정사각형의 둘레의 길이 \\(y\;cm\\)': '\\( y\;=\;4x \\)',
		'하루 \\(24\\)시간 중 깨어 있는 시간 \\(x\\)시간과 잠을 자는 시간 \\(y\\)시간': '\\( y\;=\;24\;-\;x \\)',
		'초속 \\(3\;m\\)로 \\(x\\)초 동안 움직인 거리 \\(y\;m\\)': '\\( y\;=\;3x \\)',
		'\\(1\\)개에 \\(800\\)원인 쿠키를 사고 \\(5000\\)원을 냈을 때, 거스름돈 \\(y\\)원': '\\( y\;=\;5000\;-\;800x \\)',
		'\\(1\\)개에 \\(300\;g\\)인 컵 \\(x\\)개의 무게 \\(y\;g\\)': "\\(y\;=\;300x\\)"
	}
	# 랜덤으로 정답 선택
	correct_key, correct_explanation = random.choice(list(correct_condition.items()))

	# 모든 선택지를 준비
	all_choices = [*incorrect_conditions.keys()]  # 틀린 선택지 리스트
	random.shuffle(all_choices)  # 틀린 선택지를 섞음

	# 항상 올바른 선택지를 포함하도록 설정
	all_choices = all_choices[:4]  # 틀린 선택지 4개 선택
	all_choices.append(correct_key)  # 정답 추가
	random.shuffle(all_choices)  # 최종 선택지 섞기

	# 선택지 번호 매기기 (①, ②, ③, ④, ⑤)
	choices_with_numbers = [f"{num} {choice}" for num, choice in zip(['①', '②', '③', '④', '⑤'], all_choices)]

	# 문제 생성
	stem = "다음 중 \\( y \\)가 \\( x \\)에 반비례하는 것은?\n" + "\n".join(choices_with_numbers)

	# 정답 생성 (선택지 번호만 표시)
	correct_choice_index = all_choices.index(correct_key)
	answer = f"(정답) {['①', '②', '③', '④', '⑤'][correct_choice_index]}"

	# 해설 생성 (선택지 번호와 해설만 표시)
	comment = "(해설)"
	for idx, choice in enumerate(all_choices):
		if choice == correct_key:
			comment += f"\n{['①', '②', '③', '④', '⑤'][idx]} {correct_explanation}"
		else:
			comment += f"\n{['①', '②', '③', '④', '⑤'][idx]} {incorrect_conditions[choice]}"
	comment += f"\n따라서 \\(y\\)가 \\(x\\)에 반비례하는 것은 {['①', '②', '③', '④', '⑤'][correct_choice_index]}이다."

	return stem, answer, comment

# QSNO 105283
def coordinatesM114_Stem_10_004():
	# 반비례 관계 상수 및 변수 설정
	while True:
		x1 = random.randint(3, 10)  # 첫 번째 x 값
		y1 = random.randint(-20, -2)  # 첫 번째 y 값 (항상 정수)
		a = x1 * y1  # 반비례 관계 상수 a 계산
		
		# y1과 a가 0이 아니도록 보장
		if y1 != 0 and a != 0:
			break

	# x2가 x1과 다른 값을 가지도록 설정
	while True:
		x2 = random.randint(2, 10)
		if x2 != x1:
			y2 = a // x2  # y2도 항상 정수로 유지
			if y2 != 0:
				break

	# 약분을 위한 최대공약수 계산
	gcd = math.gcd(abs(a), x2)
	simplified_a = abs(a) // gcd  # 절댓값 사용
	simplified_x2 = x2 // gcd
	sign = "-" if a < 0 else ""  # 부호 결정

	answer = '(정답)'
	# 분모가 1인 경우 정수로 처리
	if simplified_x2 == 1:
		answer += f"\\({sign}{simplified_a}\\)"
		answer_expression = f"\\(y = {sign}{simplified_a}\\)"
	elif gcd == 1:  # 약분이 필요 없는 경우
		answer += f"\\({sign}\\frac{{{abs(a)}}}{{{x2}}}\\)"
		answer_expression = f"\\(y = {sign}\\frac{{{abs(a)}}}{{{x2}}}\\)"
	else:  # 약분이 필요한 경우
		answer += f"\\({sign}\\frac{{{simplified_a}}}{{{simplified_x2}}}\\)"
		answer_expression = f"\\(y = {sign}\\frac{{{abs(a)}}}{{{x2}}} = {sign}\\frac{{{simplified_a}}}{{{simplified_x2}}}\\)"

	# 문제 생성
	stem = (
		f"\\(x\\)의 값이 \\(2\\)배, \\(3\\)배, \\(4\\)배, ...가 될 때 \\(y\\)의 값은 \\(\\frac{{1}}{{2}}\\), "
		f"\\(\\frac{{1}}{{3}}\\), \\(\\frac{{1}}{{4}}\\), ...가 되고, "
		f"\\(x={x1}\\)일 때 \\(y={y1}\\)입니다. \\(x={x2}\\)일 때 \\(y\\)의 값을 구하세요."
	)


	# 해설 작성 (MathJax 포맷)
	comment = '(해설) '
	comment += (
		f"\\(y\\)가 \\(x\\)에 반비례하므로 \\(y = \\frac{{a}}{{x}}\\) \\((a \\neq 0)\\)라고 하고 \\(x = {x1}\\),\n"
		f"\\(y = {y1}\\)를 대입하면\n"
		f"\\({y1} = \\frac{{a}}{{{x1}}} \\therefore a = {a}\\)\n"
		f"\\(\\therefore y = \\frac{{{a}}}{{x}}\\)\n\n"
		f"\\(y = \\frac{{{a}}}{{x}}\\)에 \\(x = {x2}\\)를 대입하면\n"
		f"{answer_expression}"
	)
	return stem, answer, comment

# QSNO 105284
def coordinatesM114_Stem_10_005():

	# 랜덤한 x와 y 생성 (약분되지 않도록 설정)
	while True:
		x_value = random.randint(2, 10)  # x는 2부터 10 사이의 랜덤 정수
		y_value = random.randint(2, 10)  # y는 2부터 10 사이의 랜덤 정수
		if math.gcd(x_value, y_value) == 1:  # x와 y가 서로소(약분되지 않는 경우)
			break

	# a 값 계산
	a_value = x_value * y_value

	# 정답과 오답 생성
	correct_answer = f"\\(y = \\frac{{{a_value}}}{{x}}\\)"
	wrong_answers = [
		f"\\(y = \\frac{{{y_value}}}{{x}}\\)",  # y 값만 사용한 오답
		f"\\(y = \\frac{{{x_value}}}{{x}}\\)",  # x 값만 사용한 오답
		f"\\(y = \\frac{{{random.randint(1, 10)}}}{{x}}\\)",  # 랜덤 오답 2
		f"\\(y = \\frac{{{x_value}}}{{{y_value}}}x\\)",  # 랜덤 오답 3
		f"\\(y = \\frac{{{y_value}}}{{{x_value}}}x\\)",  # 랜덤 오답 4
		f"\\(y = \\frac{{x}}{{{a_value}}}\\)"  # 잘못된 반비례 오답
	]

	# 선택지 생성 및 섞기
	all_choices = [correct_answer] + wrong_answers
	random.shuffle(all_choices)  # 섞기
	choices = all_choices[:5]  # 상위 5개만 선택

	# 정답이 선택지에 포함되지 않은 경우 예외 처리
	if correct_answer not in choices:
		choices[-1] = correct_answer  # 마지막 선택지에 정답 추가

	random.shuffle(choices)  # 다시 섞기
	correct_index = choices.index(correct_answer)

	# 문제
	stem = "\n"
	stem += f"\\(y\\)가 \\(x\\)에 반비례하고 \\(x={x_value}\\)일 때 \\(y={y_value}\\)이다. 이때 \\(y\\)를 \\(x\\)에 대한 식으로 나타내면?\n"
	for i, choice in enumerate(choices):
		stem += f"{['①', '②', '③', '④', '⑤'][i]} {choice}\n"

	# 정답
	answer = '(정답) '
	answer += f"{['①', '②', '③', '④', '⑤'][correct_index]}"

	# 해설
	comment = "(해설)\n"
	comment += f"\\(y = \\frac{{a}}{{x}} \\quad (a \\neq 0)\\)라 하고 \\(x={x_value}\\), \\(y={y_value}\\)를 대입하면:\n"
	comment += f"\\({y_value} = \\frac{{a}}{{{x_value}}} \\quad \\therefore \\quad a = {x_value} \\times {y_value} = {a_value}\\)\n"
	comment += f"\\(\\therefore \\quad y = \\frac{{{a_value}}}{{x}}\\)\n"
	return stem, answer, comment


# QSNO 105285
def coordinatesM114_Stem_10_006():

	# 랜덤으로 1번 또는 2번 문제 선택
	question_type = random.choice([1, 2])

	# 랜덤한 정수 a 생성
	a_value = random.randint(1, 30)  # 1부터 30 사이의 정수

	stem = "다음 반비례 관계의 그래프가 지나는 사분면을 모두 말하시오.\n"

	if question_type == 1:
		# 1번 문제: 음수 계수
		equation = f"\\(y = -\\frac{{{a_value}}}{{x}}\\)"
		answer = "(정답) 제\\(2\\)사분면, 제\\(4\\)사분면"

	else:
		# 2번 문제: 양수 계수
		equation = f"\\(y = \\frac{{{a_value}}}{{x}}\\)"
		answer = "(정답) 제\\(1\\)사분면, 제\\(3\\)사분면"

	# 문제
	stem += f"{equation}\n"

	comment = '(해설) 해설 없음'

	return stem, answer, comment


# QSNO 105286
def coordinatesM114_Stem_10_007():
	while True:  # 적합한 random_coefficient를 찾을 때까지 반복
		random_coefficient = random.randint(1, 20)  # 반비례 상수 (4~20 사이의 정수)

		# 1. 약수 구하기
		divisors = [i for i in range(2, random_coefficient + 1) if random_coefficient % i == 0]

		# 2. 약수 중 \(x \neq y\)와 \(y \neq 1\) 조건을 만족하는 조합이 있는지 확인
		valid_divisors = [x for x in divisors if x != random_coefficient // x and random_coefficient // x != 1]
		if valid_divisors:  # 조건을 만족하는 약수가 있다면 루프를 종료
			break

	# 3. \(x\)와 \(y\) 생성
	x = random.choice(valid_divisors)
	y = random_coefficient // x

	# 4. 잘못된 (wrong_x, wrong_y) 생성
	while True:
		wrong_x = random.randint(2, random_coefficient + 5)
		wrong_y = random.randint(2, random_coefficient + 5)
		if wrong_x * wrong_y != random_coefficient and wrong_x != wrong_y:
			break




	# 옳은 선택지와 틀린 선택지 구성
	correct_statements = {
		"원점을 지나지 않는다.": "",
		f"점 \\(({x}, {y})\\)를 지난다.": f"\\( y = \\frac{{{random_coefficient}}}{{x}} \\)에 \\(x = {x}, y = {y}\\)를 대입하면 \\({y} = \\frac{{{random_coefficient}}}{{{x}}}\\)",
		f"제\\(1\\)사분면과 제\\(3\\)사분면을 지난다.": "",
		f"\\(x\\)축, \\(y\\)축과 만나지 않는다.": "",
		f"\\(a > 0\\)일 때, \\(a\\)의 값이 작을수록 좌표축에 가까워진다.": '',
		f"\\(a &lt;0\\)일 때, \\(a\\)의 값이 클수록 좌표축에 가까워진다.":''


	}

	# 틀린 선택지 구성
	incorrect_statements = {
		f"\\(x &lt; 0\\)일 때, \\(x\\)의 값이 증가하면 \\(y\\)의 값도 증가한다.": f"\\(x &lt; 0\\)일 때, \\(x\\)의 값이 증가하면 \\(y\\)의 값은 감소한다.",
		"원점을 지난다": "원점을 지나지 않는다.",
		f"점 \\(({wrong_x}, {wrong_y})\\)를 지난다.": f"\\( y = \\frac{{{random_coefficient}}}{{x}} \\)에 \\(x = {wrong_x}, y = {wrong_y}\\)를 대입하면 \\({wrong_y} \\neq \\frac{{{random_coefficient}}}{{{wrong_x}}}\\)",
		f"제\\(2\\)사분면과 제\\(4\\)사분면을 지난다.": f"제\\(1\\)사분면과 제\\(3\\)사분면을 지난다.",

	}
	# 무작위로 4개의 옳은 선택지 선택
	selected_correct_choices = random.sample(list(correct_statements.keys()), 4)

	# 무작위로 1개의 틀린 선택지 선택
	incorrect_statement = random.choice(list(incorrect_statements.keys()))

	# 동일한 해설 처리: 선택된 `incorrect_statement`의 해설이 `correct_statements`의 해설과 동일한 경우 다시 선택
	while incorrect_statements[incorrect_statement] in correct_statements.values():
		incorrect_statement = random.choice(list(incorrect_statements.keys()))

	# 선택지 생성
	all_choices = selected_correct_choices + [incorrect_statement]

	# 선택지를 무작위로 섞기
	random.shuffle(all_choices)

	# 원각 기호로 선택지 매핑
	answer_symbols = ["①", "②", "③", "④", "⑤"]
	choices_with_symbols = {
		answer_symbols[i]: all_choices[i] for i in range(len(all_choices))
	}

	# 정답 찾기
	correct_symbol = [
		symbol for symbol, statement in choices_with_symbols.items()
		if statement == incorrect_statement
	][0]

	# 문제 출력
	stem = f"다음 중 반비례 관계 \\( y = \\frac{{{random_coefficient}}}{{x}} \\)의 그래프에 대한 설명으로 옳지 않은 것은?\n"
	for symbol, statement in choices_with_symbols.items():
		stem += f"{symbol} {statement}\n"

	# 정답 출력
	answer = f"(정답) {correct_symbol}"

	# 해설 생성
	comment = "(해설)\n"
	for symbol, statement in choices_with_symbols.items():
		# 해설이 있는 항목만 포함
		if statement in correct_statements and correct_statements[statement]:
			comment += f"{symbol} {correct_statements[statement]}\n"
		elif statement == incorrect_statement:
			comment += f"{symbol} {incorrect_statements[statement]}\n"


	return stem, answer, comment



# QSNO 105287
def coordinatesM114_Stem_10_008():

	# 랜덤으로 \( x > 0 \) 또는 \( x < 0 \) 조건 선택
	condition = random.choice(["x > 0", "x &lt; 0"])

	# 조건에 따른 그래프 사분면 계산
	if condition == "x > 0":
		stem = f"\\( x > 0 \\)일 때, 반비례 관계 \\( y = -\\frac{{5}}{{x}} \\)의 그래프가 지나는 사분면을 구하세요."
		comment = (
			f"(해설) "
			f"반비례 관계 \\( y = -\\frac{{5}}{{x}} \\)의 그래프는 제\\(2\\)사분면과 제\\(4\\)사분면을 지나는 한 쌍의 곡선이므로\n"
			f"\\( x > 0 \\)일 때 \\( y = -\\frac{{5}}{{x}} \\)의 그래프는 제4사분면을 지난다."
		)
		answer = f"(정답) 제\\(4\\)사분면"
	else:
		stem = f"\\( x &lt; 0 \\)일 때, 반비례 관계 \\( y = -\\frac{{5}}{{x}} \\)의 그래프가 지나는 사분면을 구하세요."
		comment = (
			f"(해설) "
			f"반비례 관계 \\( y = -\\frac{{5}}{{x}} \\)의 그래프는 제\\(2\\)사분면과 제\\(4\\)사분면을 지나는 한 쌍의 곡선이므로\n"
			f"\\( x &lt; 0 \\)일 때 \\( y = -\\frac{{5}}{{x}} \\)의 그래프는 제\\(2\\)사분면을 지난다."
		)
		answer = f"(정답)제\\(2\\)사분면"


	return stem, answer, comment

# QSNO 105288
def coordinatesM114_Stem_10_009():

	"""
	랜덤 숫자를 사용하여 반비례 관계 객관식 문제와 해설을 생성합니다.
	"""
	# 계수 생성 (중복 없는 정수 및 분수 포함)
	coefficients = set()
	while len(coefficients) < 5:
		if random.random() < 0.5:  # 50% 확률로 분수 추가
			numerator = random.randint(1, 10)  # 분자의 범위
			denominator = random.randint(2, 10)  # 분모의 범위
			coeff = Fraction(numerator, denominator).limit_denominator()  # 약분
			if random.random() < 0.5:  # 50% 확률로 음수화
				coeff = -coeff
		else:
			coeff = random.randint(-10, 10)  # 정수 계수
		if coeff != 0:  # 0 제외
			coefficients.add(coeff)

	coefficients = list(coefficients)  # 집합을 리스트로 변환

	# 절대값 기준으로 정답 찾기
	correct_answer = min(coefficients, key=abs)

	# 수식 표현 형식 정의
	def format_equation(coeff):
		if isinstance(coeff, Fraction):
			if coeff.denominator == 1:  # 분모가 1인 경우 정수로 표현
				return f"\\(y = \\frac{{{coeff.numerator}}}{{x}}\\)"
			else:
				# 분수 형태 (음수의 경우 마이너스를 분수 앞에 배치)
				if coeff < 0:
					return f"\\(y = -\\frac{{{abs(coeff.numerator)}}}{{{coeff.denominator}x}}\\)"
				else:
					return f"\\(y = \\frac{{{coeff.numerator}}}{{{coeff.denominator}x}}\\)"
		else:
			if coeff < 0:
				return f"\\(y = -\\frac{{{abs(coeff)}}}{{x}}\\)"
			else:
			# 정수 형태
				return f"\\(y = \\frac{{{coeff}}}{{x}}\\)"


	# 보기 생성
	choices = [format_equation(coeff) for coeff in coefficients]

	# 보기 순서 랜덤 섞기
	random.shuffle(choices)
	correct_index = choices.index(format_equation(correct_answer))

	# 객관식 번호 붙이기
	numbered_choices = [f"{answer_dict[idx]} {choice}" for idx, choice in enumerate(choices)]

	# 문제 출력
	stem = f"다음 반비례 관계의 그래프 중 좌표축에 가장 가까운 것은?\n"
	for choice in numbered_choices:
		stem += f"{choice}\n"

	answer = f"(정답) {answer_dict[correct_index]}"

	# 해설 작성
	sorted_coefficients = sorted(coefficients, key=abs)
	grouped_coefficients = [list(g) for _, g in groupby(sorted_coefficients, key=abs)]
	formatted_groups = [
		", ".join([
			f"|{coeff.numerator}|" if isinstance(coeff, Fraction) and coeff.denominator == 1  # 정수 처리 (분모가 1인 경우)
			else f"|\\(-\\frac{{{abs(coeff.numerator)}}}{{{coeff.denominator}}}\\)|" if isinstance(coeff, Fraction) and coeff < 0
			else f"|\\(\\frac{{{coeff.numerator}}}{{{coeff.denominator}}}\\)|" if isinstance(coeff, Fraction) and coeff.denominator != 1
			else f"|{coeff}|"  # 일반 정수 처리
			for coeff in group
		]) for group in grouped_coefficients
	]

	# 그룹 간에는 < 기호를 사용
	explanation_lines = " &lt; ".join(formatted_groups)

	
	comment = f"(해설) 반비례 관계 \\(y = \\frac{{a}}{{x}}\\)에서 \\(a\\)의 절댓값이 작을수록 그 그\n래프가 좌표축에 가깝다.\n"
	comment += f"{explanation_lines}"
	comment += f"이므로 그래프가 좌\n표축에 가장 가까운 것은 {answer_dict[correct_index]}이다."

	# 정답 반환
	return stem, answer, comment

# QSNO 105289
def coordinatesM114_Stem_10_010():
	base_path = 'Middle/Grade1_1/img/'  # 이미지 파일 경로
	img_name = 'coordinatesM114_Stem_10_010'   # 이미지 파일 이름
	img = load_img(base_path + img_name + '.png')
	coordinates = [(150, 140)]  # 좌표를 리스트로 정의
	# 랜덤 선택지 생성
	num = random.randint(2, 9)  # 2부터 9까지의 숫자를 랜덤으로 선택
	correct_answer = f"\\(a > {num}\\)"  # 정답 조건
	choices = [
		f"\\(a &lt; -{num}\\)", 
		f"\\(a > -{num}\\)", 
		f"\\(-{num} &lt; a &lt; 0\\)", 
		f"\\(0 &lt; a &lt; {num}\\)", 
		correct_answer]
	random.shuffle(choices)  # 선택지를 섞음
	correct_index = choices.index(correct_answer)  # 정답의 인덱스

	# 원각기호 번호 생성
	choice_markers = ["①", "②", "③", "④", "⑤"]

	# 문제
	stem = f"두 반비례 관계 \\(y = \\frac{{a}}{{x}}, y = \\frac{{{num}}}{{x}}\\)의 그래프가 그림과 같을 때, 상수 \\( a \\)의 값의 범위는?"
	stem += "\n\n"
	for i, choice in enumerate(choices):
		stem += f"{choice_markers[i]} {choice}\n"  # 원각기호와 선택지를 함께 출력
	
	# 정답
	answer = f"(정답) {choice_markers[correct_index]}\n"
	
	# 해설
	comment = f"(해설) \\( y = \\frac{{a}}{{x}} \\)의 그래프는 제\\(1\\)사분면과 제\\(3\\)사분면을 지나므로 \\( a > 0 \\)\n이때 \\( y = \\frac{{a}}{{x}} \\)의 그래프가 \\( y = \\frac{{{num}}}{{x}} \\)의 그래프보다 좌표축에서 멀리\n떨어져 있으므로\n\\(|a| > {num} \\quad \\therefore a > {num}\\)"
	
	
	# 이미지에 숫자 추가
	def add_coordinates_to_image(img, coordinates, num):
		fig, ax = plt.subplots()
		ax.imshow(img)
		ax.axis('off')

		# num1 추가 (리스트의 첫 번째 좌표)
		ax.text(coordinates[0][0], coordinates[0][1], f'{num}', color='black', fontsize=15, ha='center', va='center', fontfamily = 'serif')

		return fig

	img_coord = add_coordinates_to_image(img, coordinates, num)
	svg = save_svg_resize(50)  # SVG로 저장 및 리사이즈
	plt.close()  # Matplotlib 리소스 해제	

	return stem, answer, comment, svg

# QSNO 105290
def coordinatesM114_Stem_10_011():
	def find_valid_k_and_points():
		"""y1, x2 범위에 적합한 약수가 존재하며 a와 b의 절댓값이 다른 k를 찾음"""
		while True:
			k = random.randint(20, 50)
			y1_candidates = [i for i in range(5, 11) if k % i == 0]
			x2_candidates = [i for i in range(10, 21) if k % i == 0]
			
			# 후보 리스트가 비어 있지 않은지 확인
			if not y1_candidates or not x2_candidates:
				continue

			# 랜덤으로 y1, x2를 선택
			y1 = random.choice(y1_candidates)
			x2 = random.choice(x2_candidates)

			# a와 b 계산
			a = k // y1
			b = -k // x2

			# a와 b의 절댓값이 다르면 반환
			if abs(a) != abs(b):
				return k, y1, x2, a, b

	# 연산자 목록
	operations = ["+", "-", "*", "-"]  # 두 번째 "-"는 b - a 연산
	operation = random.choice(operations)

	# 유효한 k, y1, x2 및 a, b 찾기
	k, y1, x2, a, b = find_valid_k_and_points()

	# 연산 수행
	if operation == "+":
		result = a + b
		op_symbol = f"a + b = {a} + ({b}) ="
	elif operation == "-":
		result = a - b
		op_symbol = f"a - b = {a} - ({b}) ="
	elif operation == "*":
		result = a * b
		op_symbol = f"a \\times b = {a} \\times ({b}) ="
	else:  # b - a
		result = b - a
		op_symbol = f"b - a= {b} - a ="

	# 문제
	stem = (
		f"\n반비례 관계 \\( y = \\frac{{{k}}}{{x}} \\)의 그래프가 두 점 "
		f"\\((a, {y1})\\), \\((-{x2}, b)\\)를 지날 때, \\( a {operation} b \\)의 값을 구하시오."
	)


	# 정답
	answer = (
		f"(정답) \\({result} \\)"
	)

	# 해설
	comment = (
		f"(해설)\n"
		f"\\( y = \\frac{{{k}}}{{x}} \\)에 \\( x = a, y = {y1} \\)을 대입하면\n"
		f"\\( {y1} = \\frac{{{k}}}{{a}} \\quad \\therefore a = {a} \\)\n\n"
		f"\\( y = \\frac{{{k}}}{{x}} \\)에 \\( x = -{x2}, y = b \\)를 대입하면\n"
		f"\\( b = \\frac{{{k}}}{{-{x2}}} = {b} \\)\n\n"
		f"\\(\\therefore  {op_symbol} {result} \\)"
	)

	return stem, answer, comment

# QSNO 105291
def coordinatesM114_Stem_10_012():

	def find_valid_a_and_x():
		"""유효한 a, x1, x2를 찾는 함수"""
		while True:
			# a를 -50 ~ -10 범위의 랜덤 정수로 설정
			a = random.randint(-50, -10)

			# a의 약수 중에서 유효한 범위 (-10 ~ -2, 2 ~ 10)만 필터링
			divisors = [i for i in range(-10, 11) if i != 0 and i != -1 and i != 1 and a % i == 0]
			x1_candidates = [i for i in divisors if -15 <= i <= -2]  # x1 후보 (-10 ~ -2)
			x2_candidates = [i for i in divisors if 2 <= i <= 15]    # x2 후보 (2 ~ 10)

			# x1, x2 후보가 모두 존재하면 반환
			if x1_candidates and x2_candidates:
				x1 = random.choice(x1_candidates)
				x2 = random.choice(x2_candidates)
				return a, x1, x2

	# 유효한 a, x1, x2 생성
	a, x1, x2 = find_valid_a_and_x()

	# y1, b 계산
	y1 = a // x1
	b = a // x2

	# 연산 종류를 랜덤으로 선택
	operation = random.choice(["b - a", "a + b", "a * b", "a - b"])

	# 연산 결과 계산
	if operation == "b - a":
		result = b - a
		operation_latex = f"b - a = {b} - ({a})"
	elif operation == "a + b":
		result = a + b
		operation_latex = f"a + b = {a} + ({b})"
	elif operation == "a * b":
		result = a * b
		operation_latex = f"a \\times b = {a} \\times ({b})"
	elif operation == "a - b":
		result = a - b
		operation_latex = f"a - b = {a} - ({b})"


	# 문제
	stem = (
		f"\n두 점 \\(({x1}, {y1})\\), \\(({x2}, b)\\)가 반비례 관계 \\( y = \\frac{{a}}{{x}} \\)의 "
		f"그래프 위에 있을 때, \\({operation}\\)의 값을 구하세요."
	)

	# 정답
	answer = f"(정답) \\( {result} \\)"

	# 해설
	comment = (
		f"(해설)\n"
		f"\\( y = \\frac{{a}}{{x}} \\)에 \\( x = {x1}, y = {y1} \\)을 대입하면\n"
		f"\\( {y1} = \\frac{{a}}{{{x1}}} \\quad \\therefore a = {a} \\)\n\n"
		f"\\( y = -\\frac{{{abs(a)}}}{{x}} \\)에 \\( x = {x2}\\), \\(y = b \\)를 대입하면\n"
		f"\\( b = -\\frac{{{abs(a)}}}{{{x2}}} = {b} \\)\n\n"
		f"\\(\\therefore {operation_latex} = {result} \\)"
	)

	return stem, answer, comment


# QSNO 105292
def coordinatesM114_Stem_10_013():
	# 이미지 파일 이름과 좌표
	images_and_coordinates = [
		{"image": "01.png", "x": 4, "y": -3},
		{"image": "02.png", "x": 4, "y": -2},
		{"image": "03.png", "x": 8, "y": -2},
		{"image": "04.png", "x": 3, "y": -6},
		{"image": "05.png", "x": 6, "y": -2},
		{"image": "06.png", "x": 5, "y": -2},
		{"image": "07.png", "x": 2, "y": -6},
		{"image": "08.png", "x": 4, "y": -5},
		{"image": "09.png", "x": 5, "y": -6},
		{"image": "10.png", "x": 2, "y": -4}
	]

	selected_item = random.choice(images_and_coordinates)
	x, y = selected_item['x'], selected_item['y']
	a = x * y
	
	# 문제 stem
	stem = '다음 그림과 같은 그래프가 나타내는 반비례 관계의 식은?\n'

	box_stem = f"<img src='{html_img_url}/Middle/Grade1_1/img/coordinates/coordinatesM114_Stem_10_013_{selected_item['image']}' style='width: 65%; padding: 1%; margin: auto; margin-left: 1%;'>"
	stem += insert_html_code(box_stem)
	stem += "\n"


	correct_eq = f"\\(y = \\frac{{{a}}}{{x}}\\)" if a > 0 else  f"\\(y = -\\frac{{{abs(a)}}}{{x}}\\)"

	# 선택지 생성
	choices = [
		correct_eq,  # 정답
		f"\\(y = \\frac{{{-a}}}{{x}}\\)" if a > 0 else f"\\(y = -\\frac{{{-a}}}{{x}}\\)",  # 잘못된 부호
		f"\\(y = \\frac{{{a + random.randint(1, 5)}}}{{x}}\\)",  # 약간 다른 값
		f"\\(y = \\frac{{{a - random.randint(1, 5)}}}{{x}}\\)" if abs(a) > 5 else f"\\(y = \\frac{{{a + 2}}}{{x}}\\)",  # 다른 값
		f"\\(y = \\frac{{{random.randint(-10, 10)}}}{{x}}\\)"  # 랜덤 값

	]

	choices = set()
	choices.add(correct_eq)  # 정답 추가
	while len(choices) < 5:
		random_a = random.randint(-10, 10)
		if random_a == 0:
			continue  # 0이 분자로 나오지 않도록 방지
		random_eq = f"\\(y = \\frac{{{random_a}}}{{x}}\\)" if random_a > 0 else f"\\(y = -\\frac{{{abs(random_a)}}}{{x}}\\)"
		choices.add(random_eq)
	

	# 선택지 리스트로 변환 및 셔플
	choices = list(choices)
	random.shuffle(choices)

	for i, choice in enumerate(choices):
		stem += f"{['①', '②', '③', '④', '⑤'][i]} {choice}\n"


	# 정답 인덱스 찾기
	correct_index = choices.index(correct_eq)
	answer_index = ["①", "②", "③", "④", "⑤"][correct_index]  # 직접 원각 기호 출력
	answer = f"(정답) {answer_index}"


	# 해설 생성
	comment = (
		f"(해설) "
		f"\\(y = \\frac{{a}}{{x}} \\quad (a \\neq 0)\\) 라 하고, \\(x = {x}\\), \\(y = {y}\\)를 대입하면\n"
		f"\\({y} = \\frac{{a}}{{{x}}} \\quad \\therefore a = {a}\\)\n"
		f"\\(\\therefore y = -\\frac{{{abs(a)}}}{{x}} \\)\n"
	)

	return stem, answer, comment


# QSNO 105293
def coordinatesM114_Stem_10_014():

	def generate_coefficients():
		""" 중복되지 않는 선형 및 분수 계수 생성 """
		while True:
			linear = list(set([random.randint(-10, 15) for _ in range(4)]))
			reciprocal = list(set([random.randint(-10, 15) for _ in range(6)]))
			
			# 0과 1, -1을 제외한 값만 유지
			linear = [c for c in linear if c not in (0, 1, -1)]
			reciprocal = [c for c in reciprocal if c not in (0, 1, -1)]
			
			# 필요한 최소 길이를 충족하면 반환
			if len(linear) >= 2 and len(reciprocal) >= 3:
				return linear, reciprocal

	correct_answers = []
	incorrect_answers = []

	# 조건 충족까지 반복
	while len(correct_answers) < 2 or not (2 <= len(incorrect_answers) <= 3):
		# 랜덤한 계수 생성
		linear_coefficients, reciprocal_coefficients = generate_coefficients()

		# 선택지 생성
		options = [
			f"\\(y = {linear_coefficients[0]}x\\)",
			f"\\(y = \\frac{{{reciprocal_coefficients[0]}}}{{x}}\\)",
			f"\\(y = \\frac{{{reciprocal_coefficients[1]}}}{{x}}\\)",
			f"\\(y = {linear_coefficients[1]}x\\)",
			f"\\(y = \\frac{{{reciprocal_coefficients[2]}}}{{x}}\\)"
		]

		# 분수 형태 수정 (음수일 때 `-`를 분자 앞으로)
		for i in range(len(options)):
			options[i] = re.sub(r"\\frac\{(-?\d+)\}\{x\}", lambda m: f"\\frac{{-{abs(int(m.group(1)))}}}{{x}}" if int(m.group(1)) < 0 else m.group(0), options[i])

		# 정답 판별 초기화
		correct_answers = []
		incorrect_answers = []

		for idx, option in enumerate(options):
			# 선형 함수
			match_linear = re.search(r"y\s*=\s*(-?\d+)x", option)
			if match_linear:
				m = int(match_linear.group(1))
				if m > 0:
					correct_answers.append(idx)
				else:
					incorrect_answers.append(idx)
				continue

			# 분수 함수
			match_reciprocal = re.search(r"y\s*=\s*\\frac\{(-?\d+)\}\{x\}", option)
			if match_reciprocal:
				c = int(match_reciprocal.group(1))
				if c > 0:
					correct_answers.append(idx)
				else:
					incorrect_answers.append(idx)


	stem = "\\(x\\)와 \\(y\\) 사이의 관계를 나타내는 그래프가 제\\(1\\)사분면과 제\\(3\\)사분면을 지나는 것을 보기에서 모두 고르시오.\n"

	# 🔹 표시용 선택지 생성 (마이너스를 분자 바깥으로 이동)
	display_options = [
		re.sub(
			r"\\frac\{(-?\d+)\}\{x\}",
			lambda m: f"-\\frac{{{abs(int(m.group(1)))}}}{{x}}" if int(m.group(1)) < 0 else m.group(0),
			option
		)
		for option in options
	]

	# 선택지에 "(ㄱ), (ㄴ), (ㄷ), ..." 마커 적용
	markers = ["(ㄱ)", "(ㄴ)", "(ㄷ)", "(ㄹ)", "(ㅁ)"]
	text_list = [f"{markers[i]} {condition}\n" for i, condition in enumerate(display_options)]

	# HTML 변환
	box_stem = make_box_stem(text_list, type=1, mark_title=True, col_count=3)
	stem += insert_html_code(box_stem)

	# 해설 및 정답 생성
	incorrect_answers_str = ", ".join([markers[i] for i in incorrect_answers])
	correct_answers_str = ", ".join([markers[i] for i in correct_answers])

	# 문제 텍스트

	answer = f"(정답) {correct_answers_str}"
	comment = "(해설) "
	comment += (
		f"{incorrect_answers_str} 그래프가 제\\(2\\)사분면과 제\\(4\\)사분면을 지난다.\n"
		f"이상에서 그래프가 제\\(1\\)사분면과 제\\(3\\)사분면을 지나는 것은 {correct_answers_str}이다."
	)

	return stem, answer, comment

# QSNO 105294
def coordinatesM114_Stem_10_015():

	def generate_unique_numbers(count, exclude_set):
		"""중복되지 않는 숫자를 생성 (1, -1, 약분 방지)."""
		numbers = set()
		while len(numbers) < count:
			num = random.randint(2, 10)
			if (
				num != 0 and num not in exclude_set 
				and num not in {1, -1}  
				and num % 4 != 0  # 4의 배수를 제외하여 약분 방지
			):
				numbers.add(num)
		return list(numbers)

	def generate_unique_fractions(count):
		"""중복되지 않는 약분 불가능한 분수를 생성."""
		fractions_set = set()

		while len(fractions_set) < count:
			numerator = random.randint(2, 10)
			denominator = random.randint(2, 10)

			if numerator == denominator:
				continue  # 분자와 분모가 같으면 제외

			# 약분 가능 여부 확인
			gcd = math.gcd(numerator, denominator)
			if gcd == 1:
				fraction = Fraction(numerator, denominator)
				if fraction not in fractions_set:
					fractions_set.add(fraction)

		return [fraction for fraction in fractions_set]  # Fraction 객체 리스트로 반환

	def generate_equations():

		exclude_set = set()
		numbers = generate_unique_numbers(3, exclude_set)
		exclude_set.update(numbers)

		"""수식 생성 (약분된 형태로 출력)."""
		fractions = generate_unique_fractions(2)

		numerator1, denominator1 = fractions[0].numerator, fractions[0].denominator
		numerator2, denominator2 = fractions[1].numerator, fractions[1].denominator


		# 수식 정의 (부호 정리 적용)
		equations = [
			(f"\\( y = -\\frac{{{numerator1}}}{{{denominator1}}}x \\)", False),  # 감소
			(f"\\( y = {numbers[1]}x \\)", True),                   # 증가
			(f"\\( y = \\frac{{{numerator1}}}{{x}} \\)", False),    # 감소
			(f"\\( y = -\\frac{{{numerator2}}}{{x}} \\)", False),   # 감소
			(f"\\( y = \\frac{{{numerator2}}}{{{denominator2}}}x \\)", True),   # 증가
		]

		# 순서를 무작위로 섞기
		random.shuffle(equations)

		return equations

	# 문제 설명
	stem = f"다음 \\(x\\)와 \\(y\\) 사이의 관계를 나타내는 그래프 중 \\(x > 0\\)일 때, \(x\)의 값이 증가하면 \\(y\\)의 값도 증가하는 것을 모두 고르세요. (정답 \\(2\\)개)\n\n"

	# 랜덤 수식 생성
	equations = generate_equations()

	# 선택지와 정답 분리
	choices = [eq[0] for eq in equations]  # 수식
	correctness = [eq[1] for eq in equations]  # 증가 여부
	correct_answers = [i for i, is_correct in enumerate(correctness) if is_correct]  # 증가하는 경우만 정답
	incorrect_answers = [i for i in range(len(choices)) if i not in correct_answers]  # 증가하지 않는 경우

	# 정답이 항상 2개 보장
	correct_answers = random.sample(correct_answers, 2)  # 증가하는 함수 중 2개 무작위 선택

	# 보기 형식 추가
	formatted_choices = [f"{answer_dict[i]} {choice}" for i, choice in enumerate(choices)]
	stem += "\n".join(formatted_choices)

	# 정답을 오름차순으로 정렬
	correct_answers = sorted(correct_answers)

	# 정답 작성
	answer = "(정답) " + ", ".join([answer_dict[ans] for ans in correct_answers])

	# 해설 생성 (이미지 형식처럼 작성)
	comment = "(해설) " + f"{', '.join([answer_dict[i] for i in incorrect_answers])} \\(x > 0\\)일 때, \\(x\\)의 값이 증가하면 \\(y\\)의 값은 감소합니다."


	return stem, answer, comment


# QSNO 105295
def coordinatesM114_Stem_10_016():


	# 랜덤한 정수 a 값 (-10부터 10까지 범위, 0 제외)
	b = random.choice([i for i in range(-10, 11) if i != 0])
	# 랜덤한 정수 n 값 (1부터 10 사이의 정수)
	n = random.randint(1, 10)

	while True:  # 적합한 random_coefficient를 찾을 때까지 반복
		random_coefficient = random.randint(4, 20)  # 반비례 상수 (4~20 사이의 정수)

		# 1. 약수 구하기
		divisors = [i for i in range(2, random_coefficient + 1) if random_coefficient % i == 0]

		# 2. 약수 중 조건을 만족하는 조합 찾기
		valid_divisors = [x for x in divisors if x != random_coefficient // x and random_coefficient // x != 1]
		if valid_divisors:  # 조건을 만족하는 약수가 있다면 루프 종료
			break

	# 3. (x, y) 생성
	x = random.choice(valid_divisors)
	y = random_coefficient // x

	# 4. 잘못된 (wrong_x, wrong_y) 생성
	while True:
		wrong_x = random.randint(2, random_coefficient + 5)
		wrong_y = random.randint(2, random_coefficient + 5)
		if wrong_x * wrong_y != random_coefficient and wrong_x != wrong_y:
			break



	# 옳은 선택지와 틀린 선택지 구성
	correct_statements = {
		"원점을 지나지 않는다.": "",
		f"제\\(1\\)사분면과 제\\(3\\)사분면을 지난다.": "",
		f"\\(x\\)축, \\(y\\)축과 만나지 않는다.": "",
		f"\\(a > 0\\)일 때, \\(a\\)의 값이 작을수록 좌표축에 가까워진다.": '',
		f"\\(a &lt;0\\)일 때, \\(a\\)의 값이 클수록 좌표축에 가까워진다.":''


	}

	# 틀린 선택지 구성
	incorrect_statements = {
		f"점 \\(({n}, {n}a)\\)를 지난다.": f"\\(y = \\frac{{{b}}}{{x}} \\)에 \\( x = {n} \\), \\( y = {n}a \\)를 대입하면 \\({n}a \\neq \\frac{{{b}}}{{{n}}}\\)",
		f"\\(x &lt; 0\\)일 때, \\(x\\)의 값이 증가하면 \\(y\\)의 값도 증가한다.": f"\\(x &lt; 0\\)일 때, \\(x\\)의 값이 증가하면 \\(y\\)의 값은 감소한다.",
		"원점을 지난다": "원점을 지나지 않는다.",
		f"제\\(2\\)사분면과 제\\(4\\)사분면을 지난다.": f"제\\(1\\)사분면과 제\\(3\\)사분면을 지난다.",
		

	}

	# 무작위로 2개의 옳은 선택지 선택
	selected_correct_choices = random.sample(list(correct_statements.keys()), 2)

	# 무작위로 2개의 틀린 선택지 선택
	selected_incorrect_choices = random.sample(list(incorrect_statements.keys()), 3)

	# 선택지 생성
	all_choices = selected_correct_choices + selected_incorrect_choices

	# 선택지를 무작위로 섞기
	random.shuffle(all_choices)

	# 선택지 번호 매칭
	choices_with_symbols = {answer_dict[i]: all_choices[i] for i in range(len(all_choices))}

	# 정답 찾기
	correct_symbols = [
		symbol for symbol, statement in choices_with_symbols.items()
		if statement in selected_correct_choices
	]

	# 문제 출력
	stem = "다음 중 반비례 관계 \\( y = \\frac{a}{x} \\)의 그래프에 대한 설명으로 옳은 것을 모두 고르시오. (정답 2개)\n"
	for symbol, statement in choices_with_symbols.items():
		stem += f"{symbol} {statement}\n"

	# 정답 출력
	answer = f"(정답) {', '.join(correct_symbols)}"

	# 해설 생성
	comment = "(해설)\n"
	for symbol, statement in choices_with_symbols.items():
		if statement in correct_statements and correct_statements[statement]:
			comment += f"{symbol} {correct_statements[statement]}\n"
		elif statement in incorrect_statements:
			comment += f"{symbol} {incorrect_statements[statement]}\n"


	return stem, answer, comment

# QSNO 105296
def coordinatesM114_Stem_10_017():

	base_path = 'Middle/Grade1_1/img/'  # 이미지 파일 경로
	img_name = 'coordinatesM114_Stem_10_017'   # 이미지 파일 이름
	img = load_img(base_path + img_name + '.png')
	coordinates = [(374, 87)]  # 좌표를 리스트로 정의
	# 랜덤 선택지 생성
	num = random.randint(2, 9)  # 2부터 9까지의 숫자를 랜덤으로 선택
	correct_answer = f"\\(a &lt; -{num}\\)" # 정답 조건
	choices = [
		f"\\(a > {num}\\)",
		f"\\(a > -{num}\\)", 
		f"\\(-{num} &lt; a &lt; 0\\)", 
		f"\\(0 &lt; a &lt; {num}\\)", 
		correct_answer]
	random.shuffle(choices)  # 선택지를 섞음
	correct_index = choices.index(correct_answer)  # 정답의 인덱스

	# 원각기호 번호 생성
	choice_markers = ["①", "②", "③", "④", "⑤"]

	# 문제
	stem = f"두 반비례 관계 \\(y = \\frac{{a}}{{x}}, y = -\\frac{{{num}}}{{x}}\\)의 그래프가 그림과 같을 때, 상수 \\( a \\)의 값의 범위는?"
	stem += "\n\n"
	for i, choice in enumerate(choices):
		stem += f"{choice_markers[i]} {choice}\n"  # 원각기호와 선택지를 함께 출력
	
	# 정답
	answer = f"(정답) {choice_markers[correct_index]}\n"
	
	# 해설
	comment = f"(해설) \\( y = \\frac{{a}}{{x}} \\)의 그래프가 제\\(2\\)사분면과 제\\(4\\)사분면을 지나므로\n \\( a &lt; 0 \\)\n또 \\( y = \\frac{{a}}{{x}} \\)의 그래프가 \\( y = -\\frac{{{num}}}{{x}} \\)의 그래프보다 좌표축에서 멀리\n떨어져 있으므로\n\\(|a| > |-{num}| \\quad \\therefore a &lt; -{num} (∵ a &lt; 0)\\)"
	
	
	# 이미지에 숫자 추가
	def add_coordinates_to_image(img, coordinates, num):
		fig, ax = plt.subplots()
		ax.imshow(img)
		ax.axis('off')

		# num1 추가 (리스트의 첫 번째 좌표)
		ax.text(coordinates[0][0], coordinates[0][1], f'{num}', color='black', fontsize=19, ha='center', va='center', fontfamily='serif')

		return fig

	img_coord = add_coordinates_to_image(img, coordinates, num)
	svg = save_svg_resize(40)  # SVG로 저장 및 리사이즈
	plt.close()  # Matplotlib 리소스 해제	

	return stem, answer, comment, svg

# QSNO 105297
def coordinatesM114_Stem_10_018():

	while True:
		# 문제의 랜덤 변수 설정 (값 범위 확장)
		constant = random.choice([-12, -16, -20, -24, -28, -32, -36])  # 반비례 관계의 분자 값 (정수)
		
		# 첫 번째 점의 x 좌표는 constant의 약수 중 하나를 랜덤 선택
		point1_x_candidates = [i for i in range(2, 16) if constant % i == 0]
		point1_x = random.choice(point1_x_candidates)  # 약수 중 하나 선택

		# 두 번째 점의 y 좌표는 constant의 약수 중 하나를 랜덤 선택
		point2_y_candidates = [i for i in range(-12, 0) if constant % i == 0]  # 음수 약수만 선택
		point2_y = random.choice(point2_y_candidates)

		# 1. 첫 번째 점 (x, a)에서 a 계산
		point1_y = constant // point1_x  # 정수 나눗셈 (항상 정수)

		# 2. 두 번째 점 (b, y)에서 b 계산
		point2_x = constant // point2_y  # 정수 나눗셈 (항상 정수)

		# \( a \)와 \( b \)가 같지 않은 경우에만 루프 탈출
		if point1_y != point2_x:
			break
	# 연산 종류를 랜덤으로 선택
	operation = random.choice(["b - a", "a + b", "ab", "a - b"])

	# 연산 결과 계산
	if operation == "b - a":
		result = point2_x - point1_y
		operation_latex = f"b - a = {point2_x} - ({point1_y})"
	elif operation == "a + b":
		result = point1_y + point2_x
		operation_latex = f"a + b = {point1_y} + {point2_x}"
	elif operation == "ab":
		result = point1_y * point2_x
		operation_latex = f"a \\times b = {point1_y} \\times {point2_x}"
	elif operation == "a - b":
		result = point1_y - point2_x
		operation_latex = f"a - b = {point1_y} - {point2_x}"

	# 문제 출력 (MathJax 형식 포함)
	stem = (
		f"반비례 관계 \\( y = -\\frac{{{abs(constant)}}}{{x}} \\) 의 그래프가 두 점 \\(( {point1_x}, a )\\), "
		f"\\(( b, {point2_y} )\\) 을 지날 때, \\( {operation} \\)의 값을 구하시오."
	)

	answer = f"(정답) \\({result}\\)"

	# 해설 작성 (MathJax 형식 적용)
	comment = "(해설) "
	comment += (
		f"\\( y = -\\frac{{{abs(constant)}}}{{x}} 에 \\( x = {point1_x}, y = a \\)를 대입하면\n"
		f"\\( a = \\frac{{{constant}}}{{{point1_x}}} = {point1_y} \\)\n"
		f"\\( y = -\\frac{{{abs(constant)}}}{{x}} 에 \\( x = b, y = {point2_y} \\)를 대입하면\n"
		f"\\( {point2_y} = \\frac{{{constant}}}{{b}} \\quad \\therefore b = \\frac{{{constant}}}{{{point2_y}}} = {point2_x} \\)\n"
		f"\\( \\therefore {operation_latex} = {result} \\)"
	)
	
	return stem, answer, comment

# QSNO 105298
def coordinatesM114_Stem_10_019():
	base_path = 'Middle/Grade1_1/img/'  # 이미지 파일 경로
	img_name = 'coordinatesM114_Stem_10_019'   # 이미지 파일 이름
	img = load_img(base_path + img_name + '.png')
	coordinates = [(310, 294), (200,200)]  # 좌표를 리스트로 정의
	# 랜덤하게 점 A의 x좌표와 선분 AB 길이를 설정
	while True:
		x_a = random.randint(2, 6)  # 점 A의 x좌표 (2~10 사이의 랜덤 값)
		ab_length = random.randint(2, 10)  # 선분 AB 길이 (2~10 사이의 랜덤 값)
		y_a = random.randint(1, 7)  # 점 A의 y좌표 (1~20 사이의 랜덤 값)
		y_b = y_a - ab_length  # 점 B의 y좌표 계산

		# 상수 a 계산 및 유효성 확인
		a = -x_a * y_b
		if y_b != 0 and a != 0 and a % 4 == 0:  # 조건: y_b ≠ 0, a ≠ 0, a는 4의 배수
			break
	# 문제 본문
	equation = r"y = -\frac{a}{x}"
	stem = f"반비례 관계 \\({equation}\\)의 그래프가 오른쪽 그림과 같을 때, 점 \\(A({x_a}, {y_a})\\)을 지나고 \\(y\\)축에 평행한 직선이 \\({equation}\\)의 그래프와 만나는 점을 \\(B\\)라 하자.\n"
	stem += f"선분 \\(AB\\)의 길이가 \\({ab_length}\\)일 때, 양수 \\(a\\)의 값을 구하시오.\n"

	# 정답
	answer = f"(정답) \\({a}\\)"

	# 해설
	comment = "(해설)\n"
	comment += f"두 점 \\(A\\), \\(B\\)의 \\(x\\)좌표가 같으므로 점 \\(B\\)의 \\(x\\)좌표는 \\({x_a}\\)이다.\n"
	comment += f"\\(y = -\\frac{{a}}{{x}}\\) 에 \\(x = {x_a}\\)를 대입하면\n"
	comment += f"\\(y = -\\frac{{a}}{{{x_a}}}\\)\n"
	comment += f"즉 점 \\(B\\)의 좌표는 \\(({x_a}, -\\frac{{a}}{{{x_a}}})\\)\n"
	comment += f"이때 선분 \\(AB\\)의 길이가 \\({ab_length}\\)이므로\n"
	comment += f"\\({y_a} - \\left(-\\frac{{a}}{{{x_a}}}\\right) = {ab_length}\\)\n"
	comment += f"\\(\\frac{{a}}{{{x_a}}} = {int(ab_length - y_a)}\\)\n"
	comment += f"따라서 \\(a = {a}\\)\n"

	# 이미지에 숫자 추가
	def add_coordinates_to_image(img, coordinates, x_a, y_a):
		fig, ax = plt.subplots()
		ax.imshow(img)
		ax.axis('off')

		# x_a1 추가 (리스트의 첫 번째 좌표)
		ax.text(coordinates[0][0], coordinates[0][1], f'{x_a}', color='black', fontsize=19, ha='center', va='center', fontfamily='serif')
		ax.text(coordinates[1][0], coordinates[1][1], f'{y_a}', color='black', fontsize=19, ha='center', va='center', fontfamily='serif')


		return fig

	img_coord = add_coordinates_to_image(img, coordinates, x_a, y_a)
	svg = save_svg_resize(20)  # SVG로 저장 및 리사이즈
	plt.close()  # Matplotlib 리소스 해제	

	return stem, answer, comment, svg
