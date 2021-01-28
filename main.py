import fire
import json,  urllib.request
import re
from  parser import startParse

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def run(path):
    """
    Parse Generated OAS To Readable OAS
    :param path: Path to OAS .json file / url
    :return: Parsed Oas With Corrent Parameter
    """
    print("Used path : " + path)

    jsonData = []
    try:
        # Check if request path is url
        if re.match(regex, path) is not None : 
            # Get json with corsscomp  urlib

            print("Load From  Url")
            with urllib.request.urlopen(path) as url:
                jsonData = json.loads(url.read().decode())
        else: 
            with open(path, 'r') as myfile:
                data=myfile.read()
                jsonData = json.loads(data)


    except Exception as ex:
        print("Can't load json file")
        quit()
    pass



    # Begin Parsing Data
    print("Begin Parsing Data")

    startParse(jsonData)

    


if __name__ == "__main__":
    fire.Fire(run)