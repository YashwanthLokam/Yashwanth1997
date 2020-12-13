// Framework program
namespace FrameworkMyLib1
{
	using System;
	using System.Data;
	using System.Data.Common;
	using MySql.Data.MySqlClient;

	public class Framework1
	{
		String[] fieldNames;
		String query;
		MySqlConnection conn;
		String connString;
		MySqlCommand cmd;

		public Framework1(String connString)
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
				Console.WriteLine(error.Message);
			}
		}

		public void StoreFieldNames()
		{
			try
			{
				query = "select * from my_table1";
				cmd = new MySqlCommand(query, conn);
				DbDataReader reader = cmd.ExecuteReader();
				fieldNames = new String[reader.FieldCount - 1];
				if(reader.HasRows)
				{
					for(int index = 0; index < reader.FieldCount; index++)
					{
						if(!(String.Equals(reader.GetName(index).ToString(), "Status")))
						{
							fieldNames[index] = reader.GetName(index).ToString();
						}
					}
				}
				reader.Close();		
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
				DataTable table = new DataTable();
				MySqlDataAdapter adapter = new MySqlDataAdapter(cmd);
				adapter.Fill(table);
				for(int index = 0; index < table.Rows.Count; index++)
				{
					foreach (String fieldName in fieldNames)
					{
						Console.WriteLine(fieldName + ": " + table.Rows[index][fieldName].ToString());
					}
					Console.WriteLine("--------------------------");
				}
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
				foreach (String fieldName in fieldNames)
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