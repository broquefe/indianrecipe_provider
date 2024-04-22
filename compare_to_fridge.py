import json

def compare_to_fridge(dic, parsed_dic, a):
    with open('fridge.json') as user_file:
        fridge_json = json.load(user_file) 
    
    number_of_available_recipes=0
    for j in range (0,len(parsed_dic['Ingredients'])):
        # compteur=0
        ingredients_to_buy_compteur=0
        ingredient_to_buy_list=[]
        # for key in parsed_json:
        #     for i in range (0,len(parsed_dic['Ingredients'][j])):
        #         if key in parsed_dic['Ingredients'][j][i]:
        #             compteur+=1
        key_number=0
        i=0   
        while ingredients_to_buy_compteur <= a and i < len(parsed_dic['Ingredients'][j]):
            
            for key in fridge_json:
                if key not in parsed_dic['Ingredients'][j][i]:
                    key_number+=1
                
            if key_number == len(fridge_json):
                ingredients_to_buy_compteur+=1
                ingredient_to_buy_list.append(parsed_dic['Ingredients'][j][i])
            key_number=0
            i+=1
                    
        
        #if compteur + a >= len(parsed_dic['Ingredients'][j]):
        if i == len(parsed_dic['Ingredients'][j]) and ingredients_to_buy_compteur <= a:
            print(dic['Title'][j])
            print(dic['Link'][j])
            number_of_available_recipes+=1
            print(ingredients_to_buy_compteur)
            print("liste des ingredients à acheter :")
            print(ingredient_to_buy_list)
            print("Ingredients de la recette :")
            print(parsed_dic['Ingredients'][j])
            
    print(number_of_available_recipes)