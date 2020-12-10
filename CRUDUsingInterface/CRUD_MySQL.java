//Framework program in Java using SQLite database

import java.sql.*;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

class CRUD_MySQL implements iCRUD
{
	Connection connection;
	Statement statement;
	String query;
	ResultSet result;
	String[] fieldNames;
	JSONObject jsonObject;
	JSONArray array;
	public int createRecord(String query) throws Exception
	{
		return statement.executeUpdate(query);
	}

	public JSONObject searchRecord(String query) throws Exception
	{
		result = statement.executeQuery(query);
		return convertDataToJSON(result);
	}

	private JSONObject convertDataToJSON(ResultSet result) throws Exception
	{
		jsonObject = new JSONObject();
		array = new JSONArray();
		while(result.next())
		{
			JSONObject record = new JSONObject();
			for(int index = 0; index < fieldNames.length; index++)
			{
				record.put(fieldNames[index], result.getString(fieldNames[index]));
			}
			array.add(record);
		}
		jsonObject.put("my_table1", array);
		return jsonObject;
	}

	public JSONObject printAllRecords(String query) throws Exception
	{
		result = statement.executeQuery(query);
		return convertDataToJSON(result);
	}

	public int deleteRecord(String query) throws Exception
	{
		return statement.executeUpdate(query);
	}

	public int updateRecord(String query) throws Exception
	{
		return statement.executeUpdate(query);
	}

	public boolean checkRecordPresentOrNot(String id) throws Exception
	{
		boolean isRecordPresent = false;
		query = "select " + fieldNames[0] + " from my_table1 where Status = 'A' and " + fieldNames[0] + " = '" + id + "'";
		result = statement.executeQuery(query);
		if(result.next())
		{
			isRecordPresent = true;
		}
		return isRecordPresent;
	}

	public CRUD_MySQL()
	{
		try
		{
			String url = "jdbc:mysql://165.22.14.77/dbYashwanth?user=Yashwanth&password=Yashwanth";
			connection = DriverManager.getConnection(url);
			System.out.println("Connected Successfuly.");
			statement = connection.createStatement();
			storeFieldNames();
		}
		catch(Exception error)
		{
			System.out.println(error.getMessage());
		}
	}

	public String[] getFieldNames() throws Exception
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
		return fieldNames;
	}

	public void storeFieldNames() throws Exception
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

	public String[] getData(String fileName) throws Exception
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
}