import xmltodict
import json

def convert_xml_to_json(xml_string):
    # Convert the XML string to an OrderedDict
    xml_dict = xmltodict.parse(xml_string)
    # Convert the OrderedDict to a JSON string
    json_string = json.dumps(xml_dict)
    # Return the JSON string
    return json_string

x = convert_xml_to_json("<note><to>Mikasa</to><from>Eren</from><heading>Tatakae</heading><body>To my average self..</body></note>")
print("json : ", x)