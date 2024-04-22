from bs4 import BeautifulSoup
import requests
from threading import Thread

dic={
        "Title":[],
        "Link":[],
        "Ingredients":[]
    }

#FOODNDTV WEBSITE

def foodNDTV_recipes_list():   
    
    #euuuuh a voir si le site ré-ouvre
    recipes_website_homepage = "https://food.ndtv.com/recipes/indian-recipes"
        
    homepage = requests.get(recipes_website_homepage)

    soup = BeautifulSoup(homepage.content, 'html.parser')

    #isolate all the recipes we can find listed on the page and extracts url links to those particular recipes
    

    #click on "more results"
    
    # driver = webdriver.Chrome()
    # driver.get(recipes_website_homepage)
    
    # page_num = 0
    # driver.find_element(By.XPATH,'//*[@id="__cricketsubscribe"]/div/div[3]/a[1]').click()
    # driver.minimize_window()

    
    #recipes = soup.find_all('div', id = "recipeListing" )
    a=0
    # b=0
    #while driver.find_element(By.XPATH, '//*[@id="pagination"]/a'):
    # while a <15:
    #     if driver.find_element(By.XPATH, '//*[@id="pagination"]/a'):
    #         driver.find_element(By.XPATH,'//*[@id="pagination"]/a').click()
    #         page_num += 1
    #         print("getting page number "+str(page_num))
    #         a+=1
    recipes = soup.find_all('a', class_ = "crd_img")
    url_of_each_recipe_list=[]

    for link in recipes :
        if link.has_attr('href'):
            if link['href'].find("hindi") == -1:
                url_of_each_recipe_list.append(link['href'])
           
    dic={
        "Title":[],
        "Ingredients":[]
    }
    for i in range (0,len(url_of_each_recipe_list)):
    # for i in range (0,5):
        url_of_each_recipe = url_of_each_recipe_list[i]
        recipe_page = requests.get(url_of_each_recipe)
        soup2 = BeautifulSoup(recipe_page.content, 'html.parser')

        recipe_title = soup2.title.text

        ingredients = soup2.find_all('li', class_ ="RcpIngd-tp_li")
        ingredients_list=[]
        for j in range (0,len(ingredients)):
            ingredients_list.append(ingredients[j].get_text())

        dic['Title'].append(recipe_title)
        dic['Ingredients'].append(ingredients_list)
    print(dic['Title'][len(dic['Title'])-1])
    for i in range (0, len(dic)-1):
        if dic['Title'][i].find("Hindi") != -1:
            del dic['Title'][i]
            del dic['Ingredients'][i]
    print(len(dic['Ingredients']))
    print(len(dic['Title']))
    print(dic)
    return dic

#HARIGHOTRA WEBSITE

def harighotra_get_recipes_URL_list():
    
    #goes to harighotra main page, adds the URL of all listed recipes in a list and returns that list

    recipes_website_homepage = "https://www.harighotra.co.uk/indian-recipes/courses/mains/view-all"
        
    homepage = requests.get(recipes_website_homepage)

    soup = BeautifulSoup(homepage.content, 'html.parser')

    recipes = soup.find('ul', class_="uk-list uk-list-line cookbook-hari")

    children = recipes.findChildren("a")

    url_of_each_recipe_list=[]

    for child in children:
        if child.has_attr('href'):
            url_of_each_recipe_list.append(child['href'])

    for i in range (0, len (url_of_each_recipe_list)):
        url_of_each_recipe_list[i] = "https://www.harighotra.co.uk"+url_of_each_recipe_list[i]

    
    return url_of_each_recipe_list


def harighotra_ingredients_list(url_of_each_recipe_list, dic, start, stop):

    #goes to each URL listed in the list, and adds to dictionnary the title of the recipe as well as its ingredients

    for i in range (start,stop):

        url_of_each_recipe = url_of_each_recipe_list[i]

        recipe_page = requests.get(url_of_each_recipe)

        soup2 = BeautifulSoup(recipe_page.content, 'html.parser')

        recipe_title = soup2.title.text

        ingredients = soup2.find('div', class_ ="content")

        ingredients_list=[]

        uls = []

        for nextSibling in ingredients.findChild():
            if nextSibling.name == 'ul':
                uls.append(nextSibling)

        for ul in uls:
            for li in ul.findAll('li'):
                ingredients_list.append(li.get_text())
    

        dic['Title'].append(recipe_title)
        dic['Link'].append(url_of_each_recipe)
        dic['Ingredients'].append(ingredients_list)
        

def harighotra_get_ingredients_threading():

    #threads the action of going on each recipe's page, to improve the speed 

    url_list=harighotra_get_recipes_URL_list()

    threads=[]

    for n in range(0, len(url_list), 10):

        stop = n + 10 if n + 10 <= len(url_list) else len(url_list)

        t=Thread(target = harighotra_ingredients_list, args = (url_list, dic, n, stop))

        threads.append(t)


    for i in threads:  
        i.start()

    for j in threads:
        j.join()


def get_harighotra_recipes_dic():

#lauches the threading action and returns the full dictionnary

    harighotra_get_ingredients_threading()
    return dic

