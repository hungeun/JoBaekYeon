//정적 메소드를 호출하는 프로그램
package chap05;

public class StaticMethodExample1_1 {
	public static void main(String args[]) {
		Accumulator obj1 = new Accumulator();
		Accumulator obj2 = new Accumulator();
		obj1.accumulate(10);
		obj2.accumulate(20);
		int grandTotal = Accumulator.getGrandTotal();
		System.out.println("obj1.total = " + obj1.total);
		System.out.println("obj2.total = " + obj2.total);
		System.out.println("총계 = " + grandTotal);
		}
		}
