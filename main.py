from bs4 import BeautifulSoup

f=open("recette.html","r")
fichier=f.read()
f.close()

soup=BeautifulSoup(fichier, "html.parser")
titre=soup.find("h1")
description=soup.find("p",class_="description")
print(description.text)
print(titre.text)

div_img=soup.find("div",class_="info")
image=div_img.find("img",class_="centre info")
print(image["src"])
