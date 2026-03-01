# Qt For Python 札记（2026）

## Qt For Python 札记2026版——更新计划

2025版（即2025年创作的部分）在创作过程中已经覆盖了不少内容，但Qt提供了数量庞大的控件，支持的用法也多种多样，更别说各种控件在实际使用时遇到的问题数不胜数。

2025版立项较晚，加上笔者要预研其他教程，还有其他工作要做，导致2025版的内容只是介绍了Qt用法的很小一部分。

此外，之前内容可能还存在错误、遗漏之处，需要及时更正、补充。

因此，笔者将在2026年继续本教程系列的更新，也就是本教程的2026版。2026版将延续2025版的任务，为读者介绍Qt控件的用法。同时，对于之前已经介绍过的控件，将搜集实际使用时的各种用法和遇到的问题，深入、扩展常用控件的用法，解决相关问题。当然，之前内容如果存在遗漏、错误，后续也将会发布补充、修正的章节。

2026年，更新不止，学习不止，愿每一位读者都能学有所得。

## 25 按钮控件（更新中）

在QtWidgets程序中，除了前面常用于示例中的`QPushButton`普通按钮控件，还有很多具备按钮功能的控件。

### 25.1 `QPushButton`普通按钮控件（更新中）

`QPushButton`普通按钮控件算是最常用、最普通的按钮。如果程序中需要一个简单的、可以点击的按钮，那非普通按钮控件莫属：

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

完整用法可以参考 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html 和 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html。

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

`QPushButton`普通按钮控件支持以下信号：

- `clicked`信号，点击（包含鼠标按键按下、弹起两个过程）按钮时触发。

- `pressed`信号，按下按钮时触发。

- `released`信号，弹起按钮时触发。

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

`QPushButton`普通按钮控件支持以下方法（部分，含控件属性）：

- `autoExclusive`方法，获取控件是否启用自动独占。当多个按钮的父控件相同时，这些按钮就属于同一独占组。如果这些按钮启用了勾选和自动独占，那么，将只允许同时勾选最多一个按钮：

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

- `autoRepeat`方法，---

- 

- `setMenu`方法，设置点击按钮之后弹出的菜单。该方法支持以下参数：

  - `menu`参数，`PySide6.QtWidgets.QMenu`类型，表示弹出的菜单。

- `setToolTip`方法，按钮的工具提示（鼠标悬停时自动弹出的文字）。该方法支持以下参数：

  - `arg__1`参数，仅限位置参数（第一个位置参数），字符串类型，表示工具提示的内容。

- `setShortcut`方法，给按钮绑定快捷键，按下快捷键时触发按钮的`clicked`信号。该方法支持以下参数：

  - `key`参数，`PySide6.QtCore.Qt.Key`类型、`PySide6.QtGui.QKeySequence`类型、`PySide6.QtCore.QKeyCombination`类型、`PySide6.QtGui.QKeySequence.StandardKey`类型、字符串类型、整数类型，表示绑定的快捷键。







（下面的示例需要拆分到具体方法的示例中）

示例如下：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMenu
)

from PySide6.QtGui import QIcon

app = QApplication()
window = QWidget()
window.setWindowTitle('认识各种按钮')
window.resize(400, 300)

button = QPushButton(
    QIcon.fromTheme(
        QIcon.ThemeIcon.FolderOpen
    ),
    '有下拉菜单的按钮',
    window
)
menu = QMenu()
menu.addAction('菜单项1')
button.setMenu(menu)
button.setShortcut('ctrl+q')
button.setToolTip('快捷键为ctrl+q')

window.show()
app.exec()
```





### 25.2 `QRadioButton`按钮控件

`Q`xx控件主要用于……

完整用法可以参考 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html 和 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html。

`Q`xx控件有多种初始化方法（参数名及类型提示来自`xx.pyi`）。

第一种初始化方法支持以下参数：

- 

`Q`xx控件支持以下信号：

- `xx`信号，

`Q`xx控件支持以下方法（部分，含控件属性）：

- `xx`方法，

受限于篇幅，该控件支持的方法没法全部介绍，这里仅简单提供一个该控件的示例。至于其余的方法和更多用法，可以期待后续有关该控件的其他章节。

示例如下：





### 25.3 `QCheckBox`按钮控件

`Q`xx控件主要用于……

完整用法可以参考 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html 和 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html。

`Q`xx控件有多种初始化方法（参数名及类型提示来自`xx.pyi`）。

第一种初始化方法支持以下参数：

- 

`Q`xx控件支持以下信号：

- `xx`信号，

`Q`xx控件支持以下方法（部分，含控件属性）：

- `xx`方法，

受限于篇幅，该控件支持的方法没法全部介绍，这里仅简单提供一个该控件的示例。至于其余的方法和更多用法，可以期待后续有关该控件的其他章节。

示例如下：



### 25.4 `QCommandLinkButton`按钮控件

`Q`xx控件主要用于……

完整用法可以参考 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html 和 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html。

`Q`xx控件有多种初始化方法（参数名及类型提示来自`xx.pyi`）。

第一种初始化方法支持以下参数：

- 

`Q`xx控件支持以下信号：

- `xx`信号，

`Q`xx控件支持以下方法（部分，含控件属性）：

- `xx`方法，

受限于篇幅，该控件支持的方法没法全部介绍，这里仅简单提供一个该控件的示例。至于其余的方法和更多用法，可以期待后续有关该控件的其他章节。

示例如下：



### 25.5 `QToolButton`按钮控件

`Q`xx控件主要用于……

完整用法可以参考 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html 和 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html。

`Q`xx控件有多种初始化方法（参数名及类型提示来自`xx.pyi`）。

第一种初始化方法支持以下参数：

- 

`Q`xx控件支持以下信号：

- `xx`信号，

`Q`xx控件支持以下方法（部分，含控件属性）：

- `xx`方法，

受限于篇幅，该控件支持的方法没法全部介绍，这里仅简单提供一个该控件的示例。至于其余的方法和更多用法，可以期待后续有关该控件的其他章节。

示例如下：



## 26 弹出菜单（更新中）



菜单栏点击后弹出菜单，任意按钮点击后弹出菜单，右键弹出菜单，





## 27 `QWizard`向导对话框控件和`QWizardPage`向导页控件（更新中）



https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWizard.html

https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWizardPage.html





## 28 日期时间控件（更新中）





## 29 临时数据控件（更新中）





## 30 表格控件（更新中）





## 31 树形图控件（更新中）





## 32 （待定）





## 33 （待定）





## 34 （待定）









## x 创作灵感（非正式内容）

灵感来源（官方）：

- Qt Core：https://doc.qt.io/qt-6/zh/qtcore-index.html
- Qt GUI：https://doc.qt.io/qt-6/zh/qtgui-index.html
- Qt Network：https://doc.qt.io/qt-6/zh/qtnetwork-index.html
- Qt Quick：https://doc.qt.io/qt-6/zh/qtquick-index.html
- Qt Widgets：https://doc.qt.io/qt-6/zh/qtwidgets-index.html
- Qt Test：https://doc.qt.io/qt-6/zh/qttest-index.html
- Additional Modules：https://doc.qt.io/qt-6/zh/qt-additional-modules.html
- Tools and utilities：https://doc.qt.io/qt-6/zh/qt-tools-utilities.html



QtWidgets程序槽函数

前面说过槽函数与直接使用函数没什么区别，就好像下面改自前面的示例，使用普通函数代替槽函数：

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



执行效果是一样的，但为什么还要定义槽函数呢？这就不得不说槽函数的自动连接功能，即无需手动连接所有的信号和槽，有一个简单的方法自动将槽函数与特定信号链接。

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

- 在控件挂载、初始化完毕之后，调用`QMetaObject.connectSlotsByName(self)`。

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



与自定义信号结合：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton
)
from PySide6.QtCore import Slot,QMetaObject,Signal

app = QApplication()

class Window(QWidget):
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





重载信号：

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
        print('window[] is clicked!!!')

    @Slot(str)
    def on_mySignal_str(self,string):
        print(string)
        print('window[str] is clicked!!!')

    @Slot(int)
    def on_mySignal_int(self,integer):
        print(integer)
        print('window[int] is clicked!!!')

window = Window()

window.show()
app.exec()
```





后台运行+系统托盘+托盘的菜单+点击托盘显示主窗口：

`QApplication`实例的`setQuitOnLastWindowClosed`方法可以实现后台运行。配合托盘图标的右键菜单（在右键菜单中可以添加退出`QApplication`实例、显示主窗口的菜单项），能够实现完善的后台运行、恢复前台的功能。

完整的示例代码（通过勾选复选框启用后台运行功能）：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QSystemTrayIcon,
    QCheckBox,
    QMenu
)

app = QApplication()

if QSystemTrayIcon.isSystemTrayAvailable():
    # 注意，只有系统支持托盘时才能这样用，否则只能使用快捷键或者命令行强制退出程序
    # 关闭最后一个窗口时不退出程序
    # app.setQuitOnLastWindowClosed(False)
    tray = QSystemTrayIcon(
        app.style().standardIcon(
            app.style().StandardPixmap.SP_ComputerIcon
        ),
        app,
        visible=True
    )
    tray.showMessage(
        '提示',
        '系统托盘可用，可以启用后台运行。'
    )
    # show方法必须单独执行。
    # visible为True的话，show方法不是必须执行的。
    # tray.show()

    # 任意类型的点击托盘图标都会显示主窗口
    # tray.activated.connect(lambda:window.show())
    # 只有左键单击托盘图标才会显示主窗口
    tray.activated.connect(lambda e:window.show() if e == QSystemTrayIcon.ActivationReason.Trigger else None)
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
    # lambda e: (app.setQuitOnLastWindowClosed(False) if e == Qt.CheckState.Checked else app.setQuitOnLastWindowClosed(True))
    lambda e: (app.setQuitOnLastWindowClosed(False) if str(e) == 'CheckState.Checked' else app.setQuitOnLastWindowClosed(True))
)
checkbox.setToolTip('最好在显示系统托盘后启用后台运行')

window.show()
app.exec()
```





## 1 （修正2025.13）

原内容存在错误，修正错误。

## 1 （补充2025.13）

原内容不全面，补充内容。

## 1 （扩展2025.13）

从原内容想到的其他内容，虽然可以作为独立的内容写标题，但这部分内容确实是看完原内容才有了创作契机。

## 1 `Q`xx控件

`Q`xx控件主要用于……

完整用法可以参考 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html 和 https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html。

`Q`xx控件有多种初始化方法（参数名及类型提示来自`xx.pyi`）。

第一种初始化方法支持以下参数：

- 

`Q`xx控件支持以下信号：

- `xx`信号，

`Q`xx控件支持以下方法（部分，含控件属性）：

- `xx`方法，