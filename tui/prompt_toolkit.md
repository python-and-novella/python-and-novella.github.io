# prompt_toolkit的中文入门教程

## 0 前言

[prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/en/stable/)是一个终端UI框架，可以交互式获取命令行输入内容、创建对话框、构建终端全屏程序、显示进度条等。用法简单高效，很适合搭建类似终端开发环境这种支持自动提示的交互式操作程序。官方文档虽然条理清晰，但内容不多也比较简单。因此，本教程将在官方文档的基础上，按照常规的入门学习顺序重新排序，并添加缺失的相关知识，梳理实际开发中可能遇到的问题，制作中文入门教程。

## 1 简单开始

### 1.1 环境准备

准备工作很简单，初始化虚拟环境之后，添加`prompt-toolkit`即可，环境管理根据使用uv、pdm均可。

不过，prompt_toolkit使用了一些没有明显依赖的第三方库，为了避免后续学习过程中需要临时添加，建议这里提前添加：

- `pygments`，一些语法高亮相关的美化样式功能依赖此库，实现语法高亮。
- `asyncssh`，在SSH服务器上运行prompt_toolkit程序的社区功能依赖此库，进行相关SSH操作。

### 1.2 Hello World

和所有框架、语言开始学习的惯例一样，先看看prompt_toolkit（后面会简称为框架）的Hello World程序是什么样：

```python3
from prompt_toolkit import prompt

text = prompt('请输入任何内容：')
print(f'输入的内容是: {text}')
```

![hello_world_1](prompt_toolkit.assets/hello_world_1.png)

框架支持很多终端交互，这里演示的是获取用户输入的过程，因此，程序最终输出的是用户输入的内容。

## 2 基础知识（响应式）

本章主要依照官网基础部分，并适当调整部分内容的难易程度、结构，增加了简洁易懂的示例代码。涉及到类、方法的具体参数的含义和用途，可以参考后面章节中模块API的详细介绍。

### 2.1 输出

作为一个终端UI框架，输出内容是框架的主要功能。不同于Python内置的输出方法只是原样输出，框架能让输出内容的方式更简单、漂亮。

本节内容原文参考 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/printing_text.html 。

#### 2.1.1 输出方法

就和Python内置的`print`方法一样，框架也提供了在终端输出内容的方法——`print_formatted_text`（使用`from prompt_toolkit.shortcuts.utils import print_formatted_text`或者`from prompt_toolkit.shortcuts import print_formatted_text`或者`from prompt_toolkit import print_formatted_text`导入）。

示例如下：

```python3
from prompt_toolkit.shortcuts import print_formatted_text

# from prompt_toolkit import print_formatted_text

print_formatted_text('Hello world')
```

![print_1](prompt_toolkit.assets/print_1.png)

`print_formatted_text`方法支持以下参数：

- `*value`参数，任意类型，表示要输出到终端的内容。对于支持渲染为带格式文本的对象（下一节会介绍），会输出其渲染结果。支持传入多个符合要求的值或者解包可迭代对象。

- `sep`参数，字符串类型，表示传入多个内容时，每个内容之间的分隔符，默认为`' '`。从此参数开始，只能使用关键字传入。

- `end`参数，字符串类型，表示输出所有内容之后，末尾添加的额外字符串，默认为`'\n'`。

- `file`参数，文件类型（实际上是文本输入输出流`TextIO`），表示输出内容写入到哪个文件，默认为`None`。

- `flush`参数，布尔类型，表示是否立即显示输出，默认为`False`，即等待缓冲区填满之后之后才输出。

- `style`参数，`Style`类型，表示输出内容的样式（样式的用法下节介绍，这里暂不展开）.

- `output`参数，`Output`类型，表示内容输出到哪个IO流（需要实现`Output`抽象类）。

- `color_depth`参数，`ColorDepth`类型，表示输出内容的颜色深度，默认为`output`参数的`get_default_color_depth`方法的返回值。

- `style_transformation`参数，`StyleTransformation`类型，表示输出时如何转换样式。以下为示例：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.styles.style_transformation import ReverseStyleTransformation
  
  print_formatted_text(
      'Hello world',
      style_transformation=ReverseStyleTransformation()
  )
  ```

  ![print_3](prompt_toolkit.assets/print_3.png)

- `include_default_pygments_style`参数，布尔类型，表示输出语法标志对象时，是否启用语法标志对象本身的样式，默认为`True`。

不过，只是输出纯文本的话，那`print_formatted_text`方法就属于重复造轮子了。使用`print_formatted_text`方法，当然是为了输出带格式的文本：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

print_formatted_text(
    FormattedText(
        [
            ('red','Hello world')
        ]
    )
)
```

![print_2](prompt_toolkit.assets/print_2.png)

#### 2.1.2 带格式的文本

`print_formatted_text`方法支持将以下对象渲染为带格式的文本：

- `HTML`对象（使用`from prompt_toolkit.formatted_text import HTML`导入），该对象接收HTML类似格式的字符串，可以将`bold`（短名`b`）、`italic`（短名`i`）、`underline`（短名`u`）、`strike`（短名`s`）、`blink`、`reverse`、`hidden`等标签包含的文本渲染成对应格式（对应关系参见后面样式章节的介绍）的文本。示例如下：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.formatted_text import HTML
  
  print_formatted_text(
      HTML('<u>hello</u>'),
  )
  ```

  ![formated_text_1](prompt_toolkit.assets/formated_text_1.png)

  除了表示格式的标签，对于表示颜色的颜色名字（支持的颜色名字参见后面样式章节的介绍）作为标签，还支持将其包含的文本渲染成对应颜色的文本。示例如下：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.formatted_text import HTML
  
  print_formatted_text(
      HTML('<red>hello</red>'),
  )
  ```

  ![formated_text_2](prompt_toolkit.assets/formated_text_2.png)

  如果想要同时设置颜色和格式，可以嵌套使用标签。示例如下：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.formatted_text import HTML
  
  print_formatted_text(
      HTML('<red><u>hello</u></red>'),
  )
  ```

  ![formated_text_3](prompt_toolkit.assets/formated_text_3.png)

  除了这种通过嵌套标签的方式同时设置颜色和格式，还可以设置标签的`fg`属性（前景色）`color`属性为颜色（支持颜色名字和量化表达，，同样可以实现同时设置颜色和格式。示例如下：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.formatted_text import HTML
  
  print_formatted_text(
      HTML('<u fg="red">hello</u>'), 
      # 或者 HTML('<u color="red">hello</u>'),
  )
  ```

  ![formated_text_3](prompt_toolkit.assets/formated_text_3.png)

  当然，背景颜色也可以通过这种方式设置——设置标签的`bg`属性：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.formatted_text import HTML
  
  print_formatted_text(
      HTML('<u fg="red" bg="white">hello</u>'),
  )
  ```

  ![formated_text_4](prompt_toolkit.assets/formated_text_4.png)

  如果只是设置内容的前景色、背景色，不想设置格式，则可以使用`style`标签：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.formatted_text import HTML
  
  print_formatted_text(
      HTML('<style fg="red" bg="white">hello</style>'),
  )
  ```

  ![formated_text_4](prompt_toolkit.assets/formated_text_4.png)

  对于非保留名字（格式名、颜色名、`style`、`#document`、`html-root`为保留名字）的标签，`print_formatted_text`方法会将其映射为样式类的名字，给`print_formatted_text`方法的`style`参数传入样式类对象（具体用法参见后面样式章节的介绍），这些标签包含的文本会被渲染为样式类对应的样式：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.formatted_text import HTML
  from prompt_toolkit.styles import Style
  
  # 基于字典创建样式对象
  style = Style.from_dict({
      'a': 'red underline',
  })
  
  print_formatted_text(
      HTML('<a>hello</a>'),
      style=style
  )
  
  # 直接创建样式对象
  style = Style([
      ('b','green italic')
  ])
  
  print_formatted_text(
      HTML('<b>hello</b>'),
      style=style
  )
  ```

  ![formated_text_5](prompt_toolkit.assets/formated_text_5.png)

  需要注意的是，`HTML`对象要求字符串中的HTML标签层级严格配对，不支持自动闭合标签（不支持`'</>'`），且不能使用复合标签（不支持`'<red u>...</red u>'`），也不能错位嵌套标签（不支持`<red><u>...</red></u>`）。

- `ANSI`对象（使用`from prompt_toolkit.formatted_text import ANSI`导入），ANSI终端转义码

- 带格式的文本对象（使用`from prompt_toolkit.formatted_text import FormattedText`导入），

- 语法标志对象（使用`from prompt_toolkit.formatted_text import PygmentsTokens`导入），







#### 2.1.3 样式

##### 2.1.3.1 颜色





样式语法参考自 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/advanced_topics/styling.html 。

3.1.1 基础语法

在应用样式之前，需要先了解一下样式的基础语法。

描述样式的字符串被称之为样式字符串。在样式字符串中，以空格为间隔，每个分段描述一个基础样式，共同组成单个样式字符串，最终用于美化要修饰的内容。

样式字符串支持以下基础样式：

- 直接表示颜色或者有'fg:'前缀的颜色表达式，表示内容的前景色（也称之为字体颜色）。

  其中，颜色支持以下格式：

  - 颜色的名字，如`'red'`。可以使用`from prompt_toolkit.styles import NAMED_COLORS,ANSI_COLOR_NAMES,ANSI_COLOR_NAMES_ALIASES`导入相关字典或者列表，查询支持的颜色名。其中，`ANSI_COLOR_NAMES`和`ANSI_COLOR_NAMES_ALIASES`包含的是ANSI颜色。
  - '#'为前缀，后接6位十六进制数字，每两位数字代表一种颜色分量值（依次对应红色、绿色、蓝色的分量值）的RGB颜色标准表达方式，如`'#cc5454'`。

- 有'bg:'前缀的颜色表达式，表示内容的背景色。

- 内容格式，有：

  - `'bold'`，表示内容字体将变为粗体。
  - `'italic'`，表示内容字体将变为斜体。
  - `'underline'`，表示内容将添加下划线。
  - `'strike'`，表示内容将添加删除线。
  - `'blink'`，表示内容将闪烁（仅部分终端支持，Windows自带终端不支持）。
  - `'reverse'`，表示内容的背景色与前景色相反。
  - `'hidden'`，表示内容隐藏。

  给以上内容格式添加'no'前缀，则表示内容不使用上述样式，常用于组合基础样式与样式类时，撤销不需要的内容格式。



### 2.2 输入

https://python-prompt-toolkit.readthedocs.io/en/stable/pages/asking_for_input.html



### 2.3 对话框



### 2.4 进度条



## 3 应用程序的基础知识

除了前面直接执行、直接输出的使用方式之外，框架还支持一种类似应用程序的使用方式。在正式介绍之前，需要先区分一下框架程序的两种使用方式：

- 响应式。即前面的示例程序那种方式，执行框架提供的功能后，终端会立刻响应，输出或者输入内容，执行完成后，后面的代码正常执行。

- 应用式。这种方式则和响应式的立即响应不同，需要提前定义`Application`实例，包括布局、样式、内容、事件响应等，最后执行实例的`run`方法进入事件循环，就和GUI、Web程序常用的使用方式一样。以下为框架程序的应用式示例：

  ```python3
  from prompt_toolkit import Application
  
  app = Application()
  
  app.run()
  ```

  当然，这是一个最简单、仅用于表示框架程序应用式结构的示例，没有具体内容，也不能正常退出（因为没有设置布局，程序会提示按任意键退出）。

  为了让应用式程框架程序具备基本的交互功能，以下示例对上一个示例进行了补充，添加了一些后面的知识，读者可以提前了解一下，这里暂不具体介绍：

  ```python3
  from prompt_toolkit import Application
  from prompt_toolkit.layout import Layout
  from prompt_toolkit.widgets import Button
  
  app = Application(
      full_screen=True,
      mouse_support=True,
  )
  
  app.layout = Layout(
      Button(
          'close app',
          app.exit
      )
  )
  
  app.run()
  ```

  ![app_1](prompt_toolkit.assets/app_1.gif)

响应式适合嵌入其他框架编写的程序中，用于在终端中与用户交互，一般不会破坏其他框架的功能。

应用式则适合使用框架编写TUI程序，构建程序的主要界面，接管终端大部分的交互功能；使用其他框架时，只能使用不破坏事件循环、界面显示的功能（通常不输出内容，在单独的协程、线程、进程中执行）。

本章将介绍应用式框架程序所涉及的基础知识。涉及到类、方法的具体参数的含义和用途，可以参考后面章节中模块API的详细介绍。

### 3.1 基本结构

正如本章开头所介绍的那样，一个完整的应用式框架程序通常由以下几部分组成：

- 



样式（对齐、内边距、外边距在布局中，边框在部件中），布局（各类容器），控件、部件，定时器，后台任务，



已知知识点如下：

- 两种使用方式：响应式（直接输出），应用式（进入应用的消息循环）
- print_formatted_text可以渲染带格式的文本对象，也可以当做普通的print方法使用（但print方法不支持渲染带格式的文本对象）：https://python-prompt-toolkit.readthedocs.io/en/stable/pages/printing_text.html
- 在终端输出、获取输入，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/asking_for_input.html
- 对话框，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/dialogs.html
- 进度条，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/progress_bars.html
- 全屏应用，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/full_screen_apps.html





扩展知识点：

- 样式的语法，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/advanced_topics/styling.html
- 快捷键，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/advanced_topics/key_bindings.html
- 后台运行任务，非线程安全（https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#prompt_toolkit.application.Application.create_background_task）
- 异步事件循环，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/advanced_topics/asyncio.html
- 定时器，https://github.com/prompt-toolkit/python-prompt-toolkit/blob/main/examples/prompts/clock-input.py







## 4 进阶知识

本章将对照 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/advanced_topics/index.html 中除了基础知识介绍过内容外的其余内容，并补充一些官方手册中有但官方教程没写的内容，然后适当调整顺序，使其更有条理。







只提供widgets？layout和其他controls是否划归本章节，还是在基础里学习？



（这部分需要查看手册和官方示例，挖掘API中widgets提供的组件）





## 5 具体实例（随时更新）

本章主要根据实际问题，提供对应问题的解决实例





API文档目录（仅做参考，写完删除）

框架的API文档很全面，提供的功能也很多，但并非所有的功能都有对应的教程和示例。为了方便读者理解框架的各个模块，本节先简单总结一下API手册各个部分对应哪一类功能，后面在详细解释这一部分（模块）具体功能的参数。

API文档目录如下：

- 应用程序部分，对应`application`模块，这一部分主要为应用式框架程序中`Application`对象相关的类和功能。

  原文为 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.application 。

- 带格式的文本部分，

  原文为 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.formatted_text 。

- 缓冲，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.buffer

- 选择，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.selection

- 剪贴板，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.clipboard

- 自动补全，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.completion

- 文档对象，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.document

- 枚举变量，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.enums

- 历史记录，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.history

- 按键对象，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.keys

- 样式对象，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.styles

- 快捷功能（内部实现，直接可用的组件、功能、控件、方法、类等），https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.shortcuts

- 验证模块，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.validation

- 自动建议（有点像自动补全，需要写一下区别），https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.auto_suggest

- 渲染对象，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.renderer

- 语法高亮方案，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.lexers

- 布局，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.layout

- 容器，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#containers

- 控件，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#controls

- 其他（无法准确归类的杂项），https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#other

- 组件（部件），https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.widgets

- 过滤器，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.filters

- 按键绑定，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.key_binding

- 事件循环，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.eventloop

- 输入，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.input

- 输出，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.output

- 数据结构，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#data-structures

- 标准输出的补丁，https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#module-prompt_toolkit.patch_stdout

