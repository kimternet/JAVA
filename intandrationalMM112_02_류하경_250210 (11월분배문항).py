import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
import io
import sympy as sp
from fractions import Fraction
import sys

# Dictionary.html_function의 파일 경로 설정
module_path = "/home/aig2/directDownload/html_function.py"
if module_path not in sys.path:
    sys.path.append(module_path)

from Dictionary.html_function import *
html_img_url_demo = "https://aig.boinit.com:8080/resources/img"
html_img_url = html_img_url

# 이미지 로드 함수
def load_img(file_path):
	img = mpimg.imread(file_path)
	return img

# SVG 적용 함수 (08/06 변경)
def save_svg_resize(ratio = 60):
    # ratio : 그림 확대 / 축소를 위한 파라미터, 기본값 100      
    file = io.StringIO()
    plt.savefig(file, format='svg', dpi=300, bbox_inches='tight', pad_inches=0.1)
    file.seek(0)
    svg_data = file.getvalue()
    svg_data = svg_data.replace('<svg ', f'<svg width="{ratio}%" height="{ratio}%"  ')
    return svg_data

# QSNO 101020
def intandrationalMM112_Stem_02_001():
	import copy
	
	# 이미지 랜덤 선정
	image_number = random.randint(1, 3)

	# 이미지 파일 관련
	base_path = 'Middle/Grade1_1/img/'  # [EDIT] 이미지 파일 경로
	img_name = f'intandrationalMM112_Stem_02_001_{image_number}'   # [EDIT] 이미지 파일 이름 
	img = load_img(base_path + img_name + '.png')
	coordinates = []

	# 문제
	stem = "다음 수직선 위의 점 \\(A\\), \\(B\\), \\(C\\), \\(D\\), \\(E\\)가 나타내는 수로 옳지 않은 것은?\n\n"
	# stem += 'intandrationalMM112_Stem_02_001'

	options_lt = ["①", "②", "③", "④", "⑤"]
	alphabets_lt = ["\\(A\\)", "\\(B\\)", "\\(C\\)", "\\(D\\)", "\\(E\\)"]

	dic = {
		1: ["\\(-\\frac{11}{3}\\)", "\\(-2\\)", "\\(-\\frac{1}{2}\\)", "\\(\\frac{4}{3}\\)", "\\(3\\)"],
		2: ["\\(-\\frac{8}{3}\\)", "\\(-2\\)", "\\(-\\frac{1}{2}\\)", "\\(\\frac{5}{3}\\)", "\\(4\\)"],
		3: ["\\(-\\frac{7}{3}\\)", "\\(-\\frac{1}{2}\\)", "\\(0\\)", "\\(\\frac{5}{3}\\)", "\\(4\\)"]
	}

	dic_for_comment = copy.deepcopy(dic)

	wrong_idx_selection = random.randint(0, 4)
	if image_number == 1:
		wrong_idx_selection = random.sample([0, 2, 3], 1)[0]
	elif image_number == 2:
		wrong_idx_selection = random.sample([0, 2, 3], 1)[0]
	else:
		wrong_idx_selection = random.sample([0, 1, 3], 1)[0]

	wrong_op = dic[image_number][wrong_idx_selection]

	if image_number == 1 and wrong_idx_selection == 0:
		wrong_op_num = wrong_op[:-8]+str(1+int(wrong_op[-8:-6]))+wrong_op[-6:]
		dic[image_number][wrong_idx_selection] = wrong_op_num
	else:
		wrong_op_num = wrong_op[:-7]+str(1+int(wrong_op[-7]))+wrong_op[-6:]
		dic[image_number][wrong_idx_selection] = wrong_op_num

	stem += '\n'.join(f"{options_lt[i]} {alphabets_lt[i]}: {dic[image_number][i]}" for i in range(5))

	# 정답
	answer = f"(정답) {options_lt[wrong_idx_selection]}"

	# 해설
	comment = f"(해설) {options_lt[wrong_idx_selection]} {alphabets_lt[wrong_idx_selection]}: {dic_for_comment[image_number][wrong_idx_selection]}"

	# 이미지 부분
	def add_coordinates_to_image(img, coordinates):
		fig, ax = plt.subplots()
		ax.imshow(img)
		ax.axis('off')

		return fig

	img_coord = add_coordinates_to_image(img, coordinates)      
	svg = save_svg_resize()
	plt.close()

	return stem, answer, comment, svg

# QSNO 101021
def intandrationalMM112_Stem_02_002():

	# 이미지 파일 관련
	base_path = 'Middle/Grade1_1/img/'  # [EDIT] 이미지 파일 경로
	img_name = f'intandrationalMM112_Stem_02_002_stem'   # [EDIT] 이미지 파일 이름 
	img = load_img(base_path + img_name + '.png')
	coordinates = []

	stem = "다음 수직선 위의 점 \\(A\\), \\(B\\), \\(C\\), \\(D\\), \\(E\\)가 나타내는 정수로 옳은 것을 모두 고르면? (정답 2개)\n\n"

	options_lt = ["①", "②", "③", "④", "⑤"]
	alphabets_lt = ["\\(A\\)", "\\(B\\)", "\\(C\\)", "\\(D\\)", "\\(E\\)"]

	dic = {
		"\\(A\\)": -6,
		"\\(B\\)": -4,
		"\\(C\\)": 0,
		"\\(D\\)": 4,
		"\\(E\\)": 5
	}

	# Select 2 random positions for correct answers
	correct_indices = random.sample(range(5), 2)
	modified_dic = dic.copy()

	# Modify incorrect positions
	for i in range(5):
		if i not in correct_indices:
			key = alphabets_lt[i]
			modified_dic[key] = dic[key] + random.choice([-1, 1])

	stem += '\n'.join(f"{options_lt[i]} {alphabets_lt[i]}: {modified_dic[alphabets_lt[i]]}" for i in range(5))

	# Generate answer with correct option numbers
	answer = f"(정답) {', '.join(options_lt[i] for i in sorted(correct_indices))}"

	# Generate comment showing original values for incorrect answers
	incorrect_indices = [i for i in range(5) if i not in correct_indices]
	comment = f"(해설)"
	comment += '\n'.join(f'{options_lt[i]} {alphabets_lt[i]}: {dic[alphabets_lt[i]]}' for i in incorrect_indices)

	# 이미지 부분
	def add_coordinates_to_image(img, coordinates):
		fig, ax = plt.subplots()
		ax.imshow(img)
		ax.axis('off')

		return fig

	img_coord = add_coordinates_to_image(img, coordinates)      
	svg = save_svg_resize()
	plt.close()

	return stem, answer, comment, svg

# QSNO 101022
def intandrationalMM112_Stem_02_003():

	# 이미지 파일 관련
	base_path = 'Middle/Grade1_1/img/'  # [EDIT] 이미지 파일 경로
	img_name = f'intandrationalMM112_Stem_02_003'   # [EDIT] 이미지 파일 이름 
	img = load_img(base_path + img_name + '.png')
	coordinates = [(469, 190), (1187, 190)]

	r = random.randint(1, 5)
	x = random.randint(-5, 5)
	b_num = x - r
	d_num = x + r

	stem = f"다음 수직선에서 점 \\(B\\)가 나타내는 수는 \\({b_num}\\)이고 점 \\(D\\)가 나타내는 수는 \\({d_num}\\)이다. 두 점 \\(A\\), \\(B\\), 두 점 \\(B\\), \\(C\\), 두 점 \\(C\\), \\(D\\) 사이의 거리가 모두 같을 때, 점 \\(A\\)가 나타내는 수를 구하시오."

	answer = f"(정답) 두 점 \\(B\\), \\(D\\)가 나타내는 수는 각각 \\({b_num}\\), \\({d_num}\\)이므로 두 점 사이의 거리는 \\({r*2}\\)이다."

	comment = (
		f"(해설) 즉 두 점 \\(A\\), \\(B\\), 두 점 \\(B\\), \\(C\\), 두 점 \\(C\\), \\(D\\) 사이의 거리는\n"
		f"\\({r*2}\\) \\(\\times\\) \\(\\frac{1}{2}\\) = \\({r}\\)\n"
		f"따라서 점 \\(A\\)는 점 \\(B\\)로부터 왼쪽으로 \\({r}\\)만큼 떨어져 있으므로 점 \\(A\\)가 나타내는 수는 \\({b_num-r}\\)이다.")

	# 이미지 부분
	def add_coordinates_to_image(img, coordinates):
		fig, ax = plt.subplots()
		ax.imshow(img)
		ax.axis('off')
        
        # Ensure only valid coordinates are used
		ax.text(coordinates[0][0], coordinates[0][1], f'{b_num}', color='black', fontsize=15, ha='center', va='center')
		ax.text(coordinates[1][0], coordinates[1][1], f'{d_num}', color='black', fontsize=15, ha='center', va='center')

		return fig

	img_coord = add_coordinates_to_image(img, coordinates)      
	svg = save_svg_resize()
	plt.close()

	return stem, answer, comment, svg

# QSNO 101023
def intandrationalMM112_Stem_02_004():
	import copy

	img_idx = random.randint(1, 2)

	# 이미지 파일 관련
	base_path = 'Middle/Grade1_1/img/'  # [EDIT] 이미지 파일 경로
	img_name = f'intandrationalMM112_Stem_02_004_{img_idx}'   # [EDIT] 이미지 파일 이름 
	img = load_img(base_path + img_name + '.png')
	coordinates = []

	idx = random.randint(0, 4) # 정답(옳지 않은 수)이 될 인덱스 랜덤 추출

	options_lt = ["①", "②", "③", "④", "⑤"]
	alphabets_lt = ["\\(A\\)", "\\(B\\)", "\\(C\\)", "\\(D\\)", "\\(E\\)"]

	dic = {
		1: ["\\(-\\frac{5}{2}\\)", "\\(-\\frac{3}{2}\\)", "\\(\\frac{1}{3}\\)", "\\(1\\)", "\\(\\frac{11}{5}\\)"],
		2: ["\\(-2\\)", "\\(-\\frac{3}{2}\\)", "\\(\\frac{1}{3}\\)", "\\(\\frac{11}{5}\\)", "\\(\\frac{13}{5}\\)"]
	}

	# 원본 저장
	dic_for_comment = copy.deepcopy(dic)

	# 값 변경
	num = dic[img_idx][idx]

	if "frac" in num:
		if num in ["\\(\\frac{11}{5}\\)", "\\(\\frac{13}{5}\\)"]:
			start = num.find("{") + 1
			end = num.find("}")
			numerator = int(num[start:end]) + random.choice([-2, -1, 1, 2])
			dic[img_idx][idx] = num[:start] + str(numerator) + num[end:]
		else:
			start = num.find("{") + 1
			end = num.find("}")
			numerator = int(num[start:end]) + random.choice([1, 2])
			dic[img_idx][idx] = num[:start] + str(numerator) + num[end:]
	else:
		value = int(num[-3:-2]) + random.choice([-2, -1, 1, 2])
		dic[img_idx][idx] = f"\\({value}\\)"

	stem = f"다음 수직선 위의 다섯 개의 점 \\(A\\), \\(B\\), \\(C\\), \\(D\\), \\(E\\)가 나타내는 수로 옳지 않은 것은?\n\n"
	stem += '\n'.join(f"{options_lt[i]} {alphabets_lt[i]}: {dic[img_idx][i]}" for i in range(5))

	answer = f"(정답) {options_lt[idx]}"

	comment = f"(해설) {options_lt[idx]} 점 {alphabets_lt[idx]}가 나타내는 수는 {dic_for_comment[img_idx][idx]}이다."

	# 이미지 부분
	def add_coordinates_to_image(img, coordinates):
		fig, ax = plt.subplots()
		ax.imshow(img)
		ax.axis('off')

		return fig

	img_coord = add_coordinates_to_image(img, coordinates)      
	svg = save_svg_resize()
	plt.close()

	return stem, answer, comment, svg

# QSNO 101024
def intandrationalMM112_Stem_02_005():

	idx = random.randint(1, 5)

	dic = {
		1: [f"\\(-\\frac{4}{3}\\)", f"\\(\\frac{7}{4}\\)", "\\(-1\\)", "\\(2\\)"],
		2: [f"\\(-\\frac{5}{3}\\)", f"\\(\\frac{5}{4}\\)", "\\(-2\\)", "\\(1\\)"],
		3: [f"\\(-\\frac{1}{3}\\)", f"\\(\\frac{5}{4}\\)", "\\(0\\)", "\\(1\\)"],
		4: [f"\\(-\\frac{5}{4}\\)", f"\\(\\frac{5}{3}\\)", "\\(-1\\)", "\\(2\\)"],
		5: [f"\\(-\\frac{7}{4}\\)", f"\\(\\frac{4}{3}\\)", "\\(-2\\)", "\\(1\\)"],
	}

	stem = f"수직선에서 {dic[idx][0]}에 가장 가까운 정수와 {dic[idx][1]}에 가장 가까운 정수를 차례대로 구하시오.\n\n"

	answer = f"(정답) {dic[idx][2]}, {dic[idx][3]}"

	if int(dic[idx][1][-4]) == 7:
		letter = "을"
	else:
		letter = "를"

	comment = f"(해설) {dic[idx][0]}, {dic[idx][1]}{letter} 수직선 위에 점으로 나타내면 다음 그림과 같다.\n"
	comment_img = f"<img src='{html_img_url}/Middle/Grade1_1/img/intandrational/intandrationalMM112_Stem_02_005_{idx}.png' style='width: 90%; padding: 1%; '>\n"
	comment_img += f"따라서 {dic[idx][0]}에 가장 가까운 정수는 {dic[idx][2]}이고, {dic[idx][1]}에 가장 가까운 정수는 {dic[idx][3]}이다."
	comment += insert_html_code(comment_img) 

	return stem, answer, comment

# QSNO 101025
def intandrationalMM112_Stem_02_006():

	# 이미지 파일 관련
	base_path = '/home/aig/aig2/directDownload/Middle/Grade1_1/img/'  # [EDIT] 이미지 파일 경로
	img_name = f'intandrationalMM112_Stem_02_006'   # [EDIT] 이미지 파일 이름 
	img = load_img(base_path + img_name + '.png')
	coordinates = []

	idx = random.randint(0, 4) # 정답(옳은 것)이 될 인덱스 랜덤 추출

	x_dic = {
		"\\(A\\)": "\\(-3\\)",
		"\\(B\\)": "\\(-\\frac{5}{4}\\)",
		"\\(C\\)": "\\(\\frac{2}{3}\\)",
		"\\(D\\)": "\\(\\frac{5}{2}\\)"
	}

	r = random.choice([-2, -1, 1, 2])
	wrong_x_dic = {
		"\\(A\\)": f"\\({-3 + r}\\)",
		"\\(B\\)": f"\\(-\\frac{5 + r}{4}\\)",
		"\\(C\\)": f"\\(\\frac{2 + r}{3}\\)",
		"\\(D\\)": f"\\(\\frac{5 + r}{2}\\)"
	}

	y_dic = {
		"유리수": ["\\(-3\\)", "\\(-\\frac{5}{4}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{5}{2}\\)"],
		"음수": ["\\(-3\\)", "\\(-\\frac{5}{4}\\)"],
		"양수": ["\\(\\frac{2}{3}\\)", "\\(\\frac{5}{2}\\)"],
		"정수": ["\\(-3\\)"],
		"정수가 아닌 유리수": ["\\(-\\frac{5}{4}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{5}{2}\\)"]
	}

	wrong_y_dic = {
		"유리수": ["\\(-\\frac{5}{4}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{5}{2}\\)"],
		"음수": ["\\(-3\\)"],
		"양수": ["\\(\\frac{5}{2}\\)"],
		"정수": ["\\(-3\\)", "\\(\\frac{2}{3}\\)"],
		"정수가 아닌 유리수": ["\\(-3\\)", "\\(-\\frac{5}{4}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{5}{2}\\)"]
	}

	x = random.sample(["\\(A\\)", "\\(B\\)", "\\(C\\)", "\\(D\\)"], 2)
	y = random.sample(["유리수", "음수", "양수", "정수", "정수가 아닌 유리수"], 3)

	# 선지 생성 (idx에 해당되는 건 그대로, 나머지는 변경)
	stem = f"다음 수직선 위의 다섯 개의 점 \\(A\\), \\(B\\), \\(C\\), \\(D\\)가 나타내는 수에 대한 설명으로 옳은 것은?\n\n"

	if idx == 0:
		stem += f"① {x[0]}: {x_dic[x[0]]}\n"
	elif idx != 0:
		stem += f"① {x[0]}: {wrong_x_dic[x[0]]}\n"

	if idx == 1:
		stem += f"② {x[1]}: {x_dic[x[1]]}\n"
	elif idx != 1:
		stem += f"② {x[1]}: {wrong_x_dic[x[1]]}\n"

	if idx == 2:
		stem += f"③ {y[0]}는 {', '.join(y_dic[y[0]])}의 \\({len(y_dic[y[0]])}\\)개이다.\n"
	elif idx != 2:
		stem += f"③ {y[0]}는 {', '.join(wrong_y_dic[y[0]])}의 \\({len(wrong_y_dic[y[0]])}\\)개이다.\n"

	if idx == 3:
		stem += f"④ {y[1]}는 {', '.join(y_dic[y[1]])}의 \\({len(y_dic[y[1]])}\\)개이다.\n"
	elif idx != 3:
		stem += f"④ {y[1]}는 {', '.join(wrong_y_dic[y[1]])}의 \\({len(wrong_y_dic[y[1]])}\\)개이다.\n"

	if idx == 4:
		stem += f"⑤ {y[2]}는 {', '.join(y_dic[y[2]])}의 \\({len(y_dic[y[2]])}\\)개이다.\n"
	elif idx != 4:
		stem += f"⑤ {y[2]}는 {', '.join(wrong_y_dic[y[2]])}의 \\({len(wrong_y_dic[y[2]])}\\)개이다.\n"

	options_lt = ["①", "②", "③", "④", "⑤"]
	answer = f"(정답) {options_lt[idx]}"

	comment = (f"(해설) 네 점 \\(A\\), \\(B\\), \\(C\\), \\(D\\)가 나타내는 수는 다음과 같다.\n"
		f"\\(A\\): \\(-3\\), \\(B\\): \\(-\\frac{5}{4}\\), \\(C\\): \\(\\frac{2}{3}\\), \\(D\\): \\(\\frac{5}{2}\\)\n"
		f"③ {y[0]}는 {', '.join(y_dic[y[0]])}의 \\({len(y_dic[y[0]])}\\)개이다.\n"
		f"④ {y[1]}는 {', '.join(y_dic[y[1]])}의 \\({len(y_dic[y[1]])}\\)개이다.\n"
		f"⑤ {y[2]}는 {', '.join(y_dic[y[2]])}의 \\({len(y_dic[y[2]])}\\)개이다.\n")

	# 이미지 부분
	def add_coordinates_to_image(img, coordinates):
		fig, ax = plt.subplots()
		ax.imshow(img)
		ax.axis('off')

		return fig

	img_coord = add_coordinates_to_image(img, coordinates)      
	svg = save_svg_resize()
	plt.close()

	return stem, answer, comment, svg

# QSNO 101026
def intandrationalMM112_Stem_02_007():

	# 이미지 파일 관련
	base_path = 'Middle/Grade1_1/img/'  # [EDIT] 이미지 파일 경로
	img_name = f'intandrationalMM112_Stem_02_007'   # [EDIT] 이미지 파일 이름 
	img = load_img(base_path + img_name + '.png')
	coordinates = [(476, 180), (1147, 180)]

	idx = random.randint(0, 4) # 정답(옳은 수)이 될 인덱스 랜덤 추출

	x = random.randint(-4, 4)
	y = random.randint(5, 12)

	if (y - x) % 2 != 0:
		y += 1

	options_lt = ["①", "②", "③", "④", "⑤"]
	stem = f"다음 수직선에서 점 \\(B\\)가 나타내는 수는 \\({x}\\)이고 점 \\(D\\)가 나타내는 수는 \\({y}\\)이다. 네 점 \\(A\\), \\(B\\), \\(C\\), \\(D\\)에 대하여 두 점 \\(A\\), \\(B\\), 두 점 \\(B\\), \\(C\\), 두 점 \\(C\\), \\(D\\) 사이의 거리가 모두 같을 때, 점 \\(A\\)가 나타내는 수는?\n\n"
	for i, r in zip(range(0, 5), random.sample([-3, -2, -1, 1, 2, 3], 5)):
		if i == idx:
			stem += f"{options_lt[i]} \\({x-(y-x)//2}\\)\n"
		else:
			stem += f"{options_lt[i]} \\({x-(y-x)//2 + r}\\)\n"

	answer = f"(정답) {options_lt[idx]}"

	comment = (
		f"(해설) 두 점 \\(B\\), \\(D\\)가 나타내는 수는 각각 \\({x}\\), \\({y}\\)이므로 두 점 \\(B\\), \\(D\\) 사이의 거리가 \\({y-x}\\)이다."
		"따라서 두 점 \\(A\\), \\(B\\), 두 점 \\(B\\), \\(C\\), 두 점 \\(C\\), \\(D\\) 사이의 거리는\n"
		f"\\({y-x}\\) \\(\\times\\) \\(\\frac{1}{2}\\) = \\({(y-x)//2}\\)\n"
		f"점 \\(A\\)는 점 \\(B\\)에서 왼쪽으로 \\({(y-x)//2}\\)만큼 떨어져 있으므로 점 \\(A\\)가 나타내는 수는 \\({x-(y-x)//2}\\)이다.")

	# 이미지 부분
	def add_coordinates_to_image(img, coordinates):
		fig, ax = plt.subplots()
		ax.imshow(img)
		ax.axis('off')
        
        # Ensure only valid coordinates are used
		ax.text(coordinates[0][0], coordinates[0][1], f'{x}', color='black', fontsize=15, ha='center', va='center')
		ax.text(coordinates[1][0], coordinates[1][1], f'{y}', color='black', fontsize=15, ha='center', va='center')

		return fig

	img_coord = add_coordinates_to_image(img, coordinates)      
	svg = save_svg_resize()
	plt.close()

	return stem, answer, comment, svg

# QSNO 101027
def intandrationalMM112_Stem_02_008():

	a = random.randint(1, 9)

	if a in [1, 3, 6, 7, 8]:
		letter = "을"
	else:
		letter = "를"

	stem = f"수직선 위에 \\({a}\\){letter} 나타내는 점 \\(A\\)가 있다. 이 수직선 위에 점 \\(M\\)을 잡고, 점 \\(A\\)에 대하여 점 \\(M\\)과 대칭인 점을 점 \\(N\\)이라 하자. 점 \\(M\\)을 나타내는 수를 \\(x\\)라 할 때, 점 \\(N\\)을 나타내는 수를 \\(x\\)를 사용한 식으로 나타내시오.\n\n"

	answer = f"(정답) \\({a*2}\\) - \\(x\\)"

	comment = (
		f"(해설) 점 \\(M\\)이 점 \\(A\\)를 기준으로 왼쪽과 오른쪽에 있을 때를 나누어 생각한다.\n"
		f"(\\(i\\)) \\(x\\) \\(&gt;\\) \\({a}\\)인 경우\n"
		f"두 점 \\(A\\)와 \\(M\\) 사이의 거리가 \\(x\\) - \\({a}\\)이므로 점 \\(N\\)을 나타내는 수는\n"
		f"\\({a}\\) - (\\(x\\) - \\({a}\\)) = \\({a*2}\\) - \\(x\\)\n"
		f"(\\(ii\\)) \\(x\\) \\(&lt;\\) \\({a}\\)인 경우\n"
		f"두 점 \\(A\\)와 \\(M\\) 사이의 거리가 \\({a}\\) - \\(x\\)이므로 점 \\(N\\)을 나타내는 수는\n"
		f"\\({a}\\) + (\\({a}\\) - \\(x\\)) = \\({a*2}\\) - \\(x\\)\n"
		f"따라서 점 \\(N\\)을 나타내는 수는 \\({a*2}\\) - \\(x\\)이다.\n"
	)

	return stem, answer, comment