/******************************************************************************
1. 형 변환

final은 자료형에 값을 단 한번만 설정할 수 있게 강제하는 키워드다.
값을 한 번 설정하면 그 값을 다시 설정할 수 없다.

*******************************************************************************/

import java.util.Arrays;
import java.util.HashSet;


public class Main
{
	public static void main(String[] args) {
	    
	    // 자료형은 문자열이지만, 그 내용은 숫자로 이루어진 값이다.
	    // 이런 경우 문자열을 정수(integer)로 바꿀 수 있다.
	    // 문자열을 정수로 바꾸려면 Integer 클래스를 사용한다.
	    
	    // String -> Int
	    String num = "123";
	    int n = Integer.parseInt(num);
	    
	    // 인트 -> String
	    int s = 123;
	    String numnum = "" + s;
	    String num1 = String.valueOf(s);
	    String num2 = Integer.toString(s);
	    double d = Double.parseDouble(num); // 소수점이 포함된 숫자형태로 변환도 가능 
	    
	    System.out.println(n);
	    System.out.println(s);
	    System.out.println(num1);
	    System.out.println(num2);
	    System.out.println(d);
	    
	    // final
	    final int x = 123;
	    
	    // 리스트의 경우도 final로 선언하면 재할당은 불가능하다.
	    
	    final ArrayList<String> y = new ArrayList<>(Arrays.asList("a","b"));
	    
	    // Unmodifiable List
	    
	    // 리스트의 경우 final로 선언 할 때 리스트에 값을 더하거나 뺄 수 있다.
	    // 재할당만 불가능할 뿐이다.
	    // 만약 수정할수없는 리스트로 만들고 싶다면 List.of를 작성하면 된다.
	    
	    final List<String> i = List.of("a","b")
	    
	    
	    
	    
		
		
	}
}