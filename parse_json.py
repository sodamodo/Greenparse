import json
filepath = "resume_json/13582.json"
# readfile = open(filepath, "r")
# lines = readfile.readlines()
# readfile.close()
#
# writefile = open(filepath, "w")
# writefile.writelines([item for item in lines[:-1]])
# writefile.close()

json_file = open(filepath, "r")
json_object = json.loads(json_file.read())
print(json_object)


first_name = json_object["Resume"]["StructuredXMLResume"]["ContactInfo"]["PersonName"]["GivenName"]
midle_name =  json_object["Resume"]["StructuredXMLResume"]["ContactInfo"]["PersonName"]["MiddleName"]
last_name = json_object["Resume"]["StructuredXMLResume"]["ContactInfo"]["PersonName"]["FamilyName"]
country =  json_object["Resume"]["StructuredXMLResume"]["ContactMethod"]["PostalAddress"]["CountryCode"]
postal_code = json_object["Resume"]["StructuredXMLResume"]["ContactMethod"]["PostalAddress"]["PostalCode"]
state = json_object["Resume"]["StructuredXMLResume"]["ContactMethod"]["PostalAddress"]["Region"]
city = json_object["Resume"]["StructuredXMLResume"]["ContactMethod"]["PostalAddress"]["Municipality"]
address = json_object["Resume"]["StructuredXMLResume"]["ContactMethod"]["PostalAddress"]["DeliveryAddress"]["AddressLine"]


print(first_name, midle_name, last_name, country, postal_code)
