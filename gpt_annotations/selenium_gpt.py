from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import ssl
import time
import sys
import os
import subprocess
import pandas as pd

notebook_filename = "Untitled.ipynb"
notebook_path = os.path.abspath(notebook_filename)

try:
    ssl._create_default_https_context = ssl._create_unverified_context
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    driver.get('https://chat.openai.com/auth/login')
    time.sleep(5)

    login_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[4]/button[1]/div')
    login_btn.click()
    time.sleep(5)
    google_btn = driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/div[4]/form[2]/button/span[2]')
    google_btn.click()
    time.sleep(5)
    email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    email_input.send_keys('neurogenomics.lab.ic@gmail.com')
    email_input.send_keys(Keys.RETURN)
    time.sleep(5)
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    password_input.send_keys('microglia')
    password_input.send_keys(Keys.RETURN)
    time.sleep(10)

    next1_btn = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]/div[2]/button') 
    next1_btn.click()
    time.sleep(5)
    next2_btn = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]/div[2]/button[2]')
    next2_btn.click()
    time.sleep(5)
    done_btn = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]/div[2]/button[2]')
    done_btn.click()
    time.sleep(5)

    gpt4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/main/div[2]/div/div/div[1]/div/div/ul/li[2]/button')
    gpt4.click()
    time.sleep(5)

    prompts_df = pd.read_csv('~/Documents/gpt_prompts_2.csv')
    prompts = prompts_df['prompt'].tolist()

    previous_outputs_file = '/Users/kittymurphy/Documents/gpt_hpo_annotations_scale.csv'
    previous_outputs_exist = os.path.isfile(previous_outputs_file)

    outputs_df = pd.DataFrame()

    prompt_counter = 0

    if previous_outputs_exist:
        outputs_df = pd.read_csv(previous_outputs_file)
        prompt_counter = len(outputs_df) // 2 + 1

    num_iterations = 25

    while True:
        for _ in range(num_iterations):
            for prompt in prompts[prompt_counter:]:
                input_box_pattern = '/html/body/div[1]/div[1]/div/div/main/div[{}]/form/div/div/textarea'
                input_box = driver.find_element(By.XPATH, input_box_pattern.format('*'))
                submit_button_pattern = '/html/body/div[1]/div[1]/div/div/main/div[{}]/form/div/div/button'
                submit_button = driver.find_element(By.XPATH, submit_button_pattern.format('*'))

                input_box.clear
                input_box.send_keys(prompt)
                submit_button.click()

                time.sleep(390)

                response_box_pattern = '/html/body/div[1]/div[1]/div/div/main/div[2]/div/div/div/div[{}]/div/div[2]/div[1]/div/div/pre/div/div[2]/code'
                response_boxes = driver.find_elements(By.XPATH, response_box_pattern.format('*'))

                for response_box in response_boxes:
                    output_code = response_box.text

                    try:
                        exec(output_code)
                        output = "Code executed successfully."
                    except Exception as e:
                        output = f"Code execution error: {str(e)}"

                    filename = f'/Users/kittymurphy/Documents/gpt_hpo_annotations_mismatch_{prompt_counter}.csv'

                    if isinstance(df, pd.DataFrame):
                        if set(outputs_df.columns) == set(df.columns):
                            df_sorted = df[outputs_df.columns]
                            outputs_df = pd.concat([outputs_df, df_sorted], ignore_index=True)
                            unique_df = outputs_df.drop_duplicates()
                            unique_df.to_csv('/Users/kittymurphy/Documents/gpt_hpo_annotations_scale.csv', index=False)
                        else:
                            df.to_csv(filename, index=False)
except Exception as e:
    print(f"An error occurred: {e}")
    env = dict(os.environ)
    env['PYDEVD_DISABLE_FILE_VALIDATION'] = '1'
    subprocess.run(["jupyter", "nbconvert", "--execute", "--inplace", notebook_path], env=env)
    driver.quit()
    time.sleep(5)


