/******************************************************************************
1. enum자료형

서로 연관 있는 여러개의 상수 집합을 정의할 때 사용.

예로 어느 카페에서 판매하는 커피 종류

1. 아메리카노
2. 아이스아메리카노
3. 카페라떼

enum 자료형의 장점
1. 매직넘버를 사용할 때보다 코드가 명확하다.
2. 잘못된 값을 사용해 생길 수 있는 오류를 막을 수 있다.

*******************************************************************************/

import java.util.Arrays;
import java.util.HashSet;


public class Main
{
	    enum CoffeType{
	        AMERICANO,
	        ICE_AMERICANO,
	        CAFE_LATTE
	    };
	
	public static void main(String[] args) {
	    System.out.println(CoffeType.AMERICANO); //
	    System.out.println(CoffeType.ICE_AMERICANO);
	    System.out.println(CoffeType.CAFE_LATTE);
	    
	    
	    for (CoffeType type: CoffeType.values()){
	        System.out.print(type);
	    }
	    
	    
		
		
	}
}