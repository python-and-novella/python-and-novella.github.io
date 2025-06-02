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

和所有框架、语言开始学习的惯例一样，先看看prompt_toolkit的Hello World程序是什么样：

```python3
from prompt_toolkit import prompt

text = prompt('请输入任何内容：')
print(f'输入的内容是: {text}')
```

![hello_world_1](prompt_toolkit.assets/hello_world_1.png)

框架支持很多终端交互，这里演示的是获取用户输入的过程，因此，程序最终输出的是用户输入的内容。

## 2 基础知识



已知知识点如下：

- 两种使用方式：响应式（直接输出），应用式（进入应用的消息循环）







（需要深入挖掘所有的模块和手册，进一步确定学习顺序）



## 4 具体组件（暂定）



只提供widgets？layout和其他controls是否划归本章节，还是在基础里学习？



（这部分需要查看手册和官方示例，挖掘API中widgets提供的组件）





## 4 进阶技巧与实例