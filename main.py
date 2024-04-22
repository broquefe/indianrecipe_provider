from scrapping import get_harighotra_recipes_dic
from ingredients_parser import ingredients_list_parsing
from compare_to_fridge import compare_to_fridge

def main():

    harighotra_dic=get_harighotra_recipes_dic()

    parsed_dic=ingredients_list_parsing(harighotra_dic)
    
    compare_to_fridge(harighotra_dic, parsed_dic,1)

main()

