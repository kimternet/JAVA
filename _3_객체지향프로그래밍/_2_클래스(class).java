/******************************************************************************

1. 클래스와 객체


객체와 인스턴스의 차이는?

클래스에 의해 만들어진 "객체"를 "인스턴스"라고 한다.

Animal cat = new Animal() -> 여기서 만들어진 "cat"은 객체이자 Animal의 "인스턴스"이다.

인스턴스라는 말은 특정 객체(여기서는 cat)가 어떤 클래스의 객체인지를 관계 위주로 설명할 때 사용된다.

*****
즉, 'cat은 인스턴스' 보다 'cat은 객체'라는 표현이,

'cat은 Animal의 객체'보다 'cat은 Animal의 인스턴스'라는 표현이 훨씬 잘 어울린다.
*****


2. 메서드(Method)란?

메서드는 클래스 내에 구현된 함수를 말한다.

객체 변수에 값을 할당하기 위해 객체 변수에 값을 대입하는 방법은 여러가지가 있다.


3. 객체 변수는 공유되지 않는다.
클래스에서 가장 중요한 부분은 "객체 변수의 값이 독립적으로 유지" 된다는 점이다.

객체 지향적(object oriented)라는 말의 의미도
결국, 객체 변수의 값이 독립적으로 유지되기 때문에 가능한 것이다.

*******************************************************************************/

// 보통 클래스는 특별한 경우가 아니라면,
// 파일 단위로 하나씩 작성한다.

// 다른 파일에 있다고 가정.
class Animal {
    
    // 클래스에 선언된 변수를 객체 변수(instance variable)이라고 한다.
    // 인스턴스변수, 멤버 변수, 속성이라고도 한다.
    String name;
    
    // setName 메서드를 추가
    
    // 입력 : String name
    // 출력 : void('리턴값 없음'을 의미)
    // 즉, 입력으로 name이라는 문자열을 받고, 출력은 없는 형태의 메서드. 
    public void setName(String name){ 
        this.name = name;
    }
    
}

public class Main
{
	public static void main(String[] args) {
	    

	    Animal cat = new Animal();
	    
	    // 객체 변수에 접근하기 위해 . 도트 연산자로 접근하던 것처럼
	    // 객체가 메서드를 호출하기 위해서는 '객체.메서드' 로 호출해야한다.
        cat.setName("boby");
	    System.out.println(cat.name); // boby 출력
	    
	    // 객체 변수는 공유되지 않는다!
	    // 만약 이런경우 happy는 나중에 수행되므로
	    // cat.name의 값도 happy라는 값으로 변경되지 않을까?
	    Animal dog = new Animal();
	    dog.setName("happy"); 
	    
	    // 확인
	    
	    System.out.println(cat.name); // boby 출력
	    System.out.print(dog.name); // happy 출력
	    /*
	    
	    확인 결과
	    name 객체 변수는 공유되지 않는다는 것을 확인.
	    *** 매우 중요하다 ***
	    클래스에서 가장 중요한 부분은 <<"객체 변수의 값이 독립적으로 유지">> 된다는 점이다.
	    바로 이러한 점이 클래스 존재의 이유이기도 하다.
	    
	    하지만 static을 이용하면 객체 변수를 공유하도록 만들 수 있다.
	    
	    */
	    


	}
}