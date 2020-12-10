//Framework program in Java using MySQL database

import java.sql.*;
import java.util.Scanner;
import org.json.simple.JSONObject;
import org.json.simple.JSONArray;

class MainCRUD
{
	iCRUD objiCRUD;
	Scanner scan = new Scanner(System.in);
	String[] fieldNames;
	String[] messages;
	String query;
	String[] menu;
	String[] updatableFieldsIndex;
	JSONObject objJSON;
	JSONArray objArray;
	String errorMessage = "PLEASE ENTER A VALID OPTION."; 

	public void createRecord() throws Exception
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
		query = "insert into my_table1 values (" + fieldValues + ")";
		int noOfRowsAffected = objiCRUD.createRecord(query);
		if(noOfRowsAffected == 1)
		{
			System.out.println(messages[0]); 
		}
	}

	public void searchRecord() throws Exception
	{
		String idToSearchRecord = getId();
		boolean isRecordPresent = objiCRUD.checkRecordPresentOrNot(idToSearchRecord);
		if(isRecordPresent)
		{
			query = "select * from my_table1 where Status = 'A' and " + fieldNames[0] + " = '" + idToSearchRecord + "'";
			objJSON = objiCRUD.searchRecord(query);
			printRecord(objJSON);
		}
		else
		{
			System.out.println(messages[2]);
		}
	}

	public void printAllRecords() throws Exception
	{
		query = "select * from my_table1 where Status ='A'";
		objJSON = objiCRUD.printAllRecords(query);
		printRecord(objJSON);
	}

	public void printRecord(JSONObject objJSON) throws Exception
	{
		objArray = (JSONArray)objJSON.get("my_table1");
		for(int index = 0; index < objArray.size(); index++)
		{
			JSONObject fieldValues = (JSONObject)objArray.get(index);
			for(String fieldName : fieldNames)
			{
				System.out.println(fieldName + ": " + fieldValues.get(fieldName));
			}
		}

	}

	public void deleteRecord() throws Exception
	{
		String idToDeleteRecord = getId();
		query = "update my_table1 set Status = 'D' where " + fieldNames[0] + " = '" + idToDeleteRecord + "'";
		int noOfRowsAffected = objiCRUD.deleteRecord(query);
		if(noOfRowsAffected == 0)
		{
			System.out.println(messages[2]);
		}
		else
		{
			System.out.println(messages[1]);
		}
	}

	public void updateRecord() throws Exception
	{
		String idToUpdateRecord = getId();
		boolean isRecordPresent = objiCRUD.checkRecordPresentOrNot(idToUpdateRecord);
		if(isRecordPresent)
		{
			updatableFieldsIndex = objiCRUD.getData("updatable_fields_index");
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
				int noOfRowsAffected = objiCRUD.updateRecord(query1);
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

	private String getId()
	{
		System.out.print("Enter " + fieldNames[0] + ": ");
		String fieldValue = scan.nextLine();
		return fieldValue;
	}

	public MainCRUD(String className)
	{
		try
		{
			objiCRUD = (iCRUD) Class.forName(className).newInstance();
			storeFieldNames();
			storeMessages();
			storeMenu();
		}
		catch(Exception error)
		{
			System.out.println(error.getMessage());
		}
	}

	private void storeMessages() throws Exception
	{
		messages = objiCRUD.getData("messages");
	}

	private void storeMenu() throws Exception
	{
		menu = objiCRUD.getData("menu");
	}

	private void storeFieldNames() throws Exception
	{
		fieldNames = objiCRUD.getFieldNames();
	}

	public void printMenu() throws Exception
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
