# Douban-based book info collector

import requests
import csv

with open('finished.csv', 'w', newline='\n', encoding='utf-8') as writeto:
    fieldnames = ['isbn13', 'title', 'publisher', 'pubdate', 'price']
    writer = csv.DictWriter(writeto, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()

    with open('books.csv', 'r', encoding='utf-8') as readfrom:
        reader = csv.DictReader(readfrom)
        for row in reader:
            isbn = row['ISBN']
            r = requests.get('https://api.douban.com/v2/book/isbn/' + isbn + '?fields=isbn13,title,publisher,pubdate,price')
            book_info = r.json()
            
            writer.writerow(book_info)
