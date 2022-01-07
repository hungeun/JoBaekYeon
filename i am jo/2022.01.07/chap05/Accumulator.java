//정적 필드(static field) : static 키워드가 붙은 필드  - 정적 필드가 있는 클래스
package chap05;

public class Accumulator {
	int total = 0;
	static int grandTotal = 0; // 정적 필드를 선언하는 선언문
	void accumulate(int amount) {
	total += amount;
	grandTotal += amount; // 정적 필드를 사용하는 명령문
	}
	}
