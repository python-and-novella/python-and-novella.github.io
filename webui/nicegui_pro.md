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

- `pywebview`库，以Native Mode（窗口模式）运行NiceGUI程序时依赖该库，使用`uv add nicegui[native]`命令添加。
- `plotly`库，`ui.plotly`控件依赖该库，使用`uv add nicegui[plotly]`命令添加。
- `matplotlib`库，`ui.matplotlib`控件和`ui.pyplot`控件依赖该库，使用`uv add nicegui[matplotlib]`命令添加。
- `nicegui-highcharts`库，`ui.highchart`控件依赖该库，使用`uv add nicegui[highcharts]`命令添加。
- `libsass`库，`ui.add_scss`方法和`ui.add_sass`方法依赖该库，使用`uv add nicegui[sass]`命令添加。
- `redis`库，使用Redis存储`app.storage`时（定义环境变量`NICEGUI_REDIS_URL`）依赖该库，使用`uv add nicegui[redis]`命令添加。

如果想要将虚拟环境中的所有库升级至最新稳定版，可以使用`uv sync -U`。

若是只想升级指定库，比如`nicegui`，则使用`uv sync -P nicegui`。

升级指定库至最新测试版。因为本章节创作时，NiceGUI的3.0.0版本尚未正式发布，需要升级至最新测试版才行，或者读者想要使用其他最新测试版的功能，则可以使用`uv sync -P nicegui --prerelease allow`命令，将指定库升级至最新测试版。

## 2 认识NiceGUI程序

### 2.1 基本结构

先看示例，简单了解一下NiceGUI程序的基本结构：

```python3
# 导入模块
from nicegui import ui
# 创建控件
ui.button('Hello')
# 运行程序
ui.run()
```

示例很简单，正好对应着NiceGUI程序的三个基本组成：

- 导入模块（对象）。NiceGUI的`ui`模块提供了创建控件和运行程序的基本功能。当然除了该模块，NiceGUI还提供了其他模块和魔术对象（无需实例化即可直接访问具体单一实例对象的特殊对象），具体模块和对象会在后续使用时详细介绍，这里暂不展开。
- 创建控件。导入了模块之后，控件并不会自动创建，还需要访问具体的控件类，将其实例化，才算真正创建。关于具体控件的用法和创建，将在单独的章节中详细介绍，本章暂不展开。
- 运行程序。完成前面的步骤之后，直接运行Python文件，并不会显示控件，因为NiceGUI程序需要通过特殊的方法运行。比如示例中的`ui.run`方法就是一种运行程序的方法，构建模式、显示模式不同，该方法使用的参数也有所不同。此外，运行程序的方法也不止这一种，还有与现有FastAPI应用组合运行使用的`ui.run_with`方法。

### 2.2 构建模式

NiceGUI程序用于构建界面的代码结构不同时，对应的构建过程（模式）也有所不同。

从NiceGUI 3.0.0开始，NiceGUI程序按照是否使用`ui.page`创建页面，可划分为两种构建模式：

- 脚本模式。不使用`ui.page`创建页面的话，所有创建的控件都属于“主页面”（地址为网站的根路径）。此时的“主页面”不是真正意义上的“主页面”，虽然每个访问者打开的“主页面”内容互相独立，但这种构建模式只支持一个页面，即“主页面”。

  以下为脚本模式的示例：

  ```python3
  from nicegui import ui
  
  ui.button('Hello')
  
  ui.run()
  ```

  除了上面这种直接创建控件，默认以脚本模式构建的代码，还可以将所有创建控件的过程放在函数中，并将构建“主页面”的函数名传给`ui.run`方法的第一位置参数`root`：

  ```python3
  from nicegui import ui
  
  def index():
      ui.button('Hello')
  
  ui.run(root=index)
  ```

  相比于不用函数打包，这种方式可以自由定义“主页面”其他部分的创建顺序。

  比如，想要在当前内容的前面添加一些文字作为标题，如果不用函数打包，只能这样写：

  ```python3
  from nicegui import ui
  
  ui.label('标题')
  ui.button('Hello')
  
  ui.run()
  ```

  使用函数打包的话，可以将添加的部分打包到函数中，提前使用，最后定义具体内容：

  ```python3
  from nicegui import ui
  
  def index():
      title()
      ui.button('Hello')
  
  def title():
      ui.label('标题')
  
  ui.run(root=index)
  ```

  ![2026_2_1](nicegui_pro.assets/2026_2_1.png)

- 页面模式。脚本模式只支持一个“主页面”，一旦想创建多个页面展示不同的内容，就只能使用`ui.page`创建其他页面，这样的构建模式就是页面模式。

  需要注意的是，一旦使用了`ui.page`创建页面，就不能使用脚本模式的代码结构（即不能在页面之外创建控件，也不能使用`ui.run`的`root`参数），否则会报错。

  `ui.page`是一个类，其参数`path`表示页面对应的网站路径。但是，这样直接构建出来的页面不包含控件，需要调用`ui.page`对象，并传入函数内创建控件的函数名：
  
  ```python3
  from nicegui import ui
  
  def index():
      ui.button('Hello')
  
  index_page = ui.page('/')
  index = index_page(index)
  
  ui.run()
  ```
  
  看起来有点复杂，但如果读者有Python基础的话，就会发现，这段看似复杂的代码，其实就是一个装饰器：
  
  ```python3
  from nicegui import ui
  
  @ui.page('/')
  def index():
      ui.button('Hello')
  
  ui.run()
  ```

以上只是构建模式的简单介绍，其余参数和更多用法将在后面的章节中展开介绍。

### 2.3 单页面应用（SPA）

与页面模式效果类似的是单页面应用（Single Page Application，简称SPA），单页面应用可以在不增加普通页面的前提下，增加多个子页面，让脚本模式实现页面模式的效果。

单页面应用需要使用`ui.sub_pages`类，其第一位置参数`routes`是一个字典，网站路径为键，创建控件的函数的函数名为值，表示网站路径与具体内容的对应关系。

示例如下：

```python3
from nicegui import ui

def index():
    ui.label('Main')
    ui.separator()
    ui.sub_pages(
        {
            '/':main,
            '/a':a,
            '/b':b
        }
    )

def main():
    ui.link('Page A','/a')
    ui.link('Page B','/b')

def a():
    ui.link('Page Main','/')
    ui.link('Page B','/b')

def b():
    ui.link('Page Main','/')
    ui.link('Page A','/a')

ui.run(root=index)
```

可能读者实际运行代码之后，会产生一个疑问：既然效果与页面模式相同，那为何不直接使用页面模式？

这里就要说一下单页面应用的特殊之处：两种构建模式均可以设计为单页面应用。

假如页面模式中，有一个`/main`页面，则可以将上面脚本模式的单页面应用套用到页面模式中：

```python3
from nicegui import ui

@ui.page('/main')
def index():
    ui.label('Main')
    ui.separator()
    ui.sub_pages(
        routes={
            # 子页面的路径必须与实际路径一致
            '/main':main,
            '/main/a':a,
            '/main/b':b
        }
    )

def main():
    ui.link('Page A','/main/a')
    ui.link('Page B','/main/b')

def a():
    ui.link('Page Main','/main')
    ui.link('Page B','/main/b')

def b():
    ui.link('Page Main','/main')
    ui.link('Page A','/main/a')

ui.run()
```

但与脚本模式的单页面应用不同，页面模式的单页面应用，除了将指定路径关联为子页面之外，还可以同时关联一个普通页面：

```python3
from nicegui import ui

@ui.page('/main')
def index():
    ui.label('Main')
    ui.separator()
    ui.sub_pages(
        routes={
            # 子页面的路径必须与实际路径一致
            '/main':main,
            '/main/a':a,
            '/main/b':b
        }
    )

def main():
    ui.link('Page A','/main/a')
    ui.link('Page B','/main/b')

def a():
    ui.link('Page Main','/main')
    ui.link('Page B','/main/b')

def b():
    ui.link('Page Main','/main')
    ui.link('Page A','/main/a')

@ui.page('/main/a')
def page_a():
    ui.label('Real Page A')

@ui.page('/main/b')
def page_b():
    ui.label('Real Page B')

ui.run()
```

通过点击`/main`页面的超链接跳转至`/main/a`的话，显示的只是单页面应用的子页面：

![2026_2_2](nicegui_pro.assets/2026_2_2.png)

但是，此时刷新页面或者直接访问`/main/a`的话，则会显示`/main/a`页面：

![2026_2_3](nicegui_pro.assets/2026_2_3.png)

以上只是单页面应用的简单介绍，其余参数和更多用法将在后面的章节中展开介绍。

单页面应用与其他构建模式组合使用时，学习难度会陡然而升，容易遇到很多难以解决的问题。因此，这部分内容不太理解的话可以暂时跳过，等后续学习了其他基础之后再回过头学习。

### 2.4 显示模式

NiceGUI程序支持两种显示模式：

- 网页模式，可以将NiceGUI程序部署为网站。
- 窗口模式，可以将NiceGUI程序部署为桌面程序。

除了前面示例中以网页形式显示NiceGUI程序之外（即网页模式），还可以给`ui.run`方法的`native`参数传入`True`，以窗口形式显示NiceGUI程序（即窗口模式）：

```python3
from nicegui import ui

def index():
    title()
    ui.button('Hello')

def title():
    ui.label('标题')

ui.run(root=index,native=True)
```

![2026_2_4](nicegui_pro.assets/2026_2_4.png)

注意，窗口模式依赖`pywebview`库，需要先安装`pywebview`库才能使用。

### 2.5 运行方法

NiceGUI有两种运行NiceGUI程序的方法：

- `ui.run`方法是前面介绍的，而且后续示例中一般使用该方法，支持网页模式和窗口模式。
- `ui.run_with`方法，则一般用于将NiceGUI程序挂载到现有的FastAPI程序中，仅支持网页模式。

以下为`ui.run_with`方法的示例：

```python3
import uvicorn
from fastapi import FastAPI
from nicegui import ui

fast_app = FastAPI()
  
@ui.page('/')
def index():
    title()
    ui.button('Hello')

def title():
    ui.label('标题')

ui.run_with(
    app=fast_app,
)

uvicorn.run(app=fast_app,host='127.0.0.1',port=80)
```

也可以将NiceGUI程序挂载到指定的子路由：

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
    title()
    ui.button('Hello')

def title():
    ui.label('标题')

ui.run_with(
    app=fast_app,
    # 省略挂载路径的话，直接访问根路径（/）即可看到NiceGUI程序，但要注释掉@fast_app.get('/')和其装饰的函数
    mount_path='/gui' 
)

uvicorn.run(app=fast_app,host='127.0.0.1',port=80)
```

## 3 创建控件

创建控件看似简单，只是了解一下具控件的参数、属性、方法，没有多少难点。但在实际使用时，具体参数、方法的使用，创建的技巧，远没有看上去那么简单。

### 3.1 实例化

实例化控件类，即可创建控件：

```python3
from nicegui import ui

def index():
    ui.label('标题')
    ui.button('Hello')

ui.run(root=index,native=True)
```

除了不分配变量的用法，对于某些需要重复使用的控件，想要在后续代码中访问这些控件的属性、方法的话，则要给这些控件分配变量。因为每次实例化都是创建一个控件，即使是相同类型的控件，重复实例化也是重复创建：

```python3
from nicegui import ui

def index():
    label = ui.label('标题')
    button = ui.button('Hello')
    ui.button('World')
    button.disable()

ui.run(root=index,native=True)
```

![2026_3_1](nicegui_pro.assets/2026_3_1.png)

### 3.2 `with`的技巧

NiceGUI本质上是一个基于Quasar框架实现的网页框架，很多控件也都是网页控件。如果读者熟悉网页，知道网页的元素可以多重嵌套，进而实现复杂的效果。当然，读者不熟悉也没关系，可以将控件想象成一个盒子，盒子里可以装另一个盒子，控件也一样。

对于NiceGUI的控件来说，想要在控件中嵌入另一个控件，只需使用上下文管理器进入控件的上下文，在上下文中创建其他控件，相当于在控件内嵌入其他控件：

```python3
from nicegui import ui

def index():
    with ui.button('Hello'):
        ui.button('World')

ui.run(root=index,native=True)
```

![2026_3_2](nicegui_pro.assets/2026_3_2.png)

除了嵌套一层，还可以嵌套多层：

```python3
from nicegui import ui

def index():
    with ui.button('Hello'):
        with ui.button('World'):
            ui.button('!')

ui.run(root=index,native=True)
```

或者使用一个`with`，后接英文逗号分隔的多个对象，同样表示嵌套多层（和上个示例效果一样）：

```python3
from nicegui import ui

def index():
    with ui.button('Hello'), ui.button('World'):
        ui.button('!')
```

对于使用上下文管理器进入上下文的控件，如果想要访问该控件，可以使用`as`关键字，后接变量名，即可在控件的上下文，甚至与`with`同一缩进的作用域内，访问该控件。比如：

```python3
from nicegui import ui

def index():
    with ui.button('Hello') as button1:
        ui.button('World')
    with ui.button('Hello') as button2:
        with ui.button('World') as button3:
            ui.button('!')
    with ui.button('Hello') as button4, ui.button('World') as button5:
        ui.button('!')

ui.run(root=index,native=True)
```

请牢记这些技巧，后续使用具体控件时，这些都是基本操作。

### 3.3 控件的插槽（slot）

前面说了使用上下文管理器进入控件上下文，进而在控件内嵌入其他控件。其实，这种操作就是进入了控件的`default`插槽（插槽的概念来自Quasar控件，相关资料可以查看https://quasar.dev/components中对应的控件）。

以`ui.input`输入框控件为例，两种写法的效果是一样的：

```python3
from nicegui import ui

def index():
    with ui.input('Name'):
        ui.button('Ok')
    with ui.input('Name').add_slot('default'):
        ui.button('Ok')

ui.run(root=index,native=True)
```

![2026_3_3](nicegui_pro.assets/2026_3_3.png)

简单来说，插槽可以看作是一个控件中可以插入其他控件的位置，而不少控件有多个插槽，`default`插槽就是默认位置。如果想要在其他插槽中插入其他控件，则要使用`add_slot`方法，指定具体插槽。以输入框控件（具体参考https://quasar.dev/vue-components/input）为例：

```python3
from nicegui import ui

def index():
    my_input = ui.input('Name')
    with my_input.add_slot('before'):
        ui.button('Pre')
    with my_input.add_slot('after'):
        ui.button('Next')

ui.run(root=index,native=True)
```

可以在输入框控件前后分别添加不同的按钮：

![2026_3_4](nicegui_pro.assets/2026_3_4.png)

就是因为输入框控件前、后分别对应着不同的插槽。

### 3.4 `for`的技巧

需要创建多个有规律的控件时，熟悉Python的读者肯定第一时间想到了`for`，使用该关键字遍历可以迭代的对象：

```python3
from nicegui import ui

def index():
    for i in range(4):
        ui.button(i)

ui.run(root=index,native=True)
```

![2026_3_5](nicegui_pro.assets/2026_3_5.png)

看上去没什么问题，可是，一旦涉及到可调用对象，这个操作就会出现问题：

```python3
from nicegui import ui

def index():
    for i in range(4):
        ui.button(i,on_click=lambda :ui.notify(i))

ui.run(root=index,native=True)
```

![2026_3_6](nicegui_pro.assets/2026_3_6.png)

在创建控件的同时，给控件设置了对应的响应函数，让其在点击时，弹出对应数字的消息。不过，代码看似没有问题，点击第三个按钮时，却弹出来不一致的数字。

请读者不要着急寻找解决代码，在解决问题之前，需要先了解一下问题产生的原因：问题源于Python的延迟绑定。

简单来说，在遍历时定义函数（不限于lambda表达式）的话，如果函数直接使用遍历中间变量（即代码中的`i`），则该变量会在遍历结束时统一绑定，而非第一时间使用变量的当时值，这是函数的特性。

函数的这一特性其实在前面介绍构建模式的时候说过，就是在函数中可以使用在当前代码位置后定义的函数、对象，不会直接报错。

因此，将出错的代码中，NiceGUI的部分去掉的话，复现错误的核心代码为：

```python3
funcs = []

for i in range(4):
    funcs.append(lambda:print(i))

for func in funcs:
    func()
```

结果如下：

```shell
3
3
3
3
```

想要解决这个问题也很简单，就是让定义函数时使用该变量的值，而非该变量（为了避免混淆，lambda表达式的参数名改为`x`）：

```python3
funcs = []

for i in range(4):
    funcs.append(lambda x=i:print(x))

for func in funcs:
    func()
```

结果如下：

```shell
0
1
2
3
```

这一次，结果总算对了。

接下来，回到NiceGUI程序，执行类似的修改即可：

```python3
from nicegui import ui

def index():
    for i in range(4):
        ui.button(i,on_click=lambda x=i:ui.notify(x))

ui.run(root=index,native=True)
```

## 4 控件的样式（更新中）

NiceGUI提供了丰富美观的控件，但控件默认的样式是统一的，实际使用时总不能全用默认样式，肯定要美化一番。因此，如何修改控件的样式，值得读者认真学习。

### 4.1 支持的样式

在学习修改控件的样式之前，先了解一下NiceGUI的控件支持哪些样式：

- CSS
- TailWindCSS
- Quasar



### 4.2 `style`方法（属性）



三种有关样式的方法（控件属性）



### 4.3 `classes`方法（属性）



### 4.4 `props`方法（属性）





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





对话框背景模糊：

```python3
from nicegui import ui

with ui.dialog().props('backdrop-filter="blur(8px) brightness(40%)"') as dialog:
    ui.label('Press ESC to close').classes('text-3xl text-white')

dialog.on('show', lambda: ui.notify('Dialog opened'))
dialog.on('hide', lambda: ui.notify('Dialog closed'))
dialog.on('escape-key', lambda: ui.notify('ESC pressed'))
ui.button('Open', on_click=dialog.open)

ui.run()
```



