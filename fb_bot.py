 
import requests
from bs4 import BeautifulSoup
from secrets import username, password

class FaceBookBot():

    login_basic_url = 'https://mbasic.facebook.com/login'
    payload = {
            'email': username,
            'pass': password
        }
    
    def parse_html(self, request_url):
        with requests.Session() as session:
            post = session.post(self.login_basic_url, data=self.payload)
            parsed_html = session.get(request_url)
        return parsed_html

    def scrap_post_text(self):
        
        #REQUEST_URL = f'https://mbasic.facebook.com/Treyarch/photos/a.10150344869682724/10158045170162724'
        REQUEST_URL = f'https://mbasic.facebook.com/photo/?fbid=326371362190018&set=a.271797234314098'
        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        content = soup.find_all('div', class_ = "_2vj8")
        post_content = []
        for lines in content:
            post_content.append(lines.text)
        
        post_content = ' '.join(post_content)    
        return post_content

bot = FaceBookBot()
print(bot.scrap_post_text())
#print(bot.parse_html("https://mbasic.facebook.com"))

    