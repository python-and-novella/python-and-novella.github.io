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

- `autoExclusive`方法，---

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