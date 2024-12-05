/******************************************************************************

===============

1. 리스트(List)

================

리스트는 배열과 비슷하지만 편리한 기능이 더 많은 자료형이다.
가장 큰 차이점은, 배열은 크기가 정해져 있지만, 리스트는 변한다는 데 있다.
예로 배열의 크기를 10개로 정했다면, 10개를 초과하는 값을 담을 수 없다.
하지만 리스트는 크기가 정해져 있지 않아, 원하는 만큼값을 담을 수 있다.

자료나 값이 많아질수록 리스트는 점점 커진다.

언제사용?
-> 값의 크기를 알 수 있는 경우도 있지만, 명확하지 않을때가 있다.
자료형의 개수가 계속 변하는 상황이라면 리스트를 사용해야 한다.
예로 어부가 바다에 나가서 물고기를 포획한다고 생각하면
10마리를 잡을지, 100마리를 잡을지 모른다.
이럴 때 리스트를 사용해야 한다.

2. 리스트 자료형
리스트 자료형에서 일반적으로 사용하는 ArrayList가 있다.
외에 Vector, LinkedList 등이 있다.
=============
Arraylist
=============
1. add - 요솟값을 추가
2. get - 특정 인덱스의 값을 추출
3. size - ArrayList의 요소의 개수를 리턴한다.
4. contains - 리스트 안에 해당 항목이 있는지 판별해, 그 결과를 boolean으로 리턴
5. remove 메소드는 2가지 방식이 있다.
- remove(객체)
- remove(인덱스)
이름은 같지만, 입력하는 파라미터가 다르다.


===============

2. 제네릭스

================

제네릭스는 자바 J2SE 5.0 버전 이후 도입된 개념이다.
자료형을 안전하게 사용할 수 있도록 만들어 주는 기능.
제네릭스를 사용하면 강제로 바꿀 때 생길 수 있는 캐스팅 오류를 줄일 수 있다.

일반적인 방식: ArrayList<String> pitches = new ArrayList<String>();
선호되는 방식: ArrayList<String> pitches = new ArrayList<>();

====================
도입 전후의 차이는??
====================

ArrayList 자료형 다음에 <String>이 있는가에 있다.
제네릭스를 표현한 <String>은 'ArrayList'에 담을 수 있는 자료형은 String뿐이란 뜻.
즉, 제네릭스를 이용하면 자료형을 좀 더 명확하게 체크할 수 있다는 장점이 있다.

==================
리스트 정렬하기
==================

sort 메서드는 정렬 기준을 파라미터로 전달해야 한다. 오름차순, 내림차순
오름차순(순방향)- Comparator.naturalOrder()
내림차순(역방향)- Comparator.reverseOrder()

*******************************************************************************/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class Main
{
	public static void main(String[] args) {
		
		ArrayList pitches = new ArrayList();
		pitches.add("138");
		pitches.add("129");
		pitches.add("142");
		
		pitches.add(0,"133"); //첫번째 위치에 133 삽입.
		
		System.out.println(pitches.get(1));
		System.out.println(pitches.size());
		System.out.println(pitches.contains("142"));
		
		// 2가지 remove 메소드 방식
		System.out.println(pitches.remove("129")); // 129 삭제 후 true 리턴
		System.out.println(pitches.remove(0)); // pitches 첫 번째 항목이 133이므로, 133을 삭제하고 133을 리턴 
        
        // 제네릭스를 사용하지 않은 예
        ArrayList pitches2 = new ArrayList();
        pitches2.add("144");
        pitches2.add("155");
        
        
        // 제네릭스를 사용하지 않으면 ArrayList에 추가하는 객체는 Object 자료형으로 인식된다.
        // Object 자료형은 모든 객체가 상속하고 있는 가장 기본적인 자료형이다.
        // 따라서 ArrayList 객체인 pitches에 값을 넣을 때는 문제가 없지만,
        // 값을 가져올 때는 매번 Object 자료형에서 String 자료형으로 형 변환(casting)을 해야한다.
        String one = (String) pitches2.get(0);
        String two = (String) pitches2.get(1); //Object 자료형을 String 자료형으로 형 변환
        // 주의할 점은 String외 다른 객체도 넣을 수 있어서 형 변환 오류가 발생할 수 있다.
        
        
        
        // 제네릭스 사용한 예
        
        ArrayList<String> pitches3 = new ArrayList<>();
        pitches.add("155");
        pitches.add("130");
        
        String one1 = pitches3.get(0); // 형 변환이 필요 없음.
        String two2 = pitches3.get(1);
        // 컴파일러가 이미 알기 때문에,
        // 불필요한 코딩을 줄일 수 있고, 잘못된 형 변환 때문에 발생하는
        // 런타임 오류를 방지할 수 있다.
        
        // 다양한 방법으로 ArrayList만들기
        
        ArrayList<String> fishes = new ArrayList<>();
        fishes.add("갈치");
        fishes.add("고등어");
        fishes.add("광어");
        
        System.out.println(fishes);
        
        // 이미 문자열 배열이 존재한다면, ArrayList를 좀 더 편하게 생성할 수  있다.
        
        String[] data = {"김","박","이"};
        ArrayList<String> names = new ArrayList<>(Arrays.asList(data));
        
        System.out.println(names);
        
        // 1. String 배열 대신 String 자료형을 여러개 전달하여 생성
        // 2. , 로 구분해서 1개의 문자열로 만들기
        ArrayList<String> names2 = new ArrayList<>(Arrays.asList("최","금","정"));
        String result = "";
        for (int i = 0; i < names2.size(); i++){
            result += names2.get(i);
            result += ","; // 콤마를 추가
        }
        result = result.substring(0, result.length() - 1); // 마지막 콤마 제거
        System.out.println(result);
        
        // String.join을 사용하여 간단하게 처리하기.
        
        ArrayList<String> names3 = new ArrayList<>(Arrays.asList("김","나","박","이"));
        String result2 = String.join(",", names3);
        names3.sort(Comparator.naturalOrder()); // sort 오름차순 정렬
        System.out.println(result2);
        
        
        
	}
}