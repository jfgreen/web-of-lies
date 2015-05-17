import processing.serial.*;
import http.requests.*;
import java.util.ArrayList;
import java.util.List;

String baseURL = "http://178.62.81.21/wiki/Deception";

int dataCount = 0;



Serial serialPort;  //Serial port object
void setup() {
  
  String serialData;   // Data from Serial port

  String portName  = Serial.list()[2];
  //println(Serial.list());

  serialPort = new Serial(this, Serial.list()[2], 9600);

  print("port name = " +portName);
}

void draw() {

  

  List<String> dataList = new ArrayList<String>();


  while (serialPort.available () > 0) {
    
    String  inBuffer  = serialPort.readString();
    
    String[] temp = inBuffer.split(",");
    
    if (temp.length == 4){
    String part0 = temp[0];
    String part1 = temp[1];
    String part2 = temp[2];
    String part3 = temp[3];
    
    dataList.add(part0);
    dataList.add(part1);
    dataList.add(part2);
    dataList.add(part3);
    


    for (String dataString : dataList) {
      println(dataString);
      
      
    }

    //Query the server for text


      println("gettng data");
      String ObjectSelection = dataList.get(0);
      String deceitValue = dataList.get(1);
      String trickeryValue = dataList.get(2);
      String funnyValue = dataList.get(3); 


      String objectText = "?object="+ObjectSelection;
      String deceictText ="&value1="+deceitValue;
      String trickeryText = "&value2="+trickeryValue;
      String funnyText = "&value3="+funnyValue;

      String queryString = baseURL+objectText+trickeryText+funnyText;

      //GetRequest get = new GetRequest(queryString);
      GetRequest get = new GetRequest(baseURL);
      get.send();
      String museumText = get.getContent();
      print(museumText);
    }
    
  }
}

