import urllib.request as req
from bs4 import BeautifulSoup as bs
from pprint import pprint

def getDolar():
	url="http://dolarhoje.com/"
	site =req.urlopen(url).read()


	html = bs(site,"html.parser")
	valor = html.find_all("input",{"id":"nacional"})[0]

	return valor.get("value")

# def get_menu():
# 	url="http://www.ufc.br/restaurante/cardapio/1-restaurante-universitario-de-fortaleza"
# 	site =req.urlopen(url).read()
# 	html = bs(site,"html.parser")

# 	table=html.find_all("tbody")

# 	lines = html.table.find_all("tr")

# 	menu=[]

# 	for line in lines:
# 		columns = line.find_all("td")

# 		if(len(columns)<=1):
# 			meal = columns[0].find_all("h3")[0].get_text()
# 			print(name)
# 			menu.append({"name":name,"categories":[]})

# 		else:
# 			category = columns[0].find_all("span")[0].get_text()
# 			options = [op.get_text() for op in columns[1].find_all("span") if '(' not in op.get_text()]
# 			menu[-1]["categories"].append({"name":category,"option":[]})
# 			print(category)
# 			print(options)
# 	print(menu)
# get_menu()

'''
def get_menu_text(menu):
	text = ""
	for meal in menu :
		text+=meal["name"]+"\n"

		for category in menu["categories"]:
			text+= category["name"]+"\n"

			for op in category["options"]:
				text+=op+"\t"
'''