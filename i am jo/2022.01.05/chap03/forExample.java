	/*
		 arr�迭�� 10���� 120 ������ ���� ������ �� �迭�� ������ for�ݺ��� �̿��Ͽ� �Ʒ��� ���� ���
		 
		 	10  20  30  40
		 	50  60  70  80
		 	90 100 110 120
		 */

package chap03;

public class forExample {
	public static void main(String args[]) {
		int arr[][] = new int[3][4];
	
		for(int i = 0; value = 10; i < 3; i++) {
			for(int j = 0; j < 4; j++) {
				arr[i][j] =  value;
				value += 10;
				
			}
			
		}
		
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 4; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}
	}
}
