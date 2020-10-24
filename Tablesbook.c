#include<stdio.h>
int main()
{
	printf("How many tables do you want? ");
	int countOfTables;
	scanf("%d", &countOfTables);
	for(int tableNumber = 1; tableNumber <= countOfTables; tableNumber++)
	{
		printf("Table number: %d\n", tableNumber);
		printf("-----------------\n");
		for(int rowCounter = 1; rowCounter <= 10; rowCounter++)
		{
			printf("%d x %d = %d\n", tableNumber, rowCounter, (tableNumber * rowCounter));
		}
	}
	return 0;
}
		
		