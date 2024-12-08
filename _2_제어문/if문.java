/******************************************************************************
1. if문

조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 쓰이는 것이 if문.



2. if문과 else문의 기본 구조

if(조건문){
    <수행할 문장1>;
    ...
} else {

    <수행할 문장 A>;
    ...
    
}


  -------     예    ------
 | 조건  |   --- > | 택시 |
 --------           ------
    |   아니오      ------
    -------------> | 걷기 |
                    ------


3. and, or, not 연산자

- x && y -> x와 y모두 참이어야 참이다.

- x || y -> x와 y 둘 중 적어도 하나가 참이면 참

- !x     -> x가 거짓이면 참이다.


4. contains

List 자료형에 해당 아이템이 있는지 조사하는 contains 메서드가 있다.
특히 contains 메서드는 조건문에 많이 활용된다.

5. else if

if와 else만으로 다양한 조건, 판단을 하기 어렵다.
else if는 이전 조건이 거짓일 때 수행된다.

개수 제한없이 사용 가능

if (조건문) {
    <수행할 문장1>
    ...
}else if (조건문){
    <수행할 문장1>
    ...
}else if (조건문){
    <수행할 문장1>
    ...
}else{
    <수행할 문장1>
    ..
}


*******************************************************************************/

import java.util.ArrayList;

public class Main
{
	public static void main(String[] args) {
		
		// money = true;
		boolean money = true;
		if (money) { // true이기 때문에 맨처음 조건문에 해당
		    System.out.println("택시");
		}else{ // false면 else로 처리
		    System.out.println("걷기");
		}
        
        // 응용 1
        
        int student = 10;
        
        if (student >= 10){
            System.out.println("전원 출석");
        }else {
            System.out.println("전원 출석 안함");
        }
        
        // 응용 2
        // 돈이 10000원 이상 있거나, 카드가 있다면 택시를 타고,
        // 아니면 걸어가라
        
        int money2 = 5000;
        boolean card = true;
        
        if (money2 >= 10000 || card){
            System.out.println("택시타세요.");
        }else {
            System.out.println("걸어가세요");
        }
        
        // contains
        
        boolean hasCard = true;
        ArrayList<String> pocket = new ArrayList<String>();
        pocket.add("paper");
        pocket.add("handphone");
        
        
        if (pocket.contains("money")) { // money 판단
            System.out.println("현금 택시");
        }else{
            if (hasCard){ // money가 없으면 card판단.
                System.out.println("카드 택시");
            }else{
                System.out.println("걷기");
            }
        }
        
        // else if는 이전 조건문이 거짓일 때 수행된다.
        if (pocket.contains("money")){
            System.out.println("현금 택시");
        }else if(hasCard){ // else if로 간결하게 해결 가능.
            System.out.println("카드 택시");
        }else{
            System.out.println("걷기");
        }

	}
}