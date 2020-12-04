//Framework program in Java using SQLite database

import java.sql.*;
import java.util.Scanner;

class Framework
{
	Statement statement;
	Connection connection;
	Scanner scan = new Scanner(System.in);
	String[] fieldNames;
	String[] messages;
	ResultSet result;
	String query;
	String[] menu;
	String[] updatableFieldsIndex;
	String errorMessage = "PLEASE ENTER A VALID OPTION."; 
	public void storeFieldNames() throws SQLException
	{
		query = "select * from my_table1";
		result = statement.executeQuery(query);
		ResultSetMetaData rsmd = result.getMetaData();
		fieldNames = new String[rsmd.getColumnCount() - 1];
		for(int index = 0; index < fieldNames.length; index++)
		{
			if(rsmd.getColumnName(index + 1).equals("Status") == false)
			{
				fieldNames[index] = rsmd.getColumnName(index + 1);
			}
		}
	}

	public void createRecord() throws SQLException
	{
		String fieldValues = "";
		String fieldValue = "";
		for(String fieldName : fieldNames)
		{
			System.out.print("Enter " + fieldName + ": ");
			fieldValue = scan.nextLine();
			fieldValues += "'" + fieldValue + "'" + ", ";
		}
		fieldValues += "'A'";
		query = "insert into my_table1 values(" + fieldValues + ")";
		int noOfRowsAffected = statement.executeUpdate(query);
		if(noOfRowsAffected == 1)
		{
			System.out.println(messages[0]); 
		}
	}

	public void searchRecord() throws SQLException
	{
		String idToSearchRecord = getId();
		boolean isRecordPresent = checkRecordPresentOrNot(idToSearchRecord);
		if(isRecordPresent)
		{
			query = "select * from my_table1 where Status = 'A' and " + fieldNames[0] + " = '" + idToSearchRecord + "'";
			result = statement.executeQuery(query);
			printRecord(result);
		}
		else
		{
			System.out.println(messages[2]);
		}
	}

	public void printAllRecords() throws SQLException
	{
		query = "select * from my_table1 where Status ='A'";
		result = statement.executeQuery(query);
		printRecord(result);
	}

	public void printRecord(ResultSet result) throws SQLException
	{
		while(result.next())
		{
			for(String fieldName : fieldNames)
			{
				System.out.println(fieldName + ": " + result.getString(fieldName));
			}
			System.out.println("-----------------------------------------------------");
		}
	}

	public void deleteRecord() throws SQLException
	{
		String idToDeleteRecord = getId();
		query = "update my_table1 set Status = 'D' where " + fieldNames[0] + " = '" + idToDeleteRecord + "'";
		int noOfRowsAffected = statement.executeUpdate(query);
		if(noOfRowsAffected == 0)
		{
			System.out.println(messages[2]);
		}
		else
		{
			System.out.println(messages[1]);
		}
	}

	public void updateRecord() throws SQLException
	{
		String idToUpdateRecord = getId();
		boolean isRecordPresent = checkRecordPresentOrNot(idToUpdateRecord);
		if(isRecordPresent)
		{
			updatableFieldsIndex = getData("updatable_fields_index");
			int counter = 1;
			for(String fieldIndex : updatableFieldsIndex)
			{
				System.out.println(counter + ". Update " + fieldNames[Integer.parseInt(fieldIndex) - 1]);
				counter ++;
			}
			System.out.print("Enter a number: ");
			int choice = scan.nextInt();
			scan.nextLine();
			if(choice > 0 && choice < counter)
			{
				String fieldName = fieldNames[Integer.parseInt(updatableFieldsIndex[choice - 1]) - 1];
				System.out.print("Enter new " + fieldName + ": ");
				String fieldValue = scan.nextLine();
				String query1 = "update my_table1 set " + fieldName + " = '" + fieldValue + "' where " + fieldNames[0] + " = '" + idToUpdateRecord + "'";
				int noOfRowsAffected = statement.executeUpdate(query1);
				if(noOfRowsAffected == 1)
				{
					System.out.println(fieldName + " is updated.");
				}
				else
				{
					System.out.println("Error in updating " + fieldName + ".");
				}
			}
			else
			{
				System.out.println(errorMessage);
			}
		}
		else
		{
			System.out.println(messages[2]);
		}
	}

	public String getId()
	{
		System.out.print("Enter " + fieldNames[0] + ": ");
		String fieldValue = scan.nextLine();
		return fieldValue;
	}

	public boolean checkRecordPresentOrNot(String Id) throws SQLException
	{
		boolean isRecordPresent = false;
		query = "select " + fieldNames[0] + " from my_table1 where Status = 'A' and " + fieldNames[0] + " = '" + Id + "'";
		result = statement.executeQuery(query);
		if(result.next())
		{
			isRecordPresent = true;
		}
		return isRecordPresent;
	}

	public String[] getData(String fileName) throws SQLException
	{
		query = "select * from Config where FileName = '" + fileName + "'";
		result = statement.executeQuery(query);
		String tempData = "";
		while(result.next())
		{
			tempData = result.getString("FileContent");
		}
		return tempData.split(", ");
	}

	public Framework()
	{
		String url = "jdbc:sqlite:framework.db";
		try
		{
			Class.forName("org.sqlite.JDBC");
			connection = DriverManager.getConnection(url);
			System.out.println("Connected Successfuly.");
			statement = connection.createStatement();
			storeFieldNames();
			storeMessages();
			storeMenu();
		}
		catch(Exception error)
		{
			System.out.println(error.getMessage());
		}
	}

	public void storeMessages() throws SQLException
	{
		messages = getData("messages");
	}

	public void storeMenu() throws SQLException
	{
		menu = getData("menu");
	}

	public void printMenu() throws SQLException
	{
		while(true)
		{
			for(int index = 0; index < menu.length; index++)
			{
				System.out.println(menu[index]);
			}
			System.out.print("Enter a number: ");
			String choice = scan.next();
			scan.nextLine();
			switch(choice)
			{
				case "1": createRecord();
						break;
				case "2": searchRecord();
						break;
				case "3": printAllRecords();
						break;
				case "4": updateRecord();
						break;
				case "5": deleteRecord();
						break;
				case "6": System.out.println("Are you sure? ");
						System.out.print("Press Y or N: ");
						String exitChoice = scan.next();
						if(exitChoice.toUpperCase().equals("Y"))
						{
							connection.close();
							System.exit(0);
						}
						else if(exitChoice.toUpperCase().equals("N"))
						{
							continue;
						}
				default: System.out.println(errorMessage);
			}
		}
	}
}

class MainClass
{
	public static void main(String args[]) 
	{
		Framework framework = new Framework();
		try
		{
			framework.printMenu();
		}
		catch(SQLException error)
		{
			System.out.println(error.getMessage());
		}
	}
}