// Program to write SQL Parser

class SQLParser
{
	public String getTableName(String query)
	{
		String[] tempData = query.split(" ");
		String tempTableName = "";
		if(tempData[0].toLowerCase().equals("insert"))
		{
			tempTableName = tempData[2];
		}
		else if(tempData[0].toLowerCase().equals("update"))
		{
			tempTableName = tempData[1];
		}
		else if(tempData[0].toLowerCase().equals("select"))
		{
			for(int index = 0; index < tempData.length; index++)
			{
				if(tempData[index].toLowerCase().equals("from"))
				{
					tempTableName = tempData[index + 1];
				}
			}
		}
		return tempTableName;
	}

	public String[] getFieldNames(String query)
	{
		String fieldNames = "";
		String tempData = query.replaceAll("[(,)]", "");
		String[] tempSplittedQuery = tempData.split(" ");
		if(tempSplittedQuery[0].toLowerCase().equals("insert"))
		{
			for (int index = 3; index < tempSplittedQuery.length; index++)
			{
				if (tempSplittedQuery[index].toLowerCase().equals("values") != true)
				{
					fieldNames += tempSplittedQuery[index] + " ";
				}
				else
				{
					break;
				}
			}
		}
		else if(tempSplittedQuery[0].toLowerCase().equals("update"))
		{
			fieldNames += tempSplittedQuery[3] + " " + tempSplittedQuery[7];
		}
		else if(tempSplittedQuery[0].toLowerCase().equals("select"))
		{
			for (int index = 1; index < tempSplittedQuery.length; index++)
			{
				if (tempSplittedQuery[index].toLowerCase().equals("where"))
				{
					index += 1;
					fieldNames += tempSplittedQuery[index] + " ";
					while (index + 2 != tempSplittedQuery.length - 1)
					{
						index += 4;
						fieldNames += tempSplittedQuery[index] + " ";
					}
					break;
				}
				
			}			
		}
		return fieldNames.split(" ");
	}

	public String[] getFieldValues(String query)
	{
		String fieldValues = "";
		String tempData = query.replaceAll("[(,\')]", "");
		String[] tempSplittedQuery = tempData.split(" ");
		if(tempSplittedQuery[0].toLowerCase().equals("insert"))
		{
			int counter = 0;
			for (int index = 3; index < tempSplittedQuery.length; index++)
			{
				if (tempSplittedQuery[index].toLowerCase().equals("values"))
				{
					counter = index;
				}
				else if(index > counter && counter != 0)
				{
					fieldValues += tempSplittedQuery[index] + " ";
				}
			}
		}
		else if(tempSplittedQuery[0].toLowerCase().equals("update"))
		{
			fieldValues += tempSplittedQuery[5] + " " + tempSplittedQuery[9];
		}
		else if(tempSplittedQuery[0].toLowerCase().equals("select"))
		{
			for (int index = 1; index < tempSplittedQuery.length; index++)
			{
				if (tempSplittedQuery[index].toLowerCase().equals("where"))
				{
					index += 3;
					fieldValues += tempSplittedQuery[index] + " ";
					while (index != tempSplittedQuery.length - 1)
					{
						index += 4;
						fieldValues += tempSplittedQuery[index] + " ";
					}
					break;
				}
			}			
		}
		return fieldValues.split(" ");
	}
}