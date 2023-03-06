#https://tatianashamshurina.github.io/Resume_Tatsiana_Website/

import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#from selenium import Beautiful
import io

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://tatianashamshurina.github.io/Resume_Tatsiana_Website/")

title_of_page_website = driver.title
print("Title of page Website : ",title_of_page_website)

url_of_page_website = driver.current_url
print("URL of page Website: ",url_of_page_website)

sections_h2 = driver.find_elements(By.NAME,"h2")
for h2 in sections_h2:
    if h2 in sections_h2:
        print(h2.text)
print("*************************************************")
#chercher_image = driver.find_element(By.TAG_NAME,"img")
#print(chercher_image)
print("------------------------------------------------------")
list_links = driver.find_elements(By.TAG_NAME,"a")      #on cherche le liste des liens qui commencent par a
print("Le nombre des liens sur cette page est: ", len(list_links))

                                                            #request BACKEND
                                                     #vyvesti na pechat vse linki iz spiska
compteur=1
for link_a in list_links:
    url = link_a.get_attribute("href")
    print(compteur," - ", link_a.text,url)
    compteur=compteur+1
print("------------------------------------------------------")
for link in list_links:
    print(link.get_attribute("href"))

print("-------------------------------------------------------")

compteur_liens_brises = 0
compteur_liens_valides = 0

for link in list_links:
    url=link.get_attribute("href")
    #reponse = requests.head(url)            #ici - on a recuperé - OTSUDA VYREZAEM I vstavlyem try except
    try:
        reponse = requests.head(url)
    except:
        None

        #comment valider si li lien brise ou non
    if reponse.status_code>=400:
        print(url, " le lien est brisé")
        compteur_liens_brises = compteur_liens_brises + 1
    else:
        #print(url, " le link est Valide")
        compteur_liens_valides = compteur_liens_valides + 1
print("Le nombre des liens brisés: ", compteur_liens_brises)
print("Le nombre des liens valides: ", compteur_liens_valides)

resume_download = driver.find_element(By.LINK_TEXT,"Download Resume").click()
title_of_page = driver.title
print("Title of page to download Resume: ",title_of_page)
url_of_page_download_resume = driver.current_url
print("URL of page to download Resume: ",url_of_page_download_resume)
print("------------------------------------------------------")
#driver.switch_to.default_content()
driver.forward()
#driver.forward()
time.sleep(5)
el_title = driver.find_element(By.XPATH,"//h2[normalize-space()='Software Test Engineer']")
print(el_title.text)
print("-------------------------------------------------------")
#skills = driver.find_element(By.XPATH,"//h3[normalize-space()='Skills & Qualifications']").text
#print(skills)
#print("-------------------------------------------------------")

my_skills = driver.find_elements(By.XPATH,"//ul[@id='qualifications--list']//li")

for el in range(len(my_skills)):
    if el in my_skills:
        print(el.text)
    #my_skills_list = []
    #my_skills_list=my_skills_list.append(el)
#print(my_skills_list)

        with io.open("file.txt", 'w') as file:
            file.write(el)
print("-------------------------------------------------------")

time.sleep(4)
