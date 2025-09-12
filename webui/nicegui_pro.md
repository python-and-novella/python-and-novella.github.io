# NiceGUI札记（2026）

[TOC]

## 0 为何而写

NiceGUI（官网https://nicegui.io/）是一款优秀的WebUI、GUI框架，只需学习一定量的前端知识，就能使用NiceGUI快速搭建出美观的UI界面。

但是，官方更新很快，加上笔者2024年开始创作的《NiceGUI的中文入门教程》受限于笔者当时的思路、水平，时至今日，很多内容已经不适合最新版本。

于是，笔者结合其他框架的敏捷式教程创作经验，决定为NiceGUI的最新版本创作新的入门教程，摒弃之前事无巨细的风格，采用按时间顺序、主要内容为补充官方教程、不断穿插实际示例的敏捷开发风格。

并且，为了节省读者的付费成本，适应读者的碎片化阅读习惯，本教程不再采用整本付费的方式，而是根据章节内容的质量、字数单章付费，让读者按需购买。

当然，对于喜欢一次看个爽、不想被免费章节广告打扰的读者，也有整本买断的方式（每年两次机会）。不过，笔者不推荐这种方式。因为内容一直在更新、追加，只能提供当前内容进度的整本。而且整本买断是完全基于字数（本地编辑器统计，非微信那边的字数，会少一些）计费，虽然部分章节没有质量溢价，但免费章节和预览部分也会计费，整体价格会比全部单买略高。

## 1 安装NiceGUI

之前《NiceGUI的中文入门教程》使用PDM作为环境管理工具，这一次，将使用uv管理环境。

为什么要用uv？

原因只有一个，那就是快！速度对比如下：

![2026_1_1](nicegui_pro.assets/2026_1_1.png)

首先，新建一个空白文件夹，笔者这里新建了`nicegui_app`文件夹。进入该文件夹，运行`uv init`，即可初始化该文件夹为项目文件夹（`uv`命令需要使用`pip install uv`安装）。

此时创建的项目是空白项目，没有添加任何依赖，还需要使用`uv add nicegui`添加依赖，并自动创建虚拟环境。

NiceGUI还提供了一些可选的依赖：

- `pywebview`库，以Native Mode（本地窗口模式）运行NiceGUI程序时依赖该库，使用`uv add nicegui[native]`命令添加。
- `plotly`库，`ui.plotly`控件依赖该库，使用`uv add nicegui[plotly]`命令添加。
- `matplotlib`库，`ui.matplotlib`控件和`ui.pyplot`控件依赖该库，使用`uv add nicegui[matplotlib]`命令添加。
- `nicegui-highcharts`库，`ui.highchart`控件依赖该库，使用`uv add nicegui[highcharts]`命令添加。
- `libsass`库，`ui.add_scss`方法和`ui.add_sass`方法依赖该库，使用`uv add nicegui[sass]`命令添加。
- `redis`库，使用Redis存储`app.storage`时（定义环境变量`NICEGUI_REDIS_URL`）依赖该库，使用`uv add nicegui[redis]`命令添加。

如果想要将虚拟环境中的所有库升级至最新稳定版，可以使用`uv sync -U`。

若是只想升级指定库，比如`nicegui`，则使用`uv sync -P nicegui`。

升级指定库至最新测试版。因为本章节创作时，NiceGUI的3.0.0版本尚未正式发布，需要升级至最新测试版才行，或者读者想要使用其他最新测试版的功能，则可以使用`uv sync -P nicegui --prerelease allow`命令，将指定库升级至最新测试版。

## 2 NiceGUI程序的基本结构与运行方式

先看示例，简单了解一下NiceGUI程序的基本结构：

```python3
from nicegui import ui
  
ui.button('Hello')

ui.run()
```

示例很简单，正好对应着NiceGUI程序的三个基本组成：

- 导入模块
- 创建控件
- 运行程序



（导入模块，创建控件，运行）



从NiceGUI 3.0.0开始，NiceGUI程序按照是否使用`ui.page`方法可划分为两种模式，对应着两种基本结构：

- 脚本模式，不使用`ui.page`方法创建页面，所有控件

  

  ```python3
  ```

  

- 页面模式

  

  ```python3
  ```

  

两种模式均可以设计为单页面应用，实现细节上大致相同。



运行方式分为，网页模式和本地窗口模式，



网页模式还支持与FastAPI应用组合运行：

```python3
import uvicorn
from fastapi import FastAPI
from nicegui import ui
  
fast_app = FastAPI()
  
@ui.page('/')
def index():
    ui.label('Hello, NiceGUI!')
  
ui.run_with(
    app=fast_app,
)

uvicorn.run(app=fast_app,host='0.0.0.0',port=80)
```

或者将NiceGUI程序挂载到子路由：

```python3
import uvicorn
from fastapi import FastAPI
from nicegui import ui
  
fast_app = FastAPI()
  
@fast_app.get('/')
def root():
    return '请访问 /gui 查看NiceGUI程序'
  
# 这里的路径是相对挂载路径而言
@ui.page('/')
def index():
    ui.label('Hello, NiceGUI!')
  
ui.run_with(
    app=fast_app,
    # 省略挂载路径的话，直接访问根路径（/）即可看到NiceGUI程序，但要注释掉@fast_app.get('/')和其装饰的函数
    mount_path='/gui' 
)
  
uvicorn.run(app=fast_app,host='0.0.0.0',port=80)
```





## 3 创建控件



含with的技巧

slot的技巧

for循环的技巧



## 4 三种有关样式的方法（属性）



props，classes，style



## 3 事件



以按钮为例，介绍控件的事件使用方法

参数传入，具体的on_*方法，通用的on方法





介绍app的事件



介绍事件类`Event`类（相当于信号，一般用于共享数据，通常是与属性绑定结合使用）









## 4 属性绑定



属性绑定方法的基本用法，含具体属性绑定方法和通用属性绑定方法，



介绍绑定的技巧，字典、全局变量、性能优化



## 4 可刷新方法



refreshable

以及配套的ui.state状态控件







## 4 异步支持



支持可调用对象、函数的地方，对异步的支持情况

脚本模式、ui.page、ui.sub_pages、on_click参数、控件的异步方法（比如button的clicked，可以使用异步等待来实现分步显示）



## 4 后台任务



含定时器





## 4 快捷键——`ui.keyboard`







## 4 具体控件——`ui.button`

具体控件的基础用法免费发布，高级用法和特定问题的解决付费，最低1豆，最多9豆





## 4 自定义控件





## 5 管理网页相关文件

ui.add\_\* 和app.add\_\*





## 5 修改指定元素





## 5 环境变量

原文参考自 https://nicegui.io/documentation/section_configuration_deployment#environment_variables 。

在NiceGUI中，有些设置项只能通过修改环境变量实现：

- `MATPLOTLIB`，默认为`'true'`，表示是否自动导入`matplotlib`(`ui.pyplot`和`ui.line_plot`依赖此库），可以将此环境变量设置为`'false'`来避免自动导入，减少导入`nicegui`所需的时间，同时也会导致`ui.pyplot`和`ui.line_plot`无法使用。

  以下为用于对比的示例，读者可以修改环境变量值，冷启动（完全退出再重新打开）看看导入所需的时间：

  ```python3
  import os
  os.environ['MATPLOTLIB'] = 'false'
  
  import time
  start_time = time.time()
  
  from nicegui import ui
  
  end_time = time.time()
  
  print(f'used {end_time- start_time}')
  
  ui.button('Test')
  
  ui.run(native=True)
  ```

- `NICEGUI_STORAGE_PATH`，默认为`'.nicegui'`，表示使用`app.storage`时，需要在服务器磁盘存储数据的空间，具体使用哪个位置，默认为运行命令时当前路径下的`.nicegui`文件夹。

- `NICEGUI_REDIS_URL`，默认未设置（即为`None`），表示使用`app.storage`时，相关数据存储在哪个Redis服务器中，该环境变量需要设置为包含Redis协议的完整地址，比如`'redis://redis_server_host:6379'`，如果不设置（即默认值），则表示相关数据存储在本地文件夹中。

- `NICEGUI_REDIS_KEY_PREFIX`，默认为`'nicegui'`，表示使用`app.storage`，相关数据存储在Redis服务器中时，相关数据的键使用什么作为前缀。

- `MARKDOWN_CONTENT_CACHE_SIZE`，默认为`'1000'`，表示`ui.markdown`在内存中缓存多少个内容片段，如果使用`ui.markdown`时，程序占用内存太高，可以调整该值。

- `RST_CONTENT_CACHE_SIZE`，默认为`'1000'`，表示`ui.restructured_text`在内存中缓存多少个内容片段，如果使用`ui.restructured_text`时，程序占用内存太高，可以调整该值。

  ```python3
  from nicegui import ui
  from nicegui.elements import markdown,restructured_text
  
  import os
  os.environ['MARKDOWN_CONTENT_CACHE_SIZE'] = '1'
  os.environ['RST_CONTENT_CACHE_SIZE'] = '1'
  
  ui.label(f'MARKDOWN_CONTENT_CACHE_SIZE is {markdown.prepare_content.cache_info().maxsize}')
  ui.label(f'RST_CONTENT_CACHE_SIZE is {restructured_text.prepare_content.cache_info().maxsize}')
  
  ui.run(native=True)
  ```

xxx



