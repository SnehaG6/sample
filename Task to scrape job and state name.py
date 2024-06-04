import requests
from bs4 import BeautifulSoup
url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    job_titles = soup.find_all("h2", class_="title")
    state_names = soup.find_all("p", class_="location")
    with open("scraped_data.txt", "w") as file:
        for title, state in zip(job_titles, state_names):
            file.write(f"{title.text.strip()} - {state.text.strip()}\n")

    print("Scraping and writing to file complete.")
else:
    print("Failed to retrieve the webpage.")
