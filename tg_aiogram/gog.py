from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': 'your_image_dir'})
google_crawler.crawl(keyword='cat', max_num=100)