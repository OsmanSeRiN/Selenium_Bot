if __name__ == "__main__":
    
    
    plartform = input("İnstangram ise 'i', Youtube ise 'y' yazınız: ")
    
    if plartform == "y":
        onay_x = input("Merhaba, bu youtubenizin çalışıp çalışmadığını denemeniz adına yapılan bir programdır. Lütfen devam etmek için 1, kapatmak için q yazınız: ")
        
        if onay_x == "1":
            import Youtube_Test
            Youtube_Test.Test_youtube()
    elif plartform =="i":
        onay_x = input("Merhaba, bu youtubenizin çalışıp çalışmadığını denemeniz adına yapılan bir programdır. Lütfen devam etmek için 1, kapatmak için q yazınız: ")
        
        if onay_x == "1":
            import instangram
            instangram.test_instangram()
        else:
            input("Çıkış için q yazın. ")




       