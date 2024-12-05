/******************************************************************************
====================================================
1. 문자
=====================================================

문자 자료형은 char를 이용

많이 사용하는 편은 아니지만, 문자값을 표현하는 다양한 방식이 존재하므로
사용할 때 주의해야 한다.


====================================================
2. 문자열
====================================================

"Happy Java"
"a"
"123"

문자열은 위 처럼 문자로 구성된 문장을 뜻한다.

자바에서는 "String"으로 문자열을 표현

리터럴 표기 방식 이해하기
String a = "Happy Java" 와 String b = new String("Happy Java")에서 a, b 변수는 같은 문자열 값을 갖게 되지만 완전히 동일하지는 않다. 
첫 번째 코드는 리터럴(literal) 표기 방식이라고 하는데 고정된 값을 그대로 대입하는 방법을 말한다. 
이와 달리 두 번째 방식은 항상 새로운 String 객체를 만든다.

====================================================
3. 원시 자료형
====================================================

int, long, double, float, boolean, char 자료형을 원시(primitive) 자료형이라 한다.
이런 원시 자료형은 *new 키워드로 값을 생성할 수 없다.*
원시 자료형은 리터럴 표기 방식으로만 값을 세팅할 수 있다.

** 반드시 기억할 것 **
String은 리터럴 표기 방식을 사용할 수 있지만,
원시 자료형에 포함되지 않는다.
즉, String은 리터럴 표기 방식을 사용할 수 있도록 자바에서 특별 대우해 주는 자료형.


====================================================
4. Wrapper 클래스
====================================================

int, long, double, float, boolean, char 등의 원시 자료형에는 
각각 그에 대응하는 Wrapper 클래스가 있다.

int = Integer
long = Long
double = Double
float = Float
boolean = Boolean
char = Character

** 멀티스레드 환경에서 동기화를 지원하려면, **
** 원시 자료형 대신 Wrapper 클래스를 사용해야한다.**

====================================================
5. 문자열 내장 메서드드
====================================================

String 자료형의 내장 메서드는 문자열 객체에 속한 함수라 할 수 있다.
문자열 합치기, 분할, 대소문자 변환 등의 문자열을 다양하게 활용할 수 있도록
도와주는 역할을 한다.

String 자료형의 내장 메서드 중 자주 사용하는 것들.

1. equals = 문자열 2개가 같은지 비교하여 결괏값을 리턴(반환하는 작업업), 문자열 값을 비교할 때는  반드시 equals를 사용!
2. indexOf = 문자열에서 특정 문자열이 시작되는 위치(인덱스값)을 리턴
3. contains = 문자열에서 특정 문자열이 포함되어 있는지 여부를 리턴
4. charAt = 문자열에서 특정 위치의 "문자"를 리턴.
5. replaceAll = 문자열에서 특정 문자열을 다른 문자열로 바꿀 때 사용.
6. substring = 문자열에서 특정 문자열을 뽑아낼 때 사용.
7. toUpperCase = 문자열을 모두 대문자로 변경할 때 사용.
8. toLowerCase는 소문자
9. split = 문자열을 특정한 구분자로 나누어 문자열 배열로 리턴.
*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	    
	   String a = "Happy Java"; // 문자열의 앞과 뒤는 쌍따옴표로 감싼다.
	   String b = "a";
	   String c = "123";
	   
	   // 아래와 같이 표현도 가능
	   
	   // new 키워드는 객체를 만들 때 사용한다.
	   // 문자열은 가급적 리터럴(literal)표기 방식을 사용하는 게 좋다.
	   // 가독성도 좋고, *컴파일할 때 최적화에 도움을 주기 때문*
	   String a1 = new String("Happy Java");
	   String b2 = new String("a");
	   String c3 = new String("123");
	   
	   // 원시 자료형 리터럴 
	   boolean result = true;
	   char A = 'A';
	   int i = 100000;
	   
	   // equals
	   
	   String aa = "hello";
	   String bb = "java";
	   String cc = "hello";
	   String dd = "1java";
	   int ddd = 1;
	   
	   String aaa = "hello";
	   String bbb = new String("hello");
	   
	   System.out.println(aa.equals(bb)); // false 출력
	   System.out.println(aa.equals(cc)); // true 출력
	   
	   // == 연사자를 사용하면 false 리턴
	   // 서로 값은 같지만 다른 객체이기 때문!!
	   // == 은 2개의 자료형이 같은 객체인지를 판별할 때 사용하는 연산자.
	   System.out.println(aaa.equals(bbb)); // true
	   System.out.println(aaa==bbb); // false
	   
	   // indexOf
	   System.out.println(aa.indexOf("lo")); // 3출력
	   
	   // contains
	   System.out.println(aa.contains("h")); //true
	   
	   // charAt
	   System.out.println(aa.charAt(4)); // "o" 출력
	   System.out.println(dd.charAt(0)); // 1 "문자열 1"
	   //System.out.println(ddd.charAt(0)); // error 숫자형은 반환 x
	   
	   //replaceAll
	   System.out.println(aa.replaceAll("h","j")); // "hello" -> "jello"
	   
	   // substring(시작위치, 끝위치) 끝 위치 문자는 포함 x
	   System.out.println(aa.substring(0,2));
	   
	   // toUpperCase는 대문자자 -> toLowerCase는 소문자
	   System.out.println(aa.toUpperCase()); //HELLO
	   
	   // split 특정한 구분자로 나누어 문자열 배열로 리턴
	   String sp = "a:b:c:d:e";
	   String[] splitresult = sp.split(":");
	   
	   for(String s: splitresult){
	       System.out.println(s);
	   }
	    
	}
}