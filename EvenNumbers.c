#include<Stdio.h>
int main()
{
	printf("How many Even numbers do you want? ");
	scanf("%d", &countOfEvenNumbers);
	int evenNumber = 2;
	for(int evenNumberCounter = 1; evenNumberCounter <= countOfEvenNumbers; evenNumberCounter++, printf("%d\t", evenNumber), evenNumber = evenNumber + 2);
	{
		printf("%d\t", evenNumber);
		evenNumber = evenNumber + 2;
	}
	printf("Print all even numbers");
	return 0;
}