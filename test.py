from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)


driver.get("https://www.jiosaavn.com/artist/s.-p.-balasubrahmanyam-songs/Ix5AC5h7LSg_")


try:
    lang_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'All Languages')]")))
    lang_button.click()
    time.sleep(2)  
except Exception as e:
    print("Failed to select all languages:", e)


while True:
    try:
        load_more = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Load More')]")))
        load_more.click()
        time.sleep(2) 
    except Exception:
        print("No more 'Load More' button found.")
        break


soup = BeautifulSoup(driver.page_source, "html.parser")
songs = soup.find_all("a", class_="u-clickable-name")

song_links = [song['href'] for song in songs]


aditya_music_count = 0

for link in song_links:
    full_link = f"https://www.jiosaavn.com{link}"
    driver.get(full_link)
    time.sleep(2)  

    
    song_soup = BeautifulSoup(driver.page_source, "html.parser")
    copyright_info = song_soup.find("div", class_="copyright").text if song_soup.find("div", class_="copyright") else ""

    
    if "Aditya Music" in copyright_info:
        aditya_music_count += 1


print(f"Total songs under 'Aditya Music': {aditya_music_count}")



driver.quit()
