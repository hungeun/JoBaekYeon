/*��� �ʵ�(�Ǵ� ��� ����) : static�� final Ű���尡 ��� ���� �ʵ� �� �ʱⰪ�� �ٲ� �� �����Ƿ� ����� ����ϱ⿡ ����
		
		��� �ʵ尡 �ִ� Ŭ����
 */
package chap05;

public class LimitedValue {
	final static int UPPER_LIMIT = 100000;
	int value;
	
	void setValue(int value) {
		if (value < UPPER_LIMIT)
			this.value = value;
		else
			this.value = UPPER_LIMIT;
	}
	}
