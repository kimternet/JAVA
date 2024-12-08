/******************************************************************************

1. 객체지향 프로그래밍


*******************************************************************************/

// result 전역 변수(static 변수) 사용

class Calculator {
    static int result = 0;
    
    static int add(int num){ // add메서드는 매개 변수 num으로 받은 값을 이전에 계산한 결괏값에 더한 후 돌려주는 메서드드
        
        result += num;
        return result;
        
    }
}

// 전역 변수 삭제

class Calculator1 {
    
    int result = 0;
    
    int add(int num){
        
        result += num;
        return result;
        
    }
    
    int sub(int num){
        
        result -= num;
        return result;
    }
    
}


public class Main
{
	public static void main(String[] args) {
	    
	    Calculator cal1 = new Calculator(); // 계산기1 객체를 생성.
	    Calculator cal2 = new Calculator(); // 게산기2 객체를 생성.
	    
	    Calculator1 cal3 = new Calculator1(); // 전역변수 삭제한 객체 생성
	    Calculator1 cal4 = new Calculator1(); 

		
		System.out.println(Calculator.add(3));
		System.out.println(Calculator.add(4));
		
		System.out.println(Calculator.add(8));
		System.out.println(Calculator.add(9));
		
		System.out.println(cal3.add(4));
		System.out.println(cal3.add(5));
		
		System.out.println(cal4.sub(3));  // 객체는 독립적인 result 값을 가진다.
		System.out.println(cal4.sub(5));

	}
}