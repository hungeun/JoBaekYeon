//�ʵ� ����
package chap05;

public class Circle {
	double radius ; // �ʵ�
	Circle(double radius ) { // ������
	this.radius = radius;
	}
	double getArea() { // �޼ҵ�
	double area ;
	area = radius * radius * 3.14;
	return area;
	}
	}
