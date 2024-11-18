import pytest

from conftest import setup_browser
from pages.home_page import HomePage
from pages.search_result_page import SearchPage

URL = 'https://store.steampowered.com/'


@pytest.mark.parametrize(
    'creds',
    [
        pytest.param(('The Witcher', 10), id='The Witcher, 10'),
        pytest.param(('Fallout', 20), id='Fallout, 20')
    ]
)
def test_list_game_with_price_desc1(setup_browser, creds):
    name_games, number_of_games = creds
    print("Start Test")
    driver = setup_browser
    driver.get(URL)
    hp = HomePage(driver)
    hp.search(name_games)
    srp = SearchPage(driver)
    srp.sort_price_desc(number_of_games)
