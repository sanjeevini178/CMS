import json

dict={"EMP": ["Admin", "admin", "root", "9999999999", "admin@admin.com", "M"], 
"EMP2": ["Doctor", "doc", "doc", "9999999999", "admin@admin.com", "M"],
"EMP3": ["Receptionist","recep","recep","9999999999","admin@admin.com","M"],
"Santhosh":["Doctor","santy","santy123","9090980808","doctor@doctor.com","M"],
"Sachin":["Receptionist","sachi","sachi123","80808900909","recep@recep.com","F"],
"Sairam":["Doctor","Sai","Sairam_1926","9940502832","Sairam1926@gmail.com","M"],
"Lol":["Doctor","lol","lol@lol@lol","1234567890","lol@","M"]}

f=open('userrecord.json','w')
json.dump(dict,f)