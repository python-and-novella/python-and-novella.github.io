# Qt For Python 札记（2026）

## 2026版更新计划

2025版（即2025年创作的部分）在创作过程中已经覆盖了不少内容，但Qt提供了数量庞大的控件，支持的用法也多种多样，更别说各种控件在实际使用时遇到的问题数不胜数。

2025版立项较晚，加上笔者要预研其他教程，还有其他工作要做，导致2025版的内容只是介绍了Qt用法的很小一部分。

因此，笔者将在2026年继续本教程系列的更新，也就是本教程的2026版。2026版将延续2025版的任务，为读者介绍Qt控件的用法和更多Qt模块。同时，对于之前已经介绍过的控件，将搜集实际使用时的各种用法和遇到的问题，深入、扩展常用控件的用法，解决相关问题。当然，之前内容如果存在遗漏、错误，后续也将会发布补充、修正的章节。

2026年，更新不止，学习不止，愿每一位读者都能学有所得。当然，为了适应新的更新节奏，2026版教程将改为敏捷更新风格，争取提高更新频率。

## 控件学习指南

### 为什么会有本章

因为2026版改为敏捷更新风格，如果将官方教程完全复刻，需要付出太多精力，也有太多重复。因此，在2026版中，笔者将告诉读者如何查阅官方文档，以及本教程主要介绍哪些内容，让需要了解重点难点、有一定基础的读者无需回头查看官方文档，让基础不太扎实但有自学能力的读者可以学会如何查阅官方文档，让每位读者掌握官方文档和本教程之间的平衡。

### 如何学习官方文档

官方文档：https://doc.qt.io/qtforpython-6/modules.html

上面提供了官方的文档地址，打开之后，可以点击各个模块的链接，跳转至响应模块的文档。因此，只需使用在所使用模块的文档中，查找对应类、方法的链接，即可查阅其使用方法。

以QtWidgets程序的控件文档为例，模块名为`PySide6.QtWidgets`，但其名称为“Qt Widgets”，因此需要点击图示的链接（https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html）：

![2026_0_1](qt_for_python_pro.assets/2026_0_1.png)

跳转之后，页面如下：

![2026_0_2](qt_for_python_pro.assets/2026_0_2.png)

图中红框内的链接分别为：

1. 按照功能分类的类文档：https://doc.qt.io/qtforpython-6/overviews/qtwidgets-widget-classes.html#widgets-classes
2. 按照名称首字母分类的类文档（就在当前页面）：https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html#list-of-classes
3. 按照名称首字母分类的方法文档（就在当前页面）：https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html#list-of-functions

一般而言，常用的是模块的类，因此，只需使用1、2提供的文档即可。如果想要了解模块提供了哪些功能，可以看看1；若只是在使用具体类时遇到问题，直接在当前页面查找对应类名，跳转到类的文档即可。

比如，查找下一章要学习的`QPushButton`类：

![2026_0_3](qt_for_python_pro.assets/2026_0_3.png)

需要注意的是，官方文档看似类别清晰、内容丰富，但并非没有问题，点击上图的链接（https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html）之后，会跳转到下面的页面：

![2026_0_4](qt_for_python_pro.assets/2026_0_4.png)

图中箭头所指的链接是初始化函数的文档，但跳转之后，会看到下面的内容：

![2026_0_5](qt_for_python_pro.assets/2026_0_5.png)

看起来连重载的初始化方法都标明了，好像很全面，但别急着高兴，这里有一个坑。

先放下文档，在VSCode中写下如下代码：

```python3
from PySide6.QtWidgets import QPushButton
```

这是一段导入`QPushButton`类的代码，随后，选中其中的`QPushButton`，按`f12`键或者 右键-转到定义，可以看到以下内容（部分代码）：

```python3
class QPushButton(PySide6.QtWidgets.QAbstractButton):

    @typing.overload
    def __init__(self, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ..., *, autoDefault: bool | None = ..., default: bool | None = ..., flat: bool | None = ...) -> None: ...
    @typing.overload
    def __init__(self, icon: PySide6.QtGui.QIcon | PySide6.QtGui.QPixmap, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ..., *, autoDefault: bool | None = ..., default: bool | None = ..., flat: bool | None = ...) -> None: ...
    @typing.overload
    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ..., *, autoDefault: bool | None = ..., default: bool | None = ..., flat: bool | None = ...) -> None: ...
```

![2026_0_6](qt_for_python_pro.assets/2026_0_6.png)

该文件是PySide6提供的类型声明，用于代码提示和类型检查。从上面内容中可以发现，该类提供的几种初始化方法，参数远比文档中多，而文档没有提供相应的说明。

因此，在实际学习时，最好结合代码提示和官方文档，只看官方文档的话，会忽略掉实际支持的参数。

回到文档（https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html）：

![2026_0_7](qt_for_python_pro.assets/2026_0_7.png)

大部分控件的文档都会在开头这里提供快速跳转的链接，包括：

- 控件属性。除了这里标明的控件属性，控件还会继承父类的控件属性，因此实际控件支持的控件属性会比文档中看上去要多。

  注意，这里标明的控件属性表示其可用于该控件初始化方法中的关键字参数。

  另外，不同于Python中的属性可以直接设置、获取，控件属性是指其作为方法（或者控件属性名加了“is”前缀的方法）调用之后的返回值，想要设置控件属性，则要调用控件属性名加了“set”前缀的方法。其实，这里可以看出，Qt采用的是小驼峰命名法，因此，后续可以在得知控件属性名之后，猜测相关的获取、设置方法。

- 方法、虚拟方法、槽。方法中大部分是控件属性相关的方法（获取、设置），也就初始化方法是有确定功能的方法。而虚拟方法、槽本质上也是方法，只不过槽一般与信号组合使用，但也可以当作一个普通方法来调用。

  需要注意的是，虽然部分方法可以在创建控件时直接调用，但依然存在部分延迟生效的方法，需要先创建控件并将其分配给变量之后，才能调用其支持的方法。

- 信号。虽然示例中没有看到，但其继承了父类的信号，实际上支持不少信号（可以参考其父类`QAbstractButton`的文档）。信号一般是调用其连接函数，将其与指定的槽函数连接，实现信号的响应。

注意，这里也有一个坑。看文档（https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html）最上面的部分：

![2026_0_8](qt_for_python_pro.assets/2026_0_8.png)

这里标明了控件的继承关系，而控件实际支持的方法、控件属性、信号、槽，除了控件文档中写明的，还包含其父类（比如`QAbstractButton`类）的。想要了解其父类提供的方法、控件属性、信号、槽，可以点击继承关系中对应的父类，跳转至父类的文档。

### 关于本教程

了解完官方文档如何学习，最后简单介绍一下本教程后续章节的大概结构（后续可能会修改），如果读者觉得不太适合，可以及时反馈或者暂时先去学习官方文档。

后续章节的大概结构如下：

1. 引言。简单介绍控件功能，让读者对该控件有个简单的了解。
2. 初始化方法。前面说过官方文档的初始化方法有点“混乱”，因此笔者会重新整理控件的初始化方法，并配上必要的示例，方便读者学习。
3. 方法（部分介绍）、控件属性（部分介绍）。因为控件属性很多也是方法，因此将其归类至方法。不过，一个控件支持的方法、控件属性很多，有些控件是继承自别的控件，无限向上追溯的话，内容会很多，也会重复。而不少方法、控件属性一般不怎么用或者其他控件也有，全部介绍也比较占用时间，因此这部分内容将挑选部分来介绍，不常用的、其他控件也有的，可能会省略。读者如有需求，可以及时反馈，后续通过其他章节补充。
4. 信号和槽（尽量完整地详细介绍）。因为信号和槽属于Qt独特的机制，虽然槽本质上也是方法，但为了方便快速学习，这两个功能将单独介绍，并且尽量完整地详细介绍。
5. 扩展用法（主要是技巧相关的代码）。实际开发时，很多时候遇到的问题没有教程中说的那么简单，就是因为控件是组合使用，只看当前控件的文档或者教程，很难解决问题，因此需要扩展其他控件或者相关知识，才能解决实际遇到的问题。所以，对于部分控件，会在学完基础之后，额外补充一些和实际问题相关的扩展用法。当然，如果读者遇到了其他与控件相关的问题但当时没有介绍，也可以留言反馈，笔者将后续通过其他章节补充。

## 25 `QPushButton`普通按钮控件

本章介绍的`QPushButton`普通按钮控件算是最常用、最普通的按钮。如果程序中需要一个简单的、可以点击的按钮，那非普通按钮控件莫属：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton
)

app = QApplication()
window = QWidget()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

button = QPushButton('普通按钮',window)

window.show()
app.exec()
```

![2026_25_1](qt_for_python_pro.assets/2026_25_1.png)

`QPushButton`普通按钮控件的继承关系如下：

![2026_25_0](qt_for_python_pro.assets/2026_25_0.png)

相关文档的链接如下：

- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html

### 25.1 初始化方法

`QPushButton`普通按钮控件有多种初始化方法（参数名及类型提示来自`QtWidgets.pyi`）。

第一种初始化方法支持以下参数：

- `text`参数，仅限位置参数（第一个位置参数），字符串类型，表示显示在按钮上的文字。

- `parent`参数，`PySide6.QtWidgets.QWidget`类型，表示父控件。如果指定了父控件，那么该控件显示时，会使用父控件的位置或者嵌在父控件内（取决于该控件是否支持嵌入到其他控件）。不指定或者为`None`，则控件会在独立窗口中显示。

- `autoDefault`参数，仅限关键字参数，布尔类型，表示控件是否为自动默认按钮，默认为`False`，如果父控件为`QDialog`控件（含子类控件），则默认值为`True`。当控件获得焦点时，自动默认按钮会变为默认按钮。

- `default`参数，仅限关键字参数，布尔类型，表示控件是否为默认按钮（按钮边缘有高亮），默认为`False`。

  父控件为`QDialog`控件（含子类控件）的话，默认按钮首先获得焦点，并且优先于默认焦点顺序。此外，对于同一个`QDialog`控件而言，最多存在一个默认按钮，以控件设置该参数的顺序为最终生效顺序。无论默认按钮是否获得焦点，默认按钮都可以响应`enter`键。按下`enter`键时，会触发默认按钮的`clicked`信号。

  父控件不为`QDialog`控件（含子类控件）的话，则可以存在多个默认按钮，只有获得焦点的默认按钮可以响应`enter`键。按下`enter`键时，会触发获得焦点的默认按钮的`clicked`信号。

- `flat`参数，仅限关键字参数，布尔类型，表示控件是否为扁平按钮（鼠标悬停在按钮上的话没有悬浮特效），默认为`False`。

第二种初始化方法支持以下参数：

- `icon`参数，仅限位置参数（第一个位置参数），`PySide6.QtGui.QIcon`类型或者`PySide6.QtGui.QPixmap`类型，表示按钮的图标或者图片。

  示例如下（所需的图片`LOGO.png`请保存至源代码的同目录下）：

  ```python3
  from PySide6.QtWidgets import (
      QApplication,
      QWidget,
      QPushButton
  )
  
  from PySide6.QtGui import QIcon,QPixmap
  
  app = QApplication()
  window = QWidget()
  window.setWindowTitle('认识各种按钮')
  window.resize(400, 300)
  
  QPushButton(
      QIcon.fromTheme(
          QIcon.ThemeIcon.Battery
      ),
      '普通按钮',
      window
  )
  QPushButton(
      QPixmap('LOGO.png'),
      '普通按钮',
      window
  ).move(0,30)
  
  window.show()
  app.exec()
  ```

  ![2026_25_2](qt_for_python_pro.assets/2026_25_2.png)

- `text`参数，仅限位置参数（第二个位置参数），含义、用法参考前面。

- `parent`参数，含义、用法参考前面。

- `autoDefault`参数，仅限关键字参数，含义、用法参考前面。

- `default`参数，仅限关键字参数，含义、用法参考前面。

- `flat`参数，仅限关键字参数，含义、用法参考前面。

第三种初始化方法支持以下参数：

- `parent`参数，含义、用法参考前面。
- `autoDefault`参数，仅限关键字参数，含义、用法参考前面。
- `default`参数，仅限关键字参数，含义、用法参考前面。
- `flat`参数，仅限关键字参数，含义、用法参考前面。

### 25.2 方法、控件属性

`QPushButton`普通按钮控件支持以下方法（部分，含控件属性）：

- `autoExclusive`方法（控件属性，可使用`setAutoExclusive`方法设置），返回控件是否启用自动独占。当多个按钮的父控件相同时，这些按钮就属于同一独占组。如果这些按钮启用了勾选和自动独占，那么，将只允许同时勾选最多一个按钮：

  ```python3
  from PySide6.QtWidgets import (
      QApplication,
      QWidget,
      QPushButton
  )
  
  app = QApplication()
  window = QWidget()
  window.setWindowTitle('认识各种按钮')
  window.resize(400, 300)
  
  button = QPushButton(
      '按钮1',
      window
  )
  button.setCheckable(True)
  button.setAutoExclusive(True)
  
  button2 = QPushButton(
      '按钮2',
      window
  )
  button2.move(0,30)
  button2.setCheckable(True)
  button2.setChecked(True)
  button2.setAutoExclusive(True)
  
  window.show()
  app.exec()
  ```

  ![2026_25_3](qt_for_python_pro.assets/2026_25_3.gif)

- `autoRepeat`方法（控件属性，可使用`setAutoRepeat`方法设置），返回控件是否启用了自动重复。自动重复是按钮的控件属性，默认该控件属性为`False`。所谓自动重复（使用`setAutoRepeat`方法设置），即按住按钮时，是否以指定的初始延迟（使用`setAutoRepeatDelay`方法设置）和间隔（使用`setAutoRepeatInterval`方法设置）重复发射`clicked`、`pressed`、`released`这三个信号。

  示例如下：

  ```python3
  from PySide6.QtWidgets import (
      QApplication,
      QWidget,
      QPushButton
  )
  
  app = QApplication()
  window = QWidget()
  window.setWindowTitle('认识各种按钮')
  window.resize(400, 300)
  
  button = QPushButton(
      '按钮1',
      window
  )
  
  button.setAutoRepeat(True)
  button.setAutoRepeatDelay(3000)
  button.setAutoRepeatInterval(1000)
  button.clicked.connect(lambda :print('clicked'))
  button.pressed.connect(lambda :print('pressed'))
  button.released.connect(lambda :print('released'))
  
  window.show()
  app.exec()
  ```

  使用鼠标按住按钮不松手，即可在终端看到持续不断的输出。

- `autoRepeatDelay`方法（控件属性，可使用`setAutoRepeatDelay`方法设置），返回控件的自动重复初始延迟。

- `autoRepeatInterval`方法（控件属性，可使用`setAutoRepeatInterval`方法设置），获取控件的自动重复间隔。

- `group`方法，获取按钮所属的按钮分组。

  所谓按钮分组，即当按钮启用`autoExclusive`控件属性时，属于同一分组的按钮，将只允许同时勾选最多一个按钮。前面介绍时没有使用按钮分组，默认父控件相同时算作同一分组。但这样的用法会导致一个问题，如果父控件相同，想要让两组以上的按钮分别自动独占，就无法实现。因此，可以使用`QButtonGroup`控件的`addButton`方法，将需要分组的按钮添加到同一组，可以实现组与组之间的隔离。

  示例如下：

  ```python3
  from PySide6.QtWidgets import (
      QApplication,
      QWidget,
      QPushButton,
      QButtonGroup
  )
  
  app = QApplication()
  window = QWidget()
  window.setWindowTitle('认识各种按钮')
  window.resize(400, 300)
  
  buttons = []
  for i in range(1,5):
      # 批量生成按钮
      button = QPushButton(
      	f'按钮{i}',
          window,
      )
      button.setCheckable(True)
      button.setAutoExclusive(True)
      button.move(
          0,
          30*(i-1)
      )
      # 点击按钮会在终端输出按钮所属的按钮组
      button.clicked.connect(
          lambda e,button=button:print(
              button.group()
          )
      )
      # 最后将按钮添加到数组中
      buttons.append(button)
  
  # 两个按钮分组
  group1 = QButtonGroup(
      window,
  )
  group1.addButton(
      buttons[0],
  )
  group1.addButton(
      buttons[1],
  )
  group2 = QButtonGroup(
      window,
  )
  group2.addButton(
      buttons[2],
  )
  group2.addButton(
      buttons[3],
  )
  
  window.show()
  app.exec()
  ```

  依次点击每个按钮，可以看到四个按钮明显分为两组，控制台的输出也证明了这一点：

  ![2026_25_4](qt_for_python_pro.assets/2026_25_4.png)

- `icon`方法（控件属性，可使用`setIcon`方法设置），返回按钮的图标或者图片。

- `iconSize`方法（控件属性，可使用`setIconSize`方法设置），返回按钮图标的大小。

- `isCheckable`方法（控件属性`checkable`的获取方法，可使用`setCheckable`方法设置），返回按钮是否可勾选。

- `isChecked`方法（控件属性`checked`的获取方法，可使用`setChecked`方法设置），返回按钮是否已勾选。

- `isDefault`方法（控件属性`default`的获取方法，可使用`setDefault`方法设置），返回按钮是为默认按钮。

- `isDown`方法（控件属性`down`的获取方法，可使用`setDown`方法设置），返回按钮是否已按下。

- `isFlat`方法（控件属性`flat`的获取方法，可使用`setFlat`方法设置），返回按钮是否为扁平按钮（鼠标悬停在按钮上的话没有悬浮特效）。

- `menu`方法（控件属性，可使用`setMenu`方法设置），返回点击按钮之后弹出的菜单。

- `setMenu`方法，设置点击按钮之后弹出的菜单。

  示例如下：

  ```python3
  from PySide6.QtWidgets import (
      QApplication,
      QWidget,
      QPushButton,
      QMenu
  )
  
  app = QApplication()
  window = QWidget()
  window.setWindowTitle('认识各种按钮')
  window.resize(400, 300)
  
  button = QPushButton(
      '按钮',
      window,
  )
  
  menu = QMenu()
  menu.addAction('Hello')
  menu.addAction('World')
  button.setMenu(
      menu
  )
  
  window.show()
  app.exec()
  ```

  ![2026_25_5](qt_for_python_pro.assets/2026_25_5.png)

  该方法支持以下参数：

  - `menu`参数，`PySide6.QtWidgets.QMenu`类型，表示弹出的菜单。

- `setToolTip`方法，设置按钮的工具提示（鼠标悬停时自动弹出的文字）。该方法支持以下参数：

  - `arg__1`参数，仅限位置参数（第一个位置参数），字符串类型，表示工具提示的内容。

- `setShortcut`方法，给按钮绑定快捷键，按下快捷键时触发按钮的`clicked`信号。该方法支持以下参数：

  - `key`参数，仅限位置参数（第一个位置参数），`PySide6.QtCore.Qt.Key`类型、`PySide6.QtGui.QKeySequence`类型、`PySide6.QtCore.QKeyCombination`类型、`PySide6.QtGui.QKeySequence.StandardKey`类型、字符串类型、整数类型，表示绑定的快捷键。

- `setText`方法，设置按钮的文本。该方法支持以下参数：

  - `text`参数，仅限位置参数（第一个位置参数），字符串类型，表示按钮的文本。

- `shortcut`方法，返回按钮绑定的快捷键。

- `text`方法，返回按钮的文本。

- `toolTip`方法，返回按钮的工具提示。

### 25.3 信号和槽

`QPushButton`普通按钮控件支持以下信号（部分）：

- `clicked`信号，点击（包含鼠标按键按下、弹起两个过程）按钮时触发。

- `pressed`信号，按下按钮时触发。

- `released`信号，松开按钮时触发。

- `toggled`信号，切换按钮的勾选状态时触发。

  注意，按钮默认为不可勾选，需要通过`setCheckable(True)`启用勾选，才能在点击时切换勾选状态。

  示例如下：

  ```python3
  from PySide6.QtWidgets import (
      QApplication,
      QWidget,
      QPushButton
  )
  
  app = QApplication()
  window = QWidget()
  window.setWindowTitle('认识各种按钮')
  window.resize(400, 300)
  
  button = QPushButton(
      '可以勾选的按钮',
      window
  )
  button.setCheckable(True)
  button.toggled.connect(lambda:print('状态切换。'))
  
  window.show()
  app.exec()
  ```

`QPushButton`普通按钮控件支持以下槽（部分）：

- `showMenu`方法，弹出点击按钮之后弹出的菜单。
- `click`方法，点击按钮。
- `toggle`方法，切换按钮的勾选状态。
- `animateClick`方法，点击按钮，同时播放点击动画。

### 25.4 扩展用法

#### 25.4.1 自动创建快捷键

使用`setShortcut`方法可以给按钮设置任意快捷键，但是，如果在按钮文本中包含了“&｛符号｝”（比如`'&q'`），相当于创建了`alt + {符号对应的按键}`键为按钮的快捷键，则无需使用`setShortcut`方法。

注意，如果符号为大写字母，则默认在小写状态下也可以生效。

示例如下：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton
)

app = QApplication()
window = QWidget()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

button = QPushButton(
    '按钮（&q）',
    window,
)

button.clicked.connect(lambda e:print('Clicked!'))

window.show()
app.exec()
```

可以按下`alt + q`键，查看终端的输出结果。

## 26 `QRadioButton`单选按钮控件

上一章介绍`autoExclusive`方法时使用的示例看上去像是单选按钮，但那种费事、妥协的单选按钮并不完美，需要额外设置属性，样式上也不够直观。因此，本章要介绍的`QRadioButton`单选按钮控件，在支持不少`QPushButton`普通按钮控件功能的基础上，更适合作为单选按钮使用，代码也更简洁：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QRadioButton
)

app = QApplication()
window = QWidget()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

button = QRadioButton(
    '选项1',
    window,
)
button.setChecked(True)
button2 = QRadioButton(
    '选项2',
    window,
)
button2.move(
    0,
    30
)

window.show()
app.exec()
```

![2026_26_1](qt_for_python_pro.assets/2026_26_1.png)

`QRadioButton`单选按钮控件的继承关系如下：

![2026_26_2](qt_for_python_pro.assets/2026_26_2.png)

相关文档的链接如下：

- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QRadioButton.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html

### 26.1 初始化方法

`QRadioButton`单选按钮控件有多种初始化方法（参数名及类型提示来自`QtWidgets.pyi`）。

第一种初始化方法支持以下参数：

- `text`参数，仅限位置参数（第一个位置参数），字符串类型，表示显示在按钮上的文字。
- `parent`参数，`PySide6.QtWidgets.QWidget`类型，表示父控件。如果指定了父控件，那么该控件显示时，会使用父控件的位置或者嵌在父控件内（取决于该控件是否支持嵌入到其他控件）。不指定或者为`None`，则控件会在独立窗口中显示。

第二种初始化方法支持以下参数：

- `parent`参数，含义、用法参考前面。

### 26.2 方法、控件属性

`QRadioButton`单选按钮控件支持以下方法（部分，含控件属性）：

- `autoExclusive`方法（控件属性，可使用`setAutoExclusive`方法设置），返回控件是否启用自动独占。不同于`QPushButton`普通按钮控件需要单独设置，该控件默认为`True`，因此，当多个按钮的父控件相同时，这些按钮就属于同一独占组。那么，将只允许同时勾选最多一个按钮。

- `group`方法，获取按钮所属的按钮分组。因为该控件默认启用了`autoExclusive`控件属性，因此，想要将不同的单选隔离开，必须要分组（使用`QButtonGroup`控件的`addButton`方法，将需要分组的按钮添加到同一组）。

  示例如下：

  ```python3
  from PySide6.QtWidgets import (
      QApplication,
      QWidget,
      QRadioButton,
      QButtonGroup
  )
  
  app = QApplication()
  window = QWidget()
  window.setWindowTitle('认识各种按钮')
  window.resize(400, 300)
  
  buttons = []
  for i in range(1,5):
      # 批量生成选项
      button = QRadioButton(
      	f'选项{i}',
          window,
      )
      button.move(
          0,
          30*(i-1)
      )
      # 点击选项会在终端输出选项所属的按钮组
      button.clicked.connect(
          lambda e,button=button:print(
              button.group()
          )
      )
      # 最后将选项添加到数组中
      buttons.append(button)
    
  # 两个按钮分组
  group1 = QButtonGroup(
      window,
  )
  group1.addButton(
      buttons[0],
  )
  group1.addButton(
      buttons[1],
  )
  group2 = QButtonGroup(
      window,
  )
  group2.addButton(
      buttons[2],
  )
  group2.addButton(
      buttons[3],
  )
  
  window.show()
  app.exec()
  ```

  ![2026_26_3](qt_for_python_pro.assets/2026_26_3.png)

- `icon`方法（控件属性，可使用`setIcon`方法设置），返回按钮的图标或者图片。虽然该控件一般用于选项，但依然支持设置图标（该控件属性实际上来源于`QAbstractButton`抽象按钮控件）。

  示例如下：

  ```python3
  from PySide6.QtWidgets import (
      QApplication,
      QWidget,
      QRadioButton
  )
  from PySide6.QtGui import QIcon
  
  app = QApplication()
  window = QWidget()
  window.setWindowTitle('认识各种按钮')
  window.resize(400, 300)
  
  button = QRadioButton(
      '选项1',
      window,
  )
  button.setChecked(True)
  button2 = QRadioButton(
      '选项2',
      window,
  )
  button2.move(
      0,30
  )
  button.setIcon(
      QIcon.fromTheme(
          QIcon.ThemeIcon.Battery
      )
  )
  
  window.show()
  app.exec()
  ```

  ![2026_26_4](qt_for_python_pro.assets/2026_26_4.png)

其他的方法大部分和`QPushButton`普通按钮控件一样（部分没有。比如`menu`方法和相关方法），具体可以看官方文档。

### 26.3 信号和槽

`QRadioButton`单选按钮控件支持以下信号（部分）：

- `clicked`信号，点击（包含鼠标按键按下、弹起两个过程）按钮时触发。

- `pressed`信号，按下按钮时触发。

- `released`信号，松开按钮时触发。

- `toggled`信号，切换按钮的勾选状态时触发。

`QRadioButton`单选按钮控件支持以下槽（部分）：

- `click`方法，点击按钮。
- `toggle`方法，切换按钮的勾选状态。
- `animateClick`方法，点击按钮，同时播放点击动画。

## 27 `QCheckBox`多选按钮控件

`QCheckBox`多选按钮控件用起来几乎和`QRadioButton`单选按钮控件一样，上一章的例子，直接改名就能用：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QCheckBox
)

app = QApplication()
window = QWidget()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

button = QCheckBox(
    '选项1',
    window,
)
button.setChecked(True)
button2 = QCheckBox(
    '选项2',
    window,
)
button2.move(
    0,30
)

window.show()
app.exec()
```

![2026_27_1](qt_for_python_pro.assets/2026_27_1.png)

当然，几乎一样不代表完全一样，二者还是有一些差异，首先，既然是多选，哪怕父控件相同，每个选项的勾选状态也是独立的，默认不会自动独占（也可以启用）。此外，`QCheckBox`多选按钮控件的勾选状态也不是简单的两种。具体相关差异的示例可以参考官方文档或者后面的内容。

`QCheckBox`多选按钮控件的继承关系如下：

![2026_27_2](qt_for_python_pro.assets/2026_27_2.png)

相关文档的链接如下：

- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCheckBox.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html

### 27.1 初始化方法

`QCheckBox`多选按钮控件有多种初始化方法（参数名及类型提示来自`QtWidgets.pyi`）。

- 第一种初始化方法支持以下参数：

  - `text`参数，仅限位置参数（第一个位置参数），字符串类型，表示显示在按钮上的文字。

  - `parent`参数，`PySide6.QtWidgets.QWidget`类型，表示父控件。如果指定了父控件，那么该控件显示时，会使用父控件的位置或者嵌在父控件内（取决于该控件是否支持嵌入到其他控件）。不指定或者为`None`，则控件会在独立窗口中显示。

  - `tristate`参数，仅限关键字参数，布尔类型，表示按钮的勾选状态是否为三种（未勾选、半勾选、勾选）。

    示例如下：

    ```python3
    from PySide6.QtWidgets import (
        QApplication,
        QWidget,
        QCheckBox
    )
    from PySide6.QtCore import Qt
    
    app = QApplication()
    window = QWidget()
    window.setWindowTitle('认识各种按钮')
    window.resize(400, 300)
    
    button = QCheckBox(
        '选项1',
        window,
        tristate=True,
    )
    button.setCheckState(
        Qt.CheckState.PartiallyChecked
    )
    button2 = QCheckBox(
        '选项2',
        window,
    )
    button2.move(
        0,30
    )
    
    window.show()
    app.exec()
    ```

    ![2026_27_3](qt_for_python_pro.assets/2026_27_3.png)

  第二种初始化方法支持以下参数：

  - `parent`参数，含义、用法参考前面。
  - `tristate`参数，含义、用法参考前面。

### 27.2 方法、控件属性

`QCheckBox`多选按钮控件支持以下方法（部分，含控件属性）：

- `checkState`方法（控件属性，可使用`setCheckState`方法设置），返回控件的勾选状态。

- `isTristate`方法（控件属性`tristate`的获取方法，，可使用`setTristate`方法设置），返回控件的勾选状态是否为三种。

- `setCheckState`方法，设置控件的勾选状态。

  该方法支持以下参数：

  - `state`参数，仅限位置参数（第一个位置参数），`PySide6.QtCore.Qt.CheckState`类型，表示控件的勾选状态。`PySide6.QtCore.Qt.CheckState`类型为枚举类型，包含以下枚举成员：
    - `Unchecked`，表示未勾选。
    - `PartiallyChecked`，表示部分勾选。
    - `Checked`，表示勾选。

- `setTristate`方法，设置控件的勾选状态是否为三种。

  该方法支持以下参数：

  - `y`参数，布尔类型，表示控件的勾选状态是否为三种。

### 27.3 信号和槽

`QCheckBox`多选按钮控件支持以下信号（部分）：

- `checkStateChanged`信号，控件的勾选状态变化时触发。

  示例如下：

  ```python3
  from PySide6.QtWidgets import (
      QApplication,
      QWidget,
      QCheckBox
  )
  from PySide6.QtCore import Qt
  
  app = QApplication()
  window = QWidget()
  window.setWindowTitle('认识各种按钮')
  window.resize(400, 300)
  
  button = QCheckBox(
      '选项1',
      window,
      tristate=True,
  )
  button.setCheckState(
      Qt.CheckState.PartiallyChecked
  )
  
  def check_state(state):
      match state:
          case Qt.CheckState.Unchecked:
              print('Unchecked!')
          case Qt.CheckState.PartiallyChecked:
              print('PartiallyChecked!')
          case Qt.CheckState.Checked:
              print('Checked!')
          case _:
              print('Unexpected!')
  
  button.checkStateChanged.connect(check_state)
  
  window.show()
  app.exec()
  ```

- `clicked`信号，点击（包含鼠标按键按下、弹起两个过程）按钮时触发。

- `pressed`信号，按下按钮时触发。

- `released`信号，松开按钮时触发。

- `toggled`信号，切换按钮的勾选状态时触发。

`QCheckBox`多选按钮控件支持以下槽（部分）：

- `click`方法，点击按钮。
- `toggle`方法，切换按钮的勾选状态。
- `animateClick`方法，点击按钮，同时播放点击动画。

## 28 `QCommandLinkButton`命令链接按钮控件

`QCommandLinkButton`命令链接按钮控件看起来、用起来都很像`QPushButton`普通按钮控件：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QCommandLinkButton,
    QPushButton
)

app = QApplication()
window = QWidget()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

button = QCommandLinkButton(
    '命令链接按钮',
    '解释性的文本',
    window,
)

button2 = QPushButton(
    '普通按钮\n解释性的文本',
    window,
)
button2.move(
    0,
    60
)
button2.setIcon(
    button.icon()
)

window.show()
app.exec()
```

![2026_28_1](qt_for_python_pro.assets/2026_28_1.png)

从上面的运行结果看，二者主要区别在于`QCommandLinkButton`命令链接按钮控件看上去更“宽松”，自带一个图标，而且解释性文本与按钮文本有样式的差异，而非普通按钮那种字体完全一样。因此，如果希望用户直接了解按钮的功能，而不是将鼠标悬停在按钮上，看工具提示的话，使用`QCommandLinkButton`命令链接按钮控件更合适。

`QCommandLinkButton`命令链接按钮控件的继承关系如下：

![2026_28_2](qt_for_python_pro.assets/2026_28_2.png)

相关文档的链接如下：

- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCommandLinkButton.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html

### 28.1 初始化方法

`QCommandLinkButton`命令链接按钮控件有多种初始化方法（参数名及类型提示来自`QtWidgets.pyi`）。

第一种初始化方法支持以下参数：

- `text`参数，仅限位置参数（第一个位置参数），字符串类型，表示显示在按钮上的文字。
- `description`参数，仅限位置参数（第二个位置参数），字符串类型，表示显示在按钮上的解释性文字。
- `parent`参数，`PySide6.QtWidgets.QWidget`类型，表示父控件。如果指定了父控件，那么该控件显示时，会使用父控件的位置或者嵌在父控件内（取决于该控件是否支持嵌入到其他控件）。不指定或者为`None`，则控件会在独立窗口中显示。
- `flat`参数，仅限关键字参数，布尔类型，表示控件是否为扁平按钮（鼠标悬停在按钮上的话没有悬浮特效），默认为`False`。

第二种初始化方法支持以下参数：

- `text`参数，仅限位置参数（第一个位置参数），含义、用法参考前面。
- `parent`参数，含义、用法参考前面。
- `description`参数，仅限关键字参数，含义、用法参考前面。
- `flat`参数，仅限关键字参数，含义、用法参考前面。

第三种初始化方法支持以下参数：

- `parent`参数，含义、用法参考前面。
- `description`参数，仅限关键字参数，含义、用法参考前面。
- `flat`参数，仅限关键字参数，含义、用法参考前面。

### 28.2 方法、控件属性

`QCommandLinkButton`命令链接按钮控件支持以下方法（部分，含控件属性）：

- `description`方法（控件属性，可使用`setDescription`方法设置），返回显示在按钮上的解释性文字。

### 28.3 信号和槽

`QCommandLinkButton`命令链接按钮控件支持以下信号（部分）：

- `clicked`信号，点击（包含鼠标按键按下、弹起两个过程）按钮时触发。
- `pressed`信号，按下按钮时触发。

- `released`信号，松开按钮时触发。

- `toggled`信号，切换按钮的勾选状态时触发。

### 28.4 扩展用法

#### 28.4.1 修改图标

`QCommandLinkButton`命令链接按钮控件默认使用了箭头作为图标，那是因为该按钮的外观实际上来源于Windows Vista系统引入的同名控件，Qt通过自己的方式实现了类似的控件。该控件一般用在向导窗口中，用于指示下一步执行什么（直接执行）并且无需查看工具提示。因此，才会默认使用箭头作为图标。

不过，因为是继承自`QPushButton`普通按钮控件，所以，依然可以使用`setIcon`方法修改按钮的图标：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QCommandLinkButton
)
from PySide6.QtGui import QIcon

app = QApplication()
window = QWidget()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

button = QCommandLinkButton(
    '命令链接按钮',
    '解释性的文本',
    window,
)
button.setIcon(
    QIcon.fromTheme(
        QIcon.ThemeIcon.ApplicationExit
    )
)

window.show()
app.exec()
```

![2026_28_3](qt_for_python_pro.assets/2026_28_3.png)

## 29 `QToolButton`工具按钮控件

前面介绍的按钮都比较简单，难免有读者觉得笔者有点“敷衍”。那么，本章就顺势介绍一下用起来有点复杂的`QToolButton`工具按钮控件。

先看一下该控件的“错误”用法：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QToolButton
)

app = QApplication()
window = QWidget()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

button = QToolButton(
    window,
)
button.setText('工具按钮')

window.show()
app.exec()
```

![2026_29_1](qt_for_python_pro.assets/2026_29_1.png)

运行起来没有报错，看上去也没有异常，为何说这是“错误”用法呢？那是因为该控件一般与`QToolBar`工具栏控件、`QMainWindow`主窗口控件搭配使用，因此，“正确”用法应当是：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolButton,
    QToolBar
)

app = QApplication()
window = QMainWindow()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

toolbar = QToolBar('工具栏')
window.addToolBar(toolbar)

button = QToolButton()
button.clicked.connect(lambda:print('Clicked!'))
button.setText('工具按钮')
toolbar.addWidget(
    button
)

window.show()
app.exec()
```

![2026_29_2](qt_for_python_pro.assets/2026_29_2.png)

读者可以在运行之后拖动按钮左边的虚线，移动工具栏到任意位置。

这里提前为好学的读者预告一下注意事项（不是本章重点，后续介绍相关控件时再细讲），免得读者探索`QToolBar`工具栏控件的初始化参数时遇到难以理解的问题：

`QToolBar`工具栏控件的初始化参数并非都可以使用，官方文档中的只读属性——`floating`控件属性，被`QtWidgets.pyi`的生成工具错误捕获，导致初始化方法中包含了`floating`参数，但实际上该参数并不存在也不能使用。

`QToolButton`工具按钮控件的继承关系如下：

![2026_29_3](qt_for_python_pro.assets/2026_29_3.png)

相关文档的链接如下：

- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolButton.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html

### 29.1 初始化方法

`QToolButton`工具按钮控件的初始化方法（参数名及类型提示来自`QtWidgets.pyi`）支持以下参数：

- `parent`参数，`PySide6.QtWidgets.QWidget`类型，表示父控件。
- `popupMode`参数，仅限关键字参数，`PySide6.QtWidgets.QToolButton.ToolButtonPopupMode`类型，表示如何显示按钮的弹出菜单，默认为`PySide6.QtWidgets.QToolButton.ToolButtonPopupMode.MenuButtonPopup`，需要按住按钮一段时间（由`PySide6.QtWidgets.QStyle.StyleHint.SH_Menu_SubMenuPopupDelay`定义）才能弹出。
- `toolButtonStyle`参数，仅限关键字参数，`PySide6.QtCore.Qt.ToolButtonStyle`类型，表示按钮的显示样式（仅文本、仅图标、图标加文本），默认为`PySide6.QtCore.Qt.ToolButtonStyle.ToolButtonIconOnlyp`（仅图标）。
- `autoRaise`参数，仅限关键字参数，布尔类型，表示是否启用鼠标悬停的样式。当该控件与`QToolBar`工具栏控件组合使用时，该参数始终为`True`，其他情况默认为`False`。注意，应用程序的主题非`'Fusion'`时，该样式受限于系统主题，可能不明显。
- `arrowType`参数，仅限关键字参数，`PySide6.QtCore.Qt.ArrowType`类型，当是否将按钮图标强制设置为箭头，默认为`PySide6.QtCore.Qt.ArrowType.NoArrow`，即不设置为箭头。

### 29.2 方法、控件属性

`QToolButton`工具按钮控件支持以下方法（部分，含控件属性）：

- `arrowType`方法（控件属性，可使用`setArrowType`方法设置），含义同`arrowType`参数。
- `autoRaise`方法（控件属性，可使用`setAutoRaise`方法设置），含义同`autoRaise`参数。
- `defaultAction`方法（控件属性，可使用`setDefaultAction`方法设置），表示按钮的默认动作。
- `menu`方法（控件属性，可使用`setMenu`方法设置），返回弹出的菜单。
- `popupMode`方法（控件属性，可使用`setPopupMode`方法设置），含义同`popupMode`参数。

### 29.3 信号和槽

`QToolButton`工具按钮控件支持以下信号（部分）：

- `triggered`信号，按钮的默认动作触发时触发。
- `clicked`信号，点击（包含鼠标按键按下、弹起两个过程）按钮时触发。
- `pressed`信号，按下按钮时触发。
- `released`信号，松开按钮时触发。
- `toggled`信号，切换按钮的勾选状态时触发。

`QToolButton`工具按钮控件支持以下槽（部分）：

- `showMenu`方法，弹出菜单。
- `click`方法，点击按钮。
- `toggle`方法，切换按钮的勾选状态。
- `animateClick`方法，点击按钮，同时播放点击动画。

### 29.4 扩展用法

#### 29.4.1 按钮的显示样式

前面介绍过`toolButtonStyle`参数表示按钮的显示样式（仅文本、仅图标、图标加文本），以下为该参数各个参数值的对比示例：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolButton,
    QToolBar
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

app = QApplication()
window = QMainWindow()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

# 使用Fusion主题，让悬停效果更明显
app.setStyle('Fusion')
toolbar = QToolBar('工具栏')
window.addToolBar(toolbar)

buttons = []
for i in [
    Qt.ToolButtonStyle.ToolButtonFollowStyle,
    Qt.ToolButtonStyle.ToolButtonIconOnly,
    Qt.ToolButtonStyle.ToolButtonTextBesideIcon,
    Qt.ToolButtonStyle.ToolButtonTextOnly,
    Qt.ToolButtonStyle.ToolButtonTextUnderIcon
]:
    button = QToolButton(
        toolButtonStyle=i,
    )
    button.setText('工具按钮')
    button.setIcon(
        QIcon.fromTheme(
            QIcon.ThemeIcon.Battery
        )
    )
    buttons.append(button)
    toolbar.addWidget(
        buttons[-1]
    )

window.show()
app.exec()
```

![2026_29_4](qt_for_python_pro.assets/2026_29_4.png)

注意，`Qt.ToolButtonStyle.ToolButtonFollowStyle`表示取决于系统默认样式，在Windows系统上为只显示图标。

#### 29.4.2 菜单的弹出模式

`popupMode`参数表示如何显示按钮的弹出菜单，以下为该参数各个参数值的对比示例：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolButton,
    QToolBar,
    QMenu
)

app = QApplication()
window = QMainWindow()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

# 使用Fusion主题，让悬停效果更明显
app.setStyle('Fusion')
toolbar = QToolBar('工具栏')
window.addToolBar(toolbar)

buttons = []
menu = QMenu()
menu.addAction('菜单项')
for i in [
    QToolButton.ToolButtonPopupMode.DelayedPopup,
    QToolButton.ToolButtonPopupMode.InstantPopup,
    QToolButton.ToolButtonPopupMode.MenuButtonPopup,

]:
    button = QToolButton(
        popupMode=i,
    )
    button.setText('工具按钮')
    button.setMenu(menu)
    buttons.append(button)
    toolbar.addWidget(
        buttons[-1]
    )

window.show()
app.exec()
```

#### 29.4.3 按钮的默认动作

前面介绍`defaultAction`方法时说过一个概念——“动作”，这里简单说一下这个方法和动作的用法。至于动作的完整用法，将在后面介绍`QAction`类时展开。

动作（`QAction`类）可以理解为有形交互之后执行的无形操作：点击按钮、菜单之后打开文件，按下按键之后退出程序。

总之，动作是个抽象的概念，可以视作比响应函数更统一的响应操作。

对于支持动作的控件而言（不是所有控件都支持动作），定义动作时，可以设置一些控件支持的样式（比如文本、图标）。这样，当控件设置动作时，动作的样式会优先生效。

示例如下：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolButton,
    QToolBar
)
from PySide6.QtGui import QAction

app = QApplication()
window = QMainWindow()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

# 使用Fusion主题，让悬停效果更明显
app.setStyle('Fusion')
toolbar = QToolBar('工具栏')
window.addToolBar(toolbar)

button = QToolButton()
button.setText('工具按钮')

action = QAction(
    '退出程序', 
    toolTip='关闭窗口并退出程序'
)
action.triggered.connect(app.quit)
button.setDefaultAction(
    action
)
toolbar.addWidget(
    button
)

window.show()
app.exec()
```

![2026_29_5](qt_for_python_pro.assets/2026_29_5.png)

## 30 槽函数的自动连接

一般来说，槽函数与直接使用函数没什么区别，就好像下面改自前面的示例，使用普通函数代替槽函数：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton
)

app = QApplication()
window = QWidget()
window.setWindowTitle('信号与事件')
window.resize(400,300)
button = QPushButton('click',window)

# 信号，支持连接多个槽
button.clicked.connect(lambda :print('button is clicked'))
# 定义槽函数（伪），其实就是一般函数，可以勉强用，但功能上不如真的槽函数强大
def on_clicked():
    print('button is clicked2')

button.clicked.connect(on_clicked)

window.show()
app.exec()
```

执行效果是一样的，但为什么还要定义槽函数呢？这就不得不说槽函数的自动连接功能，即无需手动连接所有的信号和槽，有一个简单的方法自动将槽函数与特定信号连接。

想要自动连接生效，有以下关键点：

- 发出信号的控件必须设置`objectName`（在UI文件中定义，或者使用`setObjectName`方法显式设置）。

- 槽函数必须在类（继承自`QWidget`）内定义，并且命名符合要求。

  示例如下：

  ```python3
  @Slot()
  def on_{objectName}_{signalName}(self, ...):
      ...
  ```

  命名要求如下：

  - 必须使用“on_”为前缀。

  - 必须包含“{objectName}”——发送信号的控件的对象名（ 控件属性`objectName`）。
  - 必须包含“{signalName}”，——信号的变量名（即信号被分配给哪个变量，并且信号的参数签名与槽函数装饰器一致）。

- 在控件挂载、初始化完毕之后，执行`QMetaObject.connectSlotsByName(self)`，进行自动连接。

具体示例如下：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton
)
from PySide6.QtCore import Slot,QMetaObject

app = QApplication()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('自动连接槽函数')
        self.resize(400,300)
        self.button = QPushButton('click',self)
        self.button.setObjectName('button')
        QMetaObject.connectSlotsByName(self)
    @Slot()
    def on_button_clicked(self):
        print('clicked!!!')

window = Window()

window.show()
app.exec()
```

只要是信号都可以自动连接，自定义信号也可以：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton
)
from PySide6.QtCore import Slot,QMetaObject,Signal

app = QApplication()

class Window(QWidget):
    # 创建自定义信号
    mySignal = Signal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle('自动连接槽函数（自定义信号）')
        self.resize(400,300)
        self.button = QPushButton('click',self)
        self.button.clicked.connect(lambda:self.mySignal.emit('Hello'))
        self.setObjectName('window')
        QMetaObject.connectSlotsByName(self)
    
    @Slot(str)
    def on_window_mySignal(self,string):
        print(string)
        print('window is clicked!!!')

window = Window()

window.show()
app.exec()
```

## 31 重载信号

上一章介绍槽函数的自动连接时，最后一个示例使用了自定义的信号，本章顺便介绍一下自定义信号的进阶用法——重载信号。

为什么要用重载信号？上一章定义了一个简单的信号，只传入一个字符串类型的参数。假如，一个信号支持多种类型的参数（甚至无参数），想让同一个信号接收不同参数时对应不同的槽函数，就要用到重载信号。

所谓重载信号，可以简单理解为定义信号时，一次性定义信号支持的各种参数类型及其组合，无需为每一种组合分配一个变量，同时使用时也比较清晰明了：

```python3
mySignal = Signal((),(str,),(int,))
```

不使用元组的话，表示信号仅支持一种参数组合；当使用元组表示每一种参数组合时，表示信号支持每个元组对应的参数组合。此时，可以使用`mySignal[str].connect`方法连接对应参数组合的信号与槽函数。

注意，可能其他教程中使用列表表示参数组合，但在当版本（6.10.x）中，只能使用元组。

示例如下：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton
)
from PySide6.QtCore import Slot,Signal

app = QApplication()

class Window(QWidget):
    # 支持的其他类型必须使用元组来表明同级
    mySignal = Signal((),(str,),(int,))
    def __init__(self):
        super().__init__()
        self.setWindowTitle('重载信号')
        self.resize(400,300)
        self.mySignal.connect(self.on_mySignal)
        self.mySignal[str].connect(self.on_mySignal_str)
        self.mySignal[int].connect(self.on_mySignal_int)
        self.button1 = QPushButton('click[]',self)
        self.button1.clicked.connect(lambda:self.mySignal.emit())
        self.button2 = QPushButton('click[str]',self)
        self.button2.clicked.connect(lambda:self.mySignal[str].emit('Hello'))
        self.button2.move(0,30)
        self.button3 = QPushButton('click[int]',self)
        self.button3.clicked.connect(lambda:self.mySignal[int].emit(2026))
        self.button3.move(0,60)

    @Slot()
    def on_mySignal(self):
        print('mySignal[] is emitted!!!')

    @Slot(str)
    def on_mySignal_str(self,string):
        print(string)
        print('mySignal[str] is emitted!!!')

    @Slot(int)
    def on_mySignal_int(self,integer):
        print(integer)
        print('mySignal[int] is emitted!!!')

window = Window()

window.show()
app.exec()
```

当然，如果觉得每个参数组合都要单独连接一次槽函数甚至单独连接一个槽函数，有点麻烦的话，槽函数同样也支持类似的“重载”操作，只需将装饰器用在同一个函数上即可：

```python3
@Slot()
@Slot(int)
@Slot(str)
def on_window_mySignal(self,x=None):
    if x:
        print(x)
    print(f'mySignal[{type(x).__name__ if x else ""}] is emitted!!!')
```

可能读者也发现了上面的槽函数名与上一章最后的自定义信号示例相同。没错，如果参数组合包含无参数的情况，只能使用槽函数的自动连接注册：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton
)
from PySide6.QtCore import Slot,Signal,QMetaObject

app = QApplication()

class Window(QWidget):
    # 支持的其他类型必须使用元组来表明同级
    mySignal = Signal((),(str,),(int,))
    def __init__(self):
        super().__init__()
        self.setWindowTitle('重载信号')
        self.resize(400,300)
        self.button1 = QPushButton('click[]',self)
        self.button1.clicked.connect(lambda:self.mySignal.emit())
        self.button2 = QPushButton('click[str]',self)
        self.button2.clicked.connect(lambda:self.mySignal[str].emit('Hello'))
        self.button2.move(0,30)
        self.button3 = QPushButton('click[int]',self)
        self.button3.clicked.connect(lambda:self.mySignal[int].emit(2026))
        self.button3.move(0,60)
        self.setObjectName('window')
        QMetaObject.connectSlotsByName(self)

    @Slot()
    @Slot(int)
    @Slot(str)
    def on_window_mySignal(self,x=None):
        if x:
            print(x)
        print(f'mySignal[{type(x).__name__ if x else ""}] is emitted!!!')

window = Window()

window.show()
app.exec()
```

若是不使用槽函数的自动连接，则信号、槽函数的无参数版本不能与有参数版本共用槽函数，并且槽函数的装饰器不能组合（也无需组合）：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton
)
from PySide6.QtCore import Slot,Signal

app = QApplication()

class Window(QWidget):
    # 支持的其他类型必须使用元组来表明同级
    mySignal = Signal((),(str,),(int,))
    def __init__(self):
        super().__init__()
        self.setWindowTitle('重载信号')
        self.resize(400,300)
        self.mySignal.connect(self.on_mySignal_zero)
        self.mySignal[str].connect(self.on_mySignal)
        self.mySignal[int].connect(self.on_mySignal)
        self.button1 = QPushButton('click[]',self)
        self.button1.clicked.connect(lambda:self.mySignal.emit())
        self.button2 = QPushButton('click[str]',self)
        self.button2.clicked.connect(lambda:self.mySignal[str].emit('Hello'))
        self.button2.move(0,30)
        self.button3 = QPushButton('click[int]',self)
        self.button3.clicked.connect(lambda:self.mySignal[int].emit(2026))
        self.button3.move(0,60)

    @Slot()
    def on_mySignal_zero(self):
        print('mySignal[] is emitted!!!')

    @Slot()
    def on_mySignal(self,x):
        print(x)
        print(f'mySignal[{type(x).__name__}] is emitted!!!')

window = Window()

window.show()
app.exec()
```

需要注意，信号与槽函数手动连接时，槽函数装饰器的参数类型并非必需的，因此上面的示例才能正常使用。实际上，本章第一个示例中，去掉槽函数装饰器的参数，全部使用无参数的装饰器，也不会报错：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton
)
from PySide6.QtCore import Slot,Signal

app = QApplication()

class Window(QWidget):
    # 支持的其他类型必须使用元组来表明同级
    mySignal = Signal((),(str,),(int,))
    def __init__(self):
        super().__init__()
        self.setWindowTitle('重载信号')
        self.resize(400,300)
        self.mySignal.connect(self.on_mySignal)
        self.mySignal[str].connect(self.on_mySignal_str)
        self.mySignal[int].connect(self.on_mySignal_int)
        self.button1 = QPushButton('click[]',self)
        self.button1.clicked.connect(lambda:self.mySignal.emit())
        self.button2 = QPushButton('click[str]',self)
        self.button2.clicked.connect(lambda:self.mySignal[str].emit('Hello'))
        self.button2.move(0,30)
        self.button3 = QPushButton('click[int]',self)
        self.button3.clicked.connect(lambda:self.mySignal[int].emit(2026))
        self.button3.move(0,60)

    @Slot()
    def on_mySignal(self):
        print('mySignal[] is emitted!!!')

    @Slot()
    def on_mySignal_str(self,string):
        print(string)
        print('mySignal[str] is emitted!!!')

    @Slot()
    def on_mySignal_int(self,integer):
        print(integer)
        print('mySignal[int] is emitted!!!')

window = Window()

window.show()
app.exec()
```

但还是建议读者写代码时加上参数，方便自动连接，避免意料之外的错误（现在不报错不代表其他场景和后续版本没问题），也方便后续调试代码时检查参数类型。

## 32 后台运行

### 32.1 事出有因

笔者在阅读《Qt for Python PySide6 GUI界面开发详解与实例》时，偶然看到`QApplication`实例的`setQuitOnLastWindowClosed`方法用于设置关闭最后一个窗口后是否退出程序，也就是是否在关闭最后一个窗口后程序是否继续运行。笔者心想，这不就是传说中的“后台运行”吗？

于是，抱着验证代码的态度，笔者做了个简单的小程序，没想到，由此牵出一系列的问题。

### 32.2 简单实现

代码很简单，只需给`setQuitOnLastWindowClosed`方法传入`False`，关闭最后一个窗口后，程序就不会退出：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget
)

app = QApplication()
app.setQuitOnLastWindowClosed(False)

window = QWidget()
window.setWindowTitle('后台运行')
window.resize(400, 300)

window.show()
app.exec()
```

不过，看似简单的代码，却在实际使用时，遇到了小问题——程序没法正常退出了。

### 32.3 解决问题

解决方法很简单，只需提供退出程序的方法即可。但是，如何让用户交互成了问题。现在程序的窗口关闭（隐藏）了，在窗口中添加任何控件都没法显示，用户只能使用任务管理器或者快捷键退出程序。

快捷键是个不错的方案，但是需要注意的是，快捷键默认只在程序获得焦点时生效，想要程序在后台时生效，只能注册全局热键，而Qt默认不提供这样的功能。当然，其他库提供了类似的功能，并非不能实现，只是使用起来会有诸多不便，并非完美的解决方案。

快捷键这条路走不通，难道程序后台运行之后只能强制结束，也不能让窗口重新显示吗？

笔者看着右下角诸多的托盘图标，忽然来了灵感。既然其他程序后台运行时，可以通过点击托盘图标显示主窗口，那Qt有没有类似功能？

笔者简单搜索了一下，找到了提供系统托盘功能的`QSystemTrayIcon`系统托盘图标类。该类可以为程序生成一个系统托盘，这样就能通过系统托盘图标操作主窗口和程序了。

说干就干，代码并不难，但是需要注意的是，有的系统不一定支持系统托盘，需要使用`QSystemTrayIcon.isSystemTrayAvailable`方法检查一下。另外，`QSystemTrayIcon`系统托盘图标类的初始化参数`visible`必须手动设置为`True`，否则要额外调用一次`show`方法，不然系统托盘图标不会显示：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QSystemTrayIcon
)

app = QApplication()

if QSystemTrayIcon.isSystemTrayAvailable():
    app.setQuitOnLastWindowClosed(False)
    tray = QSystemTrayIcon(
        app.style().standardIcon(
            app.style().StandardPixmap.SP_ComputerIcon
        ),
        app,
        visible=True
    )
    #tray.show()
else:
    print('当前系统不支持系统托盘。')

window = QWidget()
window.setWindowTitle('后台运行')
window.resize(400, 300)

window.show()
app.exec()
```

看似有了解决方法，但结果依然不符合要求：无论单击、双击还是右击系统托盘图标，后台运行之后的窗口都不会再次显示。

思路是对的，只是解决方法还没做完，因为默认情况下，系统托盘没有人任何交互逻辑，需要开发者手动添加。

点击系统托盘图标，会触发`activated`信号。因此，只需将该信号连接到显示窗口的槽函数，就能解决之前的问题（笔者顺便在窗口中加了个退出程序的按钮）：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QSystemTrayIcon,
    QPushButton
)

app = QApplication()

if QSystemTrayIcon.isSystemTrayAvailable():
    app.setQuitOnLastWindowClosed(False)
    tray = QSystemTrayIcon(
        app.style().standardIcon(
            app.style().StandardPixmap.SP_ComputerIcon
        ),
        app,
        visible=True
    )
    tray.activated.connect(lambda:window.show())
else:
    print('当前系统不支持系统托盘。')

window = QWidget()
window.setWindowTitle('后台运行')
window.resize(400, 300)

button = QPushButton(
    '退出程序',
    window
)
button.clicked.connect(app.quit)

window.show()
app.exec()
```

### 32.4 完善方案

问题已经解决，但方案还有优化的空间：任意键点击系统托盘都会显示主窗口，能不能实现只有左键点击才会显示？

当然可以！`activated`信号会接收一个表示原因的参数，也就是使用什么按键触发的信号（左键单击、右键单击、中间单击、左键双击）。因此，只需给槽函数添加一个参数，并判断该参数的值即可：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QSystemTrayIcon,
    QPushButton
)

app = QApplication()

if QSystemTrayIcon.isSystemTrayAvailable():
    app.setQuitOnLastWindowClosed(False)
    tray = QSystemTrayIcon(
        app.style().standardIcon(
            app.style().StandardPixmap.SP_ComputerIcon
        ),
        app,
        visible=True
    )
    # 只有左键单击托盘图标才会显示主窗口
    tray.activated.connect(
        lambda e:window.show() if e == QSystemTrayIcon.ActivationReason.Trigger else None)
else:
    print('当前系统不支持系统托盘。')

window = QWidget()
window.setWindowTitle('后台运行')
window.resize(400, 300)

button = QPushButton(
    '退出程序',
    window
)
button.clicked.connect(app.quit)

window.show()
app.exec()
```

注意，左键双击包括左键单击，因此双击、单击都会显示窗口，如果想要仅限双击生效，需要修改判断的值：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QSystemTrayIcon,
    QPushButton
)

app = QApplication()

if QSystemTrayIcon.isSystemTrayAvailable():
    app.setQuitOnLastWindowClosed(False)
    tray = QSystemTrayIcon(
        app.style().standardIcon(
            app.style().StandardPixmap.SP_ComputerIcon
        ),
        app,
        visible=True
    )
    # 只有左键双击托盘图标才会显示主窗口
    tray.activated.connect(
        lambda e:window.show() if e == QSystemTrayIcon.ActivationReason.DoubleClick else None)
else:
    print('当前系统不支持系统托盘。')

window = QWidget()
window.setWindowTitle('后台运行')
window.resize(400, 300)

button = QPushButton(
    '退出程序',
    window
)
button.clicked.connect(app.quit)

window.show()
app.exec()
```

左键功能有了，右键的菜单也要安排上：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QSystemTrayIcon,
    QPushButton,
    QMenu
)

app = QApplication()

if QSystemTrayIcon.isSystemTrayAvailable():
    app.setQuitOnLastWindowClosed(False)
    tray = QSystemTrayIcon(
        app.style().standardIcon(
            app.style().StandardPixmap.SP_ComputerIcon
        ),
        app,
        visible=True
    )
    # 只有左键双击托盘图标才会显示主窗口
    tray.activated.connect(
        lambda e:window.show() if e == QSystemTrayIcon.ActivationReason.DoubleClick else None
    )
    # 给托盘添加一个右键菜单，可以退出
    tray_menu = QMenu()
    tray_menu.addAction(
        '显示主窗口'
    ).triggered.connect(lambda:window.show())
    tray_menu.addAction(
        '退出程序'
    ).triggered.connect(app.quit)
    tray.setContextMenu(tray_menu)
else:
    print('当前系统不支持系统托盘。')

window = QWidget()
window.setWindowTitle('后台运行')
window.resize(400, 300)

button = QPushButton(
    '退出程序',
    window
)
button.clicked.connect(app.quit)

window.show()
app.exec()
```

也可以添加一个多选按钮控件，用于切换是否启用后台运行：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QSystemTrayIcon,
    QPushButton,
    QMenu,
    QCheckBox
)

app = QApplication()

if QSystemTrayIcon.isSystemTrayAvailable():
    tray = QSystemTrayIcon(
        app.style().standardIcon(
            app.style().StandardPixmap.SP_ComputerIcon
        ),
        app,
        visible=True
    )
    # 只有左键双击托盘图标才会显示主窗口
    tray.activated.connect(
        lambda e:window.show() if e == QSystemTrayIcon.ActivationReason.DoubleClick else None
    )
    # 给托盘添加一个右键菜单，可以退出
    tray_menu = QMenu()
    tray_menu.addAction(
        '显示主窗口'
    ).triggered.connect(lambda:window.show())
    tray_menu.addAction(
        '退出程序'
    ).triggered.connect(app.quit)
    tray.setContextMenu(tray_menu)
else:
    print('当前系统不支持系统托盘。')

window = QWidget()
window.setWindowTitle('后台运行')
window.resize(400, 300)

# 虽然下面判断的是字符串，但仍然需要导入Qt类
from PySide6.QtCore import Qt  # noqa: E402, F401
checkbox = QCheckBox(
    '后台运行',
    window,
)
checkbox.checkStateChanged.connect(
    # 判断枚举对象
    #lambda e: (app.setQuitOnLastWindowClosed(False) if e == Qt.CheckState.Checked else app.setQuitOnLastWindowClosed(True))
    lambda e: (app.setQuitOnLastWindowClosed(False) if str(e) == 'CheckState.Checked' else app.setQuitOnLastWindowClosed(True))
)

button = QPushButton(
    '退出程序',
    window
)
button.clicked.connect(app.quit)
button.move(
    0,
    30
)

window.show()
app.exec()
```

也可以在关闭窗口时询问是否后台运行：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QSystemTrayIcon,
    QPushButton,
    QMenu,
    QMessageBox
)
from PySide6.QtCore import QEvent

app = QApplication()

if QSystemTrayIcon.isSystemTrayAvailable():
    #app.setQuitOnLastWindowClosed(False)
    tray = QSystemTrayIcon(
        app.style().standardIcon(
            app.style().StandardPixmap.SP_ComputerIcon
        ),
        app,
        visible=True
    )
    # 只有左键双击托盘图标才会显示主窗口
    tray.activated.connect(
        lambda e:window.show() if e == QSystemTrayIcon.ActivationReason.DoubleClick else None
    )
    # 给托盘添加一个右键菜单，可以退出
    tray_menu = QMenu()
    tray_menu.addAction(
        '显示主窗口'
    ).triggered.connect(lambda:window.show())
    tray_menu.addAction(
        '退出程序'
    ).triggered.connect(app.exit)
    tray.setContextMenu(tray_menu)
else:
    print('当前系统不支持系统托盘。')

window = QWidget()
window.setWindowTitle('后台运行')
window.resize(400, 300)

def on_close(e:QEvent):
    result = QMessageBox.question(
        window,
        '消息',
        '是否后台运行？',
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No
    )
    if result == QMessageBox.Yes:
        app.setQuitOnLastWindowClosed(False)
    else:
        app.setQuitOnLastWindowClosed(True)


window.closeEvent = on_close

button = QPushButton(
    '退出程序',
    window
)
button.clicked.connect(app.exit)

window.show()
app.exec()
```

![2026_32_1](qt_for_python_pro.assets/2026_32_1.png)

不过，此时需要注意，`app.quit`方法也会触发关闭事件的弹窗，需要改用`app.exit`方法来强制退出程序。

## 33 `QComboBox`下拉组合框控件

`QComboBox`下拉组合框控件也叫下拉选择框，相比于前面介绍过的单选、多选控件，下拉组合框可以将选项折叠起来，节省直接占用的空间：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QComboBox
)

app = QApplication()
window = QWidget()
window.setWindowTitle('认识下拉组合框')
window.resize(400, 300)

box = QComboBox(
    window,
)
for i in range(1,4):
    box.addItem(
        f'选项{i}',
        i
    )

window.show()
app.exec()
```

![2026_33_1](qt_for_python_pro.assets/2026_33_1.png)

`QComboBox`下拉组合框控件的继承关系如下：

![2026_33_2](qt_for_python_pro.assets/2026_33_2.png)

相关文档的链接如下：

- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QComboBox.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html

### 33.1 初始化方法

`QComboBox`下拉组合框控件的初始化方法（参数名及类型提示来自`QtWidgets.pyi`）支持以下参数：

- `parent`参数，`PySide6.QtWidgets.QWidget`类型，表示父控件。如果指定了父控件，那么该控件显示时，会使用父控件的位置或者嵌在父控件内（取决于该控件是否支持嵌入到其他控件）。不指定或者为`None`，则控件会在独立窗口中显示。

- `editable`参数，仅限关键字参数，布尔类型，表示是否允许编辑组合框内的选项，默认为`False`。编辑之后，直接回车的话，会添加新的选项。

- `maxVisibleItems`参数，仅限关键字参数，整数类型，表示下拉框最多显示多少个选项，默认不限制。

- `maxCount`参数，仅限关键字参数，整数类型，表示控件最多有多少个选项，默认不限制。

- `insertPolicy`参数，仅限关键字参数，`PySide6.QtWidgets.QComboBox.InsertPolicy`类型，表示启用`editable`参数时添加新选项的策略。

  `PySide6.QtWidgets.QComboBox.InsertPolicy`类型是枚举类型，包含以下枚举成员：

  - `NoInsert`，表示不允许添加新选项。
  - `InsertAtTop`，表示在所有选项的前面添加新选项。
  - `InsertAtCurrent`，表示替换当前选项。
  - `InsertAtBottom`，表示在所有选项的后面添加新选项。这也是该参数的默认值。
  - `InsertAfterCurrent`，表示在当前选项的前面添加新选项。
  - `InsertBeforeCurrent`，表示在当前选项的后面添加新选项。
  - `InsertAlphabetically`，表示按字符顺序插入。

- `sizeAdjustPolicy`参数，仅限关键字参数，`PySide6.QtWidgets.QComboBox.SizeAdjustPolicy`类型，表示选项内容变化时（比如启用`editable`参数、添加新选项）控件尺寸的调整策略。

  `PySide6.QtWidgets.QComboBox.InsertPolicy`类型是枚举类型，包含以下枚举成员：

  - `AdjustToContents`，表示始终根据选项内容多少调整控件大小。
  - `AdjustToContentsOnFirstShow`，表示在第一次显示时根据选项内容多少调整控件大小。这也是该参数的默认值。
  - `AdjustToMinimumContentsLengthWithIcon`，表示`minimumContentsLength`控件属性加图标的选项大小调整控件大小。注意，启用`editable`参数的话，该策略将无法生效。

- `minimumContentsLength`参数，仅限关键字参数，整数类型，表示选项内容的最小长度，仅在`sizeAdjustPolicy`参数为`PySide6.QtWidgets.QComboBox.InsertPolicy.AdjustToMinimumContentsLengthWithIcon`时生效。默认不限制。

- `iconSize`参数，仅限关键字参数，`PySide6.QtCore.QSize`类型，表示选项图标的大小。

- `placeholderText`参数，仅限关键字参数，字符串类型，表示默认没有选择任何选项时的占位文本。如果不设置该参数，将默认选择第一个选项。

- `duplicatesEnabled`参数，仅限关键字参数，布尔类型，表示启用`editable`参数时添加新选项是否允许重复添加，默认为`False`。注意，使用`addItem`方法、`addItems`方法添加选项的话不受该参数限制，始终可以添加重复选项。

- `frame`参数，仅限关键字参数，布尔类型，表示控件是否额外带一个边框，默认为`True`。

- `labelDrawingMode`参数，仅限关键字参数，`PySide6.QtWidgets.QComboBox.LabelDrawingMode`类型，表示选项文本的渲染模式。

  `PySide6.QtWidgets.QComboBox.LabelDrawingMode`类型是枚举类型，包含以下枚举成员：

  - `UseStyle`，表示使用样式。这也是该参数的默认值。
  - `UseDelegate`，表示使用委托。

### 33.2 方法、控件属性

`QComboBox`下拉组合框控件支持以下方法（部分，含控件属性）：

- `addItem`方法，添加一个选项。
- `addItems`方法，添加多个选项。
- `completer`方法（控件属性，可使用`setCompleter`方法设置），返回控件的自动补全器。
- `count`方法（控件属性），返回控件的选项数。
- `currentData`方法（控件属性），返回控件当前选择选项的选项数据。
- `currentIndex`方法（控件属性，可使用`setCurrentIndex`方法设置），返回控件当前选择选项的索引值。
- `currentText`方法（控件属性，可使用`setCurrentText`方法设置），返回控件当前选择选项的选项文本。
- `duplicatesEnabled`方法（控件属性，可使用`setDuplicatesEnabled`方法设置），返回启用`editable`参数时添加新选项是否允许重复添加。
- `findData`方法，查找选项数据，返回选项的索引值。
- `findText`方法，查找选项文本，返回选项的索引值。
- `hasFrame`方法（控件属性`frame`的获取方法），返回控件是否额外带一个边框。
- `iconSize`方法（控件属性，可使用`setIconSize`方法设置），返回选项图标的大小。
- `insertItem`方法，在指定位置插入一个选项。
- `insertItems`方法，在指定位置插入多个选项。
- `insertPolicy`方法（控件属性，可使用`setInsertPolicy`方法设置），返回启用`editable`参数时添加新选项的策略。
- `insertSeparator`方法，在指定位置插入一条分隔线。
- `isEditable`方法（控件属性`editable`的获取方法，可使用`setEditable`方法设置），返回是否允许编辑组合框内的选项。
- `itemData`方法，返回指定选项的选项数据。
- `itemIcon`方法，返回指定选项的选项图标。
- `itemText`方法，返回指定选项的选项文本。
- `lineEdit`方法，返回启用`editable`参数时的编辑框。
- `maxCount`方法（控件属性，可使用`setMaxCount`方法设置），返回控件最多有多少个选项。
- `maxVisibleItems`方法（控件属性，可使用`setMaxVisibleItems`方法设置），返回下拉框最多显示多少个选项。
- `minimumContentsLength`方法（控件属性，可使用`setMinimumContentsLength`方法设置），返回选项内容的最小长度。
- `model`方法（控件属性，可使用`setModel`方法设置），返回控件的数据模型。
- `modelColumn`方法（控件属性，可使用`setModelColumn`方法设置），返回控件使用数据模型列的索引值。
- `placeholderText`方法（控件属性，可使用`setPlaceholderText`方法设置），返回默认没有选择任何选项时的占位文本。。
- `removeItem`方法，移除指定选项。
- `sizeAdjustPolicy`方法（控件属性，可使用`setSizeAdjustPolicy`方法设置），返回选项内容变化时（比如启用`editable`参数、添加新选项）控件尺寸的调整策略。
- `validator`方法（控件属性，可使用`setValidator`方法设置），返回控件的验证器。
- `view`方法（控件属性，可使用`setView`方法设置），返回下拉框对应的控件。

### 33.3 信号和槽

`QComboBox`下拉组合框控件支持以下信号（部分）：

- `activated`信号，选择选项时触发。
- `currentIndexChanged`信号，当前选择选项的索引值改变时触发。
- `currentTextChanged`信号，当前选择选项的文本改变时触发。
- `editTextChanged`信号，启用`editable`参数时，输入框文本改变时触发（无论是否选择）。
- `highlighted`信号，下拉框中选择选项改变时触发。
- `textActivated`信号，启用`editable`参数时，输入框文本对应选项选择时触发（含创建新选项、选择已有选项之后改变了输入框的文本）。
- `textHighlighted`信号，启用`editable`参数时，下拉框中选择选项改变时触发（无论是否选择）。

`QComboBox`下拉组合框控件支持以下槽（部分）：

- `clear`方法，移除所有选项。
- `clearEditText`方法，启用`editable`参数时，清除输入框文本。
- `setCurrentIndex`方法，修改当前选择的选项。
- `setCurrentText`方法，修改当前选择的选项文本（不影响对应选项的文本）。
- `setEditText`方法，启用`editable`参数时，修改输入框文本。

### 33.4 扩展用法

#### 33.4.1 设置选项图标

添加选项时，可以同时设置选项的图标：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QComboBox,
)
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

app = QApplication()
window = QWidget()
window.setWindowTitle('认识下拉组合框')
window.resize(400, 300)

box = QComboBox(
    window,
    iconSize=QSize(
        40,40
    )
)

for i in range(1,4):
    box.addItem(
        QIcon.fromTheme(
            QIcon.ThemeIcon.Computer
        ),
        f'选项{i}',
        i
    )

window.show()
app.exec()
```

![2026_33_3](qt_for_python_pro.assets/2026_33_3.png)

#### 33.4.2 使用数据模型添加选项

除了单独调用`addItem`方法、`addItems`方法添加选项，还可以使用`setModel`方法何止数据模型，控件将自动基于数据模型中的数据生成对应选项：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QComboBox,
)
from PySide6.QtGui import QStandardItemModel,QStandardItem

app = QApplication()
window = QWidget()
window.setWindowTitle('认识下拉组合框')
window.resize(400, 300)

box = QComboBox(
    window,
)
box2 = QComboBox(
    window,
)
box2.move(
    0,30
)
model = QStandardItemModel()
model.appendRow([QStandardItem('1'),QStandardItem('a')])
model.appendRow([QStandardItem('2'),QStandardItem('b')])
box.setModel(
    model
)
box.setModelColumn(0)
box2.setModel(
    model
)
box2.setModelColumn(1)

window.show()
app.exec()
```

![2026_33_4](qt_for_python_pro.assets/2026_33_4.png)

也可以使用自动补全器，搜索数据模型，手动添加数据模型内的数据：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QComboBox,
    QCompleter
)
from PySide6.QtGui import QStandardItemModel,QStandardItem

app = QApplication()
window = QWidget()
window.setWindowTitle('认识下拉组合框')
window.resize(400, 300)

box = QComboBox(
    window,
    editable=True
)
for i in range(1,4):
    box.addItem(
        f'选项{i}',
        i
    )

model = QStandardItemModel()
model.appendRow([QStandardItem('1'),QStandardItem('a')])
model.appendRow([QStandardItem('2'),QStandardItem('b')])
completer = QCompleter(
    model
)
completer.setCompletionColumn(1)
box.setCompleter(
    completer
)

window.show()
app.exec()
```

![2026_33_5](qt_for_python_pro.assets/2026_33_5.png)

#### 33.4.3 设置选项样式

设置选项样式的方法有两种，一是使用委托（比较复杂），二是使用样式（QSS）。

使用委托的示例（因为用法比较复杂，这里不做展开，后续章节再具体介绍）：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QComboBox,
    QStyledItemDelegate
)
from PySide6.QtCore import QSize

app = QApplication()
window = QWidget()
window.setWindowTitle('认识下拉组合框')
window.resize(400, 300)

box = QComboBox(
    window,
    labelDrawingMode=QComboBox.LabelDrawingMode.UseDelegate
)
for i in range(1,4):
    box.addItem(
        f'选项{i}',
        i
    )

class CustomComboDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def sizeHint(self, option, index):
        # 默认高度
        original_size = super().sizeHint(option, index)
        return QSize(original_size.width()+10, original_size.height()+40)
    
box.setItemDelegate(
    CustomComboDelegate()
)

window.show()
app.exec()
```

![2026_33_6](qt_for_python_pro.assets/2026_33_6.png)

使用样式（QSS）的示例：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QComboBox
)

app = QApplication()
window = QWidget()
window.setWindowTitle('认识下拉组合框')
window.resize(400, 300)

box = QComboBox(
    window,
    labelDrawingMode=QComboBox.LabelDrawingMode.UseDelegate
)
for i in range(1,4):
    box.addItem(
        f'选项{i}',
        i
    )
box.setStyleSheet(
    '''
    QComboBox QAbstractItemView::item {
        /*对应上右下左的边距*/
        margin: 0px 0px 10px 20px; 
    }
    '''
)
window.show()
app.exec()
```

![2026_33_7](qt_for_python_pro.assets/2026_33_7.png)

## 34 `QDateTimeEdit`日期时间编辑框控件

`QDateTimeEdit`日期时间编辑框控件主要用于快捷编辑日期、时间，除了直接输入，右侧还有直接调整数字用的按钮，对于微调场景，操作更方便。

示例如下：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDateTimeEdit,
)
from PySide6.QtCore import QDateTime

app = QApplication()
window = QWidget()
window.setWindowTitle('认识时间控件')
window.resize(400, 300)

date = QDateTimeEdit(
    window,
    dateTime=QDateTime(
        2026,
        1,
        1,
        12,
        30,
        0
    )
)

window.show()
app.exec()
```

![2026_34_1](qt_for_python_pro.assets/2026_34_1.png)

`QDateTimeEdit`日期时间编辑框控件的继承关系如下：

![2026_34_2](qt_for_python_pro.assets/2026_34_2.png)

相关文档的链接如下：

- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDateTimeEdit.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractSpinBox.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html

### 34.1 初始化方法

`QDateTimeEdit`日期时间编辑框控件有多种初始化方法（参数名及类型提示来自`QtWidgets.pyi`）。

第一种初始化方法支持以下参数：

- `d`参数，仅限位置参数（第一个位置参数），`PySide6.QtCore.QDate`类型，表示默认日期，优先级低于`dateTime`参数、`date`参数。
- `parent`参数，`PySide6.QtWidgets.QWidget`类型，表示父控件。如果指定了父控件，那么该控件显示时，会使用父控件的位置或者嵌在父控件内（取决于该控件是否支持嵌入到其他控件）。不指定或者为`None`，则控件会在独立窗口中显示。
- `dateTime`参数，仅限关键字参数，`PySide6.QtCore.QDateTime`类型，表示默认日期和时间，优先级低于`date`参数、`time`参数。
- `date`参数，仅限关键字参数，`PySide6.QtCore.QDate`类型，表示默认日期。
- `time`参数，仅限关键字参数，`PySide6.QtCore.QTime`类型，表示默认时间。
- `maximumDateTime`参数，仅限关键字参数，`PySide6.QtCore.QDateTime`类型，表示日期和时间的最大值。
- `minimumDateTime`参数，仅限关键字参数，`PySide6.QtCore.QDateTime`类型，表示日期和时间的最小值。
- `maximumDate`参数，仅限关键字参数，`PySide6.QtCore.QDate`类型，表示日期的最大值。
- `minimumDate`参数，仅限关键字参数，`PySide6.QtCore.QDate`类型，表示日期的最小值。
- `maximumTime`参数，仅限关键字参数，`PySide6.QtCore.QTime`类型，表示时间的最大值。注意，需要同时指定日期的最大值才能生效。
- `minimumTime`参数，仅限关键字参数，`PySide6.QtCore.QTime`类型，表示时间的最小值。注意，需要同时指定日期的最小值才能生效。
- `displayFormat`参数，仅限关键字参数，字符串类型，表示时间日期的显示格式。支持的格式符如下：
  - “y”表示年，支持“yy”（仅后两位）和“yyyy”两种形式。
  - “M”表示月，支持“M”、“MM”（含补位的前导零）、“MMM”（月份缩写，与系统格式一致）、“MMMM”（月份全称，与系统格式一致）四种形式。
  - “d”表示日期，支持“d”、“dd”（含补位的前导零）、“ddd”（星期缩写，与系统格式一致）、“dddd”（星期全称，与系统格式一致）四种形式。
  - “h”表示小时（12小时制），支持“h”、“hh”（含补位的前导零）两种形式。
  - “H”表示小时（24小时制），支持“H”、“HH”（含补位的前导零）两种形式。
  - “m”表示分钟，支持“m”、“mm”（含补位的前导零）两种形式。
  - “s”表示秒，支持“s”、“ss”（含补位的前导零）两种形式。“z”表示毫秒。
  - “AP”、“A”表示上下午的大写，“ap”、“a”表示上下午的小写。
  - “t”表示时区的缩写，“tt”表示时区偏移量，“ttt”表示时区偏移值（转换为`±{小时}:{分钟}`的表达格式），“tttt”表示时区的名称。

- `calendarPopup`参数，仅限关键字参数，布尔类型，表示是否将调整按钮替换为可弹出日历选择器的按钮，用于快捷选定日期。
- `timeSpec`参数，仅限关键字参数，`PySide6.QtCore.Qt.TimeSpec`类型，表示显示时间的时区基准。
- `timeZone`参数，仅限关键字参数，`PySide6.QtCore.QTimeZone`类型，表示显示时间的时区。

第二种初始化方法支持以下参数：

- `dt`参数，仅限位置参数（第一个位置参数），`PySide6.QtCore.QDateTime`类型，表示默认日期和时间，优先级低于`dateTime`参数、`date`参数、`time`参数。
- `parent`参数，`PySide6.QtWidgets.QWidget`类型，表示父控件。如果指定了父控件，那么该控件显示时，会使用父控件的位置或者嵌在父控件内（取决于该控件是否支持嵌入到其他控件）。不指定或者为`None`，则控件会在独立窗口中显示。
- 仅限关键字参数与第一种初始化方法相同。

第三种初始化方法支持以下参数：

- `t`参数，仅限位置参数（第一个位置参数），`PySide6.QtCore.QTime`类型，表示默认时间，优先级低于`dateTime`参数、`time`参数。
- `parent`参数，`PySide6.QtWidgets.QWidget`类型，表示父控件。如果指定了父控件，那么该控件显示时，会使用父控件的位置或者嵌在父控件内（取决于该控件是否支持嵌入到其他控件）。不指定或者为`None`，则控件会在独立窗口中显示。
- 仅限关键字参数与第一种初始化方法相同。

第四种初始化方法支持以下参数：

- `parent`参数，`PySide6.QtWidgets.QWidget`类型，表示父控件。如果指定了父控件，那么该控件显示时，会使用父控件的位置或者嵌在父控件内（取决于该控件是否支持嵌入到其他控件）。不指定或者为`None`，则控件会在独立窗口中显示。
- 仅限关键字参数与第一种初始化方法相同。

### 34.2 方法、控件属性

`QDateTimeEdit`日期时间编辑框控件支持以下方法（部分，含控件属性）：

- `calendar`方法（控件属性，可使用`setCalendar`方法设置），返回控件使用的日历系统。注意，该控件属性仅当`calendarPopup`参数为`True`时可用。
- `calendarPopup`方法（控件属性，可使用`setCalendarPopup`方法设置），返回控件是否将调整按钮替换为可弹出日历选择器的按钮。
- `calendarWidget`方法（控件属性，可使用`setCalendarWidget`方法设置），返回控件的日历选择器。注意，该控件属性仅当`calendarPopup`参数为`True`时可用。
- `clearMaximumDate`方法，重置控件属性`maximumDate`。
- `clearMaximumDateTime`方法，重置控件属性`maximumDateTime`。
- `clearMaximumTime`方法，重置控件属性`maximumTime`。
- `clearMinimumDate`方法，重置控件属性`minimumDate`。
- `clearMinimumDateTime`方法，重置控件属性`minimumDateTime`。
- `clearMinimumTime`方法，重置控件属性`minimumTime`。
- `currentSection`方法，（控件属性，可使用`setCurrentSection`方法设置），返回当前编辑的时间日期区段。
- `currentSectionIndex`方法，（控件属性，可使用`setCurrentSectionIndex`方法设置），返回当前编辑的时间日期区段的索引值。
- `date`方法，（控件属性，可使用`setDate`方法设置），返回默认日期。
- `dateTime`方法，（控件属性，可使用`setDateTime`方法设置），返回默认日期时间。
- `displayFormat`方法，（控件属性，可使用`setDisplayFormat`方法设置），返回时间日期的显示格式。
- `displayedSections`方法，返回当前显示的时间日期区段。
- `maximumDate`方法，（控件属性，可使用`setMaximumDate`方法设置），返回日期的最大值。
- `maximumDateTime`方法，（控件属性，可使用`setMaximumDateTime`方法设置），返回日期时间的最大值。
- `maximumTime`方法，（控件属性，可使用`setMaximumTime`方法设置），返回时间的最大值。
- `minimumDate`方法，（控件属性，可使用`setMinimumDate`方法设置），返回日期的最小值。
- `minimumDateTime`方法，（控件属性，可使用`setMinimumDateTime`方法设置），返回日期时间的最小值。
- `minimumTime`方法，（控件属性，可使用`setMinimumTime`方法设置），返回时间的最小值。
- `sectionAt`方法，返回指定位置（索引值）的时间日期区段。
- `sectionCount`方法，返回时间日期区段的数量。
- `sectionText`方法，返回指定时间日期区段的文本。
- `setDateRange`方法，设置日期的范围（最小值、最大值）。
- `setDateTimeRange`方法，设置日期时间的范围（最小值、最大值）。
- `setSelectedSection`方法，设置当前选中的时间日期区段。
- `setTimeRange`方法，设置时间的范围（最小值、最大值）。
- `time`方法，（控件属性，可使用`setTime`方法设置），返回默认时间。
- `timeSpec`方法，（控件属性，可使用`setTimeSpec`方法设置），返回显示时间的时区基准。
- `timeZone`方法，（控件属性，可使用`setTimeZone`方法设置），返回显示时间的时区。

### 34.3 信号和槽

`QDateTimeEdit`日期时间编辑框控件支持以下信号（部分）：

- `dateChanged`信号，控件属性`date`改变时触发。
- `dateTimeChanged`信号，控件属性`dateTime`改变时触发。
- `timeChanged`信号，控件属性`time`改变时触发。

`QDateTimeEdit`日期时间编辑框控件支持以下槽（部分）：

- `setDate`方法，修改控件属性`date`。
- `setDateTime`方法，修改控件属性`dateTime`。
- `setTime`方法，修改控件属性`time`。

### 34.4 扩展用法

#### 34.4.1 需要延迟执行的方法

`setCurrentSection`方法、`setCurrentSectionIndex`方法、`setSelectedSection`方法不能立即执行，必须延迟一段时间再执行，这样才能正常生效：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDateTimeEdit,
)
from PySide6.QtCore import QTimer

app = QApplication()
window = QWidget()
window.setWindowTitle('认识时间控件')
window.resize(400, 300)

date = QDateTimeEdit(
    window,
)
# 使用定时器延时操作
# 建议不大于100ms，取决于机器性能，机器性能太差的话可以适当延长
# 不小于21ms，取决于机器性能，机器性能太差的话可以适当延长
QTimer.singleShot(100,lambda :date.setCurrentSection(QDateTimeEdit.Section.DaySection))

window.show()
app.exec()
```

#### 34.4.2 `QDateEdit`日期编辑框控件

`QDateEdit`日期编辑框控件继承自`QDateTimeEdit`日期时间编辑框控件，默认只显示日期。

示例如下：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDateEdit,
)
from PySide6.QtCore import QDate

app = QApplication()
window = QWidget()
window.setWindowTitle('认识时间控件')
window.resize(400, 300)

QDateEdit(
    QDate(
        2026,
        1,
        1,
    ),
    window
)

window.show()
app.exec()
```

![2026_34_3](qt_for_python_pro.assets/2026_34_3.png)

`QDateEdit`日期编辑框控件的继承关系如下：

![2026_34_4](qt_for_python_pro.assets/2026_34_4.png)

相关文档的链接如下：

- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDateEdit.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDateTimeEdit.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractSpinBox.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html

支持`QDateTimeEdit`日期时间编辑框控件的第一种、第四种初始化方法。

`QDateEdit`日期编辑框控件支持以下方法（部分，含控件属性）：

- `date`方法（控件属性，可使用`setDate`方法设置），表示默认日期。

`QDateEdit`日期编辑框控件支持以下信号（部分）：

- `userDateChanged`信号，控件属性`date`改变时触发。

#### 34.4.3 `QTimeEdit`时间编辑框控件

`QTimeEdit`时间编辑框控件继承自`QDateTimeEdit`日期时间编辑框控件，默认只显示时间。

示例如下：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QTimeEdit,
)
from PySide6.QtCore import QTime

app = QApplication()
window = QWidget()
window.setWindowTitle('认识时间控件')
window.resize(400, 300)

QTimeEdit(
    QTime(
        12,
        30,
        0,
    ),
    window
)

window.show()
app.exec()
```

![2026_34_5](qt_for_python_pro.assets/2026_34_5.png)

`QTimeEdit`时间编辑框控件的继承关系如下：

![2026_34_6](qt_for_python_pro.assets/2026_34_6.png)

相关文档的链接如下：

- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTimeEdit.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDateTimeEdit.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractSpinBox.html
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html

支持`QDateTimeEdit`日期时间编辑框控件的第三种、第四种初始化方法。

`QTimeEdit`时间编辑框控件支持以下方法（部分，含控件属性）：

- `time`方法（控件属性，可使用`setTime`方法设置），表示默认时间。

`QTimeEdit`时间编辑框控件支持以下信号（部分）：

- `userTimeChanged`信号，控件属性`time`改变时触发。

## 35 `PySide6.QtWidgets`模块提供的控件、类

`PySide6.QtWidgets`模块提供了不少控件，前面的章节介绍了一部分，有的读者反馈有些控件用的时候想不起来，或者部分控件还没开始介绍，不知道需要特定功能时改用哪个控件。

还好官网文档（https://doc.qt.io/qtforpython-6/overviews/qtwidgets-widget-classes.html#widgets-classes）提供了按功能分类的功能目录（仅包含部分控件），可以按需选择使用的控件。

基础部分（最常用的控件）：

| 类名                                                         | 说明                   |
| ------------------------------------------------------------ | ---------------------- |
| [`PySide6.QtWidgets.QWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget) | 基本控件               |
| [`PySide6.QtWidgets.QCheckBox`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCheckBox.html#PySide6.QtWidgets.QCheckBox) | 勾选框、复选框         |
| [`PySide6.QtWidgets.QComboBox`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QComboBox.html#PySide6.QtWidgets.QComboBox) | 下拉选择框             |
| [`PySide6.QtWidgets.QCommandLinkButton`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCommandLinkButton.html#PySide6.QtWidgets.QCommandLinkButton) | 带解释文本的预制按钮   |
| [`PySide6.QtWidgets.QDateTimeEdit`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDateTimeEdit.html#PySide6.QtWidgets.QDateTimeEdit) | 日期时间编辑框         |
| [`PySide6.QtWidgets.QTimeEdit`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTimeEdit.html#PySide6.QtWidgets.QTimeEdit) | 时间编辑框             |
| [`PySide6.QtWidgets.QDateEdit`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDateEdit.html#PySide6.QtWidgets.QDateEdit) | 日期编辑器             |
| [`PySide6.QtWidgets.QDial`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDial.html#PySide6.QtWidgets.QDial) | 旋钮                   |
| [`PySide6.QtWidgets.QFocusFrame`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFocusFrame.html#PySide6.QtWidgets.QFocusFrame) | 给其他控件套个边框     |
| [`PySide6.QtWidgets.QFontComboBox`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFontComboBox.html#PySide6.QtWidgets.QFontComboBox) | 字体的下拉选择框       |
| [`PySide6.QtWidgets.QLabel`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLabel.html#PySide6.QtWidgets.QLabel) | 显示文本或者图片       |
| [`PySide6.QtWidgets.QLCDNumber`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLCDNumber.html#PySide6.QtWidgets.QLCDNumber) | 以LCD风格显示数字      |
| [`PySide6.QtWidgets.QLineEdit`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLineEdit.html#PySide6.QtWidgets.QLineEdit) | 单行的文本编辑框       |
| [`PySide6.QtWidgets.QMenu`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMenu.html#PySide6.QtWidgets.QMenu) | 菜单                   |
| [`PySide6.QtWidgets.QProgressBar`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QProgressBar.html#PySide6.QtWidgets.QProgressBar) | 进度条                 |
| [`PySide6.QtWidgets.QPushButton`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html#PySide6.QtWidgets.QPushButton) | 普通按钮               |
| [`PySide6.QtWidgets.QRadioButton`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QRadioButton.html#PySide6.QtWidgets.QRadioButton) | 单选框                 |
| [`PySide6.QtWidgets.QScrollArea`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QScrollArea.html#PySide6.QtWidgets.QScrollArea) | 可以滚动的区域         |
| [`PySide6.QtWidgets.QScrollBar`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QScrollBar.html#PySide6.QtWidgets.QScrollBar) | 滚动条                 |
| [`PySide6.QtWidgets.QSizeGrip`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSizeGrip.html#PySide6.QtWidgets.QSizeGrip) | 调整窗口大小的拖放控件 |
| [`PySide6.QtWidgets.QSlider`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSlider.html#PySide6.QtWidgets.QSlider) | 滑块                   |
| [`PySide6.QtWidgets.QSpinBox`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSpinBox.html#PySide6.QtWidgets.QSpinBox) | 带调整按钮的整数编辑框 |
| [`PySide6.QtWidgets.QDoubleSpinBox`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDoubleSpinBox.html#PySide6.QtWidgets.QDoubleSpinBox) | 带调整按钮的小数编辑框 |
| [`PySide6.QtWidgets.QTabBar`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTabBar.html#PySide6.QtWidgets.QTabBar) | 选项卡的标签页         |
| [`PySide6.QtWidgets.QTabWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTabWidget.html#PySide6.QtWidgets.QTabWidget) | 选项卡的内容           |
| [`PySide6.QtWidgets.QToolBox`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBox.html#PySide6.QtWidgets.QToolBox) | 垂直的手风琴式折叠面板 |
| [`PySide6.QtWidgets.QToolButton`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolButton.html#PySide6.QtWidgets.QToolButton) | 一般用在工具栏中的按钮 |

高级部分（视图类控件）：

| 类名                                                         | 说明                 |
| ------------------------------------------------------------ | -------------------- |
| [`PySide6.QtWidgets.QColumnView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QColumnView.html#PySide6.QtWidgets.QColumnView) | 列视图               |
| [`PySide6.QtWidgets.QDataWidgetMapper`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDataWidgetMapper.html#PySide6.QtWidgets.QDataWidgetMapper) | 展示数据模型         |
| [`PySide6.QtWidgets.QListView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView) | 列表视图，可以带图标 |
| [`PySide6.QtWidgets.QTableView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView) | 表格                 |
| [`PySide6.QtWidgets.QTreeView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView) | 树形图               |
| [`PySide6.QtWidgets.QUndoView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QUndoView.html#PySide6.QtWidgets.QUndoView) | 展示可撤销的操作     |
| [`PySide6.QtWidgets.QCalendarWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCalendarWidget.html#PySide6.QtWidgets.QCalendarWidget) | 日历                 |

抽象部分（其他控件的基类，不单独使用，但提供的方法、属性需要了解）：

| 类名                                                         | 说明             |
| ------------------------------------------------------------ | ---------------- |
| [`PySide6.QtWidgets.QDialog`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDialog.html#PySide6.QtWidgets.QDialog) | 对话框的基类     |
| [`PySide6.QtWidgets.QAbstractButton`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html#PySide6.QtWidgets.QAbstractButton) | 按钮的基类       |
| [`PySide6.QtWidgets.QAbstractScrollArea`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractScrollArea.html#PySide6.QtWidgets.QAbstractScrollArea) | 滚动区域的基类   |
| [`PySide6.QtWidgets.QAbstractSlider`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractSlider.html#PySide6.QtWidgets.QAbstractSlider) | 滑块的基类       |
| [`PySide6.QtWidgets.QAbstractSpinBox`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractSpinBox.html#PySide6.QtWidgets.QAbstractSpinBox) | 数字编辑框的基类 |
| [`PySide6.QtWidgets.QFrame`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFrame.html#PySide6.QtWidgets.QFrame) | 带框架控件的基类 |

组织控件（不是布局控件，但可以编排其他控件）：

| 类名                                                         | 说明                                               |
| ------------------------------------------------------------ | -------------------------------------------------- |
| [`PySide6.QtWidgets.QButtonGroup`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QButtonGroup.html#PySide6.QtWidgets.QButtonGroup) | 给按钮编组                                         |
| [`PySide6.QtWidgets.QGroupBox`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGroupBox.html#PySide6.QtWidgets.QGroupBox) | 带有标题的编组控件                                 |
| [`PySide6.QtWidgets.QSplitterHandle`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSplitterHandle.html#PySide6.QtWidgets.QSplitterHandle) | 分离器控件的把手（内部控件）                       |
| [`PySide6.QtWidgets.QSplitter`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSplitter.html#PySide6.QtWidgets.QSplitter) | 分离器控件，将一块区域分隔成可以自由调整比例的两块 |
| [`PySide6.QtWidgets.QStackedWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget) | 子控件可以堆叠的容器                               |
| [`PySide6.QtWidgets.QTabWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTabWidget.html#PySide6.QtWidgets.QTabWidget) | 选项卡的内容                                       |

图形视图相关：

| 类名                                                         | 说明                           |
| ------------------------------------------------------------ | ------------------------------ |
| [`PySide6.QtWidgets.QGraphicsEffect`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsEffect.html#PySide6.QtWidgets.QGraphicsEffect) | 图形效果类的基类               |
| [`PySide6.QtWidgets.QGraphicsAnchorLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsAnchorLayout.html#PySide6.QtWidgets.QGraphicsAnchorLayout) | 在图形中用于固定控件的布局控件 |
| [`PySide6.QtWidgets.QGraphicsAnchor`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsAnchor.html#PySide6.QtWidgets.QGraphicsAnchor) | 固定控件用的锚点               |
| [`PySide6.QtWidgets.QGraphicsGridLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsGridLayout.html#PySide6.QtWidgets.QGraphicsGridLayout) | 网格布局                       |
| [`PySide6.QtWidgets.QGraphicsItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsItem.html#PySide6.QtWidgets.QGraphicsItem) | 图形的基类                     |
| [`PySide6.QtWidgets.QGraphicsObject`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsObject.html#PySide6.QtWidgets.QGraphicsObject) | 有信号、槽、属性的图形的基类   |
| [`PySide6.QtWidgets.QAbstractGraphicsShapeItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractGraphicsShapeItem.html#PySide6.QtWidgets.QAbstractGraphicsShapeItem) | 路径图形的基类                 |
| [`PySide6.QtWidgets.QGraphicsPathItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsPathItem.html#PySide6.QtWidgets.QGraphicsPathItem) | 可添加到场景中的路径图形       |
| [`PySide6.QtWidgets.QGraphicsRectItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsRectItem.html#PySide6.QtWidgets.QGraphicsRectItem) | 可添加到场景中的矩形           |
| [`PySide6.QtWidgets.QGraphicsEllipseItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsEllipseItem.html#PySide6.QtWidgets.QGraphicsEllipseItem) | 可添加到场景中的椭圆形         |
| [`PySide6.QtWidgets.QGraphicsPolygonItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsPolygonItem.html#PySide6.QtWidgets.QGraphicsPolygonItem) | 可添加到场景中的多边形         |
| [`PySide6.QtWidgets.QGraphicsLineItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsLineItem.html#PySide6.QtWidgets.QGraphicsLineItem) | 可添加到场景中的线             |
| [`PySide6.QtWidgets.QGraphicsPixmapItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsPixmapItem.html#PySide6.QtWidgets.QGraphicsPixmapItem) | 可添加到场景中的图片           |
| [`PySide6.QtWidgets.QGraphicsTextItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsTextItem.html#PySide6.QtWidgets.QGraphicsTextItem) | 可添加到场景中的文本           |
| [`PySide6.QtWidgets.QGraphicsSimpleTextItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsSimpleTextItem.html#PySide6.QtWidgets.QGraphicsSimpleTextItem) | 可添加到场景中的简单文本       |
| [`PySide6.QtWidgets.QGraphicsItemGroup`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsItemGroup.html#PySide6.QtWidgets.QGraphicsItemGroup) | 将可添加到场景中的图形编组     |
| [`PySide6.QtWidgets.QGraphicsItemAnimation`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsItemAnimation.html#PySide6.QtWidgets.QGraphicsItemAnimation) | 可添加到场景中的图形添加动画   |
| [`PySide6.QtWidgets.QGraphicsLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsLayout.html#PySide6.QtWidgets.QGraphicsLayout) | 图形布局的基类                 |
| [`PySide6.QtWidgets.QGraphicsLayoutItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsLayoutItem.html#PySide6.QtWidgets.QGraphicsLayoutItem) | 只有该类和子类可添加到布局中   |
| [`PySide6.QtWidgets.QGraphicsLinearLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsLinearLayout.html#PySide6.QtWidgets.QGraphicsLinearLayout) | 水平、垂直布局                 |
| [`PySide6.QtWidgets.QGraphicsProxyWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsProxyWidget.html#PySide6.QtWidgets.QGraphicsProxyWidget) | 将`QWidget`控件添加到场景      |
| [`PySide6.QtWidgets.QGraphicsScene`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsScene.html#PySide6.QtWidgets.QGraphicsScene) | 放置图形的场景                 |
| [`PySide6.QtWidgets.QGraphicsSceneEvent`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsSceneEvent.html#PySide6.QtWidgets.QGraphicsSceneEvent) | 场景事件的基类                 |
| [`PySide6.QtWidgets.QGraphicsSceneMouseEvent`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsSceneMouseEvent.html#PySide6.QtWidgets.QGraphicsSceneMouseEvent) | 场景的鼠标事件                 |
| [`PySide6.QtWidgets.QGraphicsSceneWheelEvent`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsSceneWheelEvent.html#PySide6.QtWidgets.QGraphicsSceneWheelEvent) | 场景的鼠标滚轮事件             |
| [`PySide6.QtWidgets.QGraphicsSceneContextMenuEvent`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsSceneContextMenuEvent.html#PySide6.QtWidgets.QGraphicsSceneContextMenuEvent) | 场景的上下文菜单事件           |
| [`PySide6.QtWidgets.QGraphicsSceneHoverEvent`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsSceneHoverEvent.html#PySide6.QtWidgets.QGraphicsSceneHoverEvent) | 场景的鼠标悬停事件             |
| [`PySide6.QtWidgets.QGraphicsSceneHelpEvent`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsSceneHelpEvent.html#PySide6.QtWidgets.QGraphicsSceneHelpEvent) | 场景的提示信息显示事件         |
| [`PySide6.QtWidgets.QGraphicsSceneDragDropEvent`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsSceneDragDropEvent.html#PySide6.QtWidgets.QGraphicsSceneDragDropEvent) | 场景的（从窗口外）拖放事件     |
| [`PySide6.QtWidgets.QGraphicsSceneResizeEvent`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsSceneResizeEvent.html#PySide6.QtWidgets.QGraphicsSceneResizeEvent) | 场景的控件尺寸调整事件         |
| [`PySide6.QtWidgets.QGraphicsSceneMoveEvent`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsSceneMoveEvent.html#PySide6.QtWidgets.QGraphicsSceneMoveEvent) | 场景的控件移动事件             |
| [`PySide6.QtWidgets.QGraphicsTransform`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsTransform.html#PySide6.QtWidgets.QGraphicsTransform) | 高级的图形变换                 |
| [`PySide6.QtWidgets.QGraphicsView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsView.html#PySide6.QtWidgets.QGraphicsView) | 用于承载场景的控件             |
| [`PySide6.QtWidgets.QGraphicsWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsWidget.html#PySide6.QtWidgets.QGraphicsWidget) | 场景中所有控件的基类           |
| [`PySide6.QtWidgets.QStyleOptionGraphicsItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleOptionGraphicsItem.html#PySide6.QtWidgets.QStyleOptionGraphicsItem) | 渲染图形相关的参数             |

模型（MVC架构）、视图（MVC架构）相关：

| 类名                                                         | 说明                           |
| ------------------------------------------------------------ | ------------------------------ |
| [`PySide6.QtWidgets.QAbstractItemDelegate`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate) | 显示、编辑数据的方式（基类）   |
| [`PySide6.QtWidgets.QAbstractItemView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView) | 视图的抽象基类                 |
| [`PySide6.QtWidgets.QColumnView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QColumnView.html#PySide6.QtWidgets.QColumnView) | 列视图                         |
| [`PySide6.QtWidgets.QDataWidgetMapper`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDataWidgetMapper.html#PySide6.QtWidgets.QDataWidgetMapper) | 将数据模型映射到控件           |
| [`PySide6.QtWidgets.QHeaderView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QHeaderView.html#PySide6.QtWidgets.QHeaderView) | 行、列的标题                   |
| [`PySide6.QtWidgets.QItemDelegate`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemDelegate.html#PySide6.QtWidgets.QItemDelegate) | 显示、编辑数据的方式           |
| [`PySide6.QtWidgets.QItemEditorFactory`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemEditorFactory.html#PySide6.QtWidgets.QItemEditorFactory) | 提供编辑数据的控件             |
| [`PySide6.QtWidgets.QItemEditorCreatorBase`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemEditorCreatorBase.html#PySide6.QtWidgets.QItemEditorCreatorBase) | 提供创建、编辑数据的控件       |
| [`PySide6.QtWidgets.QListView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView) | 列表视图                       |
| [`PySide6.QtWidgets.QListWidgetItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidgetItem.html#PySide6.QtWidgets.QListWidgetItem) | 列表视图的项                   |
| [`PySide6.QtWidgets.QListWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html#PySide6.QtWidgets.QListWidget) | 列表视图控件                   |
| [`PySide6.QtWidgets.QStyledItemDelegate`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate) | 显示、编辑数据的方式（带样式） |
| [`PySide6.QtWidgets.QTableView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView) | 表格视图                       |
| [`PySide6.QtWidgets.QTableWidgetSelectionRange`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidgetSelectionRange.html#PySide6.QtWidgets.QTableWidgetSelectionRange) | 直接与表格视图中选择的数据交互 |
| [`PySide6.QtWidgets.QTableWidgetItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidgetItem.html#PySide6.QtWidgets.QTableWidgetItem) | 表格视图的项                   |
| [`PySide6.QtWidgets.QTableWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidget.html#PySide6.QtWidgets.QTableWidget) | 表格视图控件                   |
| [`PySide6.QtWidgets.QTreeView`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView) | 树形视图                       |
| [`PySide6.QtWidgets.QTreeWidgetItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidgetItem.html#PySide6.QtWidgets.QTreeWidgetItem) | 树形视图的项                   |
| [`PySide6.QtWidgets.QTreeWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidget.html#PySide6.QtWidgets.QTreeWidget) | 树形视图控件                   |
| [`PySide6.QtWidgets.QTreeWidgetItemIterator`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidgetItemIterator.html#PySide6.QtWidgets.QTreeWidgetItemIterator) | 树形视图的项的迭代器           |

`QMainWindow`主窗口控件相关：

| 类名                                                         | 说明                   |
| ------------------------------------------------------------ | ---------------------- |
| [`PySide6.QtWidgets.QWidgetAction`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidgetAction.html#PySide6.QtWidgets.QWidgetAction) | 给动作嵌入控件         |
| [`PySide6.QtWidgets.QDockWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDockWidget.html#PySide6.QtWidgets.QDockWidget) | 让控件可浮动、停靠     |
| [`PySide6.QtWidgets.QMainWindow`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow) | 竹醋昂克               |
| [`PySide6.QtWidgets.QMdiArea`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMdiArea.html#PySide6.QtWidgets.QMdiArea) | 多个浮动的内部子窗口   |
| [`PySide6.QtWidgets.QMdiSubWindow`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMdiSubWindow.html#PySide6.QtWidgets.QMdiSubWindow) | 内部子窗口             |
| [`PySide6.QtWidgets.QMenu`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMenu.html#PySide6.QtWidgets.QMenu) | 菜单                   |
| [`PySide6.QtWidgets.QMenuBar`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMenuBar.html#PySide6.QtWidgets.QMenuBar) | 菜单栏                 |
| [`PySide6.QtWidgets.QSizeGrip`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSizeGrip.html#PySide6.QtWidgets.QSizeGrip) | 调整窗口大小的拖放控件 |
| [`PySide6.QtWidgets.QStatusBar`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar) | 状态栏                 |
| [`PySide6.QtWidgets.QToolBar`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar) | 工具栏                 |

控件外观、样式相关：

| 类名                                                         | 说明                               |
| ------------------------------------------------------------ | ---------------------------------- |
| [`PySide6.QtWidgets.QGraphicsAnchorLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsAnchorLayout.html#PySide6.QtWidgets.QGraphicsAnchorLayout) | 在图形中用于固定控件的布局控件     |
| [`PySide6.QtWidgets.QGraphicsAnchor`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsAnchor.html#PySide6.QtWidgets.QGraphicsAnchor) | 固定控件用的锚点                   |
| [`PySide6.QtWidgets.QCommonStyle`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCommonStyle.html#PySide6.QtWidgets.QCommonStyle) | 继承自基类的通用实现（不直接使用） |
| [`PySide6.QtWidgets.QStyle`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyle.html#PySide6.QtWidgets.QStyle) | 样式的基类                         |
| [`PySide6.QtWidgets.QStyleFactory`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleFactory.html#PySide6.QtWidgets.QStyleFactory) | 用于创建控件内部使用的样式对象     |
| [`PySide6.QtWidgets.QStyleOption`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleOption.html#PySide6.QtWidgets.QStyleOption) | 样式相关的配置项                   |
| [`PySide6.QtWidgets.QStyleHintReturn`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleHintReturn.html#PySide6.QtWidgets.QStyleHintReturn) | 样式提示的返回值                   |
| [`PySide6.QtWidgets.QStyleHintReturnMask`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleHintReturnMask.html#PySide6.QtWidgets.QStyleHintReturnMask) | 样式提示的返回值（遮罩层）         |
| [`PySide6.QtWidgets.QStyleHintReturnVariant`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleHintReturnVariant.html#PySide6.QtWidgets.QStyleHintReturnVariant) | 样式提示的返回值（任意值）         |
| [`PySide6.QtWidgets.QStylePainter`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStylePainter.html#PySide6.QtWidgets.QStylePainter) | 绘制样式的画笔                     |

布局相关：

| 类名                                                         | 说明                           |
| ------------------------------------------------------------ | ------------------------------ |
| [`PySide6.QtWidgets.QGraphicsAnchorLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsAnchorLayout.html#PySide6.QtWidgets.QGraphicsAnchorLayout) | 在图形中用于固定控件的布局控件 |
| [`PySide6.QtWidgets.QGraphicsAnchor`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGraphicsAnchor.html#PySide6.QtWidgets.QGraphicsAnchor) | 固定控件用的锚点               |
| [`PySide6.QtWidgets.QBoxLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QBoxLayout.html#PySide6.QtWidgets.QBoxLayout) | 垂直布局、水平布局的基类       |
| [`PySide6.QtWidgets.QHBoxLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QHBoxLayout.html#PySide6.QtWidgets.QHBoxLayout) | 水平布局                       |
| [`PySide6.QtWidgets.QVBoxLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QVBoxLayout.html#PySide6.QtWidgets.QVBoxLayout) | 垂直布局                       |
| [`PySide6.QtWidgets.QFormLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFormLayout.html#PySide6.QtWidgets.QFormLayout) | 表单布局                       |
| [`PySide6.QtWidgets.QGridLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGridLayout.html#PySide6.QtWidgets.QGridLayout) | 网格布局                       |
| [`PySide6.QtWidgets.QLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLayout.html#PySide6.QtWidgets.QLayout) | 所有布局的基类                 |
| [`PySide6.QtWidgets.QLayoutItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLayoutItem.html#PySide6.QtWidgets.QLayoutItem) | 布局项目                       |
| [`PySide6.QtWidgets.QSpacerItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSpacerItem.html#PySide6.QtWidgets.QSpacerItem) | 空白的布局项目                 |
| [`PySide6.QtWidgets.QWidgetItem`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidgetItem.html#PySide6.QtWidgets.QWidgetItem) | 将普通控件转换为布局项目       |
| [`PySide6.QtWidgets.QSizePolicy`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSizePolicy.html#PySide6.QtWidgets.QSizePolicy) | 尺寸策略                       |
| [`PySide6.QtWidgets.QStackedLayout`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedLayout.html#PySide6.QtWidgets.QStackedLayout) | 堆叠布局                       |
| [`PySide6.QtWidgets.QButtonGroup`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QButtonGroup.html#PySide6.QtWidgets.QButtonGroup) | 给按钮编组                     |
| [`PySide6.QtWidgets.QGroupBox`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGroupBox.html#PySide6.QtWidgets.QGroupBox) | 带有标题的编组控件             |
| [`PySide6.QtWidgets.QStackedWidget`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget) | 子控件可以堆叠的容器           |

最后再附上一份`PySide6.QtWidgets`模块提供的所有控件类清单（功能目录不包含所有控件类，参考自 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html）：

```python3
QAbstractButton
QAbstractGraphicsShapeItem
QAbstractItemDelegate
QAbstractItemView
QAbstractScrollArea
QAbstractSlider
QAbstractSpinBox
QAccessibleWidget
QApplication
QBoxLayout
QButtonGroup
QCalendarWidget
QCheckBox
QColorDialog
QColormap
QColumnView
QComboBox
QCommandLinkButton
QCommonStyle
QCompleter
QDataWidgetMapper
QDateEdit
QDateTimeEdit
QDial
QDialog
QDialogButtonBox
QDockWidget
QDoubleSpinBox
QErrorMessage
QFileDialog
QFileIconProvider
QFileSystemModel
QFocusFrame
QFontComboBox
QFontDialog
QFormLayout
QFrame
QGesture
QGestureEvent
QGestureRecognizer
QGraphicsAnchor
QGraphicsAnchorLayout
QGraphicsBlurEffect
QGraphicsColorizeEffect
QGraphicsDropShadowEffect
QGraphicsEffect
QGraphicsEllipseItem
QGraphicsGridLayout
QGraphicsItem
QGraphicsItemAnimation
QGraphicsItemGroup
QGraphicsLayout
QGraphicsLayoutItem
QGraphicsLineItem
QGraphicsLinearLayout
QGraphicsObject
QGraphicsOpacityEffect
QGraphicsPathItem
QGraphicsPixmapItem
QGraphicsPolygonItem
QGraphicsProxyWidget
QGraphicsRectItem
QGraphicsRotation
QGraphicsScale
QGraphicsScene
QGraphicsSceneContextMenuEvent
QGraphicsSceneDragDropEvent
QGraphicsSceneEvent
QGraphicsSceneHelpEvent
QGraphicsSceneHoverEvent
QGraphicsSceneMouseEvent
QGraphicsSceneMoveEvent
QGraphicsSceneResizeEvent
QGraphicsSceneWheelEvent
QGraphicsSimpleTextItem
QGraphicsTextItem
QGraphicsTransform
QGraphicsView
QGraphicsWidget
QGridLayout
QGroupBox
QHBoxLayout
QHeaderView
QInputDialog
QItemDelegate
QItemEditorCreatorBase
QItemEditorFactory
QKeySequenceEdit
QLCDNumber
QLabel
QLayout
QLayoutItem
QLineEdit
QListView
QListWidget
QListWidgetItem
QMainWindow
QMdiArea
QMdiSubWindow
QMenu
QMenuBar
QMessageBox
QPanGesture
QPinchGesture
QPlainTextDocumentLayout
QPlainTextEdit
QProgressBar
QProgressDialog
QProxyStyle
QPushButton
QRadioButton
QRhiWidget
QRubberBand
QScrollArea
QScrollBar
QScroller
QScrollerProperties
QSizeGrip
QSizePolicy
QSlider
QSpacerItem
QSpinBox
QSplashScreen
QSplitter
QSplitterHandle
QStackedLayout
QStackedWidget
QStatusBar
QStyle
QStyleFactory
QStyleHintReturn
QStyleHintReturnMask
QStyleHintReturnVariant
QStyleOption
QStyleOptionButton
QStyleOptionComboBox
QStyleOptionComplex
QStyleOptionDockWidget
QStyleOptionFocusRect
QStyleOptionFrame
QStyleOptionGraphicsItem
QStyleOptionGroupBox
QStyleOptionHeader
QStyleOptionHeaderV2
QStyleOptionMenuItem
QStyleOptionMenuItemV2
QStyleOptionProgressBar
QStyleOptionRubberBand
QStyleOptionSizeGrip
QStyleOptionSlider
QStyleOptionSpinBox
QStyleOptionTab
QStyleOptionTabBarBase
QStyleOptionTabWidgetFrame
QStyleOptionTitleBar
QStyleOptionToolBar
QStyleOptionToolBox
QStyleOptionToolButton
QStyleOptionViewItem
QStylePainter
QStyledItemDelegate
QSwipeGesture
QSystemTrayIcon
QTabBar
QTabWidget
QTableView
QTableWidget
QTableWidgetItem
QTableWidgetSelectionRange
QTapAndHoldGesture
QTapGesture
QTextBrowser
QTextEdit
QTileRules
QTimeEdit
QToolBar
QToolBox
QToolButton
QToolTip
QTreeView
QTreeWidget
QTreeWidgetItem
QTreeWidgetItemIterator
TakeRowResult
QUndoView
QVBoxLayout
QWhatsThis
QWidget
QWidgetAction
QWidgetItem
QWizard
QWizardPage
```

注意，部分术语、概念的翻译、表述受限于笔者水平，可能存在偏差或者错误，后续更新中，部分表述可能会有变动、改正。如果读者发现相关表述存在错误或者不准确，请不吝指正。

## 36 `QDial`旋钮控件（更新中）

`QDial`旋钮控件……



示例如下：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget
)

app = QApplication()
window = QWidget()
window.setWindowTitle('认识控件')
window.resize(400, 300)

# 添加相关控件

window.show()
app.exec()
```

（运行效果图）

`Qxxx`xxxx控件的继承关系如下：

（截图继承关系）

相关文档的链接如下：

- （由近到远每一层级对应的文档链接）
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html

### x.1 初始化方法（更新中）

`Qxxx`xxx控件有多种初始化方法（参数名及类型提示来自`QtWidgets.pyi`）。

第一种初始化方法支持以下参数：

- `xxx`参数，仅限位置参数（第一个位置参数），---

第二种初始化方法支持以下参数：

- `xxx`参数，仅限位置参数（第一个位置参数），---

### x.2 方法、控件属性（更新中）

`Qxxx`xxx控件支持以下方法（部分，含控件属性）：

- `xxx`方法，---

  该方法支持以下参数：

  - `xxx`参数，仅限位置参数（第一个位置参数），---

### x.3 信号和槽（更新中）

`Qxxx`xxx控件支持以下信号（部分）：

- `xxx`信号，---

`Qxxx`xxx控件支持以下槽（部分）：

- `xxx`方法，---

### x.4 扩展用法（更新中）

（扩展用法包含前面参数、方法、信号、槽相关的示例）

#### x.4.1 xxx（更新中）



## x 创作灵感（非正式内容）

后续内容更新转入《易森》。

灵感来源（官方）：

- `QtWidgets`模块：https://doc.qt.io/qtforpython-6/overviews/qtwidgets-widget-classes.html
- `QtGui`模块：https://doc.qt.io/qtforpython-6/overviews/qtwidgets-widget-classes.html#widgets-classes
- `QtCore`模块：https://doc.qt.io/qtforpython-6/PySide6/QtCore/index.html#list-of-classes-by-function

模块一览表（Qt 6.10.x）：

| 模块名                 | 主要用途                         | 文档链接                                                     |
| ---------------------- | -------------------------------- | ------------------------------------------------------------ |
| `Qt3DAnimation`        | 处理3D动画                       | https://doc.qt.io/qtforpython-6/PySide6/Qt3DAnimation/index.html#module-PySide6.Qt3DAnimation |
| `Qt3DCore`             | 3D相关的基础功能                 | https://doc.qt.io/qtforpython-6/PySide6/Qt3DCore/index.html#module-PySide6.Qt3DCore |
| `Qt3DExtras`           | 3D相关的额外功能                 | https://doc.qt.io/qtforpython-6/PySide6/Qt3DExtras/index.html#module-PySide6.Qt3DExtras |
| `Qt3DInput`            | 3D相关的输入功能                 | https://doc.qt.io/qtforpython-6/PySide6/Qt3DInput/index.html#module-PySide6.Qt3DInput |
| `Qt3DLogic`            | 3D相关的逻辑功能                 | https://doc.qt.io/qtforpython-6/PySide6/Qt3DLogic/index.html#module-PySide6.Qt3DLogic |
| `Qt3DRender`           | 渲染3D模型                       | https://doc.qt.io/qtforpython-6/PySide6/Qt3DRender/index.html#module-PySide6.Qt3DRender |
| `QtAsyncio`            | 相当于Qt版asyncio框架            | https://doc.qt.io/qtforpython-6/PySide6/QtAsyncio/index.html#module-PySide6.QtAsyncio |
| `QtBluetooth`          | 操作蓝牙设备                     | https://doc.qt.io/qtforpython-6/PySide6/QtBluetooth/index.html#module-PySide6.QtBluetooth |
| `QtConcurrent`         | 并行编程相关的功能               | https://doc.qt.io/qtforpython-6/PySide6/QtConcurrent/index.html#module-PySide6.QtConcurrent |
| `QtCore`               | Qt相关的基础功能                 | https://doc.qt.io/qtforpython-6/PySide6/QtCore/index.html#module-PySide6.QtCore |
| `QtDBus`               | D-Bus相关的功能                  | https://doc.qt.io/qtforpython-6/PySide6/QtDBus/index.html#module-PySide6.QtDBus |
| `QtDesigner`           | 可视化设计工具                   | https://doc.qt.io/qtforpython-6/PySide6/QtDesigner/index.html#module-PySide6.QtDesigner |
| `QtGraphs`             | 二维、三维图表                   | https://doc.qt.io/qtforpython-6/PySide6/QtGraphs/index.html#module-PySide6.QtGraphs |
| `QtGraphsWidgets`      | 三维图表                         | https://doc.qt.io/qtforpython-6/PySide6/QtGraphsWidgets/index.html#module-PySide6.QtGraphsWidgets |
| `QtGui`                | GUI相关的基础功能                | https://doc.qt.io/qtforpython-6/PySide6/QtGui/index.html#module-PySide6.QtGui |
| `QtHelp`               | 集成在线文档                     | https://doc.qt.io/qtforpython-6/PySide6/QtHelp/index.html#module-PySide6.QtHelp |
| `QtHttpServer`         | 创建HTTP服务器                   | https://doc.qt.io/qtforpython-6/PySide6/QtHttpServer/index.html#module-PySide6.QtHttpServer |
| `QtLocation`           | 定位、地图相关功能               | https://doc.qt.io/qtforpython-6/PySide6/QtLocation/index.html#module-PySide6.QtLocation |
| `QtMultimedia`         | 处理多媒体文件                   | https://doc.qt.io/qtforpython-6/PySide6/QtMultimedia/index.html#module-PySide6.QtMultimedia |
| `QtMultimediaWidgets`  | 处理多媒体文件的额外功能         | https://doc.qt.io/qtforpython-6/PySide6/QtMultimediaWidgets/index.html#module-PySide6.QtMultimediaWidgets |
| `QtNetwork`            | 网络功能                         | https://doc.qt.io/qtforpython-6/PySide6/QtNetwork/index.html#module-PySide6.QtNetwork |
| `QtNetworkAuth`        | 网络授权                         | https://doc.qt.io/qtforpython-6/PySide6/QtNetworkAuth/index.html#module-PySide6.QtNetworkAuth |
| `QtNfc`                | 操作NFC设备                      | https://doc.qt.io/qtforpython-6/PySide6/QtNfc/index.html#module-PySide6.QtNfc |
| `QtOpenGL`             | 与OpenGL库交互                   | https://doc.qt.io/qtforpython-6/PySide6/QtOpenGL/index.html#module-PySide6.QtOpenGL |
| `QtOpenGLWidgets`      | 显示OpenGL内容的控件             | https://doc.qt.io/qtforpython-6/PySide6/QtOpenGLWidgets/index.html#module-PySide6.QtOpenGLWidgets |
| `QtPdf`                | 处理PDF文件                      | https://doc.qt.io/qtforpython-6/PySide6/QtPdf/index.html#module-PySide6.QtPdf |
| `QtPdfWidgets`         | 显示PDF文件的控件                | https://doc.qt.io/qtforpython-6/PySide6/QtPdfWidgets/index.html#module-PySide6.QtPdfWidgets |
| `QtPositioning`        | 实时定位                         | https://doc.qt.io/qtforpython-6/PySide6/QtPositioning/index.html#module-PySide6.QtPositioning |
| `QtPrintSupport`       | 打印文件相关的功能               | https://doc.qt.io/qtforpython-6/PySide6/QtPrintSupport/index.html#module-PySide6.QtPrintSupport |
| `QtQml`                | 处理QML文件                      | https://doc.qt.io/qtforpython-6/PySide6/QtQml/index.html#module-PySide6.QtQml |
| `QtQuick`              | QtQuick程序的基础功能            | https://doc.qt.io/qtforpython-6/PySide6/QtQuick/index.html#module-PySide6.QtQuick |
| `QtQuick3D`            | 在QtQuick程序中显示3D内容        | https://doc.qt.io/qtforpython-6/PySide6/QtQuick3D/index.html#module-PySide6.QtQuick3D |
| `QtQuickControls2`     | QtQuick程序的配套控件            | https://doc.qt.io/qtforpython-6/PySide6/QtQuickControls2/index.html#module-PySide6.QtQuickControls2 |
| `QtQuickTest`          | QtQuick程序的测试框架            | https://doc.qt.io/qtforpython-6/PySide6/QtQuickTest/index.html#module-PySide6.QtQuickTest |
| `QtQuickWidgets`       | 在QtWidgets程序中显示QtQuick控件 | https://doc.qt.io/qtforpython-6/PySide6/QtQuickWidgets/index.html#module-PySide6.QtQuickWidgets |
| `QtRemoteObjects`      | 提供进程间通信使用的对象         | https://doc.qt.io/qtforpython-6/PySide6/QtRemoteObjects/index.html#module-PySide6.QtRemoteObjects |
| `QtScxml`              | 从SCXML文件创建状态机            | https://doc.qt.io/qtforpython-6/PySide6/QtScxml/index.html#module-PySide6.QtScxml https://www.w3.org/TR/scxml/ |
| `QtSensors`            | 操作传感器硬件                   | https://doc.qt.io/qtforpython-6/PySide6/QtSensors/index.html#module-PySide6.QtSensors |
| `QtSerialBus`          | 串行总线相关功能                 | https://doc.qt.io/qtforpython-6/PySide6/QtSerialBus/index.html#module-PySide6.QtSerialBus |
| `QtSerialPort`         | 串口通讯相关功能                 | https://doc.qt.io/qtforpython-6/PySide6/QtSerialPort/index.html#module-PySide6.QtSerialPort |
| `QtSpatialAudio`       | 空间音频相关功能                 | https://doc.qt.io/qtforpython-6/PySide6/QtSpatialAudio/index.html#module-PySide6.QtSpatialAudio |
| `QtSql`                | SQL、数据库相关功能              | https://doc.qt.io/qtforpython-6/PySide6/QtSql/index.html#module-PySide6.QtSql |
| `QtStateMachine`       | 状态机相关功能                   | https://doc.qt.io/qtforpython-6/PySide6/QtStateMachine/index.html#module-PySide6.QtStateMachine |
| `QtSvg`                | 处理SVG文件                      | https://doc.qt.io/qtforpython-6/PySide6/QtSvg/index.html#module-PySide6.QtSvg |
| `QtSvgWidgets`         | 显示SVG文件的控件                | https://doc.qt.io/qtforpython-6/PySide6/QtSvgWidgets/index.html#module-PySide6.QtSvgWidgets |
| `QtTest`               | GUI测试和基准测试                | https://doc.qt.io/qtforpython-6/PySide6/QtTest/index.html#module-PySide6.QtTest |
| `QtTextToSpeech`       | 文本转语音                       | https://doc.qt.io/qtforpython-6/PySide6/QtTextToSpeech/index.html#module-PySide6.QtTextToSpeech |
| `QtUiTools`            | 加载UI文件                       | https://doc.qt.io/qtforpython-6/PySide6/QtUiTools/index.html#module-PySide6.QtUiTools |
| `PySide6.QtWebChannel` | 服务器、客户端之间的点对点通讯   | https://doc.qt.io/qtforpython-6/PySide6/QtWebChannel/index.html#module-PySide6.QtWebChannel |
| `QtWebEngineCore`      | WebEngine的基础功能              | https://doc.qt.io/qtforpython-6/PySide6/QtWebEngineCore/index.html#module-PySide6.QtWebEngineCore |
| `QtWebEngineQuick`     | 在QtQuick程序中嵌入WebEngine     | https://doc.qt.io/qtforpython-6/PySide6/QtWebEngineQuick/index.html#module-PySide6.QtWebEngineQuick |
| `QtWebEngineWidgets`   | 在QtWidgets程序中嵌入WebEngine   | https://doc.qt.io/qtforpython-6/PySide6/QtWebEngineWidgets/index.html#module-PySide6.QtWebEngineWidgets |
| `QtWebSockets`         | 处理WebSocket协议                | https://doc.qt.io/qtforpython-6/PySide6/QtWebSockets/index.html#module-PySide6.QtWebSockets |
| `QtWebView`            | 显示网页内容                     | https://doc.qt.io/qtforpython-6/PySide6/QtWebView/index.html#module-PySide6.QtWebView |
| `QtWidgets`            | QtWidgets程序的基础功能          | https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html#module-PySide6.QtWidgets |
| `QtXml`                | 处理XML文件                      | https://doc.qt.io/qtforpython-6/PySide6/QtXml/index.html#module-PySide6.QtXml |





## x `Qxxx`xxx控件（更新中）（模板）

`Qxxx`xxx控件主要用于……

示例如下：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget
)

app = QApplication()
window = QWidget()
window.setWindowTitle('认识控件')
window.resize(400, 300)

# 添加相关控件

window.show()
app.exec()
```

（运行效果图）

`Qxxx`xxxx控件的继承关系如下：

（截图继承关系）

相关文档的链接如下：

- （由近到远每一层级对应的文档链接）
- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html

### x.1 初始化方法（更新中）

`Qxxx`xxx控件有多种初始化方法（参数名及类型提示来自`QtWidgets.pyi`）。

第一种初始化方法支持以下参数：

- `xxx`参数，仅限位置参数（第一个位置参数），---

第二种初始化方法支持以下参数：

- `xxx`参数，仅限位置参数（第一个位置参数），---

### x.2 方法、控件属性（更新中）

`Qxxx`xxx控件支持以下方法（部分，含控件属性）：

- `xxx`方法，---

  该方法支持以下参数：

  - `xxx`参数，仅限位置参数（第一个位置参数），---

### x.3 信号和槽（更新中）

`Qxxx`xxx控件支持以下信号（部分）：

- `xxx`信号，---

`Qxxx`xxx控件支持以下槽（部分）：

- `xxx`方法，---

### x.4 扩展用法（更新中）

（扩展用法包含前面参数、方法、信号、槽相关的示例）

#### x.4.1 xxx（更新中）

