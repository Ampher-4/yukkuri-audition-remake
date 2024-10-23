#首先插入模组
import yklConverter.phaseOne as phaseoneClient
import yklConverter.phaseTwo as phasetwoClient

#需要先声明client
convertclient = phaseoneClient.ConverterClient()
resolveclient = phaseoneClient.ConverterResolve()
phase2client = phasetwoClient.yklRunner()

#朝着第一个网站发送中文文本，网站会返回一整个页面。
#每次请求的时候都需要使用同一个client,这样效率更高。
response_result = convertclient.post_request("测试一下这句话")
#比如此时要发送第二条，直接使用先前的client即可。
another_response_result = convertclient.post_request("这是第二条请求")
#返回一个response对象，实际上是一整个html页面。所以我们需要进一步处理。


#使用resolveclient的resolve函数从页面中提取日语，并且裁剪空格。
#返回的就是一个日语字符串了
output_result = resolveclient.resolve(response_result)




#此时需要把日语字符串传给第二个网站，返回一个mp3二进制文件。
result = phase2client.getAudio(output_result)

 

#使用系统相应播放器播放文件
import tempfile
import os
import platform
import time

with tempfile.NamedTemporaryFile(suffix=".mp3",delete=False, dir='.') as temp_file:
    temp_file.write(result)
    temp_filename = temp_file.name

system = platform.system()
if system == 'Windows':
    os.system(f'start {temp_filename}')
elif system == 'Darwin':  # macOS
    os.system(f'afplay {temp_filename}')
elif system == 'Linux':
    os.system(f'xdg-open {temp_filename}')
else:
    raise Exception('Unsupported OS')

print("音频播放中... 本程序即将沉睡5秒，以便音频播放器调度")
time.sleep(5)
    
os.remove(temp_filename)
print("沉睡结束，音频临时文件已删除")