# PySide6拾遗

## 0 前言

PySide6各类教程已经有很多，笔者就不班门弄斧了。不过，框架在使用过程中还是有不少难点，对于心急的初学者来说，很容易在找不到解决方法之后轻言放弃。因此，笔者将代入初学者的视角，按照学习顺序记录一下使用过程中遇到的难点，并给出解释和解决方法，以便于有一定基础但囿于难点的读者按图索骥。

## 1 基础篇

本章主要介绍那些完成基础GUI程序时遇到的难点。

### 1.1 安装PySide6

学习的第一步就是安装库。不过，官方提供了不少相关的库，但并非所有的库都是必需的。以下面的虚拟环境为例，笔者添加了官方提供的相关库，其依赖关系如下（使用`uv tree`生成）：

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

项目下主动添加的库为：`pyside6`、`pyside6-examples`、`shiboken6-generator`。其中，添加了`pyside6`之后，会自动安装相关的依赖，此时就可以开始学习，无需额外安装其他相关库。当然，其他的库也有用处，只是刚开始学习的时候不一定需要。`pyside6-examples`是官方编写的示例程序，可在`pyside6_uv_app\.venv\Lib\site-packages\PySide6\examples`中找到。`shiboken6-generator`是绑定生成器，只有涉及到绑定（基于C++头文件生成Python的接口）Qt或者C++程序的接口时，才需要这个库。

需要注意的是，在使用`uv`管理虚拟环境时，单独移除`pyside6-examples`会导致`pyside6`的`__init__.py`丢失，需要使用`uv sync --reinstall`重新安装。

### 1.2 PySide6的模块（暂定）

（内容待定）

熟悉模块

PySide6各个模块的功能和用途

```python3
['QtCore', 'QtGui', 'QtWidgets', 'QtPrintSupport', 'QtSql', 'QtNetwork', 'QtTest', 'QtConcurrent', 'QtDBus', 'QtDesigner', 'QtXml', 'QtHelp', 'QtMultimedia', 'QtMultimediaWidgets', 'QtOpenGL', 'QtOpenGLWidgets', 'QtPdf', 'QtPdfWidgets', 'QtPositioning', 'QtLocation', 'QtNetworkAuth', 'QtNfc', 'QtQml', 'QtQuick', 'QtQuick3D', 'QtQuickControls2', 'QtQuickTest', 'QtQuickWidgets', 'QtRemoteObjects', 'QtScxml', 'QtSensors', 'QtSerialPort', 'QtSerialBus', 'QtStateMachine', 'QtTextToSpeech', 'QtCharts', 'QtSpatialAudio', 'QtSvg', 'QtSvgWidgets', 'QtDataVisualization', 'QtGraphs', 'QtGraphsWidgets', 'QtBluetooth', 'QtUiTools', 'QtAxContainer', 'QtWebChannel', 'QtWebEngineCore', 'QtWebEngineWidgets', 'QtWebEngineQuick', 'QtWebSockets', 'QtHttpServer', 'QtWebView', 'Qt3DCore', 'Qt3DRender', 'Qt3DInput', 'Qt3DLogic', 'Qt3DAnimation', 'Qt3DExtras', 'QtExampleIcons']
```

https://doc.qt.io/qtforpython-6/py-modindex.html





### 1.3 PySide6程序的基本结构





### 1.4 三种主窗口







## 2 进阶篇

本章主要介绍那些完成功能丰富的GUI程序时遇到的难点。

## 3 实例篇

本章主要介绍那些实现实际项目需求时遇到的难点。