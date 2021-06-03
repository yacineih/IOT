import json
import pprint

objet_1 = {
"nom":"PERRET",
"prénom":"Inés",
"âge":"0x20",
"notes":[10,12,14,20],
"commentaires":"c'est bien ;) ",
"oral": False,
"écrot": True,
"oral": None,
10:10e3
}

print (objet_1)

struct_json = json.dumps(objet_1)
print("\n")
print("\n")


print(struct_json)
print("\n")
print("\n")

struct_python2 = json.loads(struct_json)
print(struct_python2)
