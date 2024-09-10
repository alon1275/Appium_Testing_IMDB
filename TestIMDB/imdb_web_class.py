from time import sleep

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriver


class Imdb_HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver_w = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, by, value, timeout=10):
        return self.wait.until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_elements(self, by, value, timeout=10):
        return self.wait.until(
            EC.presence_of_all_elements_located((by, value))
        )

    def watchlist(self):
        return self.wait_for_element(By.XPATH, "/html/body/div[2]/nav/div[2]/div[4]/a/span")

    def sign_in_elements(self):
        return self.wait_for_elements(By.CLASS_NAME, 'list-group-item ')  # by index

    def home_logo_button(self):
        return self.wait_for_element(By.ID, "home_img_holder")

    def sign_in_page(self):
        return self.wait_for_elements(By.CLASS_NAME, "a-input-text")  # by index

    def sign_in_button(self):
        return self.wait_for_element(By.ID, "signInSubmit")

    def create_new_list_button(self):
        # Wait for the element to be clickable
        return self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ipc-icon.ipc-icon--add.ipc-btn__icon.ipc-btn__icon--pre"))
        )

    def list_name(self):
        return self.wait_for_element(By.CLASS_NAME, "ipc-textinput__input")

    def create_list_button(self):
        return self.wait_for_element(By.XPATH, "/html/body/div[2]/main/div/section/div/section/div/div[1]/section/button")

    def search_movie_for_list(self):
        return self.wait_for_element(By.CLASS_NAME, "ipc-textinput__input")

    def movie_results_search(self):
        return self.wait_for_elements(By.CSS_SELECTOR, "ul > li > div > span")  # By index

    def filter_selector_search(self):
        return self.wait_for_element(By.XPATH, "/html/body/div[2]/nav/div[2]/div[1]/form/div[1]/div/span[1]/label/span")

    def advanced_search_button(self):
        return self.wait_for_element(By.XPATH, "//div/div/div/div/ul/a/span[1]")

    def search_filters(self):
        return self.wait_for_elements(By.CLASS_NAME, "ipc-accordion__item__chevron")  # by index

    def tv_series_option(self):
        return self.wait_for_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[2]/div/section/button[2]")

    def see_results(self):
        return self.wait_for_element(By.XPATH, "//main//section//div[1]/button/span")

    def popular_tv_shows_result(self):
        return self.wait_for_elements(By.CLASS_NAME, "ipc-title__text")  # by index

    def scroll_to_element_and_click(self, by, value):
        try:
            # Wait until the element is present on the page
            element = self.wait.until(
                EC.presence_of_element_located((by, value))
            )
            # Scroll to the element to ensure it is in view
            self.driver_w.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            # Optionally, wait a bit to allow the page to settle after scrolling
            sleep(1)

            # Wait until the element is clickable
            element = self.wait.until(
                EC.element_to_be_clickable((by, value))
            )
            # Click the element
            element.click()
        except TimeoutException:
            print(f"Timeout: Element located by {by} with value {value} was not found or was not clickable.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def your_lists_button(self):
        # Parameters of the CSS Selector for the element
        return self.scroll_to_element_and_click(By.XPATH,
                                                '/html/body/div[2]/main/div/section/div/section/div/div[2]/div/div[2]/div/section[2]/div/div[1]/div/a')

    def added_actors_watchlist(self):
        return self.driver_w.find_element(By.XPATH,
                                      "//a[@class='ipc-metadata-list-summary-item__t' and @href='/list/ls546215278/?ref_=uspf_t_1']")

    def three_dots_icon(self):
        return self.wait_for_element(By.CSS_SELECTOR, 'div > button.ipc-responsive-button')

    def delete_option(self):
        return self.wait_for_element(By.ID, 'list-dropdown-option-delete')

    def confirm_delete(self):
        return self.wait_for_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div/div/button[2]')

    def account_icon(self):
        return self.wait_for_element(By.XPATH, '/html/body/div[2]/nav/div[2]/div[5]/div/label[2]/span/span')

    def your_lists_option(self):
        return self.wait_for_element(By.XPATH, '/html/body/div[2]/nav/div[2]/div[5]/div/div/div/div/span/ul/a[4]/span')

    def lists_are_null(self):
        return self.wait_for_element(By.CSS_SELECTOR, 'div>section>div.sc-8e53c551-4')

    def fan_favorites(self):
        # גלילה למטה בעמוד
        self.driver_w.execute_script("window.scrollBy(0, 2000);")

        # מציאת האלמנט לפי aria-label
        element = self.driver_w.find_element(By.CSS_SELECTOR, '[aria-label="View title page for Deadpool & Wolverine"]')

        # קבלת הערך של ה-aria-label
        aria_label_text = element.get_attribute("aria-label")

        # החזרת הטקסט של ה-aria-label
        return aria_label_text

    def search_bar(self):
        return self.driver_w.find_element(By.CSS_SELECTOR, '.imdb-header-search__input.searchTypeahead__input.react-autosuggest__input')

    def search_bar_button(self):
        return self.driver_w.find_element(By.ID, 'suggestion-search-button')

    def search_result(self):
        return self.driver_w.find_elements(By.CSS_SELECTOR, 'div>.ipc-metadata-list-summary-item__t')

    def movie_result_page(self):
        return self.driver_w.find_element(By.CSS_SELECTOR, 'div>h1>.hero__primary-text')

    def menu_button(self):
        return self.driver_w.find_element(By.ID, 'imdbHeader-navDrawerOpen')

    def top250_movies(self):
        return self.driver_w.find_element(By.XPATH, '/html/body/div[2]/nav/div[2]/aside[1]/div/div[2]/div/div[1]/span/div/div/ul/a[2]/span')

    def top3_movies(self):
        return self.driver_w.find_elements(By.CSS_SELECTOR, 'div>a>.ipc-title__text')