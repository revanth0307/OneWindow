from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

#initialize the selenium webdriver
driver = webdriver.Chrome()

# Step 1: Open the university directory page
driver.get("https://www.4icu.org/de/universities/")
time.sleep(3)  # for loading the page

# Step 2: Locate and extract state links
state_table = driver.find_element(By.CLASS_NAME, "table")
state_anchors = state_table.find_elements(By.TAG_NAME, 'a')
state_urls = [anchor.get_attribute('href') for anchor in state_anchors]
state_names_list = [anchor.text for anchor in state_anchors]

# Base URL used to form full links
base_site_url = "https://www.4icu.org"
university_data_list = []

# Step 3: Loop through each state's page to gather universities' URLs
for index, state_url in enumerate(state_urls):
    current_state = state_names_list[index]

    # Open the state-specific page
    driver.get(state_url)
    time.sleep(2) #let the page load

    # Find university table rows and extract links
    university_anchors = driver.find_elements(By.CSS_SELECTOR, "tbody a")
    university_urls = [anchor.get_attribute('href') for anchor in university_anchors]

    # Step 4: Scrape each university page
    for uni_url in university_urls:
        driver.get(uni_url)
        time.sleep(2)

        #scarp all the attributes which are required

        # Scrape the university name
        try:
            university_name = driver.find_element(By.CSS_SELECTOR, 'h1[itemprop="name"]').text
        except:
            university_name = "Not Available"

        # Scrape university's establishment year
        try:
            establish_year = driver.find_element(By.CSS_SELECTOR, 'span[itemprop="foundingDate"]').text
        except:
            establish_year = "Not Available"

        # Scrape the university type (public/private)
        try:
            type_element = driver.find_element(By.CSS_SELECTOR, '.col-sm-6.col-md-3 strong')
            university_type = type_element.text.strip() if type_element else "Unknown"
        except:
            university_type = "Unknown"

        # Scrape university logo
        try:
            logo_src = driver.find_element(By.CSS_SELECTOR, 'img[itemprop="logo"]').get_attribute('src')
        except:
            logo_src = "Not Available"

        # Scrape address details
        try:
            address_panel = driver.find_element(By.CSS_SELECTOR, 'div[itemprop="address"]')
            address_city = address_panel.find_element(By.CSS_SELECTOR, 'span[itemprop="addressLocality"]').text
            address_state = address_panel.find_element(By.CSS_SELECTOR, 'span[itemprop="addressRegion"]').text
            address_country = address_panel.find_elements(By.TAG_NAME, 'td')[-1].text
        except:
            address_city = current_state
            address_state = current_state
            address_country = "Not Available"

        # Extract social media contacts
        social_media_links = {}
        social_anchor_tags = driver.find_elements(By.TAG_NAME, 'a')
        for anchor in social_anchor_tags:
            social_url = anchor.get_attribute('href')  # Extract href attribute
            if social_url:  # Ensure the URL is not None
                if "facebook.com" in social_url:
                    social_media_links["Facebook"] = social_url
                elif "twitter.com" in social_url:
                    social_media_links["Twitter"] = social_url
                elif "youtube.com" in social_url:
                    social_media_links["YouTube"] = social_url
                elif "instagram.com" in social_url:
                    social_media_links["Instagram"] = social_url
                elif "linkedin.com" in social_url:
                    social_media_links["LinkedIn"] = social_url

        # Extract the official website URL
        try:
            official_website = driver.find_element(By.CSS_SELECTOR, 'a[itemprop="url"]').get_attribute('href')
            social_media_links["Website"] = official_website
        except:
            social_media_links["Website"] = "Not Available"

        # Prepare the university entry in the required JSON structure
        university_entry = {
            "universityDetails": {
                "name": university_name,
                "logo": logo_src,
                "establishedYear": establish_year,
                "type": university_type
            },
            "locationInfo": {
                "city": address_city,
                "state": address_state,
                "country": address_country
            },
            "socialMediaLinks": social_media_links
        }

        # Append the university data to the list
        university_data_list.append(university_entry)

# Step 5: Write the data to a JSON file
with open('university_info_selenium.json', 'w', encoding='utf-8') as output_file:
    json.dump(university_data_list, output_file, ensure_ascii=False, indent=4)

# Close the Selenium WebDriver
driver.quit()
