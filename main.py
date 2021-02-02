####################
# Practice for the web scraper
#####################


# from bs4 import BeautifulSoup
# import requests

# search = input("Enter your search:")
# #q is a get var
# paramas = {"q": search}
# r = requests.get("https://www.bing.com/search", params= paramas)

# #soup parsing with the html parser
# soup = BeautifulSoup(r.text, "html.parser")

# #looking for list items with id of b_results 
# results = soup.find("ol",{"id": "b_results"} )
# #parsing the links of the odered list we parsed
# links = results.findAll("li", {"class": "b_algo"})

# for item in links:
#     #parsing the a tags for the text
#     item_text  = item.find("a").text
#     #then parsing the text for attributes list for href tags
#     item_href = item.find("a").attrs["href"]

#     if item_text and item_href:
#         print(item_text)
#         print(item_href)
#         #finding the parent of the item, in this example h2 is parent of the a tag
#         print("\n Parent:", item.find("a").parent)
#         #finding parent of a parent from the found tag
#         print("\n Summary:", item.find("a").parent.parent.find("a").text) 

#         #finding the children item of the original li item not the children of a tag
#         children = item.children
#         for child in children:
#             print("\n Child:", child)

#         chilling = item.find("h2")
#         print("\n", "Next sibling of the h2: ", chilling.next_sibling)