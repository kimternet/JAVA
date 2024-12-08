/******************************************************************************

1. while문의 기본 구조

while(조건문) {
    <수행할 문장1>;
    <수행할 문장2>;
    <수행할 문장3>;
    ...
}               
                     -----------
                    |          |
                    V          |
시작 -> 입력 -> 조건문 -> 수행할 문장 -> 종료
                  |                       ^
                  |                       |
                  |                       |  
                  ------------------------

2. 무한 루프란?

while (true){
    <수행할 문장1>;
    ...
}

조건문 자체가 true이면 조건문은 항상 참이된다.
while문은 참인 동안에 문장들을 계속 수행하므로 무한루프에 빠지게 된다.


3. break

while문을 멈춰야할 때 사용하는 것이 break

4. continue

어떤 조건을 검사해서 참이 아닌 경우 while문을 빠져나가는 대신
while문의 맨처음, 즉 조건문으로 돌아가게 하고 싶은 경우도 있다.

예로 홀수만 출력하고 싶다고 가정.
짝수일 경우 조건문으로 continue;
홀수일 경우에는 출력

*******************************************************************************/

import java.util.ArrayList;

public class Main
{
	public static void main(String[] args) {
	    
	    int treeHit = 5;
	    
	    while(treeHit < 5) {
	        treeHit++;
	        System.out.println("나무를 "+ treeHit +"번 찍었습니다.");
	        if (treeHit == 5){
	            System.out.println("나무 넘어갑니다.");
	        }
	    }

        // 커피 자판기 만들어보기
        
        int coffee = 3;
        int money = 300;
        
        while(money > 0) {
            System.out.println(money + "원 받았습니다. 커피 드릴게요");
            coffee--;
            System.out.println("남은 커피는 "+coffee+"개 입니다.");
            
            if(coffee == 0){
                System.out.println("남은 커피가 "+coffee+"개로 판매 중지.");
                break;
            }
        }
        
        int a = 0;
        
        while(a < 10) {
            
            a++;
            if(a % 2 == 0) {
                continue; // 짝수인 경우 조건문으로 돌아간다.
            }
            
            System.out.println(a); // 홀수만 출력
        }
	}  
}
	    

