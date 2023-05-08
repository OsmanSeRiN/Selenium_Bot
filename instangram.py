from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
   
class test_instangram:
    print("!*!*!  İşlem listesi :")
    print("1 - Bir videonun beyeni adedi için Begeni yazınız.")
    print("2 - Bir videonun Görüntülenme adedi için Gor yazınız.")
    isl=input("İşleminiz Nedir?")
   
    if isl == "Begeni":

         driver = webdriver.Chrome(ChromeDriverManager().install())
         #Full window
         driver.maximize_window()
         #Youtube link print
         driver.get("https://www.instagram.com/")
         #open the prifile
         sleep(5)
         print("!!! Warning !!! Hiç bir veriniz kaydedilmemektedir!")
         name_text=input("Hesap adı ve ya e posta / :")
         pasworld_text = input("Şifreniz (en az 8 hane )/ :")
         name = driver.find_element(By.NAME,"username")
         name.send_keys(name_text)
         pasworld = driver.find_element(By.NAME,"password")
         pasworld.send_keys(pasworld_text)
         sleep(5)
         button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
         button.click()
         xpeth=input("Sayfadan incele diyip sol üstteki mause okuna tıkladıktan sonra beğeni sayısına tıklayın.Kenarda çıkan mavi alandaki koda sağ tık yapıp full Xpeth copy e tıklayın ve buraya yapıştırın: / :  ")
         
         sayı=input("Kontrol etme sürsini dakika cinsinden yazınız. / :  ")
         for i in range(1,int(sayı)):
             begeni= driver.find_element(By.XPATH,xpeth)
             begeni_text = begeni.text
             
             print(f"Beğeni sayısı / : ")
             sleep(30)
             
            
        
         input ("İşlem tamamlanmıştır.Kapatmak için q yazın.")
    elif isl == "Gor": 
         
         driver = webdriver.Chrome(ChromeDriverManager().install())
         #Full window
         driver.maximize_window()
         #Youtube link print
         driver.get("https://www.instagram.com/")
         #open the prifile
         sleep(5)
         print("!!! Warning !!! Hiç bir veriniz kaydedilmemektedir!")
         name_text=input("Hesap adı ve ya e posta / :")
         pasworld_text = input("Şifreniz (en az 8 hane )/ :")
         name = driver.find_element(By.NAME,"username")
         name.send_keys(name_text)
         pasworld = driver.find_element(By.NAME,"password")
         pasworld.send_keys(pasworld_text)
         sleep(5)
         button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
         button.click()
         xpeth=input("Sayfadan incele diyip sol üstteki mause okuna tıkladıktan sonra Görüntülenme sayısına tıklayın.Kenarda çıkan mavi alandaki koda sağ tık yapıp full Xpeth copy e tıklayın ve buraya yapıştırın: / :  ")
         
         sayı=input("Kontrol etme süresini dakika cinsinden yazınız. / :  ")
         for i in range(1,int(sayı)):
             Gor= driver.find_element(By.XPATH,xpeth)
             Gor_text = Gor.text
             
             print(f"Görüntülenme sayısı / : ")
             sleep(30)
             
            
        
         input ("İşlem tamamlanmıştır.Kapatmak için q yazın.")
    else:
      print("Yanlış giriş")
      