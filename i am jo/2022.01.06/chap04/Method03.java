//reture�� x
package chap04;

public class Method03 {
	public static void main(String args[]) {
		printCharacter('*', 30);
		System.out.println("Hello, Java");
		printCharacter('-', 30);
		}
		static void printCharacter(char ch, int num) {
		for (int cnt = 0; cnt < num; cnt++)
		System.out.print(ch);
		System.out.println();
		return;
		}
	}// 1.printCharacter �޼����� static �����ڸ� �����ϼ���.
/*
 * void printCharacter(char ch, int num){
 * 
 * for (int cnt=0; cnt<num; cnt++)
 * Sysytem.out.print(ch);
 * 
 * System.out.println();
 * }
 */