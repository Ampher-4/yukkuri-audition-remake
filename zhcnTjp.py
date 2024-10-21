import requests
import urllib.parse
import traceback

#this class has a fake header. A call on thisclass.getheader will return a fake header
#you can replace the header as you want
class request_cheater:
    fake_header:dict = {
    }

    def __init__(self):
        self.fake_header = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            #'accept-encoding': 'gzip, deflate, br, zstd',
            #Noted above line cause a page surpression error
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6',
            'cache-control': 'max-age=0',
            'connection': 'keep-alive',
            'content-length': '68',
            'content-type': 'application/x-www-form-urlencoded',
            #A cookie will be here later
            'host': 'www.ltool.net',
            'origin': 'https://www.ltool.net',
            'referer': 'https://www.ltool.net/chinese_simplified_and_traditional_characters_pinyin_to_katakana_converter_in_simplified_chinese.php',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
        }

    def getheader(self) -> dict:
        return self.fake_header

    #you can use your own header, in format of Dictionary
    def use_cust_header(self, header: dict):
        self.fake_header = header


        


#remote api is using POST method.
#in the payload, content is the chinese text to be converted.
#firstinput is OK(?)
#option is possible stands for round dot line under the input textbox(?)
#optionext is zenkaku(?)

class textClient:
    remote_site_origin = "https://www.ltool.net/chinese_simplified_and_traditional_characters_pinyin_to_katakana_converter_in_simplified_chinese.php"
    remote_api = "https://www.ltool.net/chinese_simplified_and_traditional_characters_pinyin_to_katakana_converter_in_simplified_chinese.php"
    header_handler:request_cheater

    def __init__(self):
        self.header_handler = request_cheater()


    #default post method, input zhcn string, return jp string
    def post(self,chinese_text:str, firstinput:str="OK", option:str="1", optionext:str="zenkaku") -> str:

        chinese_text = urllib.parse.quote(chinese_text)
        #encode the payload
        default_payload = {
            "content": chinese_text,
            "firstinput": firstinput,
            "option": option,
            "optionext": optionext
        }

        response_from_request:requests.Response
        try:
            response_from_request = \
                requests.request(method="POST",url=self.remote_api, \
                    headers=default_payload, data=self.header_handler.getheader())
        except Exception as e:
            traceback.print_exc(e)
            
        respheader = response_from_request.headers
        contentbody = response_from_request.content
        print(response_from_request.text)
        return "default"
        
        

#ok 1-1 xpath://*[@id="result"]/div
#not ok 6-3 xpath://*[@id="result"]/div/div



