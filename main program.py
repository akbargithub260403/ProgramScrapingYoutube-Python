# Melakukan Import Package library Python Selenium
from selenium import webdriver

"""
Melakukan Inisialisasi untuk Web Driver [ Disini saya menggunakan browser Firefox , 
untuk browser lain. Cara untuk melakukan inisialisasi nya berbeda. ]
"""
driver  = webdriver.Firefox(executable_path='./geckodriver')
driver.implicitly_wait(10)

# Memasukan URL , untuk Website yang akan di Scraping. Disini Saya menggunakan Youtube Website
driver.get('https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl')

"""
Melakukan Pencarian Terhadap Element yang ada pada HTML.
Disini saya melakukan pencarian berdasarkan [ class ] yang berada di Tag HTML.
"""
videos      = driver.find_elements_by_class_name('style-scope ytd-video-renderer')

# Melakukan For Loop , untuk Mengeluarkan data data yang berada di Element HTML.
for video in videos:
    """
    Melakukan Pencarian Terhadap Element yang ada pada HTML.
    Disini saya melakukan pencarian berdasarkan [ xpath ]
    [ xpath ] adalah sintaks untuk mendefinisikan bagian dari dokumen XML
    """
    judul               = video.find_element_by_xpath('.//*[@id="title-wrapper"]').text
    youtube_channel     = video.find_element_by_xpath('.//*[@id="byline-container"]').text
    views_video         = video.find_element_by_xpath('.//*[@id="metadata-line"]').text
    deskripsi_video     = video.find_element_by_xpath('.//*[@id="description-text"]').text

    # Menampilkan Seluruh Data yang telah Didapatkan
    print(f'Judul Video :{judul}')
    print(f'Youtube Channel :{youtube_channel}')
    print(f'Views Video :{views_video}')
    print(f'Deskripsi Video :{deskripsi_video}')
    print('='*100)