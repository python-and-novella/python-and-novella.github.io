# Qt For Python 札记（2025版）

## 0 为何而写

Qt For Python （目前库名为PySide6）各类教程已经有很多，笔者就不班门弄斧了。不过，框架在使用过程中还是有不少难点，对于心急的初学者来说，很容易在找不到解决方法之后轻言放弃。因此，笔者将代入初学者的视角，将学习心得按照时间顺序一一记下，以便于有一定基础但囿于难点的读者按图索骥。

## 1 安装PySide6的注意事项

学习的第一步就是安装库。不过，官方提供了不少相关的库，但并非所有的库都是必需的。以下面的虚拟环境（使用环境管理工具UV创建）为例，笔者添加了官方提供的相关库，其依赖关系如下（使用`uv tree`生成）：

```shell
pyside6-uv-app v0.1.0
├── pyside6 v6.9.1
│   ├── pyside6-addons v6.9.1
│   │   ├── pyside6-essentials v6.9.1
│   │   │   └── shiboken6 v6.9.1
│   │   └── shiboken6 v6.9.1
│   ├── pyside6-essentials v6.9.1 (*)
│   └── shiboken6 v6.9.1
├── pyside6-examples v6.9.1
│   ├── pyside6-addons v6.9.1 (*)
│   ├── pyside6-essentials v6.9.1 (*)
│   └── shiboken6 v6.9.1
└── shiboken6-generator v6.9.1
    └── shiboken6 v6.9.1
```

项目下主动添加的库为：`pyside6`、`pyside6-examples`、`shiboken6-generator`。其中，添加了`pyside6`之后，会自动安装相关的依赖，此时就可以开始学习，无需额外安装其他相关库。当然，其他的库也有用处，只是刚开始学习的时候不一定需要。`pyside6-examples`是官方编写的示例程序，可在`pyside6_uv_app\.venv\Lib\site-packages\PySide6\examples`中找到。`shiboken6-generator`是绑定生成器，只有涉及到绑定Qt或者C++程序的接口（基于C++头文件生成Python的接口）时，才需要这个库。

需要注意的是，在使用UV管理虚拟环境时，单独移除`pyside6-examples`会导致`pyside6`的`__init__.py`丢失，可使用`uv sync --reinstall`重新安装所有库来解决此问题。

## 2 常用模块的主要用途和相关命名规则（更新中）

PySide6（6.9.x）包含以下模块（参考https://doc.qt.io/qtforpython-6/py-modindex.html）：

- `PySide6.Qt3DAnimation`，https://doc.qt.io/qtforpython-6/PySide6/Qt3DAnimation/index.html#module-PySide6.Qt3DAnimation
- `PySide6.Qt3DCore`，https://doc.qt.io/qtforpython-6/PySide6/Qt3DCore/index.html#module-PySide6.Qt3DCore
-   [`PySide6.Qt3DExtras`](https://doc.qt.io/qtforpython-6/PySide6/Qt3DExtras/index.html#module-PySide6.Qt3DExtras)  [`PySide6.Qt3DInput`](https://doc.qt.io/qtforpython-6/PySide6/Qt3DInput/index.html#module-PySide6.Qt3DInput)  [`PySide6.Qt3DLogic`](https://doc.qt.io/qtforpython-6/PySide6/Qt3DLogic/index.html#module-PySide6.Qt3DLogic)  [`PySide6.Qt3DRender`](https://doc.qt.io/qtforpython-6/PySide6/Qt3DRender/index.html#module-PySide6.Qt3DRender)  [`PySide6.QtAsyncio`](https://doc.qt.io/qtforpython-6/PySide6/QtAsyncio/index.html#module-PySide6.QtAsyncio)  [`PySide6.QtBluetooth`](https://doc.qt.io/qtforpython-6/PySide6/QtBluetooth/index.html#module-PySide6.QtBluetooth)  [`PySide6.QtConcurrent`](https://doc.qt.io/qtforpython-6/PySide6/QtConcurrent/index.html#module-PySide6.QtConcurrent)  [`PySide6.QtCore`](https://doc.qt.io/qtforpython-6/PySide6/QtCore/index.html#module-PySide6.QtCore)  [`PySide6.QtDBus`](https://doc.qt.io/qtforpython-6/PySide6/QtDBus/index.html#module-PySide6.QtDBus)  [`PySide6.QtDesigner`](https://doc.qt.io/qtforpython-6/PySide6/QtDesigner/index.html#module-PySide6.QtDesigner)  [`PySide6.QtGraphs`](https://doc.qt.io/qtforpython-6/PySide6/QtGraphs/index.html#module-PySide6.QtGraphs)  [`PySide6.QtGraphsWidgets`](https://doc.qt.io/qtforpython-6/PySide6/QtGraphsWidgets/index.html#module-PySide6.QtGraphsWidgets)  [`PySide6.QtGui`](https://doc.qt.io/qtforpython-6/PySide6/QtGui/index.html#module-PySide6.QtGui)  [`PySide6.QtHelp`](https://doc.qt.io/qtforpython-6/PySide6/QtHelp/index.html#module-PySide6.QtHelp)  [`PySide6.QtHttpServer`](https://doc.qt.io/qtforpython-6/PySide6/QtHttpServer/index.html#module-PySide6.QtHttpServer)  [`PySide6.QtLocation`](https://doc.qt.io/qtforpython-6/PySide6/QtLocation/index.html#module-PySide6.QtLocation)  [`PySide6.QtMultimedia`](https://doc.qt.io/qtforpython-6/PySide6/QtMultimedia/index.html#module-PySide6.QtMultimedia)  [`PySide6.QtMultimediaWidgets`](https://doc.qt.io/qtforpython-6/PySide6/QtMultimediaWidgets/index.html#module-PySide6.QtMultimediaWidgets)  [`PySide6.QtNetwork`](https://doc.qt.io/qtforpython-6/PySide6/QtNetwork/index.html#module-PySide6.QtNetwork)  [`PySide6.QtNetworkAuth`](https://doc.qt.io/qtforpython-6/PySide6/QtNetworkAuth/index.html#module-PySide6.QtNetworkAuth)  [`PySide6.QtNfc`](https://doc.qt.io/qtforpython-6/PySide6/QtNfc/index.html#module-PySide6.QtNfc)  [`PySide6.QtOpenGL`](https://doc.qt.io/qtforpython-6/PySide6/QtOpenGL/index.html#module-PySide6.QtOpenGL)  [`PySide6.QtOpenGLWidgets`](https://doc.qt.io/qtforpython-6/PySide6/QtOpenGLWidgets/index.html#module-PySide6.QtOpenGLWidgets)  [`PySide6.QtPdf`](https://doc.qt.io/qtforpython-6/PySide6/QtPdf/index.html#module-PySide6.QtPdf)  [`PySide6.QtPdfWidgets`](https://doc.qt.io/qtforpython-6/PySide6/QtPdfWidgets/index.html#module-PySide6.QtPdfWidgets)  [`PySide6.QtPositioning`](https://doc.qt.io/qtforpython-6/PySide6/QtPositioning/index.html#module-PySide6.QtPositioning)  [`PySide6.QtPrintSupport`](https://doc.qt.io/qtforpython-6/PySide6/QtPrintSupport/index.html#module-PySide6.QtPrintSupport)  [`PySide6.QtQml`](https://doc.qt.io/qtforpython-6/PySide6/QtQml/index.html#module-PySide6.QtQml)  [`PySide6.QtQuick`](https://doc.qt.io/qtforpython-6/PySide6/QtQuick/index.html#module-PySide6.QtQuick)  [`PySide6.QtQuick3D`](https://doc.qt.io/qtforpython-6/PySide6/QtQuick3D/index.html#module-PySide6.QtQuick3D)  [`PySide6.QtQuickControls2`](https://doc.qt.io/qtforpython-6/PySide6/QtQuickControls2/index.html#module-PySide6.QtQuickControls2)  [`PySide6.QtQuickTest`](https://doc.qt.io/qtforpython-6/PySide6/QtQuickTest/index.html#module-PySide6.QtQuickTest)  [`PySide6.QtQuickWidgets`](https://doc.qt.io/qtforpython-6/PySide6/QtQuickWidgets/index.html#module-PySide6.QtQuickWidgets)  [`PySide6.QtRemoteObjects`](https://doc.qt.io/qtforpython-6/PySide6/QtRemoteObjects/index.html#module-PySide6.QtRemoteObjects)  [`PySide6.QtScxml`](https://doc.qt.io/qtforpython-6/PySide6/QtScxml/index.html#module-PySide6.QtScxml)  [`PySide6.QtSensors`](https://doc.qt.io/qtforpython-6/PySide6/QtSensors/index.html#module-PySide6.QtSensors)  [`PySide6.QtSerialBus`](https://doc.qt.io/qtforpython-6/PySide6/QtSerialBus/index.html#module-PySide6.QtSerialBus)  [`PySide6.QtSerialPort`](https://doc.qt.io/qtforpython-6/PySide6/QtSerialPort/index.html#module-PySide6.QtSerialPort)  [`PySide6.QtSpatialAudio`](https://doc.qt.io/qtforpython-6/PySide6/QtSpatialAudio/index.html#module-PySide6.QtSpatialAudio)  [`PySide6.QtSql`](https://doc.qt.io/qtforpython-6/PySide6/QtSql/index.html#module-PySide6.QtSql)  [`PySide6.QtStateMachine`](https://doc.qt.io/qtforpython-6/PySide6/QtStateMachine/index.html#module-PySide6.QtStateMachine)  [`PySide6.QtSvg`](https://doc.qt.io/qtforpython-6/PySide6/QtSvg/index.html#module-PySide6.QtSvg)  [`PySide6.QtSvgWidgets`](https://doc.qt.io/qtforpython-6/PySide6/QtSvgWidgets/index.html#module-PySide6.QtSvgWidgets)  [`PySide6.QtTest`](https://doc.qt.io/qtforpython-6/PySide6/QtTest/index.html#module-PySide6.QtTest)  [`PySide6.QtTextToSpeech`](https://doc.qt.io/qtforpython-6/PySide6/QtTextToSpeech/index.html#module-PySide6.QtTextToSpeech)  [`PySide6.QtUiTools`](https://doc.qt.io/qtforpython-6/PySide6/QtUiTools/index.html#module-PySide6.QtUiTools)  [`PySide6.QtWebChannel`](https://doc.qt.io/qtforpython-6/PySide6/QtWebChannel/index.html#module-PySide6.QtWebChannel)  [`PySide6.QtWebEngineCore`](https://doc.qt.io/qtforpython-6/PySide6/QtWebEngineCore/index.html#module-PySide6.QtWebEngineCore)  [`PySide6.QtWebEngineQuick`](https://doc.qt.io/qtforpython-6/PySide6/QtWebEngineQuick/index.html#module-PySide6.QtWebEngineQuick)  [`PySide6.QtWebEngineWidgets`](https://doc.qt.io/qtforpython-6/PySide6/QtWebEngineWidgets/index.html#module-PySide6.QtWebEngineWidgets)  [`PySide6.QtWebSockets`](https://doc.qt.io/qtforpython-6/PySide6/QtWebSockets/index.html#module-PySide6.QtWebSockets)  [`PySide6.QtWebView`](https://doc.qt.io/qtforpython-6/PySide6/QtWebView/index.html#module-PySide6.QtWebView)  [`PySide6.QtWidgets`](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html#module-PySide6.QtWidgets)  [`PySide6.QtXml`](https://doc.qt.io/qtforpython-6/PySide6/QtXml/index.html#module-PySide6.QtXml)

模块很多，但不是所有模块都常用，其中，常用的模块为：

- QtCore
- QtGui
- QtWidgets
- QtQuick
- QtQml



模块支持的类：

'QtCore', 

https://doc.qt.io/qt-6/qtcore-module.html

'QtGui', 

https://doc.qt.io/qt-6/qtgui-module.html

'QtWidgets', 

https://doc.qt.io/qt-6/qtwidgets-module.html

https://doc.qt.io/qt-6/qtquick-module.html

https://doc.qt.io/qt-6/qtqml-module.html



命名规则总结：

模块是Qt开头的，

具体的类是Q开头（不含Qt开头），

命名采用大驼峰规则，即每个字段的首字母大写，直接连接每个字段。

Widgets结尾的模块提供了只能用于`QApplication`







## 3 Qt程序的基本结构和两种控件



必须是，先创建程序类实例，再创建控件，最后运行程序类实例的循环方法



简单说一下程序由那几部分组成，内容不多，主要时为了引出后面三种主窗口、消息机制、QtQuick程序，这里是打一下基础。可能需要制作一些结构示意图（手绘风格）。



区分一下`QtQuick`与`QtWidgets`





## 4 Qt程序的三种程序类

如上节所讲，每个Qt程序只允许同时运行一个程序类实例，同时，该程序类实例也决定了这个Qt程序是什么类型的程序。因为，不同的程序类，实现的功能也不一样：

- `QCoreApplication`类，使用`from PySide6.QtCore import QCoreApplication`导入，不能运行任何GUI控件，只包含基本的事件循环机制，所以只能用于创建无GUI控件的控制台程序。
- `QGuiApplication`类，继承自`QCoreApplication`类，使用`from PySide6.QtGui import QGuiApplication`导入，
- `QApplication`类，继承自`QGuiApplication`类，使用`from PySide6.QtWidgets import QApplication`导入，



三者的继承关系为：`QCoreApplication -> QGuiApplication -> QApplication`。因此，继承关系也呼应了三者功能越来越强大的原因



### 4.1 `QCoreApplication`类



`QCoreApplication`的相关用法：

官网文档：https://doc.qt.io/qtforpython-6/PySide6/QtCore/QCoreApplication.html#more



```python3
# 控制台程序的简单示例
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QCoreApplication,QTimer

app = QCoreApplication()
QTimer.singleShot(1000,lambda :print('app is running'))
QTimer.singleShot(2000,lambda :print('app is still running'))
QTimer.singleShot(3000,app.quit)
app.exec()
```



```python3
# 控制台程序的复杂示例
import sys
import threading
from PySide6.QtCore import QCoreApplication,Signal,QObject

# 定义输入内容接收器类，用于处理输入的内容，通过信号传递内容
class input_receiver(QObject):
    # 定义信号
    signal = Signal(str)

    def __init__(self):
        super().__init__()
        # 连接信号，把信号接收的内容传递给处理函数
        self.signal.connect(self.handle_input)

    # 处理输入内容的函数
    def handle_input(self,data):
        # 处理退出信号
        if data.strip().lower() == 'exit':
            QCoreApplication.quit()
            return
        print(f'输入的内容为：{data.strip()}')
        print('请输入内容 (输入 exit 退出)：')

# 创建输入内容接收器对象
receiver = input_receiver()

# 无限循环获取终端输入并发送信号
def read_stdin():
    while True:
        line = sys.stdin.readline()
        # 发送信号给输入内容接收器
        receiver.signal.emit(line)

# 必须在单独的线程中执行，否则没法正常执行Qt的消息循环
thread = threading.Thread(target=read_stdin,daemon=True)
thread.start()

# 输出一次提示
print('请输入内容 (输入 exit 退出)：')

app = QCoreApplication()
app.exec()
```

上面示例的变种：

```python3
import sys
import threading
from PySide6.QtCore import QCoreApplication,Signal,QObject

# 定义输入内容接收器类，用于创建信号
class input_receiver(QObject):
    # 定义信号
    signal = Signal(str)
    def __init__(self):
        super().__init__()

# 创建输入内容接收器对象
receiver = input_receiver()

# 处理输入内容的函数
def handle_input(data):
    # 处理退出信号
    if data.strip().lower() == 'exit':
        QCoreApplication.quit()
        return
    print(f'输入的内容为：{data.strip()}')
    print('请输入内容 (输入 exit 退出)：')

# 连接信号，把信号接收的内容传递给处理函数
receiver.signal.connect(handle_input)

# 无限循环获取终端输入并发送信号
def read_stdin():
    while True:
        line = sys.stdin.readline()
        # 发送信号给输入内容接收器
        receiver.signal.emit(line)

# 必须在单独的线程中执行，否则没法正常执行Qt的消息循环
thread = threading.Thread(target=read_stdin,daemon=True)
thread.start()

# 输出一次提示
print('请输入内容 (输入 exit 退出)：')

app = QCoreApplication()
app.exec()
```







### 4.3 `QApplication`类

必须在创建QWidget控件之前创建QApplication实例



## 5 `QtWidgets`的三种主窗口



（下面的图片用表格重新写一下）





![mainwindow_1](qt_for_python.assets/mainwindow_1.png)





```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QDialog,
)

app = QApplication()

window = QWidget()
window = QMainWindow()
window = QDialog()

window.resize(400,300)

window.show()
app.exec()
```





`QDialog`的模态显示：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
)

# 必须在创建QWidget控件之前创建QApplication实例
app = QApplication()

# 窗口1正常显示
window = QDialog()
window.setWindowTitle('窗口1')
window.resize(400,300)
window.show()

# 窗口2模态显示
window2=QDialog()
window2.setWindowTitle('窗口2')
window2.resize(400,300)
window2.exec()

app.exec()
```





## 6 `QtWidgets`的信号与事件

信号（类似于消息）与事件（类似于槽函数）

为什么要混到一起讲？因为机制类似，但细节上不完全一样。



窗口的关闭事件：

```python3
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox,
    QPushButton
)
from PySide6.QtGui import QIcon

app = QApplication()
window = QWidget(windowIcon=QIcon.fromTheme(QIcon.ThemeIcon.ViewFullscreen))
window.resize(400,300)
window.show()
window2 = QWidget(windowIcon=QIcon.fromTheme(QIcon.ThemeIcon.MediaTape))
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.alert(window,0))
window2.show()

window2.closeEvent = lambda e: e.accept() if QMessageBox.question(window2,'消息','你确定要退出吗？', QMessageBox.Yes|QMessageBox.No, QMessageBox.No) == QMessageBox.Yes else e.ignore()

app.exec()
```



## 7 `QtQuick`的主窗口

QtQuick基础文档：

https://doc.qt.io/qt-6/qtquick-index.html

QML基础文档：

https://doc.qt.io/qt-6/qmlreference.html



基本类型：

https://doc.qt.io/qt-6/qtquick-qmlmodule.html

常用控件的基本类型：

https://doc.qt.io/qt-6/qtquick-controls-qmlmodule.html

对话框的基本类型：

https://doc.qt.io/qt-6/qtquick-dialogs-qmlmodule.html

QtQml的基本类型：

https://doc.qt.io/qt-6/qtqml-qmlmodule.html



QtQuick的基本示例：

使用`QQuickView`：

加载QML文件（使用`QQuickView`）：

```python3
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl
from PySide6.QtQuick import QQuickView

app = QGuiApplication()

# main.qml 内容为：
'''
import QtQuick

Rectangle {
    id: main
    width: 200
    height: 200
    color: 'green'

    Text {
        text: 'Hello World'
        anchors.centerIn: main
    }
}
'''
view = QQuickView(source=QUrl('./main.qml'))
view.resize(200,200)
view.setTitle('Main')
view.show()

app.exec()
```

加载QML字符串（使用`QQuickView`和`QQmlComponent`）：

```python3
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl,QByteArray
from PySide6.QtQuick import QQuickView
from PySide6.QtQml import QQmlComponent

app = QGuiApplication()

qml_string = '''
import QtQuick

Rectangle {
    id: main
    width: 200
    height: 200
    color: 'green'

    Text {
        text: 'Hello World'
        anchors.centerIn: main
    }
}
'''

view = QQuickView()
# 使用view的engine创建component
component = QQmlComponent(view.engine())
# 给component加载qml字符串
component.setData(QByteArray(qml_string.encode()),QUrl())
# 让view的根内容变成component，并将实际内容变为component的生成内容
view.setContent(QUrl(), component, component.create())

view.resize(200,200)
view.setTitle('Main')

view.show()

app.exec()
```

加载QML字符串（写入临时文件，也兼容Qt中其他只能加载文件的地方）：

```python3
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl
from PySide6.QtQuick import QQuickView
import tempfile

app = QGuiApplication()

qml_string = '''
import QtQuick

Rectangle {
    id: main
    width: 200
    height: 200
    color: 'green'

    Text {
        text: 'Hello World'
        anchors.centerIn: main
    }
}
'''
# 将字符串写入临时文件
with tempfile.NamedTemporaryFile(delete=False) as qml_file:
    qml_file.write(qml_string.encode())

view = QQuickView(source=QUrl.fromLocalFile(qml_file.name))

# 删除临时文件
import os
os.remove(qml_file.name)
# 或者 os.unlink(qml_file.name)

view.resize(200,200)
view.setTitle('Main')

view.show()

app.exec()
```

不想手动删除临时文件的话，可以使用`QTemporaryFile`：

```python3
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl,QTemporaryFile
from PySide6.QtQuick import QQuickView

app = QGuiApplication()

qml_string = '''
import QtQuick

Rectangle {
    id: main
    width: 200
    height: 200
    color: 'green'

    Text {
        text: 'Hello World'
        anchors.centerIn: main
    }
}
'''
# 将字符串写入临时文件，自动生成随机后缀，程序退出后自动删除
# 可以指定临时文件的非随机部分名和路径，但要求路径所表示的文件夹已经存在，否则不能正常创建临时文件
qml_file = QTemporaryFile()
if qml_file.open():
    qml_file.write(qml_string.encode())
    qml_file.close()
    # 或者使用 qml_file.flush() 写入磁盘文件

view = QQuickView(source=QUrl.fromLocalFile(qml_file.fileName()))


view.resize(200,200)
view.setTitle('Main')

view.show()

app.exec()
```

使用`QQmlApplicationEngine`加载文件和字符串都很简单，但不同于`QQuickView`，该控件默认不创建用于显示内容的主窗口，需要在QML中额外定义一个主窗口（`Window`或者`ApplicationWindow`都可以），并在主窗口的节点下挂载其他控件或者内容：

加载QML文件（使用`QQmlApplicationEngine`）：

```python3
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

app = QGuiApplication()

# main.qml 内容为：
'''
import QtQuick.Window

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        color: 'green'

        Text {
            text: 'Hello World'
            anchors.centerIn: main
        }
    }
}
'''
engine = QQmlApplicationEngine(QUrl('./main.qml'))

app.exec()
```

加载QML字符串（使用`QQmlApplicationEngine`生成窗口和窗口的内容）：

```python3
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

app = QGuiApplication()

qml_src = '''
import QtQuick.Window

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        color: 'green'

        Text {
            text: 'Hello World'
            anchors.centerIn: main
        }
    }
}
'''
engine = QQmlApplicationEngine()
engine.loadData(qml_src.encode('utf-8'),QUrl())

app.exec()
```

需要注意的是，在使用`QQmlApplicationEngine`的示例中，虽然只导入了`QtQuick.Window`模块，没有主动导入其他相关模块，但依然可以使用除了`Window`类型之外的其他类型，比如示例中的`Rectangle`类型和`Text`类型，这是因为在`QQmlApplicationEngine`或者`QQmlEngine`中，涉及到QML文件时，会自动注册`QtQuick`直属的类型（https://doc.qt.io/qt-6/qtquick-qmlmodule.html#object-types）和`QtQml`直属的类型（https://doc.qt.io/qt-6/qtqml-qmlmodule.html#object-types），这些类型无需手动导入`QtQuick`和`QtQml`即可使用。

不过，`Window`类型只是在当前Qt版本（6.x）划分为`QtQuick`的直属类型，底层为了兼容旧版本（5.x）还是将其算作原来独立模块（`QtQuick.Window`）的类型，依然需要导入对应的模块才能使用，不会自动注册。不过，在当前Qt版本中，因为其被划分为`QtQuick`的直属类型，只是导入`QtQuick`模块的话也可以使用（相当于主动注册所有直属类型）。要验证的话也简单，将为了使用`Window`类型而不得不添加的导入语句改为`import QtQuick`，`Window`类型可以正常使用：

```python3
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

app = QGuiApplication()

qml_src = '''
import QtQuick

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        color: 'green'
        Text {
            text: 'Hello World'
            anchors.centerIn: main
        }
    }
}
'''
engine = QQmlApplicationEngine()
engine.loadData(qml_src.encode('utf-8'),QUrl())

app.exec()
```

以下为直接使用其他类型的示例：

```python3
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

app = QGuiApplication()

qml_src = '''
import QtQuick.Window

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        /*
        Qt和Application都是自动注册，
        无需手动注册。
        */
        color: Qt.rgba(0, 0.5, 0, 1)
        Text {
            text: `${Application.name} (${Application.version})` //模板字符串
            anchors.centerIn: main
        }
    }
}
'''
engine = QQmlApplicationEngine()
engine.loadData(qml_src.encode('utf-8'),QUrl())

app.exec()
```

示例中，使用`Qt`的函数生成颜色对象，使用ES标准中的模板字符串（必须使用反引号包围，格式为`` `${变量}` ``）嵌入应用名称和应用版本。QML支持C语言风格的单行注释`//`和多行注释`/*……*/`。



## 8 `QtQuick`与`QtWidgets`混合使用

使用`QQuickWidget`（相当于`QQuickView`的平替，大部分功能兼容）：

加载QML文件（使用`QQuickWidget`）：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl
from PySide6.QtQuickWidgets import QQuickWidget

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

# main.qml 内容为：
'''
import QtQuick

Rectangle {
    id: main
    width: 200
    height: 200
    color: 'green'

    Text {
        text: 'Hello World'
        anchors.centerIn: main
    }
}
'''

window = QQuickWidget(source=QUrl('./main.qml'))

window.resize(200,200)
# QQuickWidget 不支持 view.setTitle('Main')
window.setWindowTitle('Main')

window.show()

# 非QtQuick部分
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```

加载QML字符串（使用`QQuickWidget`和`QQmlComponent`）：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl,QByteArray
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtQml import QQmlComponent

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

qml_string = '''
import QtQuick

Rectangle {
    id: main
    width: 200
    height: 200
    color: 'green'

    Text {
        text: 'Hello World'
        anchors.centerIn: main
    }
}
'''

window = QQuickWidget()
# 使用view的engine创建component
component = QQmlComponent(window.engine())
# 给component加载qml字符串
component.setData(QByteArray(qml_string.encode()),QUrl())
# 让view的根内容变成component，并将实际内容变为component的生成内容
window.setContent(QUrl(), component, component.create())

window.resize(200,200)
# QQuickWidget 不支持 view.setTitle('Main')
window.setWindowTitle('Main')

window.show()

# 非QtQuick部分
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```

加载QML字符串（写入临时文件，也兼容Qt中其他只能加载文件的地方）：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl
from PySide6.QtQuickWidgets import QQuickWidget
import tempfile

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

qml_string = '''
import QtQuick

Rectangle {
    id: main
    width: 200
    height: 200
    color: 'green'

    Text {
        text: 'Hello World'
        anchors.centerIn: main
    }
}
'''
# 将字符串写入临时文件
with tempfile.NamedTemporaryFile(delete=False) as qml_file:
    qml_file.write(qml_string.encode())

window = QQuickWidget(source=QUrl.fromLocalFile(qml_file.name))

# 删除临时文件
import os
os.remove(qml_file.name)
# 或者 os.unlink(qml_file.name)

window.resize(200,200)
# QQuickWidget 不支持 view.setTitle('Main')
window.setWindowTitle('Main')

window.show()

# 非QtQuick部分
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```

不想手动删除临时文件的话，可以使用`QTemporaryFile`：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl,QTemporaryFile
from PySide6.QtQuickWidgets import QQuickWidget

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

qml_string = '''
import QtQuick

Rectangle {
    id: main
    width: 200
    height: 200
    color: 'green'

    Text {
        text: 'Hello World'
        anchors.centerIn: main
    }
}
'''

# 将字符串写入临时文件，自动生成随机后缀，程序退出后自动删除
# 可以指定临时文件的非随机部分名和路径，但要求路径所表示的文件夹已经存在，否则不能正常创建临时文件
qml_file = QTemporaryFile()
if qml_file.open():
    qml_file.write(qml_string.encode())
    qml_file.close()
    # 或者使用 qml_file.flush() 写入磁盘文件

window = QQuickWidget(source=QUrl.fromLocalFile(qml_file.fileName()))

window.resize(200,200)
# QQuickWidget 不支持 view.setTitle('Main')
window.setWindowTitle('Main')

window.show()

# 非QtQuick部分
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```

使用`QQmlApplicationEngine`（加载文件和字符串都很简单，但默认不包括窗口，需要在QML中定义）：

加载QML文件（使用`QQmlApplicationEngine`）：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

# main.qml 内容为：
'''
import QtQuick.Window

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        color: 'green'

        Text {
            text: 'Hello World'
            anchors.centerIn: main
        }
    }
}
'''
engine = QQmlApplicationEngine(QUrl('./main.qml'))

# 非QtQuick部分
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```

加载QML字符串（使用`QQmlApplicationEngine`生成窗口和窗口的内容）：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

qml_src = '''
import QtQuick.Window

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        color: 'green'
        Text {
            text: 'Hello World'
            anchors.centerIn: main
        }
    }
}
'''
engine = QQmlApplicationEngine()
engine.loadData(qml_src.encode('utf-8'),QUrl())

# 非QtQuick部分
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```



## 9 `QtWidgets`的UI文件

加载UI文件：

```python3

from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtUiTools import QUiLoader

# main.ui 文件内容如下：
'''
<?xml version='1.0' encoding='UTF-8'?>
<ui version='4.0'>
 <class>MainWindow</class>
 <widget class='QWidget' name='MainWindow'>
  <property name='geometry'>
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name='windowTitle'>
   <string>Main</string>
  </property>
  <widget class='QPushButton' name='psf'>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

app = QApplication()
# 基本结构，必须分成两步
# window = QWidget()
# window.show()
# 导入UI文件的方法是一样的结构
window = QUiLoader().load('main.ui')
window.psf.setText('click')
window.psf.clicked.connect(lambda:print('Clicked!'))
window.show()
app.exec()
```



## 10 `QtQuick`的模块（草稿状态）

除了直接导入QML文件这种使用QML文件的方式，还可以将QML文件包装为模块，通过导入模块的方式使用QML文件。

### 10.1 创建模块

要使用模块，需要先创建模块文件夹，将QML文件和`qmldir`文件放在模块文件夹中，并在`qmldir`文件中编写模块名和QML文件对应的类型名。`qmldir`文件的具体语法规则参考 https://doc.qt.io/qtforpython-6/overviews/qtqml-modules-qmldir.html。

模块文件夹的目录结构如下：

```shell
App
├── main.qml
└── qmldir
```

`main.qml`文件的内容为：

```js
import QtQuick.Window

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        color: Qt.rgba(0, 0.5, 0, 1)
        Text {
            text: `${Application.name} (${Application.version})`
            anchors.centerIn: main
        }
    }
}
```

`qmldir`文件的内容为：

```python3
module App
Main 1.0 main.qml
```

`qmldir`文件不支持注释，必须按照顺序，先写模块名定义，格式为`module {模块名}`，并且模块名必须与模块文件夹的名字一致。然后写类型定义，格式为`{类型名} {版本号} {对应的QML文件名}`。其中，类型名必须是合法的变量名，版本号只能为包含一个用于分隔版本含义的英文小数点、只有两段子版本号的合法版本号，对应的QML文件名可以使用相对路径（相对于`qmldir`文件），也可以直接不带路径前缀，表示与`qmldir`文件同目录。

### 10.2 导入模块

不同于使用普通QML文件只需加载，想要使用模块的QML文件，需要用正确的方式导入模块。

导入之前，需要将模块所在的路径添加到可识别的导入路径中，有以下几种方法：

- 设置环境变量`QML2_IMPORT_PATH`为模块文件夹所在的路径，即可识别到自定义的模块。

  比如：

  ```python3
  # Python代码中，添加下面代码至创建Qt程序之前
  import os
  os.environ['QML2_IMPORT_PATH'] = './' # 可以使用相对路径和绝对路径
  # PowerShell中的话，执行下面的命令（二选一）可以临时设置环境变量
  $env:QML2_IMPORT_PATH='./'
  Set-Item -Path Env:QML2_IMPORT_PATH -Value './'
  # CMD中，执行下面的命令（二选一）可以临时设置环境变量
  set QML2_IMPORT_PATH='./'
  setx QML2_IMPORT_PATH './'
  ```

- 通过引擎对象（`QQuickView`对象、`QQuickWidget`对象的`engine`方法返回引擎对象，而`QQmlApplicationEngine`对象本身就是引擎对象）提供的方法添加模块所在的路径，即可识别到自定义的模块。方法有：

  - 使用`setImportPathList`方法设置可识别的导入路径列表，但要包括原导入路径（使用`importPathList`方法获取）：

    ```python3
    engine.setImportPathList(
        engine.importPathList()+[
            './'
        ]
    )
    ```

  - 使用`addImportPath`方法添加模块所在的路径：

    ```python3
    engine.addImportPath('./')
    ```

设置好导入路径之后，导入模块的方法也是多种多样：

- 在QML文件（或者QML字符串）中导入模块，但需要额外创建类型的实例：

  ```python3
  # QML文件或者字符串的内容为
  '''
  import App
  Main {}
  '''
  ```

- 使用引擎对象的`loadFromModule`方法导入模块，会自动创建类型的示例：

  ```python3
  engine.loadFromModule(
      'App', # 模块名
      'Main' # 类型名
  )
  ```

完整示例如下：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

# main.qml 文件的内容为
'''
import QtQuick.Window

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        color: Qt.rgba(0, 0.5, 0, 1)
        Text {
            text: `${Application.name} (${Application.version})`
            anchors.centerIn: main
        }
    }
}
'''
# qmldir 文件的内容为
'''
module App
Main 1.0 main.qml
'''

qml_src = '''
import App
Main {}
'''
engine = QQmlApplicationEngine()
engine.addImportPath('./') # 添加模块上一级的文件为导入路径
# 两种导入方式，二选一即可，同时使用会创建两个窗口
engine.loadData(qml_src.encode('utf-8'),QUrl())
engine.loadFromModule('App','Main')

# 非QtQuick部分
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```



### 10.3 模块的自定义属性

如果只是和普通QML文件一样导入就用，那模块带来的复杂性纯属多余。既然要创建模块，自然要有不一样的地方。在创建模块时，可以在模块的QML文件中添加一些自定义的属性，内部关联使用这些自定义属性。这样就能在使用时，设置模块的自定义属性，快速创建由多种元素组合、相关属性遵循一定规则的复合控件，就像自定义了新的控件一样。

在正式了解自定义属性之前，先看一下示例。

将模块中`main.qml`文件的内容修改如下：

```js
import QtQuick.Window

Window {
    //别名属性
    property alias my_text: text.text
    //字符串类型的属性，无默认值
    property string my_color
    //字符串类型的属性，有默认值
    property string my_title: 'Main'
    //自定义属性结束
    id: window
    visible: true
    title: my_title
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        //属性未传值的话使用 Qt.rgba(0, 0.5, 0, 1)
        color: window.my_color || Qt.rgba(0, 0.5, 0, 1)
        Text {
            id: text
            text: `${Application.name} (${Application.version})`
            anchors.centerIn: main
        }
    }
}
```

这样，原本只能直接使用的模块就多了三个自定义属性：`my_text`、`my_color`、`my_title`。

自定义属性的相关语法可以参考 https://doc.qt.io/qt-6/qtqml-syntax-objectattributes.html。

这里简单介绍一下示例中用到的部分语法。

在控件的中括号内使用关键字`property`，可以创建自定义属性，格式为`property {类型} {属性名} : {默认值}`。如果没有默认值的话，则格式为`property {类型} {属性名}`。创建自定义属性时，属性名只能是小写开头。只有顶层控件的属性（含自定义属性）可以被外部访问，相当于模块的自定义属性，其他控件的属性（含自定义属性）无法被外部访问。

创建好自定义属性之后，想要使用属性（自定义属性和原生属性都可以，`id`属性除外），则必须给对应控件设置`id`属性，通过`{属性所属控件的id}.{属性名}`的格式使用属性（自定义属性和原生属性都可以，`id`属性除外）。如果在同一控件内使用属性，则可以直接使用属性名，不用表明对应控件的`id`。

对于频繁使用的属性（含自定义属性），可以使用`alias`类型，定义该属性的别名，格式为`property alias {属性名的别名} : {属性所属控件的id}.{属性名}`。如果省略属性名，比如`property alias {别名} : {属性所属控件的id}`，则别名可以当作控件的`id`来使用，此时`{别名}.{属性名}`相当于`{属性所属控件的id}.{属性名}`。

顶层控件的属性（含自定义属性）能够被外部访问，相当于模块的自定义属性，在导入模块时可以将其设置为所需的值。

以下为设置模块自定义属性的方法：

- 在导入模块前，给用引擎对象的`setInitialProperties`方法传入字典可以提前设置模块的自定义属性：

  ```python3
  engine.setInitialProperties(
      {
          'my_text':'Hello',
          'my_color':'red',
          'my_title':'Hi'
      }
  )
  ```

- 在QML文件（或者QML字符串）中导入模块时，控件的创建代码可以同时设置模块的自定义属性：

  ```python3
  # QML文件或者字符串的内容为
  '''
  import App
  Main {
      my_text: 'Hello'
      my_color: 'red'
      my_title: 'Hi'
  }
  '''
  ```

完整示例如下：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

# main.qml 文件的内容为
'''
import QtQuick.Window

Window {
    //别名属性
    property alias my_text: text.text
    //字符串类型的属性，无默认值
    property string my_color
    //字符串类型的属性，有默认值
    property string my_title: 'Main'
    //自定义属性结束
    id: window
    visible: true
    title: my_title
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        //属性未传值的话使用 Qt.rgba(0, 0.5, 0, 1)
        color: window.my_color || Qt.rgba(0, 0.5, 0, 1)
        Text {
            id: text
            text: `${Application.name} (${Application.version})`
            anchors.centerIn: main
        }
    }
}
'''
# qmldir 文件的内容为
'''
module App
Main 1.0 main.qml
'''

qml_src = '''
import App
Main {
    my_text: 'Hello'
    my_color: 'red'
    my_title: 'Hi'
}
'''
engine = QQmlApplicationEngine()
engine.addImportPath('./') # 添加模块上一级的文件为导入路径
# 在导入模块前执行，会影响两种导入方式
engine.setInitialProperties(
    {
        'my_text':'Hello',
        'my_color':'red',
        'my_title':'Hi'
    }
)
# 两种导入方式，二选一即可
# engine.loadData(qml_src.encode('utf-8'),QUrl())
engine.loadFromModule('App','Main')

# 非QtQuick部分
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```



## 11 在QML中使用Python对象

想要在QML中使用Python对象，必须要先获取上下文对象（通过引擎对象的`rootContext`方法获取），然后在上下文对象中注册`Property`属性，才能在QML中使用该属性对应的Python对象。

### 11.1 获取上下文对象

`QQuickView`获取上下文对象（为了避免QML代码出错导致程序无法正常关闭，后面注册`Property`属性的示例不使用`QtQuick`程序，这里仅作为获取上下文对象的示例）：

```python3
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl,QByteArray
from PySide6.QtQuick import QQuickView
from PySide6.QtQml import QQmlComponent

app = QGuiApplication()

qml_string = '''
import QtQuick
import QtQuick.Controls

Rectangle {
    id: main
    width: 200
    height: 200
    color: 'green'
    Button {
        text: 'Click'
        width: 100
        height: 30
        anchors.centerIn: main
        onClicked: {
        //访问注册的属性
            app.quit()
        }
    }
}
'''

view = QQuickView()
# 使用view的engine创建component
component = QQmlComponent(view.engine())
# 给component加载qml字符串
component.setData(QByteArray(qml_string.encode()),QUrl())
# 让view的根内容变成component，并将实际内容变为component的生成内容
view.setContent(QUrl(), component, component.create())

view.resize(200,200)
view.setTitle('Main')

view.show()

# 获取上下文对象
root = view.engine().rootContext()

app.exec()
```



`QQuickWidget`获取上下文对象：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl,QByteArray
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtQml import QQmlComponent

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

qml_string = '''
import QtQuick
import QtQuick.Controls

Rectangle {
    id: main
    width: 200
    height: 200
    color: 'green'
    Button {
        text: 'Click'
        width: 100
        height: 30
        anchors.centerIn: main
        onClicked: {
        //访问注册的属性
            app.quit()
        }
    }
}
'''

window = QQuickWidget()
# 使用view的engine创建component
component = QQmlComponent(window.engine())
# 给component加载qml字符串
component.setData(QByteArray(qml_string.encode()),QUrl())
# 让view的根内容变成component，并将实际内容变为component的生成内容
window.setContent(QUrl(), component, component.create())

window.resize(200,200)
# QQuickWidget 不支持 view.setTitle('Main')
window.setWindowTitle('Main')

window.show()

# 获取上下文对象
root = window.engine().rootContext()

# 非QtQuick部分，避免QML代码出错，无法正常关闭
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```



`QQmlApplicationEngine`获取上下文对象：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

qml_src = '''
import QtQuick.Window
import QtQuick.Controls

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        color: 'green'
        Button {
            text: 'Click'
            width: 100
            height: 30
            anchors.centerIn: main
            onClicked: {
            //访问注册的属性
                app.quit()
            }
        }
    }
}
'''
engine = QQmlApplicationEngine()
engine.loadData(qml_src.encode('utf-8'),QUrl())

# 获取上下文对象
root = engine.rootContext()

# 非QtQuick部分，避免QML代码出错，无法正常关闭
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```



### 11.2 注册`Property`属性

使用上下文对象的`setContextObject`方法注册一个`QObject`的`Property`属性：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl,QObject,Property
from PySide6.QtQml import QQmlApplicationEngine

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

qml_src = '''
import QtQuick.Window
import QtQuick.Controls

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        color: 'green'
        Button {
            text: 'Click'
            width: 100
            height: 30
            anchors.centerIn: main
            onClicked: {
            //访问注册的属性
                app.quit()
            }
        }
    }
}
'''
engine = QQmlApplicationEngine()
engine.loadData(qml_src.encode('utf-8'),QUrl())

# 获取上下文对象
root = engine.rootContext()

# 直接注册该对象的属性（Property）到QML全局
class Obj(QObject):
    def __init__(self):
        super().__init__()
        self._app = app
    app = Property(
        object,
        fget=lambda self:self._app,
        fset=lambda self,value:setattr(self,'_app',app)
    )
root.setContextObject(Obj())

# 非QtQuick部分，避免QML代码出错，无法正常关闭
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```



使用上下文对象的`setContextProperty`方法一次注册一个`Property`属性为任意对象：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

qml_src = '''
import QtQuick.Window
import QtQuick.Controls

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        color: 'green'
        Button {
            text: 'Click'
            width: 100
            height: 30
            anchors.centerIn: main
            onClicked: {
            //访问注册的属性
                app.quit()
            }
        }
    }
}
'''
engine = QQmlApplicationEngine()
engine.loadData(qml_src.encode('utf-8'),QUrl())

# 获取上下文对象
root = engine.rootContext()

# 一次注册一个属性（Property）到QML全局
root.setContextProperty('app',app)

# 非QtQuick部分，避免QML代码出错，无法正常关闭
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```



使用上下文对象的`setContextProperties`方法一次注册多个`Property`属性为任意对象：

```python3
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine,QQmlContext

# 非QtQuick程序只能使用QApplication，不能使用QGuiApplication
app = QApplication()

qml_src = '''
import QtQuick.Window
import QtQuick.Controls

Window {
    visible: true
    title: 'Main'
    width: 200
    height: 200
    Rectangle {
        id: main
        width: 200
        height: 200
        color: 'green'
        Button {
            text: 'Click'
            width: 100
            height: 30
            anchors.centerIn: main
            onClicked: {
            //访问注册的属性
                app.quit()
            }
        }
    }
}
'''
engine = QQmlApplicationEngine()
engine.loadData(qml_src.encode('utf-8'),QUrl())

# 获取上下文对象
root = engine.rootContext()

# 使用PropertyPair类
class PropertyPair(QQmlContext.PropertyPair):
    def __init__(self,name:str,value:object):
        super().__init__()
        self.name = name
        self.value = value

# 一次注册多个属性（Property）到QML全局
root.setContextProperties(
    [
        PropertyPair('app',app)
    ]
)

# 非QtQuick部分，避免QML代码出错，无法正常关闭
window2 = QWidget()
window2.resize(400,300)
QPushButton('click',window2).clicked.connect(lambda :app.quit())
window2.show()

app.exec()
```



# Qt For Python 札记（2026版）

## 0 为何而写

2025版在创作过程中添加了不少对之前内容的修正、补充，但还是未能做到内容正确、全面。对于之前内容错误、遗漏之处，2026年，笔者将继续本教程系列的更新。当然，基础、理论部分已经写了不少，除非Qt框架后续更新之后有变动，基础、理论部分不会有其他新内容了，只会补充遗漏、修正错误、扩展用法、衍生相关内容。

## 1 （修正2025.13）

原内容存在错误，修正错误。

## 1 （补充2025.13）

原内容不全面，补充内容。

## 1 （扩展2025.13）

从原内容想到的其他内容，虽然可以作为独立的内容写标题，但这部分内容确实是看完原内容才有了创作契机。
