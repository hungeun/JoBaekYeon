package chap05.main;

import chap05.geometry.Circle;

public class PackageExample1 {
	public static void main(String args[]) {
		Circle obj = new Circle(5);                        //빨간줄인 이유 폴더에 대한 접근ㅇ 파일에 대한 접근x//import하려는 패키지에 쓰려는것들이 public이여야함
		System.out.println("반지름 = " + obj.radius);
		System.out.println("면적 = " + obj.getArea());
		}
		}