//����ʵ带 ����ϴ� ���α׷�
package chap05;

public class StaticFieldExample2 {
	public static void main(String args[]) {
		LimitedValue v = new LimitedValue();
		v.setValue(200000);
		System.out.println("v.value = " + v.value);
		System.out.println("���Ѱ� = " + LimitedValue.UPPER_LIMIT);
		}
		}