/******************************************************************************

1. 상속

자바에는 자식 클래스가 부모 클래스의 기능을 그대로 물려받을 수 있는
상속(inheritance)기능이 있다.

2. 자식클래스의 기능 확장하기

보통 부모클래스를 상속받은 자식 클래스는 부모 클래스의 기능에 더하여
좀 더 많은 기능을 갖도록 작성할 수 있다.

3. IS-A 관계란?

자식클래스는 부모클래스를 상속했다.
즉, 자식클래스는 부모클래스의 하위 개념이라고 할 수 있다.
예로 Dog은 Animal에 포함되기 때문에,
'Dog은 Animal이다.'라고 표현할 수 있다.
이러한 관계를 IS-A 관계라고 표현한다.

이렇게 IS-A 관계(상속관계)에 있을 때 자식 클래스의 객체는
부모 클래스의 자료형인 것처럼 사용할 수 있다.

아래와 같이 코딩을 할 수 있는데,
주의할 점은 Dog 클래스에만 존재하는 메서드를 사용할 수 없다.
아래와 같은 경우 Animal 크래스에 구현된 setName메서드만 사용이 가능하다.

Animal dog = new Dog(); // Dog is a Animal

하지만 이 반대의 경우, 부모 클래스로 만들어진 객체를
자식 클래스의 자료형으로 사용할 수 없다.
따라서 아래의 코드는 컴파일 오류가 발생한다.

Dog dog = new Animal(); // 컴파일 오류


4. Object 클래스란?

자바에서 만드는 모든 클래스는 Object 클래스를 상속받는다.
자바에서 만들어지는 모든 클래스는 Object 클래스를 자동으로 상속받게 되있다.
따라서 자바에서 만든 모든 객체는 Object 자료형으로 사용할 수 있다.

5. 메서드 오버라이딩(method overriding)

부모클래스의 메서드를 자식 클래스가 동일한 형태로
또 다시 구현하는 행위를 메서드 오버라이딩(method overriding)이라고 한다.
메서드 덮어쓰기라고도 한다.

6. 메서드 오버로딩(method overloading)

동일한 이름의 메서드를 또 생성할 수 있다.
단, 입력항목이 다른경우!


7. 다중 상속이란?

다중 상속은 클래스가 동시에 하나 이상의 클래스를 상속받는 것을 뜻한다.
자바는 다중 상속을 지원하지 않는다.
파이썬과 같이 다중 상속을 지원하는 언어들은
동일한 메서드를 상속받는 경우 우선순위를 정하는 규칙이 있다.


*******************************************************************************/



class Animal{
    String name;
    
    void setName(String name){
        this.name = name;
    }
}

// 클래스 상속을 위해서는 extends라는 키워드를 사용한다.
// 이제 Dog 클래스는 Animal 클래스를 상속하게 되었다.
// Dog 클래스에 객체 변수인 name과 메서드인 setName을 만들지 않았지만,
// Animal 클래스를 상속했기 때문에 예제에서 보듯이 그대로 사용이 가능하다.

class Dog extends Animal {
    // sleep 메서드를 추가하기
    void sleep() {
        System.out.println(this.name+" zzz");
    }
    
}

// 메서드 오버라이딩
class HouseDog extends Dog{
    
    void sleep(){
        System.out.println(this.name + " zzz in house");
    }
    
    
    // 이미 sleep이라는 메서드가 있지만, 동일한 이름의 sleep 메서드를 또 생성가능하다.
    // 단, 메서드의 입력 항목이 다를 경우만 가능하다.
    // 입력 항목이 다른 경우 동일한 이름의 메서드를 만들 수 있는데,
    // 이를 메서드 오버로딩이라고 부른다.
    
    void sleep(int hour){
        System.out.println(this.name + " zzz in house for " + hour + " hours");
    }
}


public class Main
{
	public static void main(String[] args) {
	    Dog dog = new Dog();
	    dog.setName("poppy");
	    System.out.println(dog.name);
	    dog.sleep(); // sleep 메서드 추가 출력
	    
	    HouseDog houseDog = new HouseDog();
	    houseDog.setName("happy");
	    houseDog.sleep(); // happy zzz 출력
	    houseDog.sleep(3); 
	
	}
}

