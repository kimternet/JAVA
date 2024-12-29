/******************************************************************************

1. 인터페이스

인터페이스가 중요한 이유는,
예시의 ZooKeeper 클래스가 동물 클래스에 의존적인 클래스에서,
동물 클래스와 상관없는 독립적인 클래스가 되었다는 점이다.

Predator 인터페이스 대신 Animal 클래스에 getFood 메서드를 추가하고 
Tiger, Lion 등에서 getFood 메서드를 오버라이딩한 후 
Zookeeper의 feed 메서드가 Predator 대신 Animal을 입력 자료형으로 사용해도 동일한 효과를 거둘 수 있다. 
하지만 상속은 자식 클래스가 부모 클래스의 메서드를 오버라이딩하지 않고 사용할 수 있기 때문에 
해당 메서드를 반드시 구현해야 한다는 ‘강제성’을 갖지 못한다. 그래서 상황에 맞게 상속을 사용할 것인지, 
인터페이스를 사용해야 할지를 결정해야 한다. 
인터페이스는 인터페이스의 메서드를 반드시 구현해야 하는 강제성을 갖는다는 점을 반드시 기억하자.


*******************************************************************************/


interface Predator {
    
    // 인터페이스는 '규칙'이기 때문에
    // 이름과 입출력에 대한 정의만 있고, 내용은 없다.
    // 즉, getFood 메서드는 인인터페이스는
    // implements한 클래스들이 강제적으로 구현해야 하는 규칙이 된다.
    
    String getFood();
    
    // 자바8 이후부터는 디폴트 메서드(default method)를 사용할 수 있다.
    // 인터페이스의 메서드는 구현체를 가질 수 없지만,
    // 디폴트 메서드를 사용하면 실제 구현된 형태의 메서드를 가질 수 있다.
    
    // 이렇게 Predator인터페이스에 printFood 디폴트 메서드를 구현하면,
    // Predator 인터페이스를 구현한 Tiger, Lion 등의 실제 클래스는,
    // printFood메서드를 구현하지 않아도 사용할 수 있다.
    // 그리고 디폴트 메서드는 오버라이딩이 가능하다.
    // 즉, printFood메서드를 실제 클래스에서 다르게 구현하여 사용할 수 있다.
    default void printFood() {
        System.out.printf("my food is %s\n", getFood());
    }
    
}

class Animal {
    String name;
    
    void setName(String name){
        this.name = name;
    }
    
}

class Tiger extends Animal implements Predator {
    
    public String getFood(){
        return "apple";
    }
    
}

class Lion extends Animal implements Predator {
    public String getFood() {
        return "banana";
    }
    
}

class ZooKeeper {
    
    // 메서드 오버로딩
    // 입력값의 자료형 타입이 다르지만,
    // 메서드명은 동일한 것.
    
    // 변경전
    
    // void feed(Tiger tiger){
    //     System.out.println("feed apple");
    // }
    
    // void feed(Lion lion) {
    //     System.out.println("feed banana");
    // }

    // 인터페이스 변경 후
    
    // tiger, lion은 각각 Tiger, Lion의 객체이기도 하지만,
    // Predator 인터페이스의 객체익디ㅗ 하다.
    // 따라서 Predator를 자료형으로 사용할 수 있는 것이다.
    // 어떤 육식동물 클래스가 추가되더라도,
    // ZooKeeper는 feed메서드를 추가할 필요가 없다.
    
    void feed(Predator predator) {
        System.out.println("feed" + predator.getFood());
    }
    
}


public class Main
{
	public static void main(String[] args) {
		ZooKeeper zooKeeper = new ZooKeeper();
		Tiger tiger = new Tiger();
		Lion lion = new Lion();
		zooKeeper.feed(tiger); 
		zooKeeper.feed(lion);
	}
}