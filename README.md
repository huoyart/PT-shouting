更新日志V1.5

1.新增配置文件config.json，配置完一次config.json后续更新只需要导入json即可，对于小白用户更加友好，需要配置的有三站cookie、iyuu key、站点开关

2.新增站点开关，在config.json配置，虽然在V1.2已经有作者提交代码，这次改为json配置

3.新增大青虫手动设置几号喊VIP，说明同上。

已知bug：大青虫在不是设定日求vip和彩虹ID时仍会发送请求无响应，后续可能会考虑重构这部分的代码


使用教程:

1.下载并安装Python3并配置好环境变量（百度解决，一般安装好mp都会自带此部分）

2.安装requests库,安装方法pip install requests（部分Python用户可能会自带此库，没有报错，能正常使用则不用理会这条）

（以上2条大多数用户都已有环境）

3.用任意手段，以文本格式打开config.json文件，包括但不限于右键文本文档打开，notepad++打开，notepad--打开，pycharm打开，vscode打开等（还不会请自行百度）

4.打开后填写相关三站cookie、iyuu key、站点开关，cookie浏览器获取，获取方法百度

5.如果需要青蛙获取下载，需到python代码最下面把注释取消，注释符号位#，删除#即可。（后续代码会修改）

6.完成上述操作后，请双击以Python方式打开，或通过任何ide运行。

7.有任何问题请百度解决，经过作者测试，无任何bug，除了大青虫返回值是乱码。



ps：

本作品有一定使用门槛，需要至少学过编程，懂最基础的意思。

作者学生党，没有空去优化代码和上大的平台，代码功底也有限。

本脚本可以自动喊大青虫VIP、上传、魔力；不可蛙上传（下载自行开启）；tosky上传、魔力。

转载请申明出处，作者霍雅，QQ3160723531，B站handsome丶霍雅，QQ群655262208

感谢QQ:1874295993（空白名）提交的V1.3代码，虽然本次更新没用上


后续想法：

1.后续可能会通过加入MP的方式，让用户更方便的使用该项目，但是由于作者水平有限，可能很长时间都没法实现

2.无法实现MP的方式的情况下，可能会外链用户文件，这样就不用每次更新都需要用户手动到代码填写配置文件

3.有人让我添加大象，但是我没有这个站点。

4.后续请求函数将会改成构造函数

5.处理大青虫喊vip问题，具体还没想好怎么改



往期更新日志：
更新日志V1.4

1.优化if函数，增加状态码判断，如404会提醒求魔力失败，HTTP响应404

2.修复已知bug


更新日志V1.3

//1.chatgpt优化代码

//2.青虫求VIP、彩虹ID改为识别当前日期为1号再执行

//3.增加各站点启用开关

//本次更新中没有使用这部分的代码，所以这部分的更新不存在


更新日志V1.2

1.修复已知bug，在不使用某个请求时，程序依旧正常运行且正常发送iyuu通知。例如程序原生没有使用青蛙喊下载，且注释掉了青蛙喊的相关代码，程序依旧正常运行，且会发送到iyuu显示青蛙求下载失败，如果需要使用青蛙求下载，直接把青蛙喊的注释符号删除即可，不需要修改其他代码，也就是不需要修改V1.1更新日志里的bug，同样的，你也可以自行屏蔽某些请求。

更新日志V1.1

1.更新iyuu（爱语飞飞）发送通知，使用方法：在代码中找到iyuu令牌和api的注释，把iyuu_key里的内容改成自己的key

目前这个有点bug，如果你要使用原生以外的喊话，如青蛙喊下载，那就需要把“定义text和desp变量”注释上面的注释删除，同时在desp变量上加入r8，虽然可以改成函数传参，但是我一开始没想到，也懒得改了，就这样吧
