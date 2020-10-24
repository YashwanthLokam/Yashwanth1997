#include<Stdio.h>
int main()
{
	printf("How many Even numbers do you want? ");
	int countOfEvenNumbers;
	scanf("%d", &countOfEvenNumbers);
	printf("Even numbers are: ");
	int evenNumber = 2;
	for(int evenNumberCounter = 1; evenNumberCounter <= countOfEvenNumbers; evenNumberCounter++, printf("%d\t", evenNumber), evenNumber = evenNumber + 2);
	//{
		//printf("%d\t", evenNumber);
		//evenNumber = evenNumber + 2;
	//}
	return 0;
}