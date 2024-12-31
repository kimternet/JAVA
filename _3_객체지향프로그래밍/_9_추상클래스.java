/******************************************************************************

1. 추상 클래스(abstract class)

추상 클래스는 클래스와 인터페이스의 특징을 모두 가지는 특별한 클래스이다.
클래스처럼 필드와 메서드를 가질 수 있고, 
인터페이스처럼 구현되지 않은 메서드(추상 메서드)도 포함할 수 있다.

2. 주요특징

- 객체 생성 불가: 추상 클래스는 단독으로 객체를 생성할 수 없으며,
반드시 이를 상속한 클래스의 객체를 생성해야 한다.

- 추상 메서드 포함: abstract 키워드를 가진 메서드는 구현부가 없으며,
상속받은 클래스에서 반드시 구현해야 한다.

- 구현된 메서드 포함 가능: 추상 클래스는 일반 메서드도 포함할 수 있어,
상송받는 클래스에 기본 동작을 제공할 수 있다.

- 필드와 생성자 사용 가능: 인터페이스와 달리 객체 변수를 정의하고,
생성자를 사용할 수 있다.

3. 추상클래스의 필요성

- 기본 동작 제공: 여러 클래스에서 공통으로 사용하는 메서드의 기본 동작을 정의
- 강제 구현: 자식 클래스가 반드시 특정 메서드를 구현하도록 강제한다.
- 유연성: 인터페이스보다 더 많은 기능(필드, 생성자 등)을 제공하면서도,
추상 메서드를 통해 다형성을 구현할 수 있다.



*******************************************************************************/

// 추상 클래스 정의

abstract class Predator extends Animal {
    // 추상메서드
    abstract String getFood();
    
    //구현된 메서드
    void printFood() {
        System.out.printf("my food is %s\n", getFood());
    }
}

class Animal{
    String name;
    
    void setName(String name){
        this.name = name;
    }
}


// Tiger 클래스: Predator 추상클래스를 상속
class Tiger extends Predator implements Barkable{
    public String getFood(){
        return "apple";
    }
    
    public void bark() {
        System.out.println("어흥");
    }
}

// lion클래스: Predator 추상클래스를 상속
class Lion extends Predator implements Barkable{
    public String getFood(){
        return "banana";
    }
    
    public void bark(){
        System.out.println("으르렁");
    }
}

interface Barkable{
    void bark();
}


class Bouncer{
    void barkAnimal(Barkable animal){
        animal.bark();
    }
}



public class Main
{
	public static void main(String[] args) {
		Tiger tiger = new Tiger();
		Lion lion = new Lion();
		
		tiger.printFood();
		lion.printFood();
		
		Bouncer bouncer = new Bouncer();
		bouncer.barkAnimal(tiger);
		bouncer.barkAnimal(lion);
	}
}