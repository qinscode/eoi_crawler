## README

# SkillSelect Selenium Script for Australian Immigration

This script is designed to automate the collection of Expression of Interest (EOI) data from the SkillSelect website provided by the Australian Department of Home Affairs. The SkillSelect platform allows skilled workers and business people to record their details to be considered for a skilled visa through an Expression of Interest. It helps manage Australia's skilled migration program and is a crucial resource for both potential migrants and Australian employers.

### Prerequisites

To run this script, ensure you have the following installed on your system:

1. Python 3.x
2. Selenium library
3. Google Chrome browser
4. ChromeDriver

### Installation

1. **Install Python**: Download and install Python from the official website [here](https://www.python.org/downloads/).

2. **Install Selenium**: Use pip to install the Selenium library.
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**: Ensure that the version of ChromeDriver matches your installed version of Google Chrome. Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/downloads) and place it in a directory included in your system's PATH.

### SkillSelect Website Structure

The SkillSelect website is structured to provide various interactive elements for users to input their details and preferences. Key elements include:

1. **Main Page**: Contains navigation elements and links to detailed data reports.
2. **Iframes**: Embedded iframes contain interactive content where users can select specific criteria, view reports, and export data.
3. **Interactive Buttons and Fields**: Elements such as buttons for navigation, search fields, and export options are used to interact with the data.

### Script Overview

The script performs the following steps to automate data collection:

1. **Open the SkillSelect EOI Data Page**: The script navigates to the SkillSelect EOI data page.
2. **Navigate Through the Site**: It clicks through various buttons and selects the appropriate iframe to interact with the website's elements.
3. **Select Data Points**: For each state in Australia, the script selects specific data points related to the state.
4. **Search for Specific State Data**: It inputs the state name in the search field and retrieves the relevant data.
5. **Export Data**: Finally, the script exports the data to a desired format for further analysis.

### How the Script Interacts with Iframes

1. **Switch to Iframe**: The script uses the `switch_to_iframe` function to switch the context to a specific iframe on the webpage. This allows it to interact with elements inside the iframe.
2. **Interact with Elements Inside Iframe**: Once inside the iframe, the script clicks buttons, inputs search criteria, and selects data points.
3. **Switch Back to Default Content**: After interacting with the iframe, the script uses the `switch_to_default_content` function to switch back to the main page context.

### Key Functions

- **wait_and_click**: Waits for an element to be clickable and then clicks it.
- **wait_and_send_keys**: Waits for an input field to be visible and then sends the specified keys to it.
- **switch_to_iframe**: Switches the context to a specified iframe to interact with elements inside it.
- **switch_to_default_content**: Switches the context back to the default content from an iframe.

### Configuration

- **STATE**: List of Australian states for which data is to be collected.
- **XPaths**: XPaths for various elements on the webpage to automate interactions.

### Usage

1. Ensure all dependencies are installed and ChromeDriver is correctly placed.
2. Copy the script into a Python file, e.g., `eoi_data_collection.py`.
3. Run the script:
   ```bash
   python eoi_data_collection.py
   ```

This script will loop through each state in Australia, navigate through the SkillSelect website, search for the specific state's data, and export the data for further analysis. If any errors occur during execution, the script will print the error and continue with the next iteration.

By automating this data collection process, the script saves time and ensures accuracy in retrieving the necessary data from the SkillSelect platform.
