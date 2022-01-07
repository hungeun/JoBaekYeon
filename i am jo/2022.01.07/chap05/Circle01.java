
// 필드, 메소드, 생성자의 위치를 바꿈
package chap05;

public class Circle01 {
	Circle01(double radius) {
		this.radius = radius;
		}
		double getArea() {
		double area;
		area = radius * radius * 3.14;
		return area;
		}
		double radius;
		}