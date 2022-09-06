#include json library
import json

#json string data
employee_string = '{"Student":{"Name":"John","Age":"15"},"Class":"10"}'

#check data type with type() method
print(type(employee_string))

#convert string to  object
json_object = json.loads(employee_string)

print(json_object)