/******************************************************************************
====================================================
1. 문자열 포매팅
=====================================================

문자열 안의 특정한 값을 바꿀 수 있게 해주는 것이 문자열 포매팅 기법
즉, 문자열 안에 어떤 값을 삽입하는 방법.

String.format 메서드 사용

====================================================
2. 문자열 포맷 코드의 종류
=====================================================
코드 | 설명 |
-------------
%s   문자열(String) <-이 코드는 어떤 형태의 값이든 변환해 넣을 수 있다.
%c	 문자 1개(character)
%d	 정수(Integer)
%f	 부동소수(floating-point)
%o	 8진수
%x	 16진수
%%	 Literal % (문자 % 자체)


====================================================
3. System.out.printf
====================================================

String.format 메서드는 포매팅된 문자열을 리턴한다.
System.out.printf 메서드를 사용하면 String.format 메서드가 없어도
같은 형식으로 간단히 포매팅된 문자열을 출력할 수 있다.

** String.format은 문자열을 리턴하는 메서드이고,
** String.out.printf는 문자열을 출력하는 메서드!

차이가 있으니 상황에 맞게 사용.

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	    
	    // 숫자 바로 대입하기
	    // %d를 입력하고 숫자 3을 두 번째 파라미터로 전달.
	    
	    // %d는 문자열 포맷 코드라고 한다.
	    System.out.println(String.format("I eat %d apples.", 3));
	    
	    // 문자열은 %s를 쓴다.
	    System.out.println(String.format("I eat %s apples", "five"));
	    
	    // 숫자값을 나타내는 변수 대입하기
	    int number = 3;
	    System.out.println(String.format("I eat %d apples.", number));
	    
	    // 값을 2개 이상 넣기
	    String day = "three";
	    System.out.println(String.format("apples: %d ,days=%s", number, day));
	    
	    // %s 포맷코드
	    // 문자열에 3을 삽입하려면 %d, 실수는 %f를 사용해야 하지만,
	    // %s는 자동으로 전달되는 파라미터 값을 문자열로 바꾼다.
	    System.out.println(String.format("apples:%s", 3));
	    System.out.println(String.format("rate is %s", 3.2344));
	    
	    // 특수문자 %는 반드시 %%로 사용해야 한다. 하나만 사용할 경우 에러발생.
	    System.out.println(String.format("%d%%", 100));
	    
	    // 응용하기
	    
	    // 정렬과 공백 표현 %10s는 전체 길이가 10인 문자열 공간에서 대입되는 값을,
	    // 가장 오른쪽에 정렬하고 나머지는 공백으로 남겨두라는 의미다.
	    System.out.println(String.format("%10s","hi"));
	    
	    // 왼쪽 정렬
	    System.out.println(String.format("%-10skim","hi"));
	    
	    // 소수점 표현하기, 숫자 4는 뒤에 이어질 소수점의 개수
	    System.out.println(String.format("%.4f", 3.421342424));
	    
	    // 전체 길이가 10인 문자열 공간에 오른쪽에 소수 정렬
	    System.out.println(String.format("%10.4f",3.4212424));
	    
	    // String.out.printf
	    System.out.printf("%d apples.", 3);
	    
	}
}