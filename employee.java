package company;

public class employee {
	String name,address;
	int yr_of_join,salary;
	
	employee(String fname, String add,int year,int sal){
		name=fname;
		address=add;
		yr_of_join=year;
		salary=sal;
	}
	void display_emp() {
		System.out.println("\nName: "+name);
		System.out.println("\nYear of Joining: "+yr_of_join);
		System.out.println("\nSalary: "+salary);
		System.out.println("\nAddress: "+address);
	}
}
