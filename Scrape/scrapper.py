import requests
import csv
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/courses?source=google&medium=cpc&device=c&keyword=geeksforgeeks&matchtype=e&campaignid=20039445781&adgroup=147845288105&gad_source=1&gclid=Cj0KCQiAwvKtBhDrARIsAJj-kTi-Va3oPTWl8M6cCDX0FGSpONR1GEkfZlN74CWCveKQUgFs4CSupmkaAh8UEALw_wcB")

soup = BeautifulSoup(req.content,"html.parser")

 
print(soup.prettify()+" /n")
# print(soup.title.get_text())
# print(soup.title.get_text())
# print(soup.prettify())


# import csv

# # Assume you have a list of dictionaries containing your scraped data
# data = [
#     {'Name': 'John', 'Age': 25, 'Location': 'New York'},
#     {'Name': 'Alice', 'Age': 30, 'Location': 'San Francisco'},
#     # Add more entries as needed
# ]

# # Specify the CSV file name
# csv_filename = 'scraped_data.csv'

# # Write the data to the CSV file
# with open(csv_filename, 'w', newline='') as csvfile:
#     fieldnames = data[0].keys()  # Assuming all dictionaries have the same keys
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     # Write the header
#     writer.writeheader()

#     # Write the data
#     writer.writerows(data)
