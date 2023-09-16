#include<iostream>
#include<cmath>
using namespace std;

float dis,root_x1,root_x2;

float discrim(float x,float y,float z)
{
    
    dis= (y*y)-(4*(x)*z);
    cout<<endl<<"The discriminant is "<<dis<<endl<<endl;
    return dis;
}
int check()
{
    if(dis<0)
    {
        cout<<"The quadratic equation doesn't have any real roots."<<endl;
        exit(0);
    }
    else if(dis==0)
    {
        cout<<"The roots are equal."<<endl<<endl;
        return dis;
    }
    else
    {
        cout<<"The roots are distinct."<<endl<<endl;
        return dis;
    }
}
float rootofx(float p, float q)
{
    root_x1=(-(q)+(sqrt(dis)))/(2*p);
    
    root_x2=(-(q)-(sqrt(dis)))/(2*p);
        
    cout<<"The first root is "<<root_x1<<endl<<endl;
    
    cout<<"The second root is "<<root_x2<<endl<<endl;
    exit(0);
    
}
int main()
{
    float val_a, val_b, val_c;
    
    cout<<"C++ Program to find the roots of a quadratic equation"<<endl;
    cout<<"\t(Only in integer or decimal)"<<endl<<endl;
    cout<<"Quadratic Equation: ax^2+bx+c=0"<<endl<<endl;
    cout<<"Enter the value of 'a' 'b' 'c' respectively"<<endl;
    cout<<"a: ";
    cin>>val_a;
    cout<<endl<<"b: ";
    cin>>val_b;
    cout<<endl<<"c: ";
    cin>>val_c;
    
    discrim(val_a,val_b,val_c);
    
    check();
    
    rootofx(val_a,val_b);

}
    