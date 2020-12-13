// Using FrameworkMyLib1 to connect to MySQL and perform InsertRecords() and PrintAllRecords()

using System;
using FrameworkMyLib1;

class Framework_MySQL
{
	public static void Main(String[] args)
    {
    	String errorMessage = "PLEASE ENTER A VALID OPTION.";
        String connString = "Server = 165.22.14.77; Database = dbYashwanth; User Id = Yashwanth; Password = Yashwanth";
    	Framework1 ObjFramework = new Framework1(connString);
    	while(true)
    	{
    		Console.WriteLine("1. Open an insurance policy\n2. Print all insurance policies.\n3. Exit");
    		Console.Write("Enter a number: ");
    		String choice = Console.ReadLine();
    		try
    		{
	    		switch(choice)
	    		{
	    			case "1" : ObjFramework.InsertRecords();
	    						break;
	    			case "2" : ObjFramework.PrintAllRecords();
	    						break;
	    			case "3" : Console.WriteLine("Are you sure? ");
	    						Console.Write("Press Y or N: ");
	    						String exitChoice = Console.ReadLine();
	    						if(String.Equals(exitChoice.ToLower(), "y"))
		    						System.Environment.Exit(0);
		    					else if(String.Equals(exitChoice.ToLower(), "n"))
		    						continue;
		    					else
		    						Console.WriteLine(errorMessage);
	    						break;
	    			default : Console.WriteLine(errorMessage);
	    						break;
	    		}
    		}
    		catch(Exception error)
    		{
    			Console.WriteLine(error.Message);
    		}
        }
    }
}