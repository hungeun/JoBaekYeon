/*
 * ���� �޼ҵ�(static method) : static Ű���尡 ���� �޼ҵ�
		���� �޼ҵ带 �����ϴ� Ŭ����
 */
package chap05;

public class Accumulator01 {
	int total = 0;
	static int grandTotal = 0;
	void accumulate(int amount) {
	total += amount;
	grandTotal += amount;
	}
	static int getGrandTotal() { // ���� �޼ҵ� ����
	return grandTotal;
	}
	}