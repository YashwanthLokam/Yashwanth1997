// Program to test interface

class TestiCRUD
{
	public static void main(String[] args)
	{
		try
		{
			String className = args[0];
			iCRUD objCRUD = (iCRUD)Class.forName(className).newInstance();
			objCRUD.printMenu();
		}
		catch(Exception error)
		{
			System.out.println("Invalid class name.");
		}
	}
}