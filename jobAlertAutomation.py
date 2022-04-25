import smtplib, ssl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'C:\\Users\\orochest\Desktop\\chromedriver_win32new\\chromedriver.exe',options=options)

indeedURLS = ["https://www.indeed.com/jobs?q=Software%20Developer&l=Traverse%20City%2C%20MI&explvl=entry_level&vjk=8cc6f0bb1c6e0863",
              "https://www.indeed.com/jobs?q=Software%20Developer&l=Traverse%20City%2C%20MI&radius=50&fromage=1&vjk=e29ee73cc45e232a"]

jobTitles= []
companyNames = []
locations = []
driver.get("https://www.linkedin.com/jobs/search/?keywords=Software%20Engineer&location=Traverse%20City%2C%20Michigan%2C%20United%20States&locationId=&geoId=105302743&f_TPR=r86400&distance=25&f_E=2&position=1&pageNum=0")

jobs = driver.find_elements(By.XPATH, "//div[@Class='base-search-card__info']")

optionsLen = len(jobs)
print(optionsLen)
for job in jobs:
    title = job.find_element(By.TAG_NAME, "h3")
    title = title.get_attribute("innerHTML")

    comp = job.find_element(By.CLASS_NAME, "hidden-nested-link")
    comp = comp.get_attribute("innerHTML")

    location = job.find_element(By.CLASS_NAME, "job-search-card__location")
    location = location.get_attribute("innerHTML")

    jobTitles.append(str(title))
    companyNames.append(str(comp))
    locations.append(str(location))


for i in range(0,len(jobTitles)):
    jobTitles[i].rstrip()
        
mailMessageString = ''

for i in range(0,len(jobTitles)):
    tempStr = ''
    tempStr = tempStr + jobTitles[i] + '\n'
    tempStr = tempStr + companyNames[i] + '\n'
    tempStr = tempStr + locations[i] + '\n'
    tempStr = tempStr + '\n' + '\n'
    mailMessageString = mailMessageString + tempStr

print(mailMessageString)
    
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ogrochester@gmail.com', 'xxxxxxx')
server.sendmail('orochest@nmu.edu', 'orochest@nmu.edu', mailMessageString)

driver.close()