Appium and Selenium Test Automation
This repository contains test automation scripts using both Appium for mobile applications and Selenium for web applications. 
The tests focus on comparing movie and TV show information between IMDb's mobile app and website, as well as managing watchlists.

Features
Web Tests: Automates interactions with IMDb's website to:
Search for movies.
Compare popular TV shows.
Check top movies and TV shows.
Create, verify, and delete watchlists.

Mobile Tests: Uses Appium to:
Search for movies and compare results with the website.
Verify fan favorites and top TV shows.
Create and manage watchlists.

Setup:
Prerequisites
Python: Make sure you have Python installed.
Appium: Ensure you have Appium server running.
WebDriver: Install necessary web drivers for browsers (e.g., GeckoDriver for Firefox).

Installation
Clone the repository:
Copy code
git clone https://github.com/username/repository.git
cd repository

Install dependencies:
Install the required Python libraries using pip:
Copy code
pip install -r requirements.txt

Ensure requirements.txt includes:
appium-python-client
selenium
webdriver-manager
unittest
Configure Appium:

Ensure Appium server is running on http://localhost:4723/wd/hub.

Update Configuration:

Update any necessary configurations in the test scripts, such as email credentials or device capabilities.

Usage
Run the tests using the following command:

Copy code
python -m unittest discover

Tests
test1_search_movie: Searches for a movie and compares results between web and mobile.
test2_Compare_Fan_Favorites: Compares fan favorites between web and mobile.
test3_Compare_Top_TV_Shows: Compares the top TV shows between web and mobile.
test4_Compare_Top_3_Movies: Compares the top 3 movies between web and mobile.
test5_Create_Verify_and_Delete_Watchlist: Creates, verifies, and deletes a watchlist on mobile and web.
