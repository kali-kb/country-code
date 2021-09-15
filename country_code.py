def get_country_code(country_name):
	new_name = country_name.replace(" ",         "_")
	code = {}
	url = "https://wikipedia.org/wiki/{}".format(new_name)
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	d_tree = soup.find_all(text="Calling code")[0].parent.parent.parent
	#for th in d_tree.th:
	#	print(th)
	country_code = (d_tree.find(class_="infobox-data").a.text)
	code[country_name] = country_code
	return code
	
print(get_country_code("Italy"))
