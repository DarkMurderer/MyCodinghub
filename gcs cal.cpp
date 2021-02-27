// this code is written by Dark Murderer
//you can find more projects at https://github.com/DarkMurderer/MyCodinghub
#include <iostream>
using namespace std;

int gcs(int num1,int num2)
{
	int gcs,rp;
	gcs = 0;
	if (num1>num2)
	{
		int remaining, devided_by;
		remaining = num1 % num2;
		devided_by = num2;
		if (remaining == 0)
		{
			gcs = num2;
		}
		else
		{
			while (remaining != 0)
			{
				rp = remaining;
				remaining = devided_by % rp;
				devided_by = rp;
			}
			gcs = rp;
		}
	}
	else if (num1 < num2)
	{
		int remaining, devided_by;
		remaining = num2 % num1;
		devided_by = num1;
		if (remaining == 0)
		{
			gcs = num1;
		}
		else
		{
			while (remaining != 0)
			{
				rp = remaining;
				remaining = devided_by % rp;
				devided_by = rp;
			}
			gcs = rp;
		}
	}
	else
	{
		gcs = num1;	
	}
	cout << gcs;
	return gcs;
}

int main()
{
	int n1,n2;
	cout << "enter first number: ";
	cin >> n1;
	cout << "enter secound number:  ";
	cin >> n2;
	gcs(n1, n2);
}

//you can find more projects at https://github.com/DarkMurderer/MyCodinghub
