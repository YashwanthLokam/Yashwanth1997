// Program to create an interface

import java.sql.*;

interface iCRUD
{	
	public int createRecord(String query) throws SQLException;
	public ResultSet searchRecord(String query) throws SQLException;
	public ResultSet printAllRecords(String query) throws SQLException;
	public int deleteRecord(String query) throws SQLException;
	public int updateRecord(String query) throws SQLException;
	public String[] getFieldNames() throws SQLException;
	public String[] getData(String fileName) throws SQLException;
}