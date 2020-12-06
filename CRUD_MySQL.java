//Framework program in Java using MySQL database

import java.sql.*;
import java.util.Scanner;

class CRUD_MySQL extends MainCRUD
{
	public CRUD_MySQL()
	{
		super("jdbc:mysql://165.22.14.77/dbYashwanth?user=Yashwanth&password=Yashwanth", "com.mysql.cj.jdbc.Driver");
	}

}
