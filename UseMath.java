// UseMath program to call NewMath program

class UseMath
{
	public static void main(String[] args)
	{
		NewMath ObjNewMath = new NewMath();
		System.out.println(ObjNewMath.add(2, 3));
		System.out.println(ObjNewMath.add(30, 40, 44));
		System.out.println(ObjNewMath.multiply(4, 9));
		System.out.println(ObjNewMath.square(3));
	}
}