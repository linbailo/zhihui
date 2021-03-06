# -广西现代职业技术学院上课自动签到和评教课堂
广西现代职业技术学院上课自动签到和评教课堂

上课签到、批量自动签到

可以上传腾讯云函数使用

不会找QQ：1628708538

第一次弄，我小白
# -教程
自己修改config.yml文件配置，都有注释

百度python安装教程

建议用腾讯云函数

依赖安装↓

pip install -r requirements.txt -t ./


openId获取↓

复制到微信，随便发送给一个人

第一：打开这个http://debugmm.qq.com/?forcex5=true

第二:然后在打开这个链接http://debugx5.qq.com/

第三：点开《信息》→✓上《打开vConsole调试功能》的勾勾

第四：打开智慧校园，看看右下角有没有《vConsole》

第五：进入智慧校园后点击《vConsole》→《Storsge》→《LocalStorsge》→复制《xd_openId》后面的东西，那个就是openId了



## 📝编辑配置文件

#### 本地测试（如果您能确保您足够熟练能够使用本项目请忽略这个步骤）

说明：本地测试的作用是为了便于您完成配置文件的修改。

1. 请先确保您拥有`python3`及以上的环境，若您的电脑没有`python3`的环境请[👉点击下载👈](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe)

2. 当您拥有`python3`环境~~时~~之前，请确保您在安装的时候有选择`Add python3.9 to Path`的选项以配置好环境变量，否则请自行百度配置好`python3`的环境变量（此步骤的作用是让我们能够直接在命令行中输入`pip`/`pip3`的命令来安装依赖）

3. 现在，我们就可以通过~~记事本~~[VSCode](https://az764295.vo.msecnd.net/stable/379476f0e13988d90fab105c5c19e7abc8b1dea8/VSCodeUserSetup-x64-1.59.0.exe)/[Notepad++](https://en.softonic.com/download/notepad-plus/windows/post-download)（不推荐使用记事本，这里提供两种常用的`代码编辑器`和它的下载地址，点击名称即可进入下载）来编辑配置文件

4. 进入文件夹，右键单击`config.yml`选择之前安装的`代码编辑器`来编辑它

5. 在编辑期间请特别注意`config.yml`的格式，如缩进、空格等内容。

6. 配置文件一共拥有多个`-user:`，每个`-user:`开始到下一个`-user:`之间为一个账号的配置，您可以在这里配置多个用户，请删除多余的用户配置，只保留您所以需要的`-user:`配置，每个`-user:`上的说明按照上面的说明更改

7. 在您配置完成`config.yml`之后，您就可以在同`config.yml`的当前目录下。找到`文件资源管理器`的`地址栏`（也就是您的文件夹显示窗口的顶部那一栏路径栏），单击空白处，清空路径地址，输入`cmd`回车以打开`cmd`界面

8. 安装依赖：到这一步，您就可以开始执行以下命令开始安装依赖了。在`cmd`中~~输入~~粘贴上以下代码按回车即可安装依赖

    `pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple`

    若出现`pip3 is not function`类似字眼，请确保您拥有`python3`环境并且配置了`环境变量`（请回看本地测试第1、2步）

    一般情况下安装过程中出现黄色字体可以无视，出现红色字体代表安装依赖出现错误，请在联系QQ1628708538询问相关的问题

9. 当您安装完成依赖后，就可以开始进行**本地测试**（这么多步骤终于到了测试的这一个步骤了，感动到自己有木有！）了

    （请在测试之前确保您当日有课并且还未提交）

    同样的在该`cmd`中输入`python index.py`并运行即可，在这里，您可能会遇到各种各样的错误

    - `No module named xxx`：出现这个情况代表您的依赖没有安装好，请仔细查看本地测试第8步

    - `其他问题`：请QQ提问

## ☁打包上云！（自动化签到的关键）

到这里，您的本地测试就已经完成了。那么您的配置文件已经没有任何问题，可以部署到云端以自动化签到了

**特别强调：请注意以下`打包`是打包`xx文件夹里的内容`还是`xx文件夹`**

#### ☁打包上腾讯云




1. 在腾讯云[云函数](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)中新建项目

2. 选择自定义创建（函数类型：事件函数；函数名称：随意（`lin`）；地域：北京（这就是地域，若控制台出现418错误，请在这里更换地域）；部署方式：代码部署；运行环境：`python3.6`；函数代码：本地上传zip包）

3. 将压缩包里的所有文件上传

4. 回到云函数创建页面，您可点击`上传`按钮以选择您的zip压缩文件

5. 打开高级配置。其他随意，您应该将其中的`内存：`改大一点如256MB，`执行超时时间：`改为99（推荐值），单个用户20s左右，请自行计算时间。一般设置大一点比较好

6. 到这里您就配置好云函数的配置了，请您点击`完成按钮`以完成项目的初始化，请您耐心等待项目创建成功......

7. 待您创建完成云函数后，请您点击`函数代码`以打开编辑器界面

8. 请您点击`函数代码`里的`在线编辑器`中的`终端`里的`新建终端`以创建一个终端

9. 执行以下代码以安装您的依赖到云函数中

   `pip3 install -r ./src/requirements.txt -t ./src -i https://mirrors.aliyun.com/pypi/simple`

10. 若您成功安装依赖，那么您的`在线编辑器`大致将如下图所示，左侧增加了一坨文件夹，底部有个黄色的`WARNING`提示

    ![示例](https://cdn.jsdelivr.net/gh/thriving123/ruoliCdn@main/images/202108161455188.png)

11. 特别的，在这里当您安装完成依赖后，您需要往下滑动，点击一下`部署`按钮以保存您在云函数上的操作，等待您的云函数部署成功之后，即可点击测试按钮以完成您的测试，看QQ推送结果。没有签到的话，看日志查询。

12. 若您没有进行`本地测试`，请注意看这里，您现在可以返回到`本地测试`的第`n`步骤以完成您的`config.yml`的配置。若您之前进行了本地测试请您忽略本步骤

13. 既然测试完成，那么就开始实现每天的自动化签到了。请您在刚才的网页页面上，找到`触发管理`并打开它，`创建触发器`。在`触发周期上`选择`自定义触发周期`，在`Cron表达式`中输入`1 0 0/8/18/23 * * * *`（本`cron表达式`代表每天的0、8、18、23点01分执行一次）（更多`cron表达式`请自行查看它的规则）

不会的，用这些cron↓

`3 16 8 * * * *`

`3 6 10 * * * *`

`3 51 14 * * * *`

`3 31 16 * * * *`

`3 51 19 * * * *`

14. 点击提交即可完成自动化签到的部署了
