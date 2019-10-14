import requests
import lxml.html

print('*format input: "https://.../"')

url = input('please insert a link to the news: ')
name_file = str(url)
name_file = name_file.replace('https:/', '[CUR_DIR]').replace('/', '_').replace('shtml', 'doc')

f = open(name_file, 'w')

class UrlParser:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_page(self):

        try:
            res = requests.get(self.base_url)
        except requests.ConnectionError:
            return

        if res.status_code < 400:
            return res.content

    def parse(self, html):
        html_tree = lxml.html.fromstring(html)
        path = ".//div[contains(@class, 'article')]//p"
        path_heading = ".//h1[contains(@itemprop, 'headline')]"
        path_time = ".//time[contains(@class, 'date_time')]"

        heading = html_tree.xpath(path_heading) [0]
        time = html_tree.xpath(path_time) [0]
        content = html_tree.xpath(path)
        
        f.write('   ' + heading.text_content() + '\n' + time.text_content() + '\n\n\n')

        for elem in content:
            elem
            text = elem.text_content()
            text1 = ''  
            c = 0 
            for i in text.split(): 
                c += len(i)  
                if c > 80:  
                    text1 += '\n'  
                    c = len(i)  
                elif text1 != '':  
                    text1 += ' '  
                    c += 1  
                text1 += i  
                
            f.write('   ' + text1 + '\n\n')
            
if __name__ == "__main__":
    
    parser = UrlParser(url)

    page = parser.get_page()

    parser.parse(page)