import time
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

# Prepare Selenium Driver Options
options = uc.ChromeOptions()
# options.add_argument('--headless')  # Run Selenium Driver in Headless Mode
# options.add_argument('--no-sandbox') # No Sandbox for Selenium Driver
# options.add_argument('--disable-dev-shm-usage') # Disable Dev Shm Usage for Selenium Driver

# Create Selenium Driver
driver: uc.Chrome = uc.Chrome(options=options)

# Initialize Action Chains
action_chains: ActionChains = ActionChains(driver)

# Set Window Size [ 800 x 800 ]
driver.set_window_position(0, 0)
driver.set_window_size(800, 800)


# Preference Flags
set_once = False



def the_gulper_bot(driver: uc.Chrome):
    """The Gulper Bot: A bot that gulps the blobs in the game gulper.io

    Args:
        driver (webdriver.Chrome): Selenium Chrome Driver

    Returns:
        None
    """

    global set_once

    # Load Gulper.io
    driver.get("https://gulper.io/")  # Load Gulper.io
    time.sleep(3)  # Wait for page to load

    # Find Web Body in Driver
    body = driver.find_element(By.TAG_NAME, "body")
    body_width = body.size['width']
    body_height = body.size['height']

    # Set Settings for Once
    if not set_once:
        driver.execute_script("document.getElementById('show-lbrd').click()")
        driver.execute_script("document.getElementById('show-nicks').click()")
        driver.execute_script("document.getElementById('show-map').click()")
        driver.execute_script("document.getElementById('graph-qual').click()")
        driver.execute_script("document.getElementById('framerate').click()")
        set_once = True
        time.sleep(0.25)
        time.sleep(10)

    # Hide Ads
    driver.execute_script("window.ADS_BLOCKED = true;")

    # Hide Stats
    driver.execute_script(
        "document.getElementById('stats').style.display = 'none'")

    # Wait for 0.25 seconds
    time.sleep(0.25)

    # Press Tab Key
    body.send_keys(Keys.TAB)
    time.sleep(0.5)

    # Type Nickname
    random_names = []
    random_names.append("GULPY_BOT_" + str(random.randint(100, 9999)))

    input_box = driver.switch_to.active_element
    input_box.send_keys(random_names[random.randint(0, len(random_names) - 1)])

    # Wait for 1 second
    time.sleep(1)

    # Find Element By Id [ start-btn ] and Click
    start_btn = driver.find_element(By.ID, "start-btn")
    start_btn.click()

    # Wait for 1 second
    time.sleep(5)

    # Step Counter
    step = 0

    driver.execute_script(
        "document.getElementById('stats').style.display = 'none'")

    while True:
        step += 1
        # Check If Elelment by Id [ game-stats ] is Visible
        game_stats = driver.find_element(By.ID, "game-stats")
        if game_stats.is_displayed():
            # Game Over
            break

        try:
            # Hover Mouse in Random Position
            position_x = random.randint(-1 *
                                        int(body_width/2)+10, int(body_width/2)-10)

            position_y = random.randint(-1 * int(body_height/2) +
                                        10, int(body_height/2)-10)

            action_chains.move_to_element(body).move_by_offset(
                position_x, position_y).perform()
            print("Moving to: " + str(position_x) + ", " + str(position_y))

            time.sleep(0.1)
            action_chains.move_to_element(body).move_by_offset(0, 0).perform()
        except Exception as e:
            # Print Error
            print(e, position_x, position_y)

            # Wait for 0.25 seconds
            time.sleep(0.1)

        if step % 10 == 0:
            # Try to Remove Stats
            driver.execute_script(
                "document.getElementById('stats').style.display = 'none'")

    # Restart Game
    the_gulper_bot(driver)


# Run the Gulper Bot
the_gulper_bot(driver)
