package chap05;

public class FieldExample2 {
	public static void main(String args[]) {
		Circle obj = new Circle(0.0);
		obj.radius = 5.0; // Circle Ŭ������ �ʵ忡 ���� ����
		double area = obj.getArea();
		System.out.println(obj.radius); // Circle Ŭ������ �ʵ� ���� ���
		System.out.println(area);
		}
		}