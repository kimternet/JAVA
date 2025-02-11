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

# # 이제 Dictionary.html_function을 불러옵니다
# from Dictionary.html_function import *

	# 이미지 로드 함수
def load_img(file_path):
	img = mpimg.imread(file_path)
	return img

# SVG 적용 함수 (08/06 변경)
def save_svg_resize(ratio = 60):
    # ratio : 그림 확대 / 축소를 위한 파라미터, 기본값 100      
    file = io.StringIO()
    plt.savefig(file, format='svg', dpi=300, bbox_inches='tight', pad_inches=0.1) # Additional option to remove the rest parts
    file.seek(0)
    svg_data = file.getvalue()
    svg_data = svg_data.replace('<svg ', f'<svg width="{ratio}%" height="{ratio}%"  ') # style="display: block; margin: auto;"
    return svg_data

# QSNO 100000
def naturalnumMM111_Stem_01_001():
    # 문제
    stem = '아래의 그림에서 소수가 있는 칸을 모두 칠할 때, 나타나는 숫자는?'

    # 데이터 정의 (3개의 데이터 중 랜덤 선택)
    data_options = [
        [
            [1, 2, 3, 5, 6],
            [8, 11, 12, 14, 15],
            [16, 17, 19, 23, 24],
            [25, 26, 27, 29, 30],
            [32, 37, 41, 43, 44],
        ],
        [
            [1, 2, 3, 5, 6],
            [8, 14, 12, 11, 15],
            [16, 17, 19, 23, 24],
            [25, 29, 27, 26, 30],
            [32, 37, 41, 43, 44],
        ],
        [
            [1, 2, 3, 5, 6],
            [8, 14, 12, 11, 15],
            [16, 17, 19, 23, 24],
            [25, 26, 27, 29, 30],
            [32, 37, 41, 43, 44],
        ],
    ]

    # 랜덤 데이터 선택
    data = random.choice(data_options)

    # DataFrame 생성
    df = pd.DataFrame(data)

    # 테이블 생성
    table_stem = make_table_stem(df)
    stem += insert_html_code(table_stem)

    # 정답 및 해설 설정
    if data == data_options[0]:  # 첫 번째 데이터셋
        stem += '① 2     ② 4     ③ 5\n'
        stem += '④ 7     ⑤ 9'
        answer = "(정답) ③"
        comment = "(해설) 소수는 1보다 큰 자연수 중에서 1과 자기 자신만을 약수로 갖는 수이다."
    elif data == data_options[1]:  # 두 번째 데이터셋
        stem += '① 2     ② 4     ③ 5\n'
        stem += '④ 7     ⑤ 9'
        answer = "(정답) ①"
        comment = "(해설) 소수는 1보다 큰 자연수 중에서 1과 자기 자신만을 약수로 갖는 수이다."
    else:  # 세 번째 데이터셋
        stem += '① 2     ② 3     ③ 5\n'
        stem += '④ 7     ⑤ 9'
        answer = "(정답) ②"
        comment = "(해설) 소수는 1보다 큰 자연수 중에서 1과 자기 자신만을 약수로 갖는 수이다."

    return stem, answer, comment

# QSNO 100001
def naturalnumMM111_Stem_01_002():
    # 사전에 정의된 문제 데이터
    problems = [
        {
            "text_list": [
                "(ㄱ) 한 자리 자연수 중 소수는 3개이다.",
                "(ㄴ) 가장 작은 합성수는 4이다.",
                "(ㄷ) 모든 합성수는 소수들의 곱으로 나타낼 수 있다.",
                "(ㄹ) 두 소수의 합은 합성수이다."
            ],
            "choices": "① (ㄱ), (ㄴ)      ② (ㄴ), (ㄷ)      ③ (ㄷ), (ㄹ)\n"
                       "④ (ㄱ), (ㄷ), (ㄹ)      ⑤ (ㄴ), (ㄷ), (ㄹ)",
            "answer": "(정답) ②",
            "comment": "(해설) (ㄱ) 한 자리 자연수 중 소수는 2, 3, 5, 7의 4개로 거짓입니다.\n"
                       "(ㄴ) 가장 작은 합성수는 4로 참입니다.\n"
                       "(ㄷ) 모든 합성수는 소수들의 곱으로 나타낼 수 있으므로 참입니다.\n"
                       "(ㄹ) 두 소수의 합은 항상 합성수가 아니므로 거짓입니다."
        },
        {
            "text_list": [
                "(ㄱ) 모든 소수는 홀수이다.",
                "(ㄴ) 1은 소수가 아니다.",
                "(ㄷ) 6은 합성수이다.",
                "(ㄹ) 두 소수의 합은 항상 합성수이다."
            ],
            "choices": "① (ㄱ), (ㄴ)      ② (ㄴ), (ㄷ)      ③ (ㄷ), (ㄹ)\n"
                       "④ (ㄱ), (ㄷ), (ㄹ)      ⑤ (ㄴ), (ㄷ), (ㄹ)",
            "answer": "(정답) ②",
            "comment": "(해설) (ㄱ) 모든 소수는 홀수라는 것은 거짓입니다. 2는 짝수 소수입니다.\n"
                       "(ㄴ) 1은 소수가 아니므로 참입니다.\n"
                       "(ㄷ) 6은 합성수로 참입니다.\n"
                       "(ㄹ) 두 소수의 합은 항상 합성수가 아니므로 거짓입니다."
        },
        {
            "text_list": [
                "(ㄱ) 한 자리 자연수 중 소수는 4개이다.",
                "(ㄴ) 가장 작은 합성수는 6이다.",
                "(ㄷ) 모든 소수는 홀수이다.",
                "(ㄹ) 1은 소수가 아니다."
            ],
            "choices": "① (ㄱ), (ㄴ)      ② (ㄴ), (ㄷ)      ③ (ㄷ), (ㄹ)\n"
                       "④ (ㄱ), (ㄹ)      ⑤ (ㄴ), (ㄷ), (ㄹ)",
            "answer": "(정답) ④",
            "comment": "(해설) (ㄱ) 한 자리 자연수 중 소수는 2, 3, 5, 7로 4개이므로 참입니다.\n"
                       "(ㄴ) 가장 작은 합성수는 4이므로 거짓입니다.\n"
                       "(ㄷ) 모든 소수가 홀수라는 것은 거짓입니다. 2는 짝수 소수입니다.\n"
                       "(ㄹ) 1은 소수가 아니므로 참입니다."
        }
    ]

    # 랜덤하게 문제 선택
    selected_problem = random.choice(problems)

    # HTML로 보기 박스 생성
    box_stem = make_box_stem(selected_problem["text_list"], mark_title=True, col_count=1)
    stem = "옳은 것을 보기에서 모두 고른 것은?\n"
    stem += insert_html_code(box_stem)
    stem += "\n" + selected_problem["choices"]

    # 정답과 해설
    answer = selected_problem["answer"]
    comment = selected_problem["comment"]

    return stem, answer, comment

# QSNO 100002
def naturalnumMM111_Stem_01_003():
    # 문제 세트 정의
    problem_sets = [
        {
            "choices": [
                "① 13은 합성수이다.",
                "② 소수 중 짝수는 없다.",
                "③ 모든 자연수는 소수이거나 합성수이다.",
                "④ 모든 소수의 약수는 2개이다.",
                "⑤ 10 이하의 자연수 중에서 소수는 5개이다."
            ],
            "answer": "(정답) ④",
            "comment": (
                "(해설) "
                "① 13은 소수이다.\n"
                "② 소수 2는 짝수이다.\n"
                "③ 자연수 1은 소수도 아니고 합성수도 아니다.\n"
                "④ 모든 소수의 약수는 2개이다.\n"
                "⑤ 10 이하의 자연수 중에서 소수는 2, 3, 5, 7의 4개이다."
            )
        },
        {
            "choices": [
                "① 2는 유일한 짝수 소수이다.",
                "② 1은 소수이다.",
                "③ 모든 소수는 홀수이다.",
                "④ 7은 합성수이다.",
                "⑤ 10은 소수이다."
            ],
            "answer": "(정답) ①",
            "comment": (
                "(해설) "
                "① 2는 유일한 짝수 소수입니다.\n"
                "② 1은 소수가 아니다.\n"
                "③ 모든 소수는 홀수라는 것은 틀렸습니다. 2는 짝수 소수입니다.\n"
                "④ 7은 소수이다.\n"
                "⑤ 10은 합성수입니다."
            )
        },
        {
            "choices": [
                "① 5는 합성수이다.",
                "② 2는 홀수이다.",
                "③ 소수는 1과 자기 자신만을 약수로 가진다.",
                "④ 1은 합성수이다.",
                "⑤ 6은 소수이다."
            ],
            "answer": "(정답) ③",
            "comment": (
                "(해설) "
                "① 5는 소수입니다.\n"
                "② 2는 짝수입니다.\n"
                "③ 소수는 1과 자기 자신만을 약수로 가진다는 정의에 부합합니다.\n"
                "④ 1은 합성수가 아닙니다.\n"
                "⑤ 6은 합성수입니다."
            )
        }
    ]

    # 랜덤하게 문제 세트 선택
    selected_problem = random.choice(problem_sets)

    # 문제 stem 생성
    stem = '다음 중 옳은 것은?\n\n'
    for choice in selected_problem["choices"]:
        stem += f"{choice}\n"

    # 정답과 해설
    answer = selected_problem["answer"]
    comment = selected_problem["comment"]

    return stem, answer, comment