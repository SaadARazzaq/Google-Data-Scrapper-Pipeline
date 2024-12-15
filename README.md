# Google Data Scrapper Pipeline

This project is a web scraping script designed to extract information about medical hospitals in England using Google search results. The data is saved into a CSV file for further analysis or use.

![Untitled design (8)](https://github.com/user-attachments/assets/e33fe887-99e3-44d9-8e4b-60b5a3439dd9)

## Features

- Scrapes hospital information, including:
  - Institute Name
  - Institute Type
  - Location
  - Total Rating
  - Phone Number
  - Website Link
- Navigates through multiple pages of search results to collect comprehensive data.
- Saves the extracted data into a CSV file named `England_hospitals_data.csv`.

## Prerequisites

- Python 3.7+
- The following Python libraries:
  - `asyncio`
  - `csv`
  - `playwright`

## Installation

1. **Install Python**: Ensure Python 3.7 or later is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Playwright**:
   ```bash
   pip install playwright
   ```

3. **Set Up Playwright Browsers**:
   Initialize the Playwright environment to download the necessary browser binaries:
   ```bash
   playwright install
   ```

4. **Ensure Google Chrome Canary**: Verify that Google Chrome Canary is installed on your system and update the `executable_path` in the script to match its location on your machine.

## Usage

1. **Run the Script**:
   Execute the script using the following command:
   ```bash
   python script_name.py
   ```

2. **Script Behavior**:
   - Opens a Chromium browser to perform the search query.
   - Extracts hospital information from Google search results.
   - Saves the collected data into `England_hospitals_data.csv` in the script's directory.

3. **Output File**:
   - The data is saved in `England_hospitals_data.csv` with the following headers:
     - `Institute Name`
     - `Institute Type`
     - `Location`
     - `Total Rating`
     - `Phone Number`
     - `Website Link`

## Notes

- The script operates in non-headless mode (`headless=False`) for debugging purposes.
- The `executable_path` for Chrome Canary must be updated to your local installation path.
- Google search results and structure may change, which could require updates to the script's selectors.

## Limitations

- The script depends on the current structure of Google's search results.
- Google may block automated requests or apply rate limits.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.

## Acknowledgments

- [Playwright Documentation](https://playwright.dev/python/docs/intro)
- Python community for their extensive libraries and support.
