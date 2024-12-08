/******************************************************************************

1. for each

- for each문은 J2SE 5.0부터 추가됨.

- for each라는 키워드가 따로 있는 게 아니다.

- for문을 이용하지만 문법이 조금 다르다.

- for (type 변수명: iterate){
    body-of-loop
}

- iterate는 루프를 돌릴 객체이다.

- iterate는 객체에서 한 개씩 순차적으로 변수명에 대입되어 for문을 수행한다.

- iterate에 사용할 수 있는 자료형은 루프를 돌릴 수 있는 
자료형(배열, ArrayList등 )만 가능.


** 변수명의 type은 iterate객체에 포함된 자료형과 일치해야한다.
** for each문은 반복 횟수를 명시적으로 주는 게 불가능하다.
* 한단계씩 순차적으로 반복할 때만 사용 가능하다는 제약이 있다.


*******************************************************************************/

import java.util.ArrayList;
import java.util.Arrays;

public class Main
{
	public static void main(String[] args) {
		
		String[] numbers = {"one","two","three"};
		
		// 기본 for문 구조
		for (int i = 0; i < numbers.length; i++){
		    System.out.println(numbers[i]);
		}
		
		// for each문
		for (String number: numbers){
		    System.out.println("for each-> "+number);
		}
		
		// for each ArrayList로 구현.
		
		ArrayList<String> fishes = new ArrayList<>(Arrays.asList("광어","고등어","갈치"));
		
		for (String fish: fishes){
		    System.out.println(fish);
		}
		
	}
}