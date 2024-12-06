/******************************************************************************
1. 맵(MAP)

tkfkadmf '이름 = 홍길동', '생일 = 몇 월 며칠' 등으로 구분할 수 있듯,
맵(Map)은 대응 관계를 쉽게 표현할 수 있게 해주는 자료형이다.

맵안 다른 언어에도 있는 자료형으로 associative array or hash라고도 불린다.

맵은 사전(dictionary)과 비슷하다. 예를들어 people이란 단어에는 사람, 
baseball이라는 단어에는 야구라는 뜻이 부합되듯이 맵은 키(key)와 값(value)를 한쌍으로 갖는다.

맵은 리스트나 배열처럼 순차적으로(sequential) 요솟값을 구하지 않고 키(key)를 이용해 값(value)을 얻는다. 
우리가 baseball이란 단어의 뜻을 찾을 때 사전의 1쪽부터 모두 읽지 않고 baseball이라는 단어가 있는 곳을 찾아 확인하는 것과 같다.

맵 자료형에는 HashMap, LinkedHashMap, TreeMap 등이 있다.


1. HashMap
- put
- get
- containsKey
- remove
- size
- keySet



LinkedHashMap과 TreeMap
맵의 가장 큰 특징은 순서에 의존하지 않고 key로 value를 가져오는 것이다. 
그런데 가끔 Map에 입력된 순서대로 데이터를 가져오거나 입력한 key에 의해 정렬(sort)하도록 저장하고 싶을 수 있다. 이럴때는 LinkedHashMap과 TreeMap을 사용하면 된다.

LinkedHashMap : 입력된 순서대로 데이터를 저장한다.
TreeMap : 입력된 key의 오름차순으로 데이터를 저장한다.

*******************************************************************************/

import java.util.HashMap;

public class Main
{
	public static void main(String[] args) {
		
		// Hashmap 역시 제네릭스를 이용한다.
		// hashmap의 제네릭스는 key, value 모두 string 자료형이다.
		// 따라서 key, value에 String 이외의 자료형은 사용할 수 없다.
		HashMap<String, String> map = new HashMap<>();
		map.put("people", "사람");
		map.put("baseball", "야구"); // put
		
		System.out.print(map.get("people")); // get
		System.out.print(map.get("java")); // null 출력
		System.out.print(map.getOrDefault("java", "자바")); // getOrDefault를 사용하면 자바 출력
		
		//containskey
		System.out.println(map.containsKey("people")); // true출력
		
		// remove 맵의 항목을 삭제
		// 해당 key의 항목을 삭제하고 value값을 리턴한다.
		System.out.println(map.remove("people"));
		
		//size 메소드는 맵 요소의 개수를 리턴한다.
		System.out.println(map.size());
		
		map.put("people","사람");
		
		//keset()메소드는 맵의 모든 key를 모아서 리턴한다.
		System.out.println(map.keySet());
	}
}