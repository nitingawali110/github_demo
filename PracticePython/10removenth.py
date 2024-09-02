mylist = ["geeks", "for", "geeks","geeks","geeks"]

word = "geeks"
n = 3

count = 0
for i in range(0, len(mylist)-1):
    if mylist[i] == word:
        count=count+1
        if count==n:
            del mylist[i]

print(mylist)


#################
# How to search Element in alist

mylist=[1,6,3,5,7]

ele=5

if(ele in mylist):
    print("element found")
else:
    print("element not found")




from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # For Chrome
driver = webdriver.Firefox()  # For Firefox
driver = webdriver.Edge()  # For Edge

#element = WebDriverWait(driver, 10).until(
    #EC.visibility_of_element_located((By.ID, "element_id"))
#)

##Explanation:** Waits up to 10 seconds for the element with the specified ID to become visible.

element=WebDriverWait(driver,10).until(EC.visibility_of_element_located(By.ID,
                                                                        "element_id"))
