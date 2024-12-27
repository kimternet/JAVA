/******************************************************************************

1. 생성자(constructor)

정의: 생성자는 객체가 생성될때 호출되며, 클래스의 이름과 동일한 특별한 메서드이다.

특징:
 - 반환 타입이 없다(void도 쓰지 않는다.)
 - 객체의 필드를 초기화하거나, 객체 생성 시 필요한 작업을 수행한다.
 - 명시적으로 생성자를 정의하지 않으면, 컴파일러가 자동으로 "기본 생성자"를 제공한다.

*******************************************************************************/

class Person {
    // 필드
    private String name;
    private int age;

    // 기본 생성자
    public Person() {
        this.name = "Unknown";
        this.age = 0;
        System.out.println("기본 생성자가 호출되었습니다.");
    }

    // 매개변수가 있는 생성자
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
        System.out.println("매개변수가 있는 생성자가 호출되었습니다.");
    }

    // 생성자 오버로딩
    public Person(String name) {
        this(name, 20); // 다른 생성자 호출
        System.out.println("오버로딩된 생성자가 호출되었습니다.");
    }

    // Getter
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}

public class Main {
    public static void main(String[] args) {
        // 기본 생성자 호출
        Person person1 = new Person();
        System.out.println("Name: " + person1.getName() + ", Age: " + person1.getAge());

        // 매개변수가 있는 생성자 호출
        Person person2 = new Person("Alice", 30);
        System.out.println("Name: " + person2.getName() + ", Age: " + person2.getAge());

        // 오버로딩된 생성자 호출
        Person person3 = new Person("Bob");
        System.out.println("Name: " + person3.getName() + ", Age: " + person3.getAge());
    }
}
