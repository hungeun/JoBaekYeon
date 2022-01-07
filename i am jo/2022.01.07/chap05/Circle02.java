//private 필드를 갖는 클래스의 예

package chap05;

public class Circle02 {
	private double radius;
	Circle02(double radius) {
	this.radius = radius;
	}
	double getArea() {
	double area;
	area = radius * radius * 3.14;
	return area;
	}
	}