package chap02;

public class IncreDecExample1 {
	public static void main(String arg[]) {
		
		int num = 0, result;
		
		result = num++;
		System.out.println(num + "," + result);
		
		result = ++num;
		System.out.println(num + "," + result);
		
		result = num--;
		System.out.println(num + "," + result);
		
		result = --num;
		System.out.println(num + "," + result);
	}
	

}
