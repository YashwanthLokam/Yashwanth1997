#include<stdio.h>
int main()
{
	printf("Enter a number to print its multiplication table: ");
	int tableNumber;
	scanf("%d", &tableNumber);
	printf("Table number: %d \n", tableNumber);
	for(int rowCounter = 0; rowCounter <= 9; rowCounter++) 
	{
		printf("%2d x %2d = %3d \n", tableNumber, rowCounter, (tableNumber * rowCounter));
	}
	return 0;
} 