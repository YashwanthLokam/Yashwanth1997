// Program to create an interface

import java.sql.*;
import org.json.simple.JSONObject;

interface iCRUD
{	
	public int createRecord(String query) throws Exception;
	public JSONObject searchRecord(String query) throws Exception;
	public JSONObject printAllRecords(String query) throws Exception;
	public int deleteRecord(String query) throws Exception;
	public int updateRecord(String query) throws Exception;
	public String[] getFieldNames() throws Exception;
	public String[] getData(String fileName) throws Exception;
	public boolean checkRecordPresentOrNot(String Id) throws Exception;
}