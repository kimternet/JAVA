/******************************************************************************
====================================================
1. StringBuffer
=====================================================

StringBuffer는 문자열을 추가하거나 변경할 때 주로 사용하는 자료형.
StringBuffer의 다양한 메서드

1. append = append 메서드를 사용하면, 문자열을 계속 추가해 나갈 수 있다.
2. insert = 특정 위치에 원하는 문자열을 삽입.


====================================================
2. StringBuilder
=====================================================

StringBuffer는 멀티스레드 환경에서 안전하고, StringBuilder는 StringBuffer보다
성능이 우수하다는 장점이 있다.
따라서 동기화를 고려할 필요가 없는 상황에서는 StringBuffer보다 StringBuilder를 사용하는 게 유리하다.

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	    
	    //StringBuffer 객체 생성
	    StringBuffer sb = new StringBuffer();
	    sb.append("hello");
	    sb.append(" ");
	    sb.append("enjoy to java");
	    sb.insert(0,"fighting"); //insert 삽입.
	    String result = sb.toString();
	    System.out.println(result);
	    System.out.println(sb.substring(0,4)); // 시작위치,끝위치, figh 출력

	    
	    // String 자료형을 사용
	    String result2 = "";
	    result2 += "hello";
	    result2 += " ";
	    result2 += "enjoy to java";
	    System.out.println(result2);
	    
	    // 내부적으로 객체를 생성하고 메모리를 사용하는 과정이 다르다.
	    // StringBuffer는 객체를 한 번만 생성하지만,
	    // String 자료형은 + 연산이 있을 때마다 새로운 String 객체를 생성하므로
	    // 총 4개의 String 자료형 객체가 만들어 진다.
	    // 또 String 자료형은 값이 한 번 생성되면 변경할 수 없다.
	    // toUpperCase와 같은 메서드를 보면 문자열이 변경되는 것같지만,
	    // 해당 메서드를 수행할 때 또 다른 String 객체를 생성하여 리턴할 뿐이다.
	    // 반면 StringBuffer 자료형은 값을 변경할 수 있으므로, 생성된 값을 언제든지 수정할 수 있다다.
	    // 하지만, StringBuffer는 String 자료형보다 무겁고, 메모리 사용량도 많고 속도도 느리다.
	    // 따라서 문자열을 추가하거나 변경하는 작업이 많으면 StringBuffer를, 적으면 String을 사용하는 게 좋다. 
	    
	    
	    
	    
	    //StringBuilder
	    
	    StringBuilder ab = new StringBuilder();
	    ab.append("Buffer와");
	    ab.append("Builder는");
	    ab.append("차이가");
	    ab.append("있습니다.");
	    String result3 = ab.toString();
	    System.out.println(result3);
	    
	    
	    
	}
}