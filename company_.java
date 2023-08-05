package company;

import java.util.Scanner;

public class company_ {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		String name,address;
		int yr_of_join,salary;
		
		employee[] emp=new employee[3];
		
		for(int i=0;i<3;i++){
			System.out.println("\nEmployee "+(i+1)+"\nEnter name: ");
			name=scan.nextLine();
			System.out.println("Enter address: ");
			address=scan.nextLine();
			System.out.println("Enter year of joining: ");
			yr_of_join=Integer.parseInt(scan.nextLine());
			System.out.println("Enter salary: ");
			salary=Integer.parseInt(scan.nextLine());
			emp[i]=new employee(name,address,yr_of_join,salary);	
		}
		System.out.println("Employee Details");
		for(int i=0;i<3;i++) {
			System.out.println("\nEmployee"+(i+1));
			emp[i].display_emp();
		}
	}
}
