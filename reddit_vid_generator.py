from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pyperclip
import webbrowser

# Initialize variables
page_title = "Page Title Unavailable"
content_text = "Content Unavailable"

# Initialize and configure Chrome browser
options = webdriver.ChromeOptions()

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

try:
    # Navigate to Reddit's popular page
    driver.get("https://www.reddit.com/r/popular")

    # Wait for user to interact manually and get the URL of the desired post
    input("Scroll and click on the Reddit post you're interested in. "
          "After copying the URL, paste it here and press Enter to continue... ")

    # Prompt user to paste the copied URL
    post_url = input("Paste the URL here: ")

    # Navigate to the pasted URL
    driver.get(post_url)

    # Wait for the page to load
    wait = WebDriverWait(driver, 20)

    # Print the title of the page
    page_title = driver.title
    print("Page Title:", page_title)

    # Wait until the post content is visible
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'mb-sm')))

    # Get the page source
    page_source = driver.page_source

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the main content div inside the post
    main_content_div = soup.find('div', {'class': 'mb-sm'})

    if not main_content_div:
        raise Exception("Could not find the main content div")

    # Find the inner content div
    inner_content_div = main_content_div.find('div', {'class': 'md'})

    if not inner_content_div:
        raise Exception("Could not find the inner content div")

    # Extract the text content from each paragraph
    paragraphs = inner_content_div.find_all('p')
    content_text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])

    print("Page Content:")
    print(content_text)

except Exception as e:
    print("Error retrieving page content:", e)

finally:
    # Generate the prompt for the YouTube video script
    prompt = f"You are an extremely popular Youtuber who makes viral videos. Generate an engaging, " \
             f"humorous narrative (approximately 60 seconds in length) based on the following reddit post for a " \
             f"YouTube video. Be sure to prompt the viewer to leave their " \
             f"thoughts for engagement: Title-{page_title} Content-{content_text}. Include a video title and description at the top " \
             f"for me too."

    # Copy the prompt to clipboard using pyperclip
    pyperclip.copy(prompt)

    # Launch a new window manually for ChatGPT interaction
    gpt_url = 'https://chatgpt.com/'
    webbrowser.open_new(gpt_url)

    # Prompt the user to interact manually with ChatGPT
    input("Copy the script and press enter after you have finished interacting with ChatGPT manually...")

    # Navigate to the text to video AI page
    text_to_vid = "https://studio.d-id.com/"
    webbrowser.open_new(text_to_vid)

    # Close the browser
    driver.quit()
