package chap05.practice;

import java.util.Random;

public class RandomExample {
	public static void main(String[] args) {
		 Random random = new Random();
		 random.setSeed(System.currentTimeMillis()); 
		 
		 System.out.println("10 �̸��� ���� ���� ����: " + random.nextInt(10));
		 }
	}
