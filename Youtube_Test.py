from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
   
class youtube:
    print("!*!*!  İşlem listesi :")
    print("1 - Video adeti sorgulama için Video_Adet yazınız.")
    print("2 - Bir videonun beyeni adedi için Begeni yazınız.")
    print("3 - Bir videonun Izlenme adedi için Izlenme yazınız.")
    isl=input("İşleminiz Nedir?")
    if isl == "Video_Adet" :
       #Open the chrome
       driver = webdriver.Chrome(ChromeDriverManager().install())
       #Full window
       driver.maximize_window()
       #Youtube link print
       driver.get("https://www.youtube.com/")
       #5 sec stop (for upload )
       sleep(5)
       #Warning!
       print("!*!*! : 5 saniye bekleyiniz")
       #video search
       onay = input("Video adet bilgisi istiyorsanız Evet yazınız. !*!*! :")
       
       if onay=="Evet":
         name=input("!*!*! : Adet aratmak istediğiniz video ismini girin /=")
         input_search = driver.find_element(By.NAME,"search_query")
         input_search.send_keys(name)
         search_button = driver.find_element(By.ID,"search-icon-legacy")
         search_button.click()
         sleep(5)
       #Number of titles
       Video_amount=driver.find_elements(By.ID,"dismissible")
       #Be member youtube
        #member_record = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
       #Member button click
        #member_record.click()
       #Warning!
       print(f"!*!*! : Bu içerik için {len(Video_amount)} adet video bulunmaktadır.")
       input ("İşlem tamamlanmıştır.Kapatmak için q yazın.")
    elif isl == "Begeni":
         link=input("Link bilgisi giriniz !*!*!:")
         id_1 = input("videonun bulunduğu alana sol tık yapıp incele kısmından buton alanının ID ismini kopyala yapıştır yapınız. !*!*! :")
         driver = webdriver.Chrome(ChromeDriverManager().install())
          #Full window
         driver.maximize_window()
       #Youtube link print
         driver.get(link)
       #5 sec stop (for upload )
         sleep(5)
         X=0
         int(X)
         print("60 saniyede bir kontrol edilecektir. Dakika cinsinden süre belirleyiniz !*!*! : ")
         sec = input()
         
         while int(X) < int(sec) :
           bgn = driver.find_element(By.ID,id_1)
           bgn_text=bgn.text
           print(f"Beğeni adedi: {bgn_text}")
           sleep(30)
           X=X+1 
         input ("İşlem tamamlanmıştır.Kapatmak için q yazın.")
    elif isl == "Izlenme": 
         link=input("Link bilgisi giriniz !*!*!:")
         Xpath_1 = input("videonun bulunduğu alana sol tık yapıp incele kısmından izlenme alanının ID ismini kopyala yapıştır yapınız. !*!*! :")
         driver = webdriver.Chrome(ChromeDriverManager().install())
          #Full window
         driver.maximize_window()
         #Youtube link print
         driver.get(link)
         #5 sec stop (for upload )
         X=0
         int(X)
         print("60 saniyede bir kontrol edilecektir. Dakika cinsinden süre belirleyiniz !*!*! : ")
         sec = input()
         
         while int(X) < int(sec) :
           izl = driver.find_element(By.ID,Xpath_1)
           izl_text=izl.text
           print(f"izlenme adedi: {izl_text}")
           sleep(30)
           X=X+1 
           
         input ("İşlem tamamlanmıştır.Kapatmak için q yazın.")  
    else:
      print("Yanlış giriş")
      
      
   