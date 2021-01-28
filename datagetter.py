
import json
class DataGetter():
    def db(params):
        query =   ("SELECT " + params[2]+  " FROM  " + params[1])

        q =  ""
        try: 

            if(params[3]): 
                parsedJson = params[3].replace("=>" , ":")
                parsedParams =  json.loads(parsedJson)
                for par in parsedParams:
                    q = par + " = '" + parsedParams[par]+ "'" 
        except : 
            pass    
            
        if q != "" :
            query = query + " WHERE " +  q
             

        return query
        


    def raw(returningdata):
        
        return  returningdata