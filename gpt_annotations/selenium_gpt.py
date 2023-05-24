## Code to automate ChatGPT using selenium ##

# start the chromedriver
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
driver.get('https://chat.openai.com/auth/login')

# log in to chat GPT 
login_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[4]/button[1]/div')
login_btn.click()
google_btn = driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/div[4]/form[2]/button/span[2]')
google_btn.click()
# option 1 enter email and password
email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_input.send_keys('neurogenomics.lab.ic@gmail.com')
email_input.send_keys(Keys.RETURN)
password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys('microglia')
password_input.send_keys(Keys.RETURN)

#option 2, select existing account 
email_input = driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[2]')
email_input.click()

# chatGPT "this is a free research preview" 
next1_btn = driver.find_element(By.XPATH, '//*[@id="radix-:r8:"]/div/div/div[4]/button')
next1_btn.click()
next2_btn = driver.find_element(By.XPATH, '//*[@id="radix-:r8:"]/div/div/div[4]/button[2]')
next2_btn.click()
done_btn = driver.find_element(By.XPATH, '//*[@id="radix-:r8:"]/div/div/div[4]/button[2]')
done_btn.click()

# model selection
gpt4 = driver.find_element(By.XPATH, '//*[@id="radix-:ri:"]/div') 
gpt4.click()

# send prompts 
import pandas as pd 
prompts_df = pd.read_csv('~/Documents/gpt_prompts.csv') 
prompts = prompts_df['prompt'].tolist() 


outputs_df = pd.DataFrame()  # Create an empty DataFrame for the combined output

for prompt in prompts:
    # Locate the input box and submit button
    input_box = driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div/main/div[3]/form/div/div[2]/textarea')  
    submit_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/main/div[3]/form/div/div[2]/button')
    # Send the prompt to the input box and click the submit button
    input_box.clear()
    input_box.send_keys(prompt)
    submit_button.click()
    # Wait for the response
    time.sleep(120)  # You can adjust this depending on the response time

    response_box_pattern = '//*[@id="__next"]/div[2]/div[2]/div/main/div[2]/div/div/div/div[{}]/div/div[2]/div[1]/div/div/pre/div/div[2]/code'
    response_boxes = driver.find_elements(By.XPATH, response_box_pattern.format('*'))

    for response_box in response_boxes:
        output_code = response_box.text
        
        try:
            exec(output_code)
            output = "Code executed successfully."
        except Exception as e:
            output = f"Code execution error: {str(e)}"
        
        if isinstance(df, pd.DataFrame):
            outputs_df = pd.concat([outputs_df, df], ignore_index=True)  # Concatenate the current DataFrame
        
