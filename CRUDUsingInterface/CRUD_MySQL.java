//Framework program in Java using SQLite database

import java.sql.*;

class CRUD_MySQL implements iCRUD
{
	Connection connection;
	Statement statement;
	String query;
	ResultSet result;
	String[] fieldNames;
	public int createRecord(String query) throws SQLException
	{
		return statement.executeUpdate(query);
	}

	public ResultSet searchRecord(String query) throws SQLException
	{
		return statement.executeQuery(query);
	}

	public ResultSet printAllRecords(String query) throws SQLException
	{
		return statement.executeQuery(query);
	}

	public int deleteRecord(String query) throws SQLException
	{
		return statement.executeUpdate(query);
	}

	public int updateRecord(String query) throws SQLException
	{
		return statement.executeUpdate(query);
	}

	public CRUD_MySQL()
	{
		try
		{
			String url = "jdbc:mysql://165.22.14.77/dbYashwanth?user=Yashwanth&password=Yashwanth";
			connection = DriverManager.getConnection(url);
			System.out.println("Connected Successfuly.");
			statement = connection.createStatement();
		}
		catch(Exception error)
		{
			System.out.println(error.getMessage());
		}
	}

	public String[] getFieldNames() throws SQLException
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
}