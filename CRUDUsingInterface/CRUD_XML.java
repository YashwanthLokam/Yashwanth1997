// package com.javacodegeeks.java.core;
 
import java.io.File;
import java.io.FileWriter;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;  
import org.w3c.dom.Node; 
import java.util.Scanner;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject; 

class CRUD_XML implements iCRUD
{
    DocumentBuilderFactory dbf;  
    DocumentBuilder db;  
    Document document;  
    Element root;
    String[] fieldNames;
    String[] fieldValues;
    File file = new File("F:/Training/Java/data.xml"); 
    SQLParser objSQLParser = new SQLParser();
    
    public int createRecord(String query) throws Exception
    {
        fieldNames = getFieldNames();
        fieldValues = objSQLParser.getFieldValues(query);
        Element child = document.createElement("record");
        root.appendChild(child);
        Attr attr = document.createAttribute("Status");
        attr.setValue("A");
        child.setAttributeNode(attr);
        for(int index = 0; index < fieldNames.length; index++)
        {
            Element subChild = document.createElement(fieldNames[index]);
            subChild.appendChild(document.createTextNode(fieldValues[index]));
            child.appendChild(subChild);
        }
        saveRecords();
        return 1;
    }

    public JSONObject printAllRecords(String query) throws Exception
    {  
		JSONObject jsonObject = new JSONObject();
		JSONArray array = new JSONArray();
	    fieldNames = getFieldNames();
	    String tableName = objSQLParser.getTableName(query);
        NodeList nodeList = document.getElementsByTagName("record");  
        for(int index = 0; index < nodeList.getLength(); index++)   
        {  
            Node node = nodeList.item(index);
            Element eElement = (Element) node;
            String attribute = eElement.getAttribute("Status");
            if(attribute.equals("A"))   
            {  
	            JSONObject record = new JSONObject();
	            NodeList childNodes = node.getChildNodes();
                for(int childNodesIndex = 0; childNodesIndex < fieldNames.length; childNodesIndex++)
                {
                	Node nNode = childNodes.item(childNodesIndex);
                    record.put(nNode.getNodeName(), nNode.getTextContent());  
                }
	            array.add(record);
            }
        }
        jsonObject.put(tableName, array);
        return jsonObject;  
    }

    public int deleteRecord(String query) throws Exception
    {
    	int recordDeletedStatus = 0;
	    fieldNames = objSQLParser.getFieldNames(query);
	    fieldValues = objSQLParser.getFieldValues(query);
        NodeList nodeList = document.getElementsByTagName("record");
        for(int index = 0; index < nodeList.getLength(); index++)
        {
        	Node node = nodeList.item(index);
        	Element eElement = (Element) node;
        	String attribute = eElement.getAttribute("Status");
        	if(attribute.equals("A") && eElement.getElementsByTagName(fieldNames[1]).item(0).getTextContent().equals(fieldValues[1]))
        	{
        		eElement.setAttribute("Status", fieldValues[0]);
        		saveRecords();
        		recordDeletedStatus = 1;
        		break;
        	}
        }
        return recordDeletedStatus;  
    }

    public int updateRecord(String query) throws Exception
    {
    	int recordUpdatedStatus = 0;
	    fieldNames = objSQLParser.getFieldNames(query);
	    fieldValues = objSQLParser.getFieldValues(query);
        NodeList nodeList = document.getElementsByTagName("record");
        for(int index = 0; index < nodeList.getLength(); index++)
        {
        	Node node = nodeList.item(index);
        	Element eElement = (Element) node;
        	String attribute = eElement.getAttribute("Status");
        	if(attribute.equals("A") && eElement.getElementsByTagName(fieldNames[1]).item(0).getTextContent().equals(fieldValues[1]))
        	{
	        	NodeList childNodes = node.getChildNodes();
	    		for(int nodeIndex = 0; nodeIndex < childNodes.getLength(); nodeIndex++)
	    		{
	    			Node nNode = childNodes.item(nodeIndex);
		        	if(nNode.getNodeName().equals(fieldNames[0]))
		        	{
		        		nNode.setTextContent(fieldValues[0]);
		        		saveRecords();
		        		recordUpdatedStatus = 1;
		        		break;
		        	}
	    		}
        	}
    	}
    	return recordUpdatedStatus;
    }

    public JSONObject searchRecord(String query) throws Exception
    {
        JSONObject jsonObject = new JSONObject();
		JSONArray array = new JSONArray();
	    fieldNames = getFieldNames();
	    fieldValues = objSQLParser.getFieldValues(query);
	    String tableName = objSQLParser.getTableName(query);
        NodeList nodeList = document.getElementsByTagName("record");  
        for(int index = 0; index < nodeList.getLength(); index++)   
        {  
            Node node = nodeList.item(index);
            Element eElement = (Element) node;
            String attribute = eElement.getAttribute("Status");
            if(attribute.equals("A") && eElement.getElementsByTagName(fieldNames[0]).item(0).getTextContent().equals(fieldValues[1]))   
            {  
				JSONObject record = new JSONObject();
                for(int fieldNamesIndex = 0; fieldNamesIndex < fieldNames.length; fieldNamesIndex++)
                {
                    record.put(fieldNames[fieldNamesIndex], eElement.getElementsByTagName(fieldNames[fieldNamesIndex]).item(0).getTextContent());  
                }
                array.add(record);
		        jsonObject.put(tableName, array);   
                break; 
            }  
        }
        return jsonObject;
    }

    public void saveRecords() throws Exception
    {
		TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        DOMSource domSource = new DOMSource(document);
        StreamResult streamResult = new StreamResult(new FileWriter(file));
        transformer.transform(domSource, streamResult);
    }

    public boolean checkRecordPresentOrNot(String id) throws Exception
	{
		boolean isRecordPresent = false;
		NodeList nodeList = document.getElementsByTagName("record");  
        for(int index = 0; index < nodeList.getLength(); index++)   
        {  
            Node node = nodeList.item(index);
            Element eElement = (Element) node;
            String attribute = eElement.getAttribute("Status");
            if(attribute.equals("A") && eElement.getElementsByTagName(fieldNames[0]).item(0).getTextContent().equals(id))
            {
            	isRecordPresent = true;
            }
        }
		return isRecordPresent;
	}

    public CRUD_XML()
    {
    	try
    	{
	    	dbf = DocumentBuilderFactory.newInstance();  
		    db = dbf.newDocumentBuilder();  
		    document = db.parse(file);  
		    root = document.getDocumentElement();
		    document.getDocumentElement().normalize();
		}
		catch(Exception error)
		{
			System.out.println(error.getMessage());
		}
    }

    public String[] getFieldNames() throws Exception
    {
    	String tempData = "";
		File objFile = new File("fields.cfg");
		Scanner objScan = new Scanner(objFile);
		while(objScan.hasNextLine())
		{
			tempData = objScan.nextLine();
		}
    	return tempData.split(", ");
    }

    public String[] getData(String fileName) throws Exception
    {
    	String tempData = "";
    	fileName += ".cfg";
    	File objFile = new File(fileName);
    	Scanner objScan = new Scanner(objFile);
    	while(objScan.hasNextLine())
    	{
    		tempData = objScan.nextLine();
    	}
    	return tempData.split(", ");
    }
}
