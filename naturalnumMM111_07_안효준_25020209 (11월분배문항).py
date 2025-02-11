# 아래 라이브러리를 로컬 서버로 반드시 추가해주세요
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
import pandas as pd
from math import gcd
import io
import sympy as sp
import sys
from fractions import Fraction
from Dictionary.html_function import *
from functools import reduce
import matplotlib

def load_img(file_path):
	img = mpimg.imread(file_path)
	return img

# SVG 적용 함수 (08/06 변경)
def save_svg_resize(ratio = 100):
	# ratio : 그림 확대 / 축소를 위한 파라미터, 기본값 100      
	file = io.StringIO()
	plt.savefig(file, format='svg', dpi=300, bbox_inches='tight', pad_inches=0.1) # Additional option to remove the rest parts
	file.seek(0)
	svg_data = file.getvalue()
	svg_data = svg_data.replace('<svg ', f'<svg width="{ratio}%" height="{ratio}%"  ') # style="display: block; margin: auto;"
	return svg_data

# QSNO 100240
def naturalnumMM111_Stem_07_001():
    # 이미지 파일 경로 및 이름
    base_path = 'Middle/Grade1_1/img/'
    img_name = 'naturalnumMM111_Stem_07_001'
    img = load_img(base_path + img_name + '.png')  # 이미지 불러오기

    def not_add_coordinates_to_image(img):
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis('off')
        return fig

    img_no_coord = not_add_coordinates_to_image(img)
    svg = save_svg_resize(70)

    # 최소공배수 계산 함수
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    def calculate_lcm(numbers):
        return reduce(lcm, numbers)

    # 랜덤 값 생성 (합리적인 범위 내에서 조정)
    while True:
        width = random.randint(6, 8)  # 가로 (좁은 범위로 제한)
        depth = random.randint(6, 10)  # 세로
        height = random.randint(8, 12)  # 높이

        edge_length = calculate_lcm([width, depth, height])

        # 최소공배수가 너무 작은 값(<= width, depth, height)이나 비현실적인 경우 제외
        if edge_length > max(width, depth, height) and edge_length <= 100:  # edge_length 제한
            break

    # 각 차원에서 필요한 상자의 개수 계산
    num_boxes_width = edge_length // width
    num_boxes_depth = edge_length // depth
    num_boxes_height = edge_length // height
    total_boxes = num_boxes_width * num_boxes_depth * num_boxes_height

    # 문제
    stem = (
        f"가로, 세로의 길이가 각각 \\({width}\\;cm\\), \\({depth}\\;cm\\)이고 높이가 \\({height}\\;cm\\)인 "
        f"직육면체 모양의 상자가 있다. 이 상자를 빈틈없이 쌓아서 부피가 최소인 정육면체를 만들려고 할 때, "
        f"상자는 모두 몇 개가 필요한지 구하시오."
    )

    # 정답
    answer = f"(정답) \\({total_boxes}\\)(개)"

    # 해설
    comment = (
        f"(해설) 부피가 최소인 정육면체는 한 모서리의 길이가 최소인 경우이므로 정육면체의 한 모서리의 길이는 "
        f"\\({width}\\), \\({depth}\\), \\({height}\\)의 최소공배수이어야 한다. "
        f"\\({width}\\), \\({depth}\\), \\({height}\\)의 최소공배수는 \\({edge_length}\\)이므로 필요한 상자의 개수는 "
        f"가로 \\({edge_length} \\div {width} = {num_boxes_width}\\)(개), "
        f"세로 \\({edge_length} \\div {depth} = {num_boxes_depth}\\)(개), "
        f"높이 \\({edge_length} \\div {height} = {num_boxes_height}\\)(개)이다.\n"
        f"따라서 상자는 \\({num_boxes_width} \\times {num_boxes_depth} \\times {num_boxes_height} = {total_boxes}\\)(개)가 필요하다."
    )

    return stem, answer, comment, svg

# QSNO 100241
def naturalnumMM111_Stem_07_002():
    # 이미지 파일 경로 및 이름
    base_path = 'Middle/Grade1_1/img/'
    img_name = 'naturalnumMM111_Stem_07_002'
    img = load_img(base_path + img_name + '.png')  # 이미지 불러오기

    def not_add_coordinates_to_image(img):
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis('off')
        return fig

    img_no_coord = not_add_coordinates_to_image(img)
    svg = save_svg_resize(70)

    # 최소공배수 계산 함수
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    def calculate_lcm(numbers):
        return reduce(lcm, numbers)

    # 랜덤 톱니 수 생성 함수
    def generate_random_teeth():
        while True:
            teeth_a = random.randint(50, 150)  # 톱니 수 A (더 큰 범위)
            teeth_b = random.randint(20, 100)  # 톱니 수 B (더 작은 범위)
            
            if teeth_a > teeth_b:  # A가 B보다 항상 크도록 보장
                lcm_value = calculate_lcm([teeth_a, teeth_b])
                if lcm_value <= 1000 and teeth_a != teeth_b:  # 최소공배수 제한 및 A ≠ B
                    return teeth_a, teeth_b, lcm_value

    # 랜덤 톱니 수 생성
    teeth_a, teeth_b, lcm_value = generate_random_teeth()

    # 각 톱니바퀴의 회전 횟수 계산
    rotations_a = lcm_value // teeth_a
    rotations_b = lcm_value // teeth_b

    # 문제 stem
    stem = (
        f"톱니의 수가 각각 \\({teeth_a}\\)(개), \\({teeth_b}\\)(개)인 두 톱니바퀴 \\(A\\), \\(B\\)가 서로 맞물려 있다. "
        f"두 톱니바퀴가 맞물려 돌기 시작하여 처음을 다시 같은 톱니에서 맞물리는 것은 "
        f"\\(A\\), \\(B\\)가 각각 몇 바퀴 회전한 후인지 구하시오."
    )

    # 정답
    answer = f"(정답) \\(A\\):\\({rotations_a}\\)(바퀴), \\(B\\):\\({rotations_b}\\)(바퀴)"

    # 해설
    comment = (
        f"(해설) 두 톱니바퀴가 처음으로 다시 같은 톱니에서 맞물릴 때까지 돌아간 톱니의 수는 "
        f"\\({teeth_a}\\)와 \\({teeth_b}\\)의 최소공배수이므로 \\({lcm_value}\\)(개)이다. "
        f"따라서 두 톱니바퀴가 처음으로 다시 같은 톱니에서 맞물리는 것은 "
        f"톱니바퀴 \\(A\\)가 \\({lcm_value} \\div {teeth_a} = {rotations_a}\\)(바퀴), "
        f"톱니바퀴 \\(B\\)가 \\({lcm_value} \\div {teeth_b} = {rotations_b}\\)(바퀴) 회전한 후이다."
    )

    return stem, answer, comment, svg

# QSNO 100242
def naturalnumMM111_Stem_07_003():
    # 문제 유형 정의
    problems = [
        {
            "stem": "6과 9의 공배수를 모두 구하시오.",
            "answer": "18, 36, 54, ...",
            "comment": "공배수는 18, 36, 54, ...이다."
        },
        {
            "stem": "6과 9의 최소공배수를 구하시오.",
            "answer": "18",
            "comment": "최소공배수는 18이다."
        },
        {
            "stem": "6과 9의 최소공배수의 배수를 모두 구하시오.",
            "answer": "18, 36, 54, ...",
            "comment": "최소공배수 18의 배수는 18, 36, 54, ...이다."
        }
    ]

    # 랜덤하게 하나의 문제 선택
    selected_problem = random.choice(problems)

    # 공통 stem
    common_stem = "6과 9에 대하여 다음을 구하시오.\n\n"

    # 박스에 들어갈 stem
    text_list = [f"{selected_problem['stem']}"]

    # 박스 형태로 문제 stem 만들기
    box_stem = make_box_stem(text_list, type=1, mark_title=False, col_count=1)
    stem = common_stem + insert_html_code(box_stem) + "\n"

    # 정답 및 해설
    answer = f"(정답) {selected_problem['answer']}"
    comment = f"(해설) {selected_problem['comment']}"

    return stem, answer, comment

def naturalnumMM111_Stem_07_004():
    problems = [
        {
            "original_stem": "다음 중 두 수 \\(2^2 \\times 5^2\\), \\(2^3 \\times 5 \\times 7\\)의 공배수가 아닌 것을 모두 고르면? (정답 2개)",
            "options": [
                "\\(2^2\\times5^2\\times7^2\\)",
                "\\(2^3\\times5^2\\times7\\)",
                "\\(2^3\\times5^2\\times7^2\\)",
                "\\(2^3\\times3^3\\times5\\times7\\)",
                "\\(2^3\\times5^2\\times7^2\\)"
            ],
            "correct_indices": [0, 3],
            "lcm": "\\(2^3\\times5^2\\times7\\)"
        },
        {
            "original_stem": "다음 중 두 수 \\(3^2 \\times 5\\), \\(2^3 \\times 3 \\times 7\\)의 공배수가 아닌 것을 모두 고르면? (정답 2개)",
            "options": [
                "\\(2^3\\times3^2\\times5\\times7\\)",
                "\\(2^3\\times3^3\\times5\\)",
                "\\(3^2\\times5\\times7^2\\)",
                "\\(2^2\\times3^3\\times7\\)",
                "\\(2^3\\times3^2\\times5\\times7^2\\)"
            ],
            "correct_indices": [2, 3],
            "lcm": "\\(2^3\\times3^2\\times5\\times7\\)"
        },
        {
            "original_stem": "다음 중 두 수 \\(5^2 \\times 7\\), \\(3 \\times 7^2\\)의 공배수가 아닌 것을 모두 고르면? (정답 2개)",
            "options": [
                "\\(3\\times5^2\\times7^3\\)",
                "\\(5^2\\times7^2\\)",
                "\\(3\\times5^2\\times7^2\\)",
                "\\(3^2\\times5\\times7^2\\)",
                "\\(3^2\\times5^2\\times7^2\\)"
            ],
            "correct_indices": [0, 3],
            "lcm": "\\(3\\times5^2\\times7^2\\)"
        },
        {
            "original_stem": "다음 중 두 수 \\(2^3 \\times 3^2\\), \\(2 \\times 3 \\times 5\\)의 공배수가 아닌 것을 모두 고르면? (정답 2개)",
            "options": [
                "\\(2^3\\times3^2\\times5\\)",
                "\\(2^4\\times3\\times5\\)",
                "\\(2^3\\times3^2\\times5^2\\)",
                "\\(2^2\\times3^3\\)",
                "\\(2^3\\times3^2\\times5\\times7\\)"
            ],
            "correct_indices": [1, 3],
            "lcm": "\\(2^3\\times3^2\\times5\\)"
        }
    ]
    
    # 랜덤하게 하나의 문제 선택
    selected_problem = random.choice(problems)
    
    # 보기 내용을 섞기
    shuffled_options = selected_problem["options"].copy()
    random.shuffle(shuffled_options)
    
    # 새로운 정답 번호 찾기
    new_correct_answers = []
    for original_idx in selected_problem["correct_indices"]:
        original_option = selected_problem["options"][original_idx]
        new_idx = shuffled_options.index(original_option)
        new_correct_answers.append(f"{'①②③④⑤'[new_idx]}")
    
    # 정답을 정렬된 순서로 표시
    new_correct_answers.sort()
    
    # stem 생성
    stem_lines = [selected_problem["original_stem"]]
    for i, option in enumerate(shuffled_options):
        stem_lines.append(f"{'①②③④⑤'[i]} {option}")
    stem = "\n".join(stem_lines)
    
    # 해설 생성 (번호 순서대로)
    answer_pairs = []
    for symbol in ["①", "②", "③", "④", "⑤"]:
        if symbol in new_correct_answers:
            idx = '①②③④⑤'.index(symbol)
            answer_pairs.append((symbol, shuffled_options[idx]))
    
    comment = f"(해설) 두 수의 최소공배수는 {selected_problem['lcm']}입니다.\n"
    for i, (symbol, option) in enumerate(answer_pairs):
        comment += f"{symbol} {option}은 {selected_problem['lcm']}의 배수가 아닙니다.\n"
    comment = comment.rstrip()
    
    answer = f"(정답) {', '.join(new_correct_answers)}"
    
    return stem, answer, comment


# QSNO 100244
def naturalnumMM111_Stem_07_005():
    # 최소공배수 랜덤 설정 (20 ~ 50 사이의 값)
    lcm = random.randint(20, 50)

    # 최대값을 180 ~ 200 사이의 랜덤 값으로 설정
    max_value = random.randint(180, 200)

    # max_value 이하의 공배수 개수 계산
    count = max_value // lcm

    # 보기 생성
    choices = [
        count - 2, count - 1, count, count + 1, count + 2
    ]
    random.shuffle(choices)  # 보기를 랜덤하게 섞음

    # 정답 인덱스
    correct_index = choices.index(count)

    # 문제
    stem = (
        f"두 자연수 \\(A\\), \\(B\\)의 최소공배수가 {lcm}일 때, "
        f"\\(A\\), \\(B\\)의 공배수 중 {max_value} 이하의 자연수의 개수는?\n"
    )
    stem += "① {0}     ② {1}     ③ {2}\n".format(choices[0], choices[1], choices[2])
    stem += "④ {0}     ⑤ {1}".format(choices[3], choices[4])

    # 정답
    answer = f"(정답) {['①', '②', '③', '④', '⑤'][correct_index]}\n"

    # 해설
    comment = (
        f"(해설) \\(A\\), \\(B\\)의 공배수는 두 수의 최소공배수인 {lcm}의 배수입니다. "
        f"이때 \\({max_value} \\div {lcm} = {max_value / lcm:.1f}\\)이므로 "
        f"{max_value} 이하의 공배수의 개수는 {count}개입니다."
    )

    return stem, answer, comment