/******************************************************************************

1. FOR문

for문도 while문과 마찬가지로 문장을 반복해서 수행해야 할 경우 사용.


- 기본구조

for(초기치; 조건문; 증가치){
    ...
}


*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
		
    String[] numbers = {"one","two","three"};
    
    for (int i = 0; i < numbers.length; i++){
        System.out.println(numbers[i]);
    }
    
    int[] score ={60, 80, 20, 30, 10};
    
    // i값이 0부터 시작하여 1씩 증가하며 for문 수행.
    for(int j = 0; j < score.length; j++){
        
        if(score[j] >= 60){ //score[j]가 아닌 그냥 j랑 혼동 x
            System.out.println((j+1) + "번 합격");
        }else{
            System.out.println((j+1) +"번 불합격");
        }
    }
    
    // continue로 합격 학생만 출력하기.
    
    for (int j = 0; j < score.length; j++){
        if(score[j] < 60){
            continue;
        }
        System.out.println((j+1)+"번 학생 합격");
    }
    
    // 이중 for문으로 구구단 만들기
    
    for (int x = 2; x < 10; x++){
        for(int y = 1; y < 10; y++){
            System.out.print(x*y+" "); // 공백
        }
        System.out.println(""); //줄바꿈
        
    }
		
    }
}