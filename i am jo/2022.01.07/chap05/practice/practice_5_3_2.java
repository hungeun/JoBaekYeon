package chap05.practice;

import java.util.Random;

public class practice_5_3_2 {
	
	public static void main(String[] args) {
		
		 Random random = new Random();
		 random.setSeed(System.currentTimeMillis()); 
		 
		 int lotto[] = new int[6];

		 
		 for(int i = 0; i < 6; i++) {
			 lotto[i] = random.nextInt(45) + 1;
			 
			 for(int j = 0; j < i; j++) {
				 
				 if(i == 0)
					 break;
				 if(lotto[i] == lotto[j]) {
					 i--;
				 }
			 }
		 }
		 
		 selectChange(lotto);
		 
		 System.out.print("로또 번호 : ");
		 for (int i = 0; i < 5; i ++) {
			 System.out.print(lotto[i] + "  ");
		 }
	}
	static void selectChange(int[] lotto) {
		int temp; 
		
		for(int i = 0; i < 6; i++) {
			for(int j = i + 1; j < 6; j++) {
				if(lotto[i] > lotto[j]){
					temp = lotto[i];
					lotto[i] = lotto[j];
					lotto[j] = temp;
				}
			}
		}
	}
}