**Document Title: Google Maps Business Skimping v1 Documentation**

### Objective:

The objective of this Python script is to skimp business information from Google Maps based on user-defined search queries and locations. The script utilizes the Playwright library to automate interactions with the Google Maps web interface, extract data, and organize it into a structured format. The primary goal is to provide users with a convenient way to gather minimal business details, such as name, address, website, and phone number, for quick analysis or storage with minimal resource usage.

### Requirements:

1. **Command-Line Arguments:**
   - `-s` or `--search`: Specify the skimp term for Google Maps (e.g., "dentist").
   - `-l` or `--location`: Specify the location for the skimp (e.g., "new york").

   If these arguments are not provided, the script defaults to skimping for "dentist new york."

2. **Web Skimping:**
   - Use Playwright to automate the browser for interacting with Google Maps.
   - Perform a skimp based on the user-provided skimp term and location.
   - Extract minimal business information from the skimp results, including name, address, website, and phone number.

3. **Data Structuring:**
   - Define two data classes (`Business` and `BusinessList`) to structure the skimmed data.
   - Use these classes to create a Pandas DataFrame for easy manipulation and analysis of the skimped data.

4. **Data Output:**
   - Save the skimmed business data to both Excel (.xlsx) and CSV (.csv) files.
   - Files are named based on the skimp term (e.g., "skimped_map_data.xlsx" and "skimped_map_data.csv").

### Approach:

1. **Initialization:**
   - Initialize Playwright and launch a Chromium browser.

2. **Skimp Execution:**
   - Navigate to Google Maps and perform a skimp based on the user-defined skimp term and location.
   - Handle user-provided or default skimp parameters.

3. **Skimping Business Information:**
   - Locate and extract minimal information from the skimp results, including business name, address, website, and phone number.
   - Utilize XPath expressions to target specific elements on the page.

4. **Data Structuring:**
   - Organize the skimmed data into instances of the `Business` class and store them in a `BusinessList` object.

5. **Data Output:**
   - Convert the data to a Pandas DataFrame for easy manipulation.
   - Save the data to Excel and CSV files using the provided methods in the `BusinessList` class.

6. **Closing Browser:**
   - Close the browser instance after skimping and saving the data.

### Tech Stack:

- **Programming Language:** Python
- **Web Automation Library:** Playwright
- **Data Manipulation Library:** Pandas

### Usage:

The script is intended to be executed from the command line, accepting user-provided skimp and location parameters. Example usage:

```bash
python main.py -s "eatery" -l "los angeles"
```

If no skimp term and location are provided, the script defaults to:

```bash
python main.py
```

### Conclusion:

This script provides a straightforward and resource-efficient solution for skimping business information from Google Maps, allowing users to quickly gather essential data for rapid analysis or storage with minimal overhead. Users can tailor the skimp parameters based on their specific requirements.