from parse_ingredients import parse_ingredient

def ingredients_list_parsing(dic):
    output_dic={
     'Ingredients':[[]for u in range (0, len(dic['Ingredients']))],
     'Quantity':[[]for u in range (0, len(dic['Ingredients']))],
     'Unit':[[]for u in range (0, len(dic['Ingredients']))]
    }
    for u in range (0, len(dic['Ingredients'])):
        for i in range (0, len(dic['Ingredients'][u])):
            dic['Ingredients'][u] = list(filter(None, dic['Ingredients'][u]))
    for u in range (0, len(dic['Ingredients'])):
        for i in range (0, len(dic['Ingredients'][u])):
            if dic['Ingredients'][u][i].find('ï¿') != -1:
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace("ï¿", "")
            if dic['Ingredients'][u][i].find('½\\xa0') != -1:
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace("½\\xa0", "0.5 ")
            if dic['Ingredients'][u][i].find('½') != -1:
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace("½", "0.5 ")
            if dic['Ingredients'][u][i].find('half') != -1:
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace("half", "0.5 ")
            if dic['Ingredients'][u][i].find('½\xa0') != -1:
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace("½\xa0", "0.5 ")
            if dic['Ingredients'][u][i].find('\\xa0') != -1:
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace("\\xa0", "")
            if dic['Ingredients'][u][i].find('\xa0') != -1:
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace("\xa0", "")
            if dic['Ingredients'][u][i].find("a ") != -1 and dic['Ingredients'][u][i][0] == 'a':
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace("a ", "1 ")
            if dic['Ingredients'][u][i].find(" a ") != -1:
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace(" a ", " 1 ")
            if dic['Ingredients'][u][i].find('of ') != -1:
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace("of ", "")
            if dic['Ingredients'][u][i].find(',') != -1:
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace(",", "")
            if dic['Ingredients'][u][i].find(' or ') != -1:
                dic['Ingredients'][u][i]=dic['Ingredients'][u][i].replace(" or ", "-")
            if (dic['Ingredients'][u][i][0].isdigit() == False) and (dic['Ingredients'][u][i][0] != '0'):
                dic['Ingredients'][u][i]="1 "+dic['Ingredients'][u][i]

            # print(dic['Ingredients'][u][i])
            # print(u)
            # print(i)
            result=parse_ingredient(dic['Ingredients'][u][i])
            output_dic['Ingredients'][u].append(result.name)
            output_dic['Quantity'][u].append(result.quantity)
            output_dic['Unit'][u].append(result.unit)

            
    return output_dic