# Making the soup:
# To parse a document, pass it into the BeautifulSoup constructor. You can pass in a string or an open filehandle:

from bs4 import BeautifulSoup
import requests

url_list = []


# Creating the BeautifulSoup object, usually called soup:
with open("LectureSchedule.html") as file:
    soup = BeautifulSoup(file,'html.parser')

# The find_all method returns a list:
a_list = soup.find_all('a')
for tag in a_list:
    # You can iterate over a tag’s children using the .children generator:
    for child in tag.children:
        if 'Handout' in child:
            url_list.append(tag['href'])

# Opening file so it's ready to write into:
opened_file = open("lectures.html", "w")

for url in url_list:
    # requests.get() is a function imported from the Python requests library.
    # 'verify=False' will allow us to skip the website's https authenticity verification 
    # process, which a browser usually handles automatically.
    response_object = requests.get(url, verify=False)

    if response_object.status_code == 200:
        #append page text to group file:
        opened_file.write(response_object.text)
    else:
        print(f"Oh, no! Status code {response_object.status_code}!")
        continue


opened_file.close()
    



# <a target="_blank" href="http://fellowship.hackbrightacademy.com/materials/t1/lectures/maze-traversal/">
#                     <i class="fa fa-file-text"></i>
#                     Handout
#                   </a>



#A tag’s children are available in a list called .contents:
# soup.a.contents[0]



# Instead of getting them as a list, you can iterate over a tag’s children using the .children generator:

# for child in title_tag.children:
#     print(child)
# # The Dormouse's story