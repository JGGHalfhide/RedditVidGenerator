# RedditVidGenerator

RedditVidGenerator is a Python script that automates the process of scraping a Reddit post's content and generating a humorous, engaging narrative for a YouTube video. The script leverages Selenium to interact with Reddit, BeautifulSoup to parse HTML content, and pyperclip to copy generated prompts from ChatGPT to be used with D-ID text-to-video conversion. The script also opens necessary web pages for further manual interactions.

## Features

- Automatically navigates to Reddit's popular posts.
- Allows user to manually select a post and input the URL.
- Scrapes the content of the selected Reddit post.
- Generates a narrative prompt for a YouTube video via ChatGPT.
- Copies the generated prompt to the clipboard.
- Opens the web page for D-ID text-to-video conversion.

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver (download from [here](https://sites.google.com/a/chromium.org/chromedriver/))
- Selenium: `pip install selenium`
- BeautifulSoup: `pip install beautifulsoup4`
- pyperclip: `pip install pyperclip`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RedditPostScraper.git
   cd RedditPostScraper
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have Google Chrome installed and download the corresponding version of ChromeDriver.

## Usage

1. Run the script:
   ```bash
   python reddit_vid_generator.py
   ```

2. The script will open Google Chrome and navigate to Reddit's popular page. Manually scroll and click on the Reddit post you're interested in.

3. Copy the URL of the selected post, paste it into the terminal, and press Enter.

4. The script will scrape the content of the post, generate a narrative prompt, and copy it to your clipboard.

5. The script will open a new browser window for ChatGPT interaction. Paste the copied prompt into ChatGPT to generate the video script.

6. Once you have the script from ChatGPT, the script will open the text-to-video AI page for further processing.

## Troubleshooting

- Ensure the path to `chromedriver` is correctly specified.
- If the script fails to find elements on the page, increase the wait time in the `WebDriverWait` function.
- Make sure all required Python packages are installed.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [pyperclip](https://pypi.org/project/pyperclip/)
- [Reddit](https://www.reddit.com/)
