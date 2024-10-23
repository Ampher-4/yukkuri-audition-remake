import yklConverter.phaseOne as phaseoneClient
import yklConverter.phaseTwo as phasetwoClient
import urllib.parse

convertclient = phaseoneClient.ConverterClient()
resolveclient = phaseoneClient.ConverterResolve()

def phaseonetest(input:str) -> str:
    response_result = convertclient.post_request(input)
    #now got a response object

    output_result = resolveclient.resolve(response_result)

    return str(output_result)

#this is true result: 
# ジアーン シュウ ゥルゥ ドーァ(ディー) ジョーン ウエン ジュワン ホワン チュヨン ウエイ ゥリー ユイ シー ファー イン ドーァ(ディー) ゴーン ジュイ
    print(output_result)

phase2client = phasetwoClient.yklRunner()
result = phase2client.getAudio("シーイーシアジョーァゴーァドーンシイ")