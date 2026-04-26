# Flet札记（2026）

[TOC]

## 0 为何而写

Flet（官网https://flet.dev/）是一款优秀的WebUI、GUI框架，底层使用谷歌的Flutter框架实现，所以控件比较美观。而Flet框架实现了Flutter框架的Python接口，方便Python开发者使用Flutter框架的控件快速搭建出美观的UI界面。

虽然Flet框架类似其他基于Web的GUI框架（比如NiceGUI），但Flet框架提供了运行时，使其作为桌面程序运行时，不需要额外安装类似浏览器的框架（比如`pywebview`库）来提供壳子，因为框架自带壳子。另外Flet框架也提供了完善的打包、编译支持（虽然体积依然比较大），方便分发给客户（无需安装Python）。

因此，基于对各方面优缺点的考量，笔者觉得有必要给读者介绍一下Flet框架，算是作为NiceGUI、Qt等现有方案的补充，也是使用Python开发GUI程序时一个不错的备选方案。

## 1 安装Flet（更新中）

一如既往，依然使用uv创建初始环境。

首先，新建一个空白文件夹，笔者这里新建了`flet_app`文件夹。进入该文件夹，运行`uv init`，即可初始化该文件夹为项目文件夹（`uv`命令需要使用`pip install uv`安装）。

此时创建的项目是空白项目，没有添加任何依赖，还需要使用`uv add flet`添加依赖（或者使用`uv add flet[all]`包含其他运行方式的可选依赖，但不包括特定控件所需的扩展），并自动创建虚拟环境。

如果想要将虚拟环境中的所有库升级至最新稳定版，可以使用`uv sync -U`。

若是只想升级指定库，比如`flet`，则使用`uv sync -P flet`。

升级指定库至最新测试版。因为本章节创作时，Flet的1.0版本尚未正式发布，需要升级至最新测试版才行，或者读者想要使用最新测试版的功能，则可以使用`uv sync -P flet --prerelease allow`命令，将指定库升级至最新测试版。



（因为部分组件在Github上，并且部分涉及Flutter框架、dart库的操作也需要通过国内镜像加速，因此，后面还要补充中国环境下，如何设置相关的镜像、加速。）



## 2 Flet程序的基本结构

先看示例，简单了解一下Flet程序的基本结构：

```python3
import flet as ft

def main(page: ft.Page):
    page.add(ft.Button('Hello'))

ft.run(main)
```





完整一点的示例：

```python3
import flet as ft

async def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 300
    #page.window.left = 400
    #page.window.top = 300
    page.title = 'Hello'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Button(
            'Hello World',
            on_click=page.window.close
        )
    )
    await page.window.center()

ft.run(main)
```

