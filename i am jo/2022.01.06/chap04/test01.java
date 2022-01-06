/*
 * 중첨 for 문을 사용하여 다음의 수평 구구단을 출력 하세요.
 * [2단] 	[3단]	[4단]	[5단] 	[6단]	[7단]	[8단]	[9단]
 */
package chap04;

public class test01 {
	public static void main(String args[]) {
		System.out.println("\n\t 중첩 for 문을 사용하여 다음의 수평 구구단을 출력하세요.");
		System.out.println("\t 단, 외부와 내부 각 하나씪의 for문을 사용하세요\n");
		
		for(int num = 0; num < 10; num++) {
			for(int dan = 2; dan < 10; dan++) {
				if(num == 0) {
					System.out.printf("[%d 단\t",dan);
					
				}
				else 
			}
		}
	}
}
