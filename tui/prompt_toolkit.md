# prompt_toolkit的中文入门教程

[toc]

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

框架支持很多终端交互，这里演示的是运行响应式代码，获取用户输入的过程，此外，框架还可以使用响应式代码（实际上是应用式）生成对话框：

```python3
from prompt_toolkit.shortcuts import message_dialog

message_dialog(
    title='退出',
    text='按下回车或者点击确认按钮退出程序',
    ok_text='确认'
).run()
```

![hello_world_2](prompt_toolkit.assets/hello_world_2.png)

甚至可以自由定义布局、内容，运行应用式代码生成一个全屏的TUI程序：

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

- `HTML`对象（使用`from prompt_toolkit.formatted_text import HTML`或者`from prompt_toolkit import HTML`导入，完整用法参考 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#prompt_toolkit.formatted_text.HTML ），该对象接收HTML类似格式的字符串，可以将`bold`（短名`b`）、`italic`（短名`i`）、`underline`（短名`u`）、`strike`（短名`s`）、`blink`、`reverse`、`hidden`等标签包含的文本渲染成对应格式（对应关系参见后面样式章节的介绍）的文本。示例如下：

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

  需要注意的是，`HTML`对象要求字符串中的HTML标签层级严格配对，不支持自动闭合标签（不支持`'</>'`），且不能使用复合标签（不支持`'<red u>...</red u>'`），也不能错位嵌套标签（不支持`'<red><u>...</red></u>'`）。

- `ANSI`对象（使用`from prompt_toolkit.formatted_text import ANSI`或者`from prompt_toolkit import ANSI`导入，完整用法参考 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#prompt_toolkit.formatted_text.ANSI ），该对象接收包含ANSI终端转义码的字符串。示例如下：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.formatted_text import ANSI
  
  print_formatted_text(
      ANSI('\x1b[31mhello\x1b[32m')
  )
  ```

  ![formated_text_6](prompt_toolkit.assets/formated_text_6.png)

- `FormattedText`对象（使用`from prompt_toolkit.formatted_text import FormattedText`导入，完整用法参考 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#prompt_toolkit.formatted_text.FormattedText ），`HTML`对象和`ANSI`对象实际上在框架内部被映射为`FormattedText`对象的参数，最后渲染的是`FormattedText`对象。因此，直接使用`FormattedText`对象也可以：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.formatted_text import FormattedText
  
  print_formatted_text(
      FormattedText(
          [
              ('red underline','hello'),
          ]
      )
  )
  ```

  ![formated_text_3](prompt_toolkit.assets/formated_text_3.png)

  `FormattedText`对象的参数比较特别，是元素为元组的可迭代对象，元组的第一个元素为样式字符串（具体语法参见后面样式章节的介绍），元组的第二个元素为原始文本，二者结合，即表示文本的渲染结果。

  除了使用样式字符串，还可以使用样式类，给`print_formatted_text`方法的`style`参数传入样式类对象（具体用法参见后面样式章节的介绍），在样式字符串中使用`'class:{样式类}'`，文本就会被渲染为样式类对应的样式：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.formatted_text import FormattedText
  from prompt_toolkit.styles import Style
  
  # 基于字典创建样式对象
  style = Style.from_dict(
      {
          'a': 'red underline',
  	}
  )
  
  print_formatted_text(
      FormattedText(
          [
              ('class:a','hello'),
          ]
      ),
      style=style
  )
  
  # 直接创建样式对象
  style = Style(
      [
      	('b','green italic')
  	]
  )
  
  print_formatted_text(
      FormattedText(
          [
              ('class:b','hello'),
          ]
      ),
      style=style
  )
  ```

  ![formated_text_5](prompt_toolkit.assets/formated_text_5.png)

- `PygmentsTokens`对象（使用`from prompt_toolkit.formatted_text import PygmentsTokens`导入，完整用法参考 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#prompt_toolkit.formatted_text.PygmentsTokens ），和`FormattedText`对象的参数类似，只不过`PygmentsTokens`对象的参数中，元组的第一个元素不是样式字符串，而是将代码语法高亮时的标志，最终渲染时，就会根据语法高亮的情况将对应的部分代码渲染为指定样式：

  ```python3
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.formatted_text import PygmentsTokens
  from pygments.token import Token
  
  print_formatted_text(
      PygmentsTokens(
          [
              (Token.Keyword, 'print'),
              (Token.Punctuation, '('),
              (Token.Literal.String.Double, '"'),
              (Token.Literal.String.Double, 'hello'),
              (Token.Literal.String.Double, '"'),
              (Token.Punctuation, ')'),
              (Token.Text, '\n'),
          ]
      )
  )
  ```

  ![formated_text_7](prompt_toolkit.assets/formated_text_7.png)

  当然，代码比较长的时候，每一部分都这样单独指定其对应的标志未免也太费事，这时可以导入`pygments`的语法高亮方案（比如`PythonLexer`），使用`lex`方法一步到位创建元素为元组（元素为标志、代码）的可迭代对象：

  ```python3
  import pygments
  from pygments.lexers.python import PythonLexer
  from prompt_toolkit.formatted_text import PygmentsTokens
  from prompt_toolkit import print_formatted_text
  
  print_formatted_text(
      PygmentsTokens(
          pygments.lex(
              'print("Hello")',
              lexer=PythonLexer()
          )
      )
  )
  ```

  ![formated_text_7](prompt_toolkit.assets/formated_text_7.png)

  虽然语法高亮方案自带样式，但依然可以传入覆盖了语法高亮样式类的样式对象，指定标志的样式：

  ```python3
  import pygments
  from pygments.lexers.python import PythonLexer
  from prompt_toolkit.formatted_text import PygmentsTokens
  from prompt_toolkit import print_formatted_text
  from prompt_toolkit.styles import Style
  
  style = Style(
      [
          ('pygments.literal.string.double','red underline')
      ]
  )
  
  print_formatted_text(
      PygmentsTokens(
          pygments.lex(
              'print("Hello")',
              lexer=PythonLexer()
          )
      ),
      style=style
  )
  ```

  ![formated_text_8](prompt_toolkit.assets/formated_text_8.png)

  实际上，在渲染`PygmentsTokens`对象时，标志都有对应的、指明样式类的样式字符串，比如`Token.Literal.String.Double`对应`'class:pygments.literal.string.double'`。具体规则就是将标志全部转化为小写之后，将'token'替换为'pygments'，即为该标志渲染时使用的样式类。

虽然`print_formatted_text`方法可以将上面的对象渲染为带格式的文本，但很多时候给的并非上述对象，而是普通的字符串或者对象，如果想要将其转换为带格式的文本，可以试试一个简单的方法——`to_formatted_text`（使用`from prompt_toolkit.formatted_text import to_formatted_text`导入，完整用法参考 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#prompt_toolkit.formatted_text.to_formatted_text ）。

`to_formatted_text`方法支持以下参数：

- `value`参数，字符串类型、元素为元组的列表（同`FormattedText`对象的参数，方法返回使用列表作为参数构建的`FormattedText`对象）、实现了`__pt_formatted_text__`方法的对象（即本节介绍的、可渲染为带格式文本的对象）、调用之后返回前面几种类型的可调用类型、除了前面几种类型之外的任意类型（只有`auto_convert`参数为`True`时才能正常转换），表示要转换的原始对象。
- `style`参数，字符串类型，表示方法返回结果的样式。对于`value`参数原本设置的样式（如列表、可渲染为带格式文本的对象），该参数不会覆盖；`value`参数原本未设置的样式，可通过此参数设置（哪怕这部分内容已经设置了其他样式，依然可以补充未设置的样式）。
- `auto_convert`参数，布尔类型，对于`value`参数为其余任意类型时，可以设置此参数为`True`来自动转换，该参数默认为`False`。

以下为示例：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import to_formatted_text,HTML

print_formatted_text(
    to_formatted_text(
        'hello',
        style='red bg:white'
    )
)
print_formatted_text(
    to_formatted_text(
        [
            ('red','hello')
        ],
        style='green bg:white'
    )
)
print_formatted_text(
    to_formatted_text(
        HTML('<style bg="white">hello</style>'),
        style='red bg:green'
    )
)
print_formatted_text(
    to_formatted_text(
        locals(),
        auto_convert=True
    )
)
```

![formated_text_9](prompt_toolkit.assets/formated_text_9.png)

`to_formatted_text`方法可以将任意内容转换为带格式的文本，`to_plain_text`方法则可以反向转换——将转带格式的文本转换为没有格式的字符串，如果需要获取显示内容的无格式字符串，可以使用`to_plain_text`方法：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML,to_plain_text

print_formatted_text(
    to_plain_text(HTML('<red>hello</red>')),
)
```

`HTML`对象和`ANSI`对象都支持`format`方法，可以和Python中字符串的`format`方法一样，在这两个对象的原始内容中使用格式化表达，灵活替换部分内容，就像模板一样：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML,ANSI

print_formatted_text(
    HTML('<red>hello {s}</red>').format(s='Python'),
)

print_formatted_text(
    ANSI('\x1b[31mhello {s}\x1b[32m').format(s='Python')
)
```

![formated_text_10](prompt_toolkit.assets/formated_text_10.png)

和上面模板用法类似的是，想要在无格式的字符串中灵活替换带格式的文本，可以使用同样支持`format`方法的`Template`类（使用`from prompt_toolkit.formatted_text import Template`导入，具体用法参考 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#prompt_toolkit.formatted_text.Template ）：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML,Template

print_formatted_text(
    Template('Answer is {}').format(HTML('<red>hello</red>')),
)
```

![formated_text_11](prompt_toolkit.assets/formated_text_11.png)

需要注意的是，`Template`类的`format`方法不支持命名的占位格式符，只能使用匿名的占位格式符。

#### 2.1.3 样式

前面讲了很多内容与样式有关，但是先讲样式的话，很多与特定对象相关的样式用法会导致读者迷惑，因此，样式的学习放在了这里。

本节内容原文参考 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/advanced_topics/styling.html 。

##### 2.1.3.1 基础样式

在样式中，用得最多的就是颜色，而框架提供了以下两种颜色相关的样式：

- 直接表示颜色或者有'fg:'前缀的颜色表达式，表示内容的前景色（也称之为字体颜色）。

  其中，颜色支持以下格式：

  - 颜色的名字，如`'red'`。可以使用`from prompt_toolkit.styles import NAMED_COLORS,ANSI_COLOR_NAMES,ANSI_COLOR_NAMES_ALIASES`导入相关字典或者列表，查询支持的颜色名。其中，`ANSI_COLOR_NAMES`和`ANSI_COLOR_NAMES_ALIASES`包含的是ANSI颜色。
  - '#'为前缀，后接6位十六进制数字，每两位数字代表一种颜色分量值（依次对应红色、绿色、蓝色的分量值）的RGB颜色标准表达方式，如`'#cc5454'`。

  上面提到的颜色表达，也可以用在框架中其他使用颜色的地方，但部分对象（如`HTML`对象）只支持颜色名字。

- 有'bg:'前缀的颜色表达式，表示内容的背景色。

除了颜色，还支持通过样式修改内容的格式：

- `'bold'`，表示内容字体将变为粗体。
- `'italic'`，表示内容字体将变为斜体。
- `'underline'`，表示内容将添加下划线。
- `'strike'`，表示内容将添加删除线。
- `'blink'`，表示内容将闪烁（仅部分终端支持，Windows自带终端不支持）。
- `'reverse'`，表示内容的背景色与前景色相反。
- `'hidden'`，表示内容隐藏。

给以上内容格式添加'no'前缀，则表示内容不使用上述样式，常用于组合基础样式与样式类时，撤销不需要的内容格式。

使用基础样式时，不同的基础样式可以组合，使用空格间隔，构成复合样式。无论是基础样式还是复合样式，将其放在字符串中，就成了样式字符串。

对于`to_formatted_text`方法的`style`参数、`FormattedText`对象的参数等支持字符串作为样式的，可以使用样式字符串，修改输出内容的样式。

##### 2.1.3.2 样式类

`print_formatted_text`方法的`style`参数接收的是样式对象，需要通过样式对象创建样式类才能使用样式类对应的样式。

样式类可以看做是给基础样式或者复合样式分配了一个变量名，这样就能在样式字符串内，通过`'class:{样式类}'`的格式使用该样式：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style

# 基于字典创建样式对象
style = Style.from_dict(
    {
    	'a': 'red underline',
	}
)

print_formatted_text(
    HTML('<a>hello</a>'),
    style=style
)

# 直接创建样式对象
style = Style(
    [
    	('b','green italic')
	]
)

print_formatted_text(
    HTML('<b>hello</b>'),
    style=style
)
```

![formated_text_5](prompt_toolkit.assets/formated_text_5.png)

样式类（使用`from prompt_toolkit.styles import Style`导入）支持以下参数：

- `style_rules`参数，元素为元组的列表，表示样式类与具体样式的对应关系。元组的第一个元素为样式类名字，可以自定义（可在被渲染的对象中通过`'class:{样式类}'`的格式使用该样式类），也可以使用框架已经规定的样式类名字（部分对象不支持使用指定样式类，比如`PygmentsTokens`对象）；元组的第二个元素为样式类对应的样式字符串，表示该样式类的样式。

样式类支持以下属性：

- `style_rules`属性，同`style_rules`参数。

样式类支持以下类方法：

- `from_dict`方法，相比于直接使用样式类，该方法将样式类与具体样式的对应关系变成了字典的键、值对应关系，在某些场景下更方便。

##### 2.1.3.3 样式类的用法

在样式字符串内，通过`'class:{样式类}'`的格式使用样式类是基础用法。然而，样式类的用法远没有这么简单。

基础样式中支持的颜色名字和内容格式，还可以将其作为样式类来使用，其中`bold`（短名`b`）、`italic`（短名`i`）、`underline`（短名`u`）、`strike`（短名`s`）还支持短名作为样式类：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

print_formatted_text(
    FormattedText(
        [
            ('class:red','hello')
        ]
    )
)

print_formatted_text(
    FormattedText(
        [
            ('class:b','hello')
        ]
    )
)
```

![style_1](prompt_toolkit.assets/style_1.png)

在定义样式类的时候，如果样式类名为空格分隔的两个样式类，比如`'a aa'`，则只有同时设置了这两个样式类的样式字符串才会应用该样式类对应的样式：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style

# 基于字典创建样式对象
style = Style.from_dict(
    {
    	'a aa': 'italic red',
	}
)

print_formatted_text(
    FormattedText(
        [
            ('class:a class:aa','hello')
        ]
    ),
    style=style
)
print_formatted_text(
    FormattedText(
        [
            ('class:aa','hello')
        ]
    ),
    style=style
)
print_formatted_text(
    FormattedText(
        [
            ('class:a','hello')
        ]
    ),
    style=style
)
```

![style_2](prompt_toolkit.assets/style_2.png)

在使用样式类的时候，如果样式类名为英文句号连接的两个样式类，比如`'class:a.aa'`，则实际应用的是该样式类和以开头部分为核心依次去掉末尾部分的样式类，比如`'class:a.aa'`相当于`'class:a class:a.aa'`（与[Pygments](http://pygments.org/) 的词法分析相同）。

在定义样式类的时候，如果没有定义单独的样式类，只定义了英文句号连接的两个样式类。则在应用时，只有与定义完全相同的样式类才会应用其对应的样式：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style

# 基于字典创建样式对象
style = Style.from_dict(
    {
        'a.aa': 'red italic',
	}
)

print_formatted_text(
    FormattedText(
        [
            ('class:a.aa','hello')
        ]
    ),
    style=style
)
print_formatted_text(
    FormattedText(
        [
            ('class:aa.a','hello')
        ]
    ),
    style=style
)
```

![style_3](prompt_toolkit.assets/style_3.png)

如果定义的时候，定义了单独的样式类。则在应用时，按照实际应用的样式类的顺序，后者会覆盖前者相同类型的样式：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style

# 基于字典创建样式对象
style = Style.from_dict(
    {
        'a': 'yellow',
        'aa': 'blue',
        'a.aa': 'red',
        'aa.a': 'green',
	}
)

print_formatted_text(
    FormattedText(
        [
            ('class:a.aa','hello')
        ]
    ),
    style=style
)
print_formatted_text(
    FormattedText(
        [
            ('class:aa.a','hello')
        ]
    ),
    style=style
)
```

![style_4](prompt_toolkit.assets/style_4.png)

就和HTML中的CSS应用顺序一样，也遵循越靠近内容，优先级越高。比如：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style

# 基于字典创建样式对象
style = Style.from_dict(
    {
        'a': 'yellow',
	}
)

print_formatted_text(
    HTML(
        '<a color="red">hello</a>'
    ),
    style=style
)
```

`'<a color="red">hello</a>'`中设置了文字的颜色，但因为其归属于`HTML`对象内部，转换为带格式的文本对象之后，其生成的样式类对应的样式字符串为`'class:a fg:red'`，因此，实际渲染出来的文字颜色是红色，而非样式对象中的黄色：

![formated_text_2](prompt_toolkit.assets/formated_text_2.png)

使用下面的代码可以看到`HTML`对象对应的样式字符串：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML,to_formatted_text
from prompt_toolkit.styles import Style

# 基于字典创建样式对象
style = Style.from_dict(
    {
        'a': 'yellow',
	}
)

print_formatted_text(
    to_formatted_text(
        HTML(
            '<a color="red">hello</a>'
        )
    ).__repr__(),
    style=style
)
```

如果想在其他地方使用`pygments`的语法高亮的样式，除了要指定样式类为标志渲染时对应的样式类，还要使用`get_style_by_name`方法（使用`from pygments.styles import get_style_by_name`导入）获取`pygments`主题对应的样式（`pygments`支持多种主题，具体参考 https://pygments.org/styles/ ），再使用`style_from_pygments_cls`方法（使用`from prompt_toolkit.styles.pygments import style_from_pygments_cls`导入）将其转换为框架的样式对象：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML,FormattedText
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from pygments.styles import get_style_by_name

style = style_from_pygments_cls(get_style_by_name('monokai'))

print_formatted_text(
    FormattedText(
        [
            ('class:pygments.literal.string','hello')
        ]
    ),
    style=style
)

print_formatted_text(
    HTML(
        '<pygments.literal.string>hello</pygments.literal.string>'
    ),
    style=style
)
```

![style_5](prompt_toolkit.assets/style_5.png)

使用`merge_styles`方法（使用`from prompt_toolkit.styles import merge_styles`导入）可以将多个样式对象合并为一个，该方法接收元素为样式对象的列表，返回按照顺序合并后的样式对象（就和样式字符串中的样式优先级一样，排在后面的样式对象会覆盖前面相同的样式）：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
from prompt_toolkit.styles import merge_styles

style = merge_styles(
    [
        Style.from_dict(
            {
                'a': 'red underline',
            }
        ),
        Style(
            [
                ('a', 'green italic')
            ]
        )
    ]
)

print_formatted_text(
    FormattedText(
        [
            ('class:a', 'hello'),
        ]
    ),
    style=style
)
```

![style_6](prompt_toolkit.assets/style_6.png)

终端在显示样式的颜色时，不同的颜色深度（颜色位数）会影响显示的效果（还要看终端对颜色的支持情况）：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

for color_depth in [
    'DEPTH_1_BIT',
    'DEPTH_4_BIT',
    'DEPTH_8_BIT',
    'DEPTH_24_BIT',
]:
    print_formatted_text(
        FormattedText(
            [
                ('class:green', 'hello'),
            ]
        ),
        color_depth=color_depth
    )
```

![style_7](prompt_toolkit.assets/style_7.png)

具体颜色深度（颜色位数）与支持的颜色、字符串值等对应情况可以参考下表：

| 颜色位数 | 支持的颜色 | 字符串值         | `ColorDepth`类的枚举成员  | `ColorDepth`类的枚举成员（别名） |
| -------- | ---------- | ---------------- | ------------------------- | -------------------------------- |
| 1位      | 黑与白     | `'DEPTH_1_BIT'`  | `ColorDepth.DEPTH_1_BIT`  | `ColorDepth.MONOCHROME`          |
| 4位      | ANSI颜色   | `'DEPTH_4_BIT'`  | `ColorDepth.DEPTH_4_BIT`  | `ColorDepth.ANSI_COLORS_ONLY`    |
| 8位      | 256色      | `'DEPTH_8_BIT'`  | `ColorDepth.DEPTH_8_BIT`  | `ColorDepth.DEFAULT`             |
| 24位     | 真彩色     | `'DEPTH_24_BIT'` | `ColorDepth.DEPTH_24_BIT` | `ColorDepth.TRUE_COLOR`          |

除了给方法的`color_depth`参数传入对应的字符串，还可以使用`ColorDepth`类的枚举成员：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.output.color_depth import ColorDepth

for color_depth in [
    'DEPTH_4_BIT',
    ColorDepth.DEPTH_4_BIT,
    ColorDepth.ANSI_COLORS_ONLY,
]:
    print_formatted_text(
        FormattedText(
            [
                ('class:green', 'hello'),
            ]
        ),
        color_depth=color_depth
    )
```

![style_8](prompt_toolkit.assets/style_8.png)

不仅`print_formatted_text`方法有`color_depth`参数，框架中还有不少方法、类支持该参数，若是需要修改一个程序中所有显示内容的颜色深度（颜色位数），每个方法都设置一次`color_depth`参数难免有些麻烦。这时，可以设置环境变量`PROMPT_TOOLKIT_COLOR_DEPTH`为对应的字符串值，就能强制所有框架程序使用指定的颜色深度（颜色位数），或者在程序内单独设置环境变量，这样的话，该程序的所有输出内容都会使用指定的颜色深度（颜色位数）：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
import os

os.environ['PROMPT_TOOLKIT_COLOR_DEPTH'] = 'DEPTH_4_BIT'

print_formatted_text(
    FormattedText(
        [
            ('class:green', 'hello'),
        ]
    ),
)
```

和`color_depth`参数一样有用的，就是`style_transformation`参数，给该参数传入`StyleTransformation`类（该类是抽象类，需要实现`transform_attrs`方法，具体参考 https://python-prompt-toolkit.readthedocs.io/en/stable/pages/reference.html#prompt_toolkit.styles.StyleTransformation ）对象，即可实现将渲染后的内容再处理一下（转换样式）：

```python3
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
from prompt_toolkit.styles.style_transformation import ReverseStyleTransformation

print_formatted_text(
    FormattedText(
        [
            ('class:green', 'hello'),
        ]
    ),
    style_transformation=ReverseStyleTransformation()
)
```

`ReverseStyleTransformation`可以将交换前景色与背景色：

![style_9](prompt_toolkit.assets/style_9.png)

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





`Application`类支持以下参数：

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

