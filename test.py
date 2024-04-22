from spellchecker import SpellChecker
import inflect
from scrapping import get_harighotra_recipes_dic
from ingredients_parser import ingredients_list_parsing
import json
from parse_ingredients import parse_ingredient


# p=inflect.engine()

# print(p.plural("tomato"))
# print(p.plural("carrot"))
# print(p.plural("tomatoes"))
 
# spell = SpellChecker()
 
# # find those words that may be misspelled
# misspelled = spell.unknown([ "chiken"])
 
# for word in misspelled:
#     # Get the one `most likely` answer
#     print(p.plural(spell.correction(word)))
 
#     # Get a list of `likely` options
#     print(spell.candidates(word))

dic=get_harighotra_recipes_dic()
# print(dic['Ingredients'])
# print(len(dic['Ingredients']))
# print(dic['Ingredients'][0])
# print(len(dic['Ingredients'][0]))
# print(dic['Ingredients'][0][0])
# print(len(dic['Ingredients'][0][0]))
# a=3
# b='chicken'
c=[]
# print(dic['Title'])
# for i in range(0,len(dic['Title'])):
#     if dic['Title'][i].find('paneer') != -1 or dic['Title'][i].find('Panneer') != -1:
#         c.append(dic['Ingredients'][i])
# print(dic['Ingredients'][2])
# with open('ingredients.txt', 'w+') as f:
#     for items in c:
#         f.write('%s\n' %items)
# dic={
#     'product':[],
#     'quantity':[],
#     'unit':[]
# }
guillements=[]

# f=open('ingredients.txt', 'r')
# string=f.read()
# for i in range (0, len(string)):
#     if string[i]=="'":
#         guillements.append(i)

# list=[]

# a=0
# b=1
# dic={
#     'Ingredients':[]
# }

# for i in range(0, len(guillements)):
#     if i == b:
#         phrase=""
#         for j in range (guillements[a]+1, guillements[b]):
#             phrase+=string[j]
#         list.append(str(phrase))
#         a+=2
#         b+=2

# dic['Ingredients'].append(list)
# print(dic['Ingredients'])

dic2=ingredients_list_parsing(dic)

print(dic['Title'][2])
print(dic2['Ingredients'][2])
print(dic2['Quantity'][2])

print(dic['Title'][52])
print(dic2['Ingredients'][52])
print(dic2['Quantity'][52])

print(dic['Title'][82])
print(dic2['Ingredients'][82])
print(dic2['Quantity'][82])
# a=[]
# for i in range (0,len(dic2['Quantity'][82])):
#     print(dic2['Ingredients'][82][i])
#     #r=parse_ingredient(dic2['Ingredients'][82][i])
#     #a.append(r.name)
# print(a)
# for i in range (0, len(list)):
    
#     if list[i].find('½\\xa0') != -1:
#         list[i]=list[i].replace("½\\xa0", "0.5 ")
#     if list[i].find('\\xa0') != -1:
#         list[i]=list[i].replace("\\xa0", "")
#     if list[i].find("a ") != -1 and list[i][0] == 'a':
#         list[i]=list[i].replace("a ", "1 ")
#     if list[i].find(" a ") != -1:
#         list[i]=list[i].replace(" a ", " 1 ")
#     if list[i].find('of ') != -1:
#         list[i]=list[i].replace("of ", "")
#     if list[i][0].isdigit() == False:
#         list[i]="1 "+list[i]
#     if list[i].find(' or ') != -1:
#         print(list[i].find(' or '))
#         list[i]=list[i].replace(" or ", "-")
         
# print(list)

# for i in range (0, len(list)-1):
#ingredient = parse_ingredient.parse_multiple(list)
#ing_list.append(ingredient.product)
#result = parse_ingredient("12 ounces lean ground beef, preferably 85 percent lean")
    #if i != 6 :
        # result2=parse_ingredient(list[i])
#print(f"Found results: \n {result}")
        # dic["product"].append(result2.name)
        # dic["quantity"].append(result2.quantity)
        # dic["unit"].append(result2.unit)

# with open("fridge.json", "w") as outfile:
#     json.dump(dic, outfile)
#print(json.dumps(ingredient.as_dict()))

# for i in range (0, len(list)):
    
with open('fridge.json') as user_file:
   parsed_json = json.load(user_file)

a=["carrots","chicken cuts","flour","tomatoes", "fish with coriander"]
# check = all(item in parsed_json for item in a)
# print(check)
#pbs      tbsp  

for j in range (0,len(dic2['Ingredients'])):
    compteur=0
    for key in parsed_json:
        for i in range (0,len(dic2['Ingredients'][j])):
            if key in dic2['Ingredients'][j][i]:
                compteur+=1
        
    if compteur +4 > len(dic2['Ingredients'][j]):
        print(dic['Title'][j])
    else:
        print("eeeeh non")