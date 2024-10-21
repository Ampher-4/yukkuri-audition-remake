import urllib.parse
import requests
import tempfile
import cv2
import os
import urllib

def 谁问我了():
    addr = "https://api.kuleu.com/api/suiji_renshe"
    respond_all = requests.get(addr, proxies=None)

    print(respond_all.text)


def QRcode_gen(text:str="Amathea_Outpost", size:int=200, user_proxy=None)->bytes:
    addr="https://api.kuleu.com/api/qrcode"
    addr += "?"

    
    addr += "frame=1&e=L&"#test only

    text_after_convert = urllib.parse.quote(text)
    addr += ("text="+text_after_convert)
    addr += "&"
    addr += ("size="+str(size))

    resp = requests.get(url=addr, proxies=user_proxy)
    return resp.content

def QRcode_display(bytes_str:bytes):#return tmp file location
    tmpfile = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    tmpfile.write(bytes_str)
    tmpfilepath = tmpfile.name
    tmpfile.close()
    return tmpfilepath

def QRcode_close(filepath):#call this each time you make a display call.
    os.remove(filepath)




if(__name__ == "__main__"):
    proxy_groups = {
        "http":"http://127.0.0.1:7890",
        "https":"http://127.0.0.1:7890"
    }
    while(1):

        userinput:str = input("input the text you want to encode: ")

        QRCode_picture = QRcode_gen(text=userinput,user_proxy=proxy_groups)

        QRcode_tmpfile = QRcode_display(QRCode_picture)

        image = cv2.imread(QRcode_tmpfile)
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        QRcode_close(QRcode_tmpfile)







