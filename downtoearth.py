
from requests import get
from bs4 import BeautifulSoup

import io




url = input("enter the down to earth url to be scrapped:\n")
file_name = input("enter the file name to be stored along with proper extension:\n")
response = get(url)

#UNDER-CONSTRUCTION

#take words to be searched as input
# N = int(input("enter the number of words to be searched:\n"))
# word_list = list(map(lambda x: input("enter word number x"), range(0, N)))



html_soup = BeautifulSoup(response.text, "lxml")

	
heading = str(html_soup.find("div", class_="container_2").find_all(text = lambda s:"h3" in s))    #heading of the article

main_content = html_soup.find("div",{'id':'main_article_content'}).find_all(text  = lambda s: "p" in s)


# main_content = html_soup.find("div",{'id':'main_article_content'}).find_all("p")   #extract the contents of the file
# print(main_content)





with io.open(file_name, mode='a', encoding='utf-8') as f:
	 f.write(str(heading))
	 f.write(str(main_content))












#UNDER-CONSTRUCTION

#extract list of other urls(in_progress)

# list_of_urls = list(map(lambda link: link.get('href'), html_soup.find_all("a")))






