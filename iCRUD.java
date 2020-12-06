// Program to create an interface

import java.sql.SQLException;

interface iCRUD
{	
	public void createRecord() throws SQLException;
	public void searchRecord() throws SQLException;
	public void printAllRecords() throws SQLException;
	public void deleteRecord() throws SQLException;
	public void updateRecord() throws SQLException;
	public void printMenu() throws SQLException;
}