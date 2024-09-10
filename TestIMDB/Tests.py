import unittest
from time import sleep
from appium import webdriver as mobile_webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver as web_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from TestIMDB.imdb_mobile_class import Imdb_mobileElements
from TestIMDB.imdb_web_class import Imdb_HomePage


class ImdbTests(unittest.TestCase):
    def setUp(self):
        # Set up Web Driver (Web)
        self.driver_web = web_driver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver_web.get("https://www.imdb.com/")
        self.driver_web.maximize_window()
        self.driver_web.implicitly_wait(10)
        self.homepage_web = Imdb_HomePage(self.driver_web)

        # Set up Mobile Driver (Appium)
        self.appium_server_url_local = 'http://localhost:4723/wd/hub'
        self.capabilities = dict(
            platformName="Android",
            deviceName="Pixel7a",
            udid="emulator-5554",
            appActivity="com.imdb.mobile.HomeActivity",
            appPackage="com.imdb.mobile",
            platformVersion="35",
            adbExecTimeout=60000
        )
        self.driver_mobile = mobile_webdriver.Remote(self.appium_server_url_local, self.capabilities)
        self.driver_mobile.implicitly_wait(10)
        self.mobile_elements = Imdb_mobileElements(self.driver_mobile)

    def tearDown(self):
        if self.driver_web:
            self.driver_web.quit()
        if self.driver_mobile:
            self.driver_mobile.quit()

    def test1_search_movie(self):
        movie_name = "The Matrix"

        # Web search
        self.homepage_web.search_bar().send_keys(movie_name)
        self.homepage_web.search_bar_button().click()
        WebDriverWait(self.driver_web, 10).until(
            EC.element_to_be_clickable(self.homepage_web.search_result()[0])
        ).click()
        movie_name_web = self.homepage_web.movie_result_page().text

        # Mobile search
        self.mobile_elements.continue_button().click()
        self.mobile_elements.not_now_button().click()
        self.mobile_elements.search_button().click()
        self.mobile_elements.search_field().click()
        self.mobile_elements.search_field2().send_keys(movie_name)
        result1 = self.mobile_elements.result1()
        self.assertEqual(result1.text, movie_name, "Movie not found on mobile!")
        result1.click()
        movie_name_mobile = self.mobile_elements.title_result1().text

        print(f'Mobile: {movie_name_mobile}, Web: {movie_name_web}')
        self.assertEqual(movie_name_mobile, movie_name_web)

    def test2_Compare_Fan_Favorites(self):
        # Web Fan Favorites
        movie_web = self.homepage_web.fan_favorites().replace("View title page for ", "").strip()

        # Mobile Fan Favorites
        self.mobile_elements.continue_button().click()
        self.mobile_elements.not_now_button().click()
        movie_mobile = self.mobile_elements.fan_favorites().text

        print(f'Web: {movie_web}, Mobile: {movie_mobile}')
        self.assertEqual(movie_web, movie_mobile, "Fan favorites do not match!")

    def test3_Compare_Top_TV_Shows(self):
        # Web search for top TV shows
        self.homepage_web.filter_selector_search().click()
        self.homepage_web.advanced_search_button().click()
        self.homepage_web.search_filters()[1].click()
        self.homepage_web.tv_series_option().click()
        self.homepage_web.see_results().click()

        # Collect top 4 TV shows (web)
        tv_shows_web = [
            show.text.split('. ', 1)[-1].strip()
            for show in self.homepage_web.popular_tv_shows_result()[1:5]
        ]

        # Mobile search for top TV shows
        self.mobile_elements.continue_button().click()
        self.mobile_elements.not_now_button().click()
        self.mobile_elements.search_button().click()
        self.mobile_elements.search_field().click()
        self.mobile_elements.advanced_search_select().click()
        self.mobile_elements.tv_series_select().click()
        self.mobile_elements.see_results_button().click()

        # Collect top 4 TV shows (mobile)
        tv_shows_mobile = [
            show.text.strip() for show in self.mobile_elements.tv_series_title_results()[:4]
        ]

        print(f'Web: {tv_shows_web}, Mobile: {tv_shows_mobile}')
        for tv_web, tv_mobile in zip(tv_shows_web, tv_shows_mobile):
            self.assertEqual(tv_web, tv_mobile, "TV shows do not match!")

    def test4_Compare_Top_3_Movies(self):
        # Web top 3 movies
        self.homepage_web.menu_button().click()
        self.homepage_web.top250_movies().click()
        top_movies_web = [
            movie.text for movie in self.homepage_web.top3_movies()[:3]
        ]

        # Mobile top 3 movies
        self.mobile_elements.continue_button().click()
        self.mobile_elements.not_now_button().click()
        self.mobile_elements.search_button().click()
        self.mobile_elements.top250_movies().click()
        top_movies_mobile = [
            movie.text for movie in self.mobile_elements.top3_movies()[:3]
        ]

        print(f'Web: {top_movies_web}, Mobile: {top_movies_mobile}')
        self.assertEqual(top_movies_web, top_movies_mobile)

    def test5_Create_Verify_and_Delete_Watchlist(self):
        # Mobile: Create watchlist with two actors
        self.mobile_elements.continue_button().click()
        self.mobile_elements.imdb_account_sign_in().click()
        self.mobile_elements.imdb_account_username().send_keys("capara1275@gmail.com")
        self.mobile_elements.imdb_account_password().send_keys("123456Gol")
        self.mobile_elements.account_sign_in_button().click()
        self.mobile_elements.profile_icon().click()
        self.mobile_elements.tip_exit().click()
        self.mobile_elements.watchlist_button().click()
        self.mobile_elements.add_list_watchlist().click()
        self.mobile_elements.list_name().send_keys("Israeli_Actors")
        self.mobile_elements.list_type_name().click()
        self.mobile_elements.list_save().click()

        # Add actors to the list
        actors = ["Gal Gadot", "Mark Ivanir"]
        for actor in actors:
            self.mobile_elements.add_list_watchlist().click()
            self.mobile_elements.insert_text_name().send_keys(actor)
            self.mobile_elements.search_result_by_name(actor).click()

        # Verify added actors
        added_actors = [
            actor.text for actor in self.mobile_elements.added_names_to_list()[:2]
        ]
        self.assertEqual(added_actors, ["1. Gal Gadot", "2. Mark Ivanir"])

        # Web: Verify and delete watchlist
        self.homepage_web.watchlist().click()
        self.homepage_web.sign_in_elements()[0].click()
        self.homepage_web.sign_in_page()[0].send_keys("capara1275@gmail.com")
        self.homepage_web.sign_in_page()[1].send_keys("123456Gol")
        self.homepage_web.sign_in_button().click()
        WebDriverWait(self.driver_web, 10).until(
            EC.presence_of_element_located(self.homepage_web.your_lists_button())
        ).click()

        self.homepage_web.three_dots_icon().click()
        self.homepage_web.delete_option().click()
        self.homepage_web.confirm_delete().click()

        # Verify list deletion
        lists_are_null = self.homepage_web.lists_are_null().text
        self.assertEqual("You have not created any lists yet. Create a new list", lists_are_null)

    if __name__ == '__main__':
        unittest.main()




