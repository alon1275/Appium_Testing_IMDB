from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Imdb_mobileElements:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, by, value, timeout=10):
        return self.wait.until(
            EC.presence_of_element_located((by, value))
        )

    def continue_button(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.imdb.mobile:id/welcome_dialog_continue"]')

    def not_now_button(self):
        return self.wait_for_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.imdb.mobile:id/splash_not_now']")

    def search_button(self):
        return self.wait_for_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.imdb.mobile:id/navigation_bar_item_icon_view"])[2]')

    def search_field(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.imdb.mobile:id/search_src_text"]')

    def search_field2(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/search_src_text')

    def result1(self):
        return self.wait_for_element(AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.imdb.mobile:id/suggestion"])[1]')

    def title_result1(self):
        return self.wait_for_element(AppiumBy.XPATH, '(//android.widget.TextView[@text="The Matrix"])[1]')

    def profile_icon(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/navigation_user_profile')

    def home_icon(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/navigation_home')

    def tip_exit(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.imdb.mobile:id/exit"]')

    def sign_in_button(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/sign_in_button')

    def imdb_account_sign_in(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/imdb_auth_portal')

    def imdb_account_username(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.webkit.WebView[@text="IMDb Sign-In"]/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.EditText')

    def imdb_account_password(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.webkit.WebView[@text="IMDb Sign-In"]/android.view.View/android.view.View[2]/android.view.View[4]/android.widget.EditText')

    def account_sign_in_button(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.Button[@text="Sign in"]')

    def watchlist_button(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/user_lists')

    def list_title(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.imdb.mobile:id/label"]')

    def movie1_2(self):
        return self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.imdb.mobile:id/primaryText"]')

    def advanced_search_select(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Advanced Search"]')

    def tv_series_select(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.Button[@text="TV Series"]')

    def see_results_button(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/see_results')

    def tv_series_title_results(self):
        return self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.imdb.mobile:id/primaryText"]')

    def add_list_watchlist(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.ImageButton[@resource-id="com.imdb.mobile:id/fab"]')

    def list_name(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/list_name')

    def list_type_name(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/name')

    def list_save(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/save_list_button')

    def added_list(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/label')

    def insert_text_name(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/search_src_text')

    def gal_gadot_result(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.imdb.mobile:id/label" and @text="Gal Gadot"]')

    def mark_ivanir_result(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.imdb.mobile:id/label" and @text="Mark Ivanir"]')

    def added_names_to_list(self):
        return self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.imdb.mobile:id/primaryText"]')

    def rate_shows_movies_button(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.imdb.mobile:id/button"]')

    def popular_movies_rate(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.imdb.mobile:id/widget_text" and @text="Popular movies"]')

    def rate_this_button(self):
        return self.wait_for_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.imdb.mobile:id/rateButton"]')

    def star_10(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/star_10')

    def rate_button(self):
        return self.wait_for_element(AppiumBy.ID, 'com.imdb.mobile:id/rate_title_button')

    def fan_favorites(self):
        # Scroll down until the element with the specified text is visible
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Deadpool & Wolverine"));')

        # Find and return the element after scrolling
        return self.driver.find_element(by=AppiumBy.XPATH,
                                        value='//android.widget.TextView[@resource-id="com.imdb.mobile:id/main_line" and @text="Deadpool & Wolverine"]')

    def top250_movies(self):
        # Scroll down until the element with the specified resource-id is visible
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.imdb.mobile:id/outer_cardview").instance(5));')

        # Find and return the element after scrolling
        return self.driver.find_element(by=AppiumBy.XPATH,
                                        value='(//android.widget.FrameLayout[@resource-id="com.imdb.mobile:id/outer_cardview"])[5]/android.view.ViewGroup')

    def top3_movies(self):
        return self.driver.find_elements(by=AppiumBy.XPATH, value='(//android.widget.TextView[@resource-id="com.imdb.mobile:id/primaryText" and (@text="1. The Shawshank Redemption" or @text="2. The Godfather" or @text="3. The Dark Knight")])')