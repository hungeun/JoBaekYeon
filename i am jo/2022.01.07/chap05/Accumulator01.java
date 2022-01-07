/*
 * 정적 메소드(static method) : static 키워드가 붙은 메소드
		정적 메소드를 포함하는 클래스
 */
package chap05;

public class Accumulator01 {
	int total = 0;
	static int grandTotal = 0;
	void accumulate(int amount) {
	total += amount;
	grandTotal += amount;
	}
	static int getGrandTotal() { // 정적 메소드 선언
	return grandTotal;
	}
	}