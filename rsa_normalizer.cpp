#include <iostream>
using namespace std;
long long int p,q,n,e,entext,pntext;
long double norencrypt(int a,int b){
	e=5; int i;entext=1;	
pntext=a*100+b;
	for(i=1;i<=e;i++){
		entext=entext*(pntext);
	entext=entext%n;
	}
	return entext/240579029592611.0;
}
int main() 
{	// your code goes
 	long double enc[100];
int i,j,k,a[100],b[100],c[100];
	p=15485863;              q=15535397;
    n=240579029592611;
	for(i=1;i<68;i++){
		cin>>a[i]>>b[i];
		enc[i]=norencrypt(a[i],b[i]);
	    cout<<enc[i]<<";";
			}
	return 0;
}
