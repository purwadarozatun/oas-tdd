import json
from  datagetter import DataGetter
import uuid

def startParse(jsonFile) : 
    paths = readPaths(jsonFile, "paths")
    for path in paths:
        print("## " + path)
        pathMethods =  paths[path]
        
        for method in pathMethods:
            print(">>> " +  method)
            methodData  =  pathMethods[method]
            
            requestSummary =    methodData['summary']  if "summary" in methodData else "(Not Set)"
            print(">>>> " + requestSummary)
            
            if(method in ["post" , "put" ,  "patch"]):
                requestParams =   methodData['parameters']  if "parameters" in methodData else []
                requestBody =   methodData['requestBody']  if "requestBody" in methodData else {}
                requestContent =  list(requestBody["content"].items())[0][1]
                # print(methodData)
                parsed =  parseData(requestContent['schema'])
                print("Parameters :   "  + json.dumps(parsed, indent = 2))
                
                
            


def readPaths(jsonFile , paths) :
    return jsonFile[paths]


def parseData(data):
    # Handle Ref Data
    if('$ref' in data) :
        print("INI REF")

    elif(data["type"] ==  'object' ):
        
        return parseObject(data)
    elif(data["type"] ==  'array' ): 
        return parseArray(data)

    else :
        return (parseFieldData(data['default']) if 'default' in data else "") 

    
        

def parseObject(data):
    properties =   data["properties"]
    generated = {}
    for prop in properties : 
        generated[prop] = parseData(properties[prop])

    return  generated
        
     
def parseArray(data):
    print("ARray") 
     

def parseFieldData(f): 

    from faker import Faker
    fake = Faker()
    try:   
        data = getattr(fake, '%s' % f)()
        return data
    except Exception as ex: 
        return generateCustomData(f)

def generateCustomData(f): 
    splited =  f.split(":")
    
    if(len(splited) > 1) :
        try: 
            cmd =  splited[0]
            return getattr(DataGetter, '%s' % cmd)(splited)
        except Exception as ex:
            pass


    if(f == "uuid"):
        return  str(uuid.uuid4())

    

    return f
