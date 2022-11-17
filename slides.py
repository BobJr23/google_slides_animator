from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ScrollOrigin
import time, random


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
print(
    """
0: appear
1: disappear
2: fade in
3: fade out
4: fly in left
5: fly in right
6: fly in bottom
7: fly in top
8: fly out left
9: fly out right
10: fly out bottom
11: fly out to top
12: zoom in
13: zoom out
14: spin
"""
)

# set link to google slide link. google slide must have the setting "anyone on the internet can edit" in the share section
link = r"Google Slides Link"
PATH = r"{PATH to Chromedriver"
driver = webdriver.Chrome(PATH, options=chrome_options)
# GO

driver.get(link)


def make_words(words, animation, offx, offy):

    for x in words:
        if x == "*":  # new line
            offy += 25
            offx = 50
            continue

        element = driver.find_element(By.ID, "textboxButton")
        element.click()
        ActionChains(driver).move_to_element_with_offset(element, offx, offy).perform()
        ActionChains(driver).click(None).perform()
        actions = ActionChains(driver)
        actions.send_keys(x)
        actions.perform()
        time.sleep(0.3)
        element = driver.find_element(By.CLASS_NAME, "punch-animation-sidebar-add-text")
        element.click()
        time.sleep(0.6)

        fade, animationtype = driver.find_elements(
            By.CLASS_NAME, "punch-sidebar-tile-type-select"
        )[-2:]
        scroll = driver.find_element(By.CLASS_NAME, "punch-animation-sidebar-scroll")
        scroll_origin = ScrollOrigin.from_element(scroll)
        ActionChains(driver).scroll_from_origin(scroll_origin, 0, 1000).perform()
        time.sleep(0.3)

        try:
            fade.click()
        except:
            time.sleep(1)
            fade.click()
        time.sleep(0.2)
        z = driver.find_elements(By.CLASS_NAME, "goog-menuitem")[
            -1 * (15 - animation)  # CHANGE
        ]
        z.click()
        time.sleep(0.2)
        animationtype.click()
        time.sleep(0.2)
        timing = driver.find_elements(By.CLASS_NAME, "goog-menuitem")[
            -2
        ]  # -2 represents trigger after previous animation. Expirement with the values
        timing.click()
        draggable = driver.find_elements(
            By.CLASS_NAME, "docs-material-slider-thumb-grabber"
        )[-1]

        ActionChains(driver).drag_and_drop_by_offset(
            draggable, 40, 0
        ).perform()  # the 40 represents how fast the animation goes. you can play around with the number
        offx += 13 + len(x) * 14
        if offx > 1100:  # new line. Adjust these values based on monitor size
            offy += 25
            offx = 50
    return offx, offy


driver.implicitly_wait(1)
element = driver.find_element(By.ID, "slideTransitionButton")
element.click()
offx = 50
offy = 50
"""
0: appear
1: disappear
2: fade in
3: fade out
4: fly in left
5: fly in right
6: fly in bottom
7: fly in top
8: fly out left
9: fly out right
10: fly out bottom
11: fly out to top
12: zoom in
13: zoom out
14: spin
"""
while True:

    # word, animation = input(
    #     "What is your word and animation (words//number  format)   ' * ' indicates new line"
    # ).split("//")

    word, animation = (
        r"Example text here",  # you can add input() if you want. Make sure all the text is in ONE line only, the bot will automatically make new line. * also creates new line
        # (check comments above)
        12,  # int(input) . This is the animation number in list above
    )
    words = word.split()
    offx, offy = make_words(
        words,
        animation,
        offx,
        offy,
    )
    input()
"""

"""
