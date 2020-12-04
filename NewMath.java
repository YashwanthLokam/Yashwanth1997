// NewMath program which has only square method

class NewMath extends MyMath
{
	public int square(int number)
	{
		return number * number;
	}

	public int add(int firstNumber, int secondNumber, int thirdNumber)
	{
		return firstNumber + secondNumber + thirdNumber;
	}

	public int add(int firstNumber, int secondNumber)
	{
		int total = firstNumber + secondNumber;
		System.out.println("Total = " + total);
		return total;
	}
}