#include <iostream>
using namespace std;
 
int main() {
	// your code goes here
	int i,a[68],b[68],c;double x[68];
	for(i=1;i<=67;i++)
	{
		cin>>a[i]>>b[i];
		a[i]=a[i]+2;c=a[i]%26;a[i]=c;
		b[i]=b[i]+2;c=b[i]%26;b[i]=c;
		x[i]=(26*a[i]+b[i])/675.0;
		cout<<a[i]<<" "<<b[i]<<";";
	}
	return 0;
}
