import random
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests
import time
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

def handle_alert(driver):
    """
    Handles any unexpected alert pop-ups in the browser.
    """
    try:
        alert = Alert(driver)
        print(f"Alert detected: {alert.text}")  # Log the alert text for debugging
        alert.dismiss()  # Or use alert.accept() if you want to proceed
    except NoAlertPresentException:
        print("No alert is present.")
    except Exception as e:
        print(f"Error while handling alert: {e}")

def get_names():
    name_list = [
    "Ali Khan", "Ahmed Patel", "Hassan Sharma", "Usman Singh", "Bilal Kapoor", "Imran Reddy", "Faisal Yadav", "Kamran Verma",
    "Nadeem Chauhan", "Rizwan Jain", "Abdullah Nair", "Arif Iyer", "Tariq Pillai", "Irfan Kumar", "Aamir Verma", "Kashif Sharma",
    "Majid Kapoor", "Nasir Yadav", "Shahid Reddy", "Sohail Chauhan", "Qasim Iyer", "Tahir Pillai", "Asad Nair", "Rafiq Kumar",
    "Yasin Verma", "Riaz Kapoor", "Mubashir Chauhan", "Murtaza Jain", "Farhan Yadav", "Muzammil Nair", "Saad Pillai",
    "Tanveer Iyer", "Zubair Chauhan", "Waqar Yadav", "Salman Sharma", "Rashid Verma", "Azhar Kapoor", "Javed Nair",
    "Junaid Pillai", "Moin Iyer", "Nasir Chauhan", "Yousaf Yadav", "Haroon Sharma", "Adnan Kapoor", "Mehmood Verma",
    "Akhtar Jain", "Sultan Yadav", "Hamza Nair", "Zahid Pillai", "Shabbir Iyer", "Zia Chauhan", "Fahad Yadav", "Jamil Verma",
    "Sajid Iyer", "Adeel Chauhan", "Raheel Yadav", "Noman Iyer", "Shakeel Pillai", "Rauf Chauhan", "Iqbal Yadav",
    "Jawad Verma", "Arshad Pillai", "Amir Iyer", "Waheed Yadav", "Rameez Kapoor", "Najeeb Verma", "Sabir Yadav",
    "Zulfiqar Chauhan", "Ijaz Nair", "Saleem Iyer", "Atif Pillai", "Aftab Yadav", "Zafar Verma", "Fahim Chauhan",
    "Hafeez Yadav", "Khurram Kapoor", "Luqman Nair", "Nawaz Yadav", "Adil Verma", "Aurangzeb Chauhan", "Tanweer Yadav",
    "Ahsan Pillai", "Qaiser Nair", "Ghulam Verma", "Shoaib Yadav", "Pervez Kapoor", "Ilyas Iyer", "Sharif Yadav",
    "Younis Verma", "Sarwar Chauhan", "Azam Pillai", "Noman Yadav", "Shafiq Iyer", "Mudassir Yadav", "Rahim Nair",
    "Babar Verma", "Waseem Yadav", "Abid Chauhan", "Tauseef Nair", "Asif Yadav", "Nisar Pillai", "Yaqoob Chauhan",
    "Khalid Yadav", "Zaman Kapoor", "Aisha Pillai", "Sana Yadav", "Fatima Chauhan", "Hira Yadav", "Nadia Kapoor",
    "Samina Chauhan", "Farida Yadav", "Naima Iyer", "Zainab Yadav", "Mehak Kapoor", "Saima Yadav", "Tahira Nair",
    "Noreen Yadav", "Bushra Kapoor", "Ambreen Chauhan", "Tasneem Yadav", "Sadia Nair", "Fauzia Chauhan", "Gulnaz Pillai",
    "Shabnam Yadav", "Nighat Kapoor", "Nusrat Iyer", "Rukhsar Yadav", "Shazia Nair", "Shahnaz Yadav", "Shamim Kapoor",
    "Nida Yadav", "Nazia Pillai", "Hina Yadav", "Asma Kapoor", "Rabia Nair", "Zeba Yadav", "Naila Pillai", "Nadia Yadav",
    "Iram Kapoor", "Kausar Chauhan", "Najma Yadav", "Sabiha Nair", "Shaista Yadav", "Shehnaz Kapoor", "Sobia Chauhan",
    "Tabassum Yadav", "Uzma Pillai", "Yasmin Yadav", "Fareeha Kapoor", "Sarwat Yadav", "Shama Chauhan", "Shazia Yadav",
    "Fozia Nair", "Lubna Yadav", "Samar Chauhan", "Aneela Yadav", "Farkhanda Pillai", "Huma Yadav", "Kanwal Verma",
    "Parveen Yadav", "Razia Chauhan", "Roohi Yadav", "Tania Pillai", "Umaima Yadav", "Yasmeen Kapoor", "Nayab Yadav",
    "Rukhsana Pillai", "Zohra Yadav", "Fahmida Nair", "Gulshan Kapoor", "Iffat Yadav", "Javeria Chauhan", "Kiran Yadav",
    "Madiha Pillai", "Naheed Yadav", "Quratulain Nair", "Roshan Yadav", "Shireen Kapoor", "Zubaida Yadav", "Atiya Chauhan",
    "Fariha Yadav", "Ishrat Pillai", "Laila Chauhan", "Marina Yadav", "Rehana Pillai", "Sajida Yadav", "Shakeela Nair",
    "Tanzila Yadav", "Yumna Chauhan", "Bisma Yadav", "Hooriya Kapoor", "Maimoona Yadav", "Nabeela Pillai", "Rafia Yadav",
    "Sabiya Kapoor", "Tahira Yadav", "Ummara Nair", "Zarish Yadav", "Farzana Chauhan", "Jannat Yadav", "Kinza Kapoor",
    "Naima Pillai", "Rukhsar Yadav", "Sarina Chauhan", "Tayyaba Yadav", "Uzma Nair", "Wajiha Yadav", "Yasira Pillai"
]


    return random.choice(name_list)

def solve_captcha():

    API_KEY = "0879506b2d7382c9fd5748ec94ca6bde"

    def solve(image_path):
        # Step 1: Upload the image to 2Captcha
        url = "http://2captcha.com/in.php"
        with open(image_path, "rb") as image_file:
            files = {'file': image_file}
            data = {'key': API_KEY, 'method': 'post'}
            response = requests.post(url, files=files, data=data)
        
        if response.status_code != 200 or "OK" not in response.text:
            raise Exception("Failed to upload captcha image: " + response.text)
        
        # Extract the captcha ID
        captcha_id = response.text.split('|')[1]
        print(f"Captcha ID: {captcha_id}")

        # Step 2: Poll for the solution
        result_url = f"http://2captcha.com/res.php?key={API_KEY}&action=get&id={captcha_id}"
        while True:
            result_response = requests.get(result_url)
            if "CAPCHA_NOT_READY" in result_response.text:
                time.sleep(5)  # Wait for 2Captcha to solve
                continue
            if "OK" in result_response.text:
                return result_response.text.split('|')[1]
            else:
                raise Exception("Failed to get captcha solution: " + result_response.text)

    # Example Usage
    image_path = "captcha.png"  # Path to your captcha image
    try:
        captcha_text = solve(image_path)
        print(f"Captcha Solved: {captcha_text}")
        return captcha_text
    except Exception as e:
        print(e)
        solve(image_path=image_path)
number_of_tabs = 6
wait_in_seconds = 0.001
def join_meeting():
    try:
        for driver in chrome_drivers:
            for i in range(number_of_tabs):
                driver.get(input_url)
                handle_alert(driver)
                base_uri = ""
                is_base_uri = False
                while is_base_uri == False:
                    try:
                        base_uri = driver.find_element(By.ID,'teamsLauncher').get_property("baseURI")
                        if base_uri:
                            is_base_uri = True
                    except:
                        handle_alert(driver)
                        if driver.current_url == 'https://teams.live.com/_#/modern-calling/':
                            is_base_uri = True
                        continue
                    
                is_join_Btn = False
                joinBtn = ''   

                if base_uri and is_base_uri:
                    driver.execute_script("window.open();")

                    new_tab = driver.window_handles[-1]

                    first_tab = driver.window_handles[-2]
                    driver.switch_to.window(first_tab)
                    driver.close()

                    driver.switch_to.window(new_tab)
                    driver.get(base_uri)
                else:
                    is_join_Btn = True
                


                while is_join_Btn ==False:
                    try:
                        joinBtn = WebDriverWait(driver, wait_in_seconds).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Join meeting from this browser"]'))
                        )
                        # joinBtn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Join meeting from this browser"]')
                        if joinBtn:
                            is_join_Btn = True
                    except:
                        handle_alert(driver)
                        continue

                if joinBtn and is_join_Btn:
                    joinBtn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Join meeting from this browser"]')
                    joinBtn.click()

        
                element_visible = ''

                is_loaded = False
                is_V2_page = False
                while is_loaded ==False and "https://teams.microsoft.com/v2/?meetingjoin=true" not in driver.current_url:# !='https://teams.microsoft.com/v2/?meetingjoin=true':
                    try:
                        # element_visible = WebDriverWait(driver, wait_in_seconds).until(
                        # EC.visibility_of_element_located((By.TAG_NAME, "iframe"))
                        # )
                        element_visible = driver.find_element(By.TAG_NAME, "iframe")
                        if element_visible:
                            print(f'Element has been found for {i}')
                            is_loaded = True
                    except:
                        try:
                            # element_visible =  WebDriverWait(driver, wait_in_seconds).until(
                            # EC.visibility_of_element_located((By.CSS_SELECTOR,'div[aria-label="Choose your video and audio options for Meeting"]'))
                            # )
                            element_visible = driver.find_element(By.CSS_SELECTOR,'div[aria-label="Choose your video and audio options for Meeting"]')
                            if element_visible:
                                print(f'Element has been found for {i}')
                                is_loaded = True
                                is_V2_page = True
                        except:
                            handle_alert(driver)
                            continue
                if is_V2_page == False and "https://teams.microsoft.com/v2/?meetingjoin=true" not in driver.current_url:# !='https://teams.microsoft.com/v2/?meetingjoin=true':
                    driver.switch_to.frame(element_visible)
                elif is_V2_page:
                    driver.refresh()

                input_name = ''
                is_page_fully_loaded = False

                while is_page_fully_loaded == False:
                    try:
                        input_name = WebDriverWait(driver, wait_in_seconds).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR,'input[placeholder="Type your name"]'))
                            )
                        # input_name = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Type your name"]')
                        if input_name:
                            is_page_fully_loaded = True
                    except:
                        handle_alert(driver)
                        continue

                if is_page_fully_loaded:
                    name = get_names()
                    input_name.clear()
                    try:
                        input_name.send_keys(name)
                    except:
                        handle_alert(driver)
                        input_name.send_keys(name)

                    try:
                        disable_audio_btn = driver.find_element(By.CSS_SELECTOR,'div[aria-label="Don\'t use audio"]')
                        disable_audio_btn.click()
                    except TimeoutException:
                            print("Audio disable button not found or not clickable.")
                    except Exception as e:
                        # print(f"An error occurred while disabling audio: {e}")
                        pass

                    try:
                        disable_mic = driver.find_element(By.CSS_SELECTOR,'#microphone-button')
                        disable_mic.click()
                    except TimeoutException:
                        print("Mic disable button not found or not clickable.")

                    except Exception as e:
                        # print(f"An error occurred while disabling audio: {e}")
                        pass
                    try:
                        disable_cam = WebDriverWait(driver, wait_in_seconds).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#video-button'))
        )
                        disable_cam.click()
                    except TimeoutException:
                        print("Camera disable button not found or not clickable.")
                    except Exception as e:
                        # print(f"An error occurred while disabling the camera: {e}")
                        pass
                    
                        
                    finally:
                        # is_join_Btn = False
                        # join_btn = None
                        # while is_join_Btn == False:
                        #     try:
                        #         join_btn = WebDriverWait(driver, wait_in_seconds).until(EC.visibility_of_element_located(By.CSS_SELECTOR, 'button[aria-label="Join now"]'))
                        #         if join_btn:
                        #             is_join_Btn = True
                        #     except:
                        #         continue
                        try:
                            #time.sleep(1)
                            join_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[aria-label="Join now"]')))
                            join_btn.click()
                            image_url = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//img[@data-tid="HIP-Captcha-Image"]')))
                            image_url.screenshot('captcha.png')

                            captcha_text= solve_captcha()
                            cap_in = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[@placeholder="Type the characters you see"]')))
                            cap_in.send_keys(captcha_text)
                            submit = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//button[@data-tid="HIP-Captcha-Submit"]')))
                            submit.click()
                            
                        except Exception as e:
                            print(f'Exception while clicking join now button {e}')
                            driver.refresh()
                            handle_alert(driver)
                            try:
                                join_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[aria-label="Join now"]')))
                                join_btn.click()
                                image_url = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//img[@data-tid="HIP-Captcha-Image"]')))
                                image_url.screenshot('captcha.png')

                                captcha_text= solve_captcha()
                                cap_in = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[@placeholder="Type the characters you see"]')))
                                cap_in.send_keys(captcha_text)
                                submit = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'//button[@data-tid="HIP-Captcha-Submit"]')))
                                submit.click()
                            
                            except:
                                pass
                        try:
                            handle_alert(driver)
                        except:
                            pass
                        if i < number_of_tabs-1:
                            try:
                                driver.execute_script("window.open();")
                            except:
                                handle_alert(driver)
                                driver.execute_script("window.open();")

                            new_tab = driver.window_handles[-1]
                            driver.switch_to.window(new_tab)

        is_meeting_ended = False

        while is_meeting_ended == False:
            try:
                btn = chrome_drivers[-1].find_element(By.CSS_SELECTOR,'button[data-tid="anon-meeting-end-screen-rejoin-button"]')
                if btn:
                    is_meeting_ended = True
            except:
                handle_alert(driver)
                continue
            
        print("Meeting has been ended or you have been removed.")
        chrome_drivers[0].quit()

    except:
        pass

#start chrome webdriver
input_url = input("Enter URL of the meeting:")
number_of_instances = int(input("How many Users would you like to add:"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--log-level=3")
#chrome_options.add_argument('--headless')

chrome_drivers = []
for i in range(0,number_of_instances):
    driver = webdriver.Chrome(options=chrome_options)
    chrome_drivers.append(driver)


# for driver in chrome_drivers:
#     t = threading.Thread(target=join_meeting, args=[driver])
#     t.start()
join_meeting()