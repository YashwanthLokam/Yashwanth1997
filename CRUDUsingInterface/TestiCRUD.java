// Program to test interface

class TestiCRUD
{
	public static void main(String[] args)
	{
		try
		{
			String className = args[0];
			MainCRUD objMainCRUD = new MainCRUD(className);
			objMainCRUD.printMenu();
		}
		catch(Exception error)
		{
			System.out.println(error.getMessage());
			error.printStackTrace();
		}
	}
}