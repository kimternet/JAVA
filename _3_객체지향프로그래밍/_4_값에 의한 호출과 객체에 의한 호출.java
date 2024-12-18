/******************************************************************************

1. 값에 의한 호출과 객체에 의한 호출

메서드에 값(원시 자료형)을 전달하는 것과 객체를 전달하는 것에는 큰 차이가 있다.
이것은 매우 중요하다.

메서드에 객체를 전달할 경우 메서드에서 객체 변수의 값을 변경할 수 있다.


*******************************************************************************/

//Updater 클래스는 전달받은 숫자를 1만큼 증가시키는 
// update라는 메서드를 가지고 있다.

class Updater {
    void update(int count){
        count++;
    }
}

// Counter클래스는 count라는 객체변수를 가지고 있다.
// Main클래스의 main메서드는 Counter클래스에 의해 생성된 myCounter객체의 겍체변수인
// count값을 Updater클래스를 이용하여 증가시키고자 한다.
// 하지만 실행해보면 예상과다르다.

class Counter{
    int count = 0; // 객체변수
}

public class Main
{
	public static void main(String[] args) {
		Counter myCounter = new Counter();
		System.out.println("before update:" + myCounter.count);
		
		
		Updater myUpdater = new Updater();
		myUpdater.update(myCounter.count);
		System.out.println("after update:"+myCounter.count);
	}
}

// 예상과 다른 이유는, 객체 변수 count의 값을
// update메서드에 넘겨서 변경시키더라도 값에 변화가 없다.
// 이유는 update메서드는 값을 (int 자료형)을 전달받았기 때문이다.

// 아래와 같이 변경하면 된다.
// 차이점은!
// update 메서드의 입력항목에 있다.
// 이전에는 int count와 같이 값을 전달받았다면,
// 지금은 Counter counter와 같이 객체를 전달받도록 변경한 것이다.
// update 메서드를 호출하는 부분도 다음처럼 바뀌었다.

class Updater {
    void update(Counter counter) {
        counter.count++;
    }
}

class Counter {
    int count = 0; // 객체 변수
}


public class Main {
    public static void main(String[] args){
        Counter myCounter = new Counter();
        System.out.println("before update:"+myCounter.count);
        Updater myUpdater = new Updater();
        myUpdater.update(myCounter);
        System.out.println("after update:"+myCounter.count);
    }
}

// MyCounter 객체의 count값이 1만큼 증가되었다.
// 이렇게 메서드의 입력으로 객체를 전달하면 메서드가 입력받은 객체를
// 그대로 사용하기 때문에 메서드가 객체의 속성값을 변경하면, 
// 메서드 수행 후에도 객체의 변경된 속성값이 유지된다.