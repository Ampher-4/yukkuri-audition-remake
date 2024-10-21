import Converter as testsubject
import urllib.parse

convertclient = testsubject.ConverterClient()
resolveclient = testsubject.ConverterResolve()
def test(input:str):
    response_result = convertclient.post_request(input)
    #now got a response object

    '''

    with open("./test.html", 'w', encoding='utf-8') as cacher:
        cacher.write(response_result)
'''
    output_result = resolveclient.snworks(response_result)

    print(output_result)
    urllib.parse.unquote(output_result)

#this is true result: 
# ジアーン シュウ ゥルゥ ドーァ(ディー) ジョーン ウエン ジュワン ホワン チュヨン ウエイ ゥリー ユイ シー ファー イン ドーァ(ディー) ゴーン ジュイ
    print(output_result)

test("将输入的中文转换成为日语式发音的工具")