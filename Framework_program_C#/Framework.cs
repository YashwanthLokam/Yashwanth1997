// Framework program 

namespace FrameworkLib
{
	using System;
	using System.Data;
	using System.Data.Common;
	using MySql.Data.MySqlClient;

	public class Framework
	{
		String[] fieldNames;
		String query;
		MySqlConnection conn;
		String connString;
		MySqlCommand cmd;

		public Framework(String connString)
		{
			this.connString = connString;
			try
	        {
		        this.conn = new MySqlConnection(connString);
		        conn.Open();
		        Console.WriteLine("Connection is established.");
				StoreFieldNames();
			}
			catch(Exception error)
	        {
	        	Console.WriteLine(error.StackTrace);
	        }
		}

	    public void StoreFieldNames()
	    {
	    	try
	    	{
		    	query = "select * from my_table1";
		        cmd = new MySqlCommand(query, conn);
		        DataTable table = new DataTable();
		        MySqlDataAdapter dataAdapter = new MySqlDataAdapter(cmd);
		        dataAdapter.Fill(table);
		        fieldNames = new String[table.Columns.Count - 1];
		        for(int index = 0; index < table.Columns.Count; index++)
		        {
		        	if(!(String.Equals(table.Columns[index].ToString(), "Status")))
		        	{
		            	fieldNames[index] = table.Columns[index].ToString();
		        	}
		        }
	    	}
	    	catch(Exception error)
	    	{
	    		throw error;
	    	}
	    }

	    public void PrintAllRecords()
	    {
		    try
		    {
			    query = "select * from my_table1 where Status = 'A'";
		        cmd = new MySqlCommand(query, conn);
		        DbDataReader reader = cmd.ExecuteReader();
		        if(reader.HasRows)
		        {
		            while(reader.Read())
		            {
			            foreach(String fieldName in fieldNames)
		            	{
			                Console.WriteLine(fieldName + ": " + reader.GetString(reader.GetOrdinal(fieldName)));
		            	}
		            	Console.WriteLine("--------------------------");
		            }
		        }
		        reader.Close();
		    }
		    catch(Exception error)
		    {
		    	throw error;
		    } 
	    }

	    public void InsertRecords()
	    {
	    	try
	    	{
		    	String fieldValues = "";
				String fieldValue = "";
				foreach(String fieldName in fieldNames)
				{
					Console.Write("Enter " + fieldName + ": ");
					fieldValue = Console.ReadLine();
					fieldValues += "'" + fieldValue + "'" + ", ";
				}
				fieldValues += "'A'";
				query = "insert into my_table1 values(" + fieldValues + ")";
		        cmd = new MySqlCommand(query, conn);
				int noOfRowsAffected = cmd.ExecuteNonQuery();
				if(noOfRowsAffected == 1)
				{
					Console.WriteLine("Records are stored in the database."); 
				}
	    	}
	    	catch(Exception error)
	    	{
	    		throw error;
	    	}
	    }
	}
} 
