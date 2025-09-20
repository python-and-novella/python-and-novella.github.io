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
  
  看起来有点复杂，但如果读者细心观察的话，就会发现，这段看似复杂的代码，其实就是一个装饰器：
  
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

## 4 修改样式

NiceGUI提供了丰富美观的控件，但控件默认的样式是统一的，实际使用时总不能全用默认样式，肯定要美化一番。因此，如何修改控件的样式，值得读者认真学习。

### 4.1 修改样式的方法

在学习修改控件的样式之前，先了解一下NiceGUI的控件支持哪些修改样式的方法：

- `style`方法（属性），支持CSS，可以直接设置具体的Web样式，比如颜色、边距等。CSS的语法可参考 https://developer.mozilla.org/zh-CN/docs/Web/CSS。
- `classes`方法（属性），支持tailwindcss，可以设置tailwindcss框架定义的CSS变量，让控件应用这些变量对应的CSS样式。tailwindcss的语法可参考 https://tailwindcss.com/。
- `props`方法（属性），支持Quasar控件的属性，可以设置对应Quasar控件的属性，包括但不限于样式相关的属性。具体控件支持的属性可参考 https://quasar.dev/components。

可能读者看到上面的介绍有点疑惑，为何这些方法后，还用括号补充说明是属性？在NiceGUI最新版本中，这三种方法，可以通过调用的方式添加、修改样式。同时，控件还支持同名的字典（或者列表）属性，可以使用字典（或者列表支持的方式添加、修改样式，字典的键即为样式名。

### 4.2 `style`方法（属性）

示例如下：

```python3
from nicegui import ui

def index():
    button = ui.button('Hello')
    button.style('color:red!important')
    button.style['background'] = 'green!important'

ui.run(root=index,native=True)
```

![2026_4_1](nicegui_pro.assets/2026_4_1.png)

需要注意的是，默认控件的样式优先级较高，需要通过添加`!important`来提高自定义样式的优先级，否则不会生效。

部分样式支持使用`props`方法（属性）去掉，比如控件的背景色、前景色（文字颜色）。此时不用添加`!important`来提高自定义样式的优先级：

```python3
from nicegui import ui

def index():
    button = ui.button('Hello')
    button.props('color text-color')
    button.style('color:red')
    button.style['background'] = 'green'

ui.run(root=index,native=True)
```

![2026_4_1](nicegui_pro.assets/2026_4_1.png)

### 4.3 `classes`方法（属性）

示例如下：

```python3
from nicegui import ui

def index():
    label = ui.label('Hello')
    label.classes('bg-yellow-400')
    label.classes.append('text-blue-600')

ui.run(root=index,native=True)
```

![2026_4_2](nicegui_pro.assets/2026_4_2.png)

`classes`属性是一个列表，因此只能使用列表的方法。

NiceGUI的很多控件自带样式，其样式源于Quasar框架，而部分样式使用`!important`修饰，优先级高于没有使用`!important`修饰的普通样式。

虽然tailwindcss的普通样式默认优先级高于Quasar框架的普通样式，但添加“!”为前缀或者后缀（在tailwindcss中等效于使用`!important`修饰）的tailwindcss样式，遇到Quasar框架使用`!important`修饰的相同样式（比如背景颜色）时，优先级反而会比Quasar框架的低。

想要理解这个反常现象，需要先了解两个相关知识：

- 从NiceGUI 3.0.0开始，内部使用了级联层（@layer）决定样式的优先级，具体顺序如下：

  ```css
  theme, 
  base, 
  quasar(Quasar框架的预定义样式类类名在这一层), 
  nicegui, 
  components, 
  utilities(tailwindcss框架的预定义样式类类名在这一层), 
  overrides
  ```

  对于普通样式，越靠下的层级，优先级越高。

- 对于同样使用`!important`修饰的相同样式，则基于上面的级联层顺序，优先级则是相反的，具体可以参考 https://developer.mozilla.org/en-US/docs/Web/CSS/@layer#layer_order_and_the_!important_flag，完整的优先级顺序如下图所示：

  ![2026_4_3](nicegui_pro.assets/2026_4_3.png)

那么，问题来了，默认控件的颜色样式就是使用`!important`修饰的，如果想要将其改为tailwindcss的颜色，怎么解决？

可以使用`props`方法（属性）去掉控件原本的背景色、前景色（文字颜色），再使用`classes`方法（属性）修改为指定的背景色、前景色（文字颜色），此时不用添加“!”为前缀或者后缀：

```python3
from nicegui import ui

def index():
    button = ui.button('Hello')
    button.props('color text-color')
    button.classes('bg-red-700 text-green-700')

ui.run(root=index,native=True)
```

![2026_4_4](nicegui_pro.assets/2026_4_4.png)

### 4.4 `props`方法（属性）

示例如下：

```python3
from nicegui import ui

def index():
    button = ui.button('Hello')
    button.props('text-color=green')
    button.props['color'] = 'red'

ui.run(root=index,native=True)
```

![2026_4_5](nicegui_pro.assets/2026_4_5.png)

需要注意的是，Quasar控件的属性有两种类型，布尔类型和其他类型。如果是布尔类型的属性，可以不用赋值，添加该属性相当于给该属性赋值为`True`。

## 5 创建事件的响应函数

NiceGUI中，如果用户执行了动作（比如点击），会产生相应的事件，控件就会执行对应事件的响应函数。因此，想要根据用户的动作执行对应的函数，只需定义事件对应的响应函数即可。

### 5.1 响应控件的事件

 对于控件而言，定义事件的响应函数有三种方式：

- “on”开头的参数。比如`ui.button`按钮控件的`on_click`参数，支持可调用对象。

  示例如下：

  ```python3
  from nicegui import ui
  
  def index():
      ui.button(
          'Hello',
          on_click = lambda :ui.notify('Hello')
      )
  
  ui.run(root=index,native=True)
  ```

- “on”开头的方法。比如`ui.button`按钮控件的`on_click`方法，该方法的参数为可调用对象。

  示例如下：

  ```python3
  from nicegui import ui
  
  def index():
      ui.button(
          'Hello'
      ).on_click(
          lambda :ui.notify('Hello')
      )
  
  ui.run(root=index,native=True)
  ```

- `on`方法。效果类似“on”开头的方法，但该方法的第一个参数为事件类型，可以定义任意JavaScript中支持的事件类型。比如，`on_click`方法，效果等于`on`方法的第一个参数为`'click'`。

  示例如下：

  ```python3
  from nicegui import ui
  
  def index():
      ui.button(
          'Hello'
      ).on(
          'click',
          lambda :ui.notify('Hello')
      )
  
  ui.run(root=index,native=True)
  ```

### 5.2 响应NiceGUI程序的事件

除了可以定义控件的响应函数，NiceGUI程序也支持一些事件，可以定义这些事件的响应函数。

想要定义NiceGUI程序事件的响应函数，需要导入`app`对象，调用该对象的“on”开头的方法。比如，`on_startup`方法用于定义NiceGUI程序启动完成时的响应函数：

```python3
from nicegui import ui,app

def index():
    ui.button(
        'Hello'
    ).on(
        'click',
        lambda :ui.notify('Hello')
    )

app.on_startup(lambda :print('程序已启动……'))
ui.run(root=index,native=True)
```

### 5.3 响应信号（`Event`类）

事件类——`Event`类（使用`from nicegui import Event`导入）虽然从名字上看应该和事件、响应函数相关，但要是从用法看，该类被称作信号更合适。

信号是NiceGUI 3.0.0引入的新功能。之前版本中类似脚本模式的NiceGUI程序可以共享全局作用域内控件的状态、数据，但在NiceGUI 3.0.0版本中，脚本模式下，全局作用域内的控件相当于放在单独的函数中，无法在全局作用域中共享其状态、数据。为了解决此需求，NiceGUI新增了具备信号功能的`Event`类。

在全局作用域内创建`Event`类对象之后，可以在定义控件的响应函数时，将控件的状态、数据通过`Event`类对象的`emit`方法发射为信号，其他通过`subscribe`方法订阅信号而定义的响应函数，会在接收到信号时执行响应函数。

示例如下：

```python3
from nicegui import ui,Event

signal_obj = Event()
shared_value = ''
def update_shared_value(x):
    global shared_value
    shared_value=x

def index():
    # 订阅信号，更新全局变量，以便于新打开的页面自动使用该值作为初始值
    signal_obj.subscribe(update_shared_value)
    input = ui.input(value=shared_value)
    # 订阅信号
    signal_obj.subscribe(lambda x:input.set_value(x))
    # 发射信号
    input.on_value_change(lambda :signal_obj.emit(input.value))

ui.run(root=index,port=80)
```

在运行代码之后，可以在浏览器中打开多个标签页，地址为`http://127.0.0.1/`，在任意一个标签页中输入框内输入内容，其他标签页中输入框的内容会自动同步。

## 6 绑定属性

上一章介绍了如何同步脚本模式同一控件之间的状态、数据，但是，如果想要同步同一页面（脚本模式、页面模式）中不同控件之间、控件与任意对象属性之间的状态、数据，则不用那么复杂，控件提供了简单的属性绑定方法，可以单向或者双向绑定控件的可绑定属性、对象的属性。

如果控件存在可绑定属性，则该控件会存在以下三种相关的属性绑定方法：

- `bind_{属性名}_from`方法，将该属性与其他对象的指定属性绑定，其他对象的指定属性发生改变，该控件的该属性同步发生变化，反之不会触发同步。
- `bind_{属性名}_to`方法，将该属性与其他对象的指定属性绑定，该控件的该属性发生改变，其他对象的指定属性同步发生变化，反之不会触发同步。
- `bind_{属性名}`方法，将该属性与其他对象的指定属性绑定，发起绑定和被绑定的属性中，只要一方发生变化，另一方同步发生变化。

示例如下：

```python3
from nicegui import ui

class data_class:
    value = 'no value'

def index():
    ui.input('输入').bind_value(
        data_class,
        'value'
    )
    ui.button(
        '显示',
        on_click = lambda :ui.notify(data_class.value)
    )

ui.run(root=index,native=True)
```

## 7 创建可刷新方法

绑定属性可以单向或者双向绑定控件的可绑定属性、对象的属性，无需额外执行控件的刷新方法。比如：

```python3
from nicegui import ui

def index():
    my_label = ui.label('')
    my_input = ui.input('输入')
    my_input.bind_value(my_label,'text')  

ui.run(root=index,native=True)
```

![2026_7_1](nicegui_pro.assets/2026_7_1.png)

但是，如果“属性”不是控件的属性，而是诸如个数之类需要重新创建控件的“属性”，绑定属性就没法直接实现，需要做一些额外的事情：

```python3
from nicegui import ui

count = 2
def index():
    my_input = ui.number(
        '个数',
        value=1,
        min=1,
        max=10,
        format='%d'
    )
    e = ui.element()
    def rebuild():
        e.clear()
        with e:
            for i in range(
                int(my_input.value)
            ):
                ui.label('A')
    rebuild()
    my_input.bind_value(
        globals(),
        'count',
    )
    my_input.on_value_change(rebuild)

ui.run(root=index,native=True)
```

![2026_7_2](nicegui_pro.assets/2026_7_2.png)

字母的个数与输入框内的数字是同步了，但需要使用全局变量存储个数，还需要借助额外的控件作为容器，容器内的多个控件比较紧凑，样式还要额外调整。

其实，可以使用NiceGUI提供的`refreshable`类（用于装饰函数）、`refreshable_method`类（用于装饰类的方法）创建可刷新方法（函数），直接调用其`refresh`方法，一步实现清除创建的控件、重新创建控件：

```python3
from nicegui import ui

def index():
    my_input = ui.number(
        '个数',
        value=1,
        min=1,
        max=10,
        format='%d'
    )
    @ui.refreshable
    def rebuild():
        for i in range(int(my_input.value)):
            ui.label('A')
    my_input.on_value_change(
        rebuild.refresh
    )
    rebuild()

ui.run(root=index,native=True)
```

代码简洁不少，但效果更好：

![2026_7_3](nicegui_pro.assets/2026_7_3.png)

需要注意的是，在`refreshable`类、`refreshable_method`类装饰的函数（方法）内，所有创建的控件都会在调用`refresh`方法时重新创建，不会保存控件的状态：

```python3
from nicegui import ui

def index():
    @ui.refreshable
    def rebuild():
        my_input = ui.number(
            '个数',
            value=1,
            min=1,
            max=10,
            format='%d'
        )
        my_input.on_value_change(
            rebuild.refresh
        )
        for i in range(int(my_input.value)):
            ui.label('A')
    rebuild()

ui.run(root=index, native=True)
```

如果想要保存控件的状态，可以使用前面用过的绑定属性：

```python3
from nicegui import ui

count = 1
def index():
    @ui.refreshable
    def rebuild():
        my_input = ui.number(
            '个数',
            value=1,
            min=1,
            max=10,
            format='%d'
        )
        my_input.bind_value(
            globals(),
            'count',
        )
        my_input.on_value_change(
            rebuild.refresh
        )
        for i in range(int(my_input.value)):
            ui.label('A')
    rebuild()

ui.run(root=index, native=True)
```

也可以使用只与`refreshable`类、`refreshable_method`类配合使用的`ui.state`状态方法。

`ui.state`状态方法的参数为初始值，该方法返回一个元组。元组的第一个元素为调用`refresh`方法之后的保存值（第一次返回的是初始值），元组的第二个元素为修改保存值的赋值方法。

于是，将所有控件一股脑地塞入可刷新方法中之后，代码如下：

```python3
from nicegui import ui

def index():
    @ui.refreshable
    def rebuild():
        num,set_num = ui.state(1)
        my_input = ui.number(
            '个数',
            value=num,
            min=1,
            max=10,
            format='%d'
        )
        # 修改保存值
        my_input.on_value_change(
            lambda :set_num(my_input.value)
        )
        my_input.on_value_change(
            rebuild.refresh
        )
        for i in range(int(my_input.value)):
            ui.label('A')
    rebuild()

ui.run(root=index, native=True)
```

## 8 使用异步

在Python中，有一种函数叫异步函数。与之相对的，就是同步函数。同步函数就是常见的函数，异步函数就是在定义函数时使用`async`修饰的函数。

一般来说，函数执行之后，就会立即得到结果。但是，如果函数执行的操作比较耗时，程序就会卡住，需要等函数执行完，程序才会恢复。这个就是同步函数的执行过程。

于是，异步函数为了解决卡住程序的问题，使用异步处理要执行的耗时操作。所谓异步，就是执行之后不会立即要求得到结果，而是按照顺序继续执行后续的代码，并按照完成顺序依次得到结果。

光说的话，不太直观，那就用代码对比一下。

先看同步函数的示例：

```python3
from nicegui import ui
import time

def do_something():
    ui.notify('start')
    time.sleep(3)
    ui.notify('ok')

def index():
    ui.button('Do Something',on_click=do_something)

ui.run(root=index,native=True)
```

![2026_8_1](nicegui_pro.assets/2026_8_1.gif)

可以看到，虽然函数中，两个通知之间加入了延时，但两个通知还是同时弹出。

换成异步函数的话，结果就符合预期了：

```python3
from nicegui import ui
import asyncio

async def do_something():
    ui.notify('start')
    await asyncio.sleep(3)
    ui.notify('ok')

def index():
    ui.button('Do Something',on_click=do_something)

ui.run(root=index,native=True)
```

![2026_8_2](nicegui_pro.assets/2026_8_2.gif)

NiceGUI对异步的支持如下：

- 响应函数可以是异步函数。

- 脚本模式、页面模式、单页面应用创建页面的函数可以是异步函数。

  示例如下：

  ```python3
  from nicegui import ui
  import asyncio
  
  async def do_something():
      ui.notify('start')
      await asyncio.sleep(3)
      ui.notify('ok')
  
  async def index():
      ui.button('Do Something',on_click=do_something)
  
  ui.run(root=index,native=True)
  ```

- 部分控件、对象提供了可以异步等待的方法，用于实现在指定动作、状态之后才执行后续操作。

  比如，`ui.button`按钮控件的`clicked`方法就是一个异步函数，只有在点击按钮之后，该函数才会执行：
  
  ```python3
  from nicegui import ui
  
  async def index():
      await ui.button('Do Something One').clicked()
      await ui.button('Do Something Two').clicked()
      await ui.button('Do Something Three').clicked()
  
  ui.run(root=index,native=True)
  ```
  
  ![2026_8_3](nicegui_pro.assets/2026_8_3.gif)

## 9 创建后台任务

上一章节介绍异步的时候，可以看到直接执行包含`time.sleep`的同步函数会导致问题，但是，如果在后台任务中执行同步函数，就不会有这样问题。

NiceGUI提供了两种后台执行任务的方法，均为异步函数，由`run`模块提供：

-   `run.cpu_bound`方法，常用于占用较多CPU资源的后台任务，该方法会创建新的进程操作，让进程池的进程数扩大。
-   `run.io_bound`方法，常用于占用较多IO资源的后台任务开，因为这类后台任务不会占用太多CPU资源，因此，该方法只是创建新的线程操作，操作完线程会关闭。

示例如下：

```python3
from nicegui import ui,run
import time

def sleep():
    time.sleep(3)

async def do_something():
    ui.notify('start')
    await run.cpu_bound(sleep)
    ui.notify('ok')

def index():
    ui.button('Do Something',on_click=do_something)

ui.run(root=index,native=True)
```

![2026_8_2](nicegui_pro.assets/2026_8_2.gif)

可以看到，虽然执行的是包含`time.sleep`的同步函数，但因为将其放在后台任务中执行，所以，结果符合预期。

## 10 使用定时器

上一章讲了在后台任务中执行函数，这一章说一下效果有点类似，但是常用于重复执行函数的定时器。

NiceGUI提供了两种定时器：

- `ui.timer`定时器，控件层级的定时器。
- `app.timer`定时器，程序层级的定时器。

`ui.timer`定时器和`app.timer`定时器基本用法相同，但使用场景有所差别。

先看基本用法：

```python3
from nicegui import ui

def index():
    button = ui.button('Do Something')
    def do_something():
        button.disable()
        ui.timer(3,lambda :ui.notify('ok'))
    button.on_click(do_something)

ui.run(root=index,native=True)
```

点击按钮之后，响应函数先禁用按钮，防止重复点击。然后创建一个定时器，每隔三秒弹出一条通知。

如果是`app.timer`定时器，则不能使用这种创建控件的操作：

```python3
from nicegui import ui,app

def index():
    button = ui.button('Do Something')
    def do_something():
        button.disable()
        app.timer(3,lambda :print('ok'))
    button.on_click(do_something)

ui.run(root=index,native=True)
```

除此以外，两种定时器还有一个区别：控件的响应函数创建了`ui.timer`定时器，那`ui.timer`定时器就属于这个控件的父控件（或者创建定时器位置所属上下文的控件）；一旦父控件清空所有子控件，`ui.timer`定时器也会随之清除。而`app.timer`定时器属于当前程序，不会因为这样的操作而被清除掉。

示例如下：

```python3
from nicegui import ui,app

def index():
    with ui.element() as element:
        ui.timer(3,lambda :print('ui is ok'))
        app.timer(3,lambda :print('app is ok'))
    ui.button('Clear Timers',on_click=element.clear)

ui.run(root=index,native=True)
```

点击按钮之后，终端只会输出`app is ok`，因为`app.timer`定时器属于当前程序，不受影响。

## 11 绑定快捷键（更新中）

`ui.keyboard`







## 12 使用环境变量

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

## 13 使用`ui.button`按钮控件（更新中）

具体控件的基础用法免费发布，高级用法和特定问题的解决付费，最低1豆，最多9豆





## 4 使用`ui.button`按钮控件（更新中）

具体控件的基础用法免费发布，高级用法和特定问题的解决付费，最低1豆，最多9豆



## 4 自定义控件





## 5 管理网页相关文件

ui.add\_\* 和app.add\_\*





## 5 修改指定控件

先说控件的`move`方法可以移动控件的位置，



再说

ui.query

ui.teleport

ElementFilter







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



## x 单页面应用的扩展内容

`ui.sub_pages`的`add`方法，

不同的404情况：



（根据本教程前面的概念定义需修改下面对应的概念名词，核实最新版本对应示例代码的执行情况是否相同）



访问不存在的地址，情况根据是否为单页面应用、是否为NiceGUI脚本而有所不同。

非单页面应用的NiceGUI脚本不再显示404页面。因为新版本自动捕获子路由，访问不存在的地址，依然显示首页的内容。

比如，下面的示例不显示404页面：

```python3
from nicegui import ui

ui.link('到其他页面（不存在）', '/other')

ui.run(port=80)
```

单页面应用的NiceGUI脚本，情况会有点复杂：

```python3
from nicegui import ui

def index():
    ui.link('到其他页面（不存在）', '/other')
    ui.separator()
    ui.sub_pages({'/': main, '/page1': page1})

def main():
    ui.label('/（子页面）的内容')
    ui.link('去page1（子页面）', '/page1')

def page1():
    ui.label('page1（子页面）的内容')
    ui.link('回到/（子页面）', '/')

ui.run(root=index,port=80)
```

结果如下表所示：

| 当前地址             | 访问不存在的地址后           | 页面内容          | 刷新后内容      |
| -------------------- | ---------------------------- | ----------------- | --------------- |
| 根路由`/`            | 地址变为不存在的地址`/other` | 子页面显示404提示 | 页面显示500页面 |
| 子路由`/page1`       | 地址不变                     | 子页面显示404提示 | 子页面          |
| 不存在的地址`/other` | 无                           | 页面显示500页面   | 页面显示500页面 |

如果不是NiceGUI脚本，所有页面都是使用`ui.page`定义的私有页面，则正常显示404页面，也可以自定义404页面。

比如，下面的示例正常显示404页面：

```python3
from nicegui import ui

@ui.page('/')
def _():
    ui.link('到其他页面（不存在）', '/other')

ui.run(port=80)
```

还可以自定义404页面：

```python3
from nicegui import ui

@ui.page('/')
def _():
    ui.link('到其他页面（不存在）', '/other')

# 自定义HTTP报错的响应页面
from nicegui import app,Client
from fastapi import Request

@app.exception_handler(404)
def exception_handler_404(request:Request, exception: Exception):
    from urllib.parse import urlparse
    with Client(ui.page(''),request=request) as client:
        ui.label(f'页面 {urlparse(str(request.url)).path[1:]} 不存在').classes('')
    return client.build_response(request, 404)

ui.run(port=80)
```

注意，自定义404页面**不支持**NiceGUI脚本，强行使用会导致NiceGUI脚本的自动捕获子路由无法正常使用。

若是单页面应用，情况会有点复杂：

```python3
from nicegui import ui

@ui.page('/')
@ui.page('/{_:path}')  # 不使用这个的话，刷新子路由时会变成对应的普通页面
def _():
    ui.link('到其他页面（不存在）', '/other')
    ui.separator()
    ui.sub_pages({'/': main, '/page1': page1})

def main():
    ui.label('/（子页面）的内容')
    ui.link('去page1（子页面）', '/page1')

def page1():
    ui.label('page1（子页面）的内容')
    ui.link('回到/（子页面）', '/')

ui.run(port=80)
```

结果如下表所示：

| 当前地址             | 访问不存在的地址后           | 页面内容          | 刷新后内容      |
| -------------------- | ---------------------------- | ----------------- | --------------- |
| 根路由`/`            | 地址变为不存在的地址`/other` | 子页面显示404提示 | 页面显示404页面 |
| 子路由`/page1`       | 地址变为不存在的地址`/other` | 子页面显示404提示 | 页面显示404页面 |
| 不存在的地址`/other` | 无                           | 页面显示404页面   | 页面显示404页面 |





## x 绑定属性的扩展内容

### x.1 通用绑定方法

通用的绑定方法：

```python3
from nicegui.binding import bind_from,bind_to,bind
```



示例如下：

```python3
from nicegui import ui
from nicegui.binding import bind

class data_class:
    value = 'no value'

class data_class2:
    value = 'no value'

def index():
    my_input = ui.input('输入')
    bind(
        my_input,
        'value',
        data_class,
        'value'
    )
    bind(
        data_class,
        'value',
        data_class2,
        'value'
    )
    ui.button(
        '显示',
        on_click = lambda :ui.notify(data_class2.value)
    )

ui.run(root=index,native=True)
```





介绍绑定的技巧，字典、全局变量、性能优化

与字典绑定：

```python3
from nicegui import ui

data_dict = {'value':'no value'}

def index():
    ui.input('输入').bind_value(
        data_dict,
        'value'
    )
    ui.button(
        '显示',
        on_click = lambda :ui.notify(data_dict['value'])
    )

ui.run(root=index,native=True)
```

与全局变量绑定：

```python3
from nicegui import ui

value = 'no value'

def index():
    ui.input('输入').bind_value(
        globals(),
        'value'
    )
    ui.button(
        '显示',
        on_click = lambda :ui.notify(globals()['value'])
    )

ui.run(root=index,native=True)
```



（下面内容需要优化表达与示例）

在NiceGUI中有两种类型的绑定：

1.   "Bindable properties" （可绑定属性）会自动检测写入访问并触发值变动传播。大多数 NiceGUI 元素使用这种可绑定属性，例如`ui.input`的`value`或 `ui.label`的`text`。基本上所有带有`bind()`方法的属性都支持这种类型的绑定。
2.   另一种绑定"active links"（活动链接）不会自动检测写入访问并触发值变动传播。如果将标签文本绑定到字典或自定义数据模型的属性，NiceGUI 的绑定模块则需要主动检查值是否发生变化。这个主动检查是通过每 0.1 秒运行一次`refresh_loop()`来完成。主动检查间隔可以通过设置`ui.run()`的参数`binding_refresh_interval`来修改。

可绑定属性非常高效，只要值不变，就不会产生任何性能开销（相对而言比较小而已）。但活动链接需要每秒检查所有绑定值10 次。这可能会消耗比较多的性能，尤其是活动链接的绑定关系非常复杂、非常多的时候。

因为不能让主线程阻塞太久，所以如果太多主动检查导致运行`refresh_loop()`的耗时过长，程序会发出警告。当然，可以配置阈值`binding.MAX_PROPAGATION_TIME`（默认为 0.01 秒）来消除警告。但是，这个警告是有意义的，是在告诉开发者性能可能存在问题。比如，CPU在更新绑定花费太长时间的话，主线程就没法做别的事情，程序界面会因此卡住。

为了避免性能出问题，需要将活动链接改为可绑定属性之间的绑定，需要使用`binding.BindableProperty()`来创建可绑定属性。于是，基于第一小节的代码，将字典改为数据类，在数据类中定义两个可绑定属性，控件的绑定改为与数据类对象的绑定。代码如下：

```python3
from nicegui import ui, binding

class data_base:
    name = binding.BindableProperty()
    age = binding.BindableProperty()
    def __init__(self) -> None:
        self.name = 'Bob'
        self.age = 17

data =data_base()

ui.label().bind_text_from(data, 'name', backward=lambda n: f'Name: {n}')
ui.label().bind_text_from(data, 'age', backward=lambda a: f'Age: {a}')

ui.input(label='name:').bind_value(data,'name')
ui.number(label='age:').bind_value(data,'age',forward=lambda x:int(x))

ui.run(native=True)
```

因为代码中的绑定数量很少，因此差异不大，如果将绑定数量放大百倍，就能看出两种绑定的性能差异。





## x `Event`类的用法



（简单说一下类、方法的用途，提供一下NiceGUI框架和Quasar框架（如果有的话）那边的文档地址，写个简单的示例，可以按照实际情况配上说明性图片或者效果图片）



该类支持以下参数：



该类支持以下属性：



该类支持以下方法：





## x `ui.button`按钮控件的用法



（简单说一下控件的用途，提供一下NiceGUI框架和Quasar框架那边的文档地址，写个简单的示例，配上图片）



控件支持以下参数：



控件支持以下属性：



控件支持以下方法：



## x 创作要点

前面系统性介绍基础知识和相关概念，并附上简单的示例，免费发布。

后面针对相关方法、类的具体参数和用法收费发布，内容详细，至少一千字，收费1豆起，最多9豆。

后面具体问题的分析、解决代码大部分收费，少部分免费发布，用于维持热度。
