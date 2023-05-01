# Download Iris flower images and set limits. This is a hack to allow us to run tests with a lot of files
from google_images_download import google_images_download
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"iris_flower","limit":240,"print_urls":True, "output_directory": "D:/STUDY/CODE/ML/PredFlower/Data/flowers/iris", "chromedriver": "C:/Users/Nguyen Duc Thinh/Downloads/Compressed/chromedriver_win32/chromedriver.exe"}

paths = response.download(arguments)
