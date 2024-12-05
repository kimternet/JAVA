/******************************************************************************
====================================================
1. bool(boolean type)
=====================================================

참, 거짓의 값을 갖는 자료형을 불(boolean)이라고 한다.
불 자료형에 대입되는 값은 참 똔느 거짓만 가능.

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	    
	    boolean isSuccess = true;
	    boolean isTest = false;
	    
	    System.out.println(isSuccess);
	    System.out.println(isTest);
	    
	    boolean a = 2 > 1; // 참
	    boolean b = 1 == 2; // 거짓
	    boolean c = 3 % 2 == 1; // 참
	    boolean d = "3".equals("2"); // 거짓
	    
	    System.out.println(a);
	    System.out.println(b);
	    System.out.println(c);
	    System.out.println(d);
	    
	    // boolean타입 조건문
	    
	    int base = 180;
	    int height = 185;
	    boolean isTall = height > base;
	    
	    if (isTall){
	        System.out.println("키가 크다");
	    }
	    
	    
	    int i = 3;
	    boolean isOdd = i % 2 == 1;
	    System.out.println(isOdd); // true 출력
	    
	}
}