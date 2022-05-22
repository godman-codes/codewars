def domain_name(url):
   if url.startswith('http://'):
      url = url.replace('http://', '')
      if url.startswith('www.'):
         url = url.replace('www.', '')
   elif url.startswith('https://'):
      url = url.replace('https://', '')
      if url.startswith('www.'):
         url = url.replace('www.', '')
   elif url.startswith('www.'):
      url = url.replace('www.', '')
   print(url.split('.')[0])


domain_name("http://google.com")
domain_name("http://google.co.jp")
domain_name("www.xakep.ru")
domain_name("https://youtube.com") 