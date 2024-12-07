/******************************************************************************
1. 집합(Set)

집합 자료형은 집합과 관련된 것을 쉽게 처리하기 위해 만든 것으로,
HashSet, TreeSet, LikedHashSet등이 있다.
이 중 가장 많이 사용하는 것은 HashSet이다.

집합 자료형의 2가지 특징

1. 중복 허용 x
2. 순서가 없다.

리스트나 배열은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있다.
하지만 집합 자료형은 순서가 없다. 따라서 인덱싱으로 값을 얻을 수 없다.
이는 마치 맵(Map)자료형과 비슷하다. 맵자료형 역시 순서가 없는 자료형이라
인덱싱을 지원하지 않는다.


TreeSet과 LinkedHashSet
집합 자료형의 특징은!? "순서가 없다."
그런데, 집합에 입력한 순서대로 데이터를 가져오거나,
오름차순으로 정렬된 데이터를 가져오고 싶을 수 있다.
이럴 때는 TreeSet과 LinkedHashSet을 사용한다.

TreeSet: 값을 오름차순으로 정열해 저장.
LinkedHashSet: 값을 입력한 순서대로 정렬.

*******************************************************************************/

import java.util.Arrays;
import java.util.HashSet;


public class Main
{
	public static void main(String[] args) {
	    
	    // 중복 X
		HashSet<String> set = new HashSet<>(Arrays.asList("H","e","l","l","o"));
		set.add("java"); // add로 추가가능
		set.add("study");
		set.add("enjoy");
		set.add("java1");
		set.addAll(Arrays.asList("my","dream")); // addAll 메소드로 한번에 추가 가능.
		set.remove("java1"); // remove메소드로  특정 값 제거
		System.out.println(set);
		
		// 제네릭스로 int를 사용하고 싶다면 int의  Wrapper클래스인 Integer를 대신 사용
		HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
		HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8, 9));
		
		// 교집합구하기
		
		HashSet<Integer> intersection = new HashSet<>(s1); // s1으로 intersection생성
		intersection.retainAll(s2); // 교집합 수행
		System.out.println(intersection);
		
		
		// 합집합 구하기
		HashSet<Integer> union = new HashSet<>(s1); //s1으로 union생성
		union.addAll(s2);
		System.out.println(union);
		
		// 차집합 구하기
		HashSet<Integer> substract = new HashSet<>(s1); // s1으로 substract생성
		substract.removeAll(s2); // 차집합 수행
		System.out.println(substract); 
		
		
	}
}