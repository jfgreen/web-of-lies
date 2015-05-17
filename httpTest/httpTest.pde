import http.requests.*;

String baseURL = "http://178.62.81.21/wiki/";

String objectText = "deciet";
String queryString;

      int ObjectSelection = 1;
      float deceitValue = 234 ;
      float trickeryValue = 123;
      float funnyValue = 99; 
      
      deceitValue = map(deceitValue,0,255,0,40);
      trickeryValue = map(trickeryValue,0,255,0,40);
      funnyValue = map(funnyValue,0,255,0,40);
      
      
      
      
      
/*

Scarab_(artifact)
coffeepot
athena
*/


      switch(ObjectSelection){
        
        case 1:  objectText = "Scarab_(artifact)";
                 break;
        case 2:  objectText = "coffeepot";
                  break;
        
        case 3:  objectText = "athena";
                  break;
      }
      
      

      //String objectText = "?object="+ObjectSelection;
      String deceictText ="&value1="+deceitValue;
      String trickeryText = "&value2="+trickeryValue;
      String funnyText = "&value3="+funnyValue;

      queryString = baseURL+ objectText+"?data="+deceictText+"," + trickeryText+","+ funnyText;
      println(queryString);

      GetRequest get = new GetRequest(queryString);
      //GetRequest get = new GetRequest(baseURL);
      get.send();
      String museumText = get.getContent();
      print(museumText);
