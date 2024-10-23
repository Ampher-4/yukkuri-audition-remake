# 中文->油库里语音 转换器

此项目受[btc-99的批量中文语音转换油库里](https://github.com/btc-99/Yukkuri-audition)启发，使用python的request库重写了一遍核心api,提供了一组可以高度复用的python模组。这样一来执行速度有提升，同时也无需在电脑里安装多一个浏览器。

# 如何使用（基础）
可参考[usage_example.py]()文件。

# 如何使用 （进阶）
这里假定读者拥有一定的python基础，能够简单理解http协议中GET与POST的概念。

## 项目模块划分
yklConverter是一个python包，里面包含了phaseOne还有phaseTwo两个子模组。分别对应“从ltool网站把中文转换成日语”还有“从yukumo网站把日语转换成音频”两个阶段。

## api说明
phaseOne:ConverterClient: 负责将中文字符串传给ltool网站，并且拿取返回值。使用时应该先实例化一个ConvertClient类，并且复用该类的post_request方法。

phaseOne: ConvertClient: post_request: content参数填入要翻译的中文。 option参数对应了ltool网站中的6种翻译方式，填入字符串包装的数字。option_ext参数则是选择3种不同的翻译文字。”全角片假“对应zenkaku（默认选项）， ”半角假名“对于hankaku，“平假名”对应hiragana.
比如：想要选择从左到右第二个选项，就填入“2”。 该参数默认选择第一种。
返回一个字符串，内容是一整个html页面(原网站是php建的，处理post方式就是如此生草),需要进一步使用ConverterResolve的resolve方法处理。
警告：”5“和”6“这两个选项完全是broken的，原网站的html tag有问题，会返回带着html部分内容的字符串，我并没有适配这两个选项。


phaseOne:ConverterResolve: 负责将装载整个html页面的string过滤，过滤出日语，并且对日语去除空格和括号内内容。

phaseOne:ConvertResolve: resolve: html_content参数填入调用ConverterClient.post_request后的返回值。xpath_expression是用于定位日语在html页面里位置的，留默认参数即可，无需显式为其赋值。
返回一个裁剪掉空格和括号的日语字符串。
警告：没有考虑“5”和“6”这两个选项，因为这两个选项返回结果的日语在另一条xpath里。由于上一个类我没有对“5”“6”做处理，这里统一保持不处理。


phaseTwo: yklRunner: 负责将日语字符串传给yukumo网站，返回二进制音频文件的字节串

phaseTwo: yklRunner: getAudio: fmt_jpn参数填入日语字符串。sound_option填入要使用的声线。填入的内容为原网站声线代码的后缀。比如要使用AT1-F1就填入f1（默认参数）， AT2-RM3就填入rm3. 
返回二进制音频文件的字节串（是b‘xxxx’这种，不是字符串！）。使用者需要自己打开文件，并且将音频字节串写入，写入后记得关闭文件以保存。
警告：AT10开头的还没有做适配，因为get payload有许多可调参数，后续会加入支持。

