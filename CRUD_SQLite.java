//Framework program in Java using SQLite database

import java.sql.*;
import java.util.Scanner;

class CRUD_SQLite extends MainCRUD
{
	public CRUD_SQLite()
	{
		super("jdbc:sqlite:D:/Prat1/Yashwanth1997/framework.db", "org.sqlite.JDBC");
	}
}

