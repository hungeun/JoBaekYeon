//���� �ʵ�(static field) : static Ű���尡 ���� �ʵ�  - ���� �ʵ尡 �ִ� Ŭ����
package chap05;

public class Accumulator {
	int total = 0;
	static int grandTotal = 0; // ���� �ʵ带 �����ϴ� ����
	void accumulate(int amount) {
	total += amount;
	grandTotal += amount; // ���� �ʵ带 ����ϴ� ��ɹ�
	}
	}
