from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

courses = BeautifulSoup(html.text, 'html.parser')

# Select elements with the combined class names
selected_courses = courses.select('.heading-25-extrabold.color-black')

# Print the selected elements (this will print the entire element as a list)
print(selected_courses)

# Iterate over the selected elements and print their text content
for course in selected_courses:
    print(course.get_text().strip())
