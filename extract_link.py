import csv
# class ScrapingLinks:

def get_link():
    str_link = None
    with open('link.csv', encoding='utf-8-sig') as csvFile:
        reader = csv.reader(csvFile)
        count = 0

        for row in reader:
            count = count + 1
            if count > 2:
                if str_link is None:
                    print('mujib la sani')
                    str_link = row[0]

                else:
                    str_link = str_link + ',' + row[0]
    return str_link


link_lists = get_link().split(',')

with open('protik.csv', 'w', newline='') as file:
    custom_writer = csv.writer(file)
    for link in link_lists:
        custom_writer.writerow(['https://www.ultimatespecs.com' + link])




