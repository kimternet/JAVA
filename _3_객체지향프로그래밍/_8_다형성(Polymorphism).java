/******************************************************************************

1. 다형성(Polymorphism)

다형성이란, 하나의 객체가 여러가지 형태를 가질 수 있는 성질을 말한다.
부모 클래스(혹은 인터페이스)를 통해 자식 클래스(혹은 구현체)의 메서드를 호출할 수 있는 유연성을 제공한다.

왜 다형성이 필요할까?

코드의 유연성 - 새로운 객체(클래스)를 추가해도 기존 코드를 수정하지 않아도 된다.
가독성 향상 - 복잡한 분기문을 단순화할 수 있다.
유지보수 용이 - 변경이 필요한 부분을 최소화할 수 있다.


핵심

- 부모 클래스 타입(또는 인터페이스)으로 자식 객체를 참조할 수 있다.
- 인터페이스는 다형성을 더 잘 지원하며, 메서드 호출 시 해당 객체의 구현된 메서드가 실행된다.
- 코드를 확장 가능하게 만들어 유지보수를 쉽게 한다.

*******************************************************************************/

//인터페이스 정의

interface Barkable {
    void bark(); // 추상 메서드
}

// Animal 클래스 정의

class Animal {
    String name;
    
    void setName(String name){
        this.name=name;
    }
}


// Tiger 클래스: Animal을 상속받고 Barkable 인터페이스 구현.
class Tiger extends Animal implements Barkable {
    public void bark() {
        System.out.println("어흥");
    }
}


class Lion extends Animal implements Barkable {
    public void bark() {
        System.out.println("으르렁");
    }
}

// Bouncer 클래스: 다형성 활용

class Bouncer {
    void barkAnimal(Barkable animal){
        animal.bark();
    }
}


public class Main
{
	public static void main(String[] args) {
		Tiger tiger = new Tiger();
		Lion lion = new Lion();
		
		Bouncer bouncer = new Bouncer();
		bouncer.barkAnimal(tiger); 
		bouncer.barkAnimal(lion);
	}
}