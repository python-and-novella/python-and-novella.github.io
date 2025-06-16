# NiceGUI拾遗

## 0 为什么要写这个系列

《NiceGUI的中文入门教程》完成后，NiceGUI一直处于不断更新中，同时《NiceGUI的中文入门教程》也不是完美的，需要不断补充、修改内容，这也导致该教程后续不断增补内容，影响教程的完整性，也不好写标题。为了和《NiceGUI的中文入门教程》的系统性教程做出区分，《NiceGUI拾遗》应运而生。《NiceGUI拾遗》采用线性编写原则，按照时间顺序编写《NiceGUI的中文入门教程》中的遗漏内容、NiceGUI的更新内容，采取想起哪些写哪些的原则，但是标题中会尽量简短地与内容关联，避免出现《NiceGUI的中文入门教程》中为了确保教程完整性不得不沿用原标题的情况。

此外，《NiceGUI的中文入门教程》中的具体示例也会放在这里继续更新，并在标题中体现示例的主要用途。

简而言之，本系列教程可以看作是《NiceGUI的中文入门教程》的续作，但是叙述上不再沿用系统性架构，而是采用类似于敏捷开发式叙述方式，随时补充新内容且不会在原始位置修改已发布的内容（但可能单开一节用于修订之前的内容）。

## 1 使用环境变量配置NiceGUI程序

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

## 2 通过点击按钮来关闭NiceGUI程序

一般来说，关闭NiceGUI程序的正确操作是在终端按下`Ctrl`+`C`。但是，NiceGUI程序作为一个网站运行时，用户是接触不到终端的。假如需要通过网页关闭NiceGUI程序，可以使用`app.shutdown()`来关闭整个程序，代码如下：

```python3
from nicegui import ui,app

ui.button('shutdown',on_click=app.shutdown)

ui.run(native=True)
```





1，在native mode下，`ui.download`不能下载怎么办？

因为pywebview默认不允许网页弹出下载，需要使用`app.native.settings['ALLOW_DOWNLOADS'] = True`修改pywebview的配置，代码如下：

```python3
from nicegui import ui, app

app.native.settings['ALLOW_DOWNLOADS'] = True
ui.button("Download", on_click=lambda: ui.download(b'Demo text','demo_file.txt'))

ui.run(native=True)
```

2，如何让native mode运行在QT的QtWebEngine中？

默认情况下，如果Windows系统安装了Webview2，native mode优先采用Webview2当作浏览器运行时，哪怕Python添加了QT6相关的包（PyQT6、PySide6）。如果想要native mode采用QtWebEngine当做浏览器运行时，需要手动指定PyWebview的Web engine（参考文档见[官方](https://pywebview.flowrl.com/guide/web_engine.html)），代码如下：

```python3
from nicegui import ui, app

app.native.start_args['gui'] = 'qt'
app.native.start_args['icon'] = 'favicon.ico'
# For 'gui' arg,you needn't assign it usually,besides you want to change the render; 
#  'edgechromium' is best on Windows ;
# qt based is a litte heavy,but it can be used on Windows/Linux/Mac;
# try to install qt libs by `pip install pywebview[qt]` or else:
#  'qt' needs ["QtPy", "PyQt6", "PyQt6-WebEngine"];
#  'qt6' needs ["QtPy", "PyQt6", "PyQt6-WebEngine"];
#  'pyside6' needs ["QtPy", "PySide6"];

ui.button('Say Hi',on_click=lambda :ui.notify('Hello World!'))

ui.run(native=True)
```

使用QtWebEngine当做浏览器运行时，窗口图标默认为Windows默认图标，而不是Python的图标，可以像代码中一样，使用`app.native.start_args['icon'] = 'favicon.ico'`指定，路径默认为源代码同目录，可以使用相对路径或者绝对路径。

3，如何让native mode运行时使用固定版本或者非系统自带的Webview2？

默认情况下，如果Windows系统安装了Webview2，native mode优先采用系统的Webview2当作浏览器运行时。但是，系统的Webview2更新很快，而且是自动进行，若是开发的程序与最新版Webview2不兼容或者想要避免系统Webview2版本更新导致的潜在问题，则可以设置环境变量`WEBVIEW2_BROWSER_EXECUTABLE_FOLDER`为指定版本Webview2解压之后的路径，让native mode运行时使用固定版本Webview2。

固定版本Webview2可以到[Webview2官网](https://developer.microsoft.com/zh-cn/microsoft-edge/webview2)下载，本解决方案参考自[微软开发者文档](https://learn.microsoft.com/zh-cn/microsoft-edge/webview2/concepts/distribution?tabs=dotnetcsharp#details-about-the-fixed-version-runtime-distribution-mode)。

代码如下：

```python3
from nicegui import ui
import os
import pathlib
os.environ['WEBVIEW2_BROWSER_EXECUTABLE_FOLDER'] = str(pathlib.Path(__file__).parent/'Microsoft.WebView2.FixedVersionRuntime.135.0.3179.98.x64')

ui.run(native=True)
```

这里是将固定版本Webview2解压之后，将包含可执行文件`msedgewebview2.exe`的文件夹放到源代码的同级目录中，读者在实际使用时可以自行变换路径。





1，网站在标题栏的logo是NiceGUI的logo，如何指定为自己的logo？

修改`ui.run()`的默认参数`favicon`为自己logo的地址或者emoji字符`🚀`，例如：`ui.run(favicon='🚀')`。







1，为什么有时候创建在`ui.refreshable`装饰的函数内的控件不会刷新？

以下面代码为例：

```python3
from nicegui import ui
from datetime import datetime

@ui.refreshable
def time_box(container:ui.element):
    with container:
        ui.label(datetime.now())

card1 = ui.card()
time_box(card1)

ui.button('refresh1',on_click=time_box.refresh)

ui.run(native=True)
```

先创建了一个`ui.card`，然后给`refreshable`修饰的方法传入，在方法内部，想要通过`with container`的方法，在`ui.card`内部创建可以刷新的时间标签。然而，实际执行的时候就会发现，标签并没有如预期那样刷新，而是不断创建新的标签。

为什么？

其实，`refreshable`方法相当于创建了一个可刷新的元素，并将方法内部创建的元素的父元素指定为可刷新元素。每次调用刷新方法，实际上是先清空可刷新元素，然后执行一遍方法内部创建元素的过程。但是，使用`with container`之后，接下来创建的元素的父元素是`container`，而不是可刷新元素，因此，每次调用刷新方法之后，方法内部创建的元素不会被清空，反而因为重新创建了一遍元素，`container`下的元素会多一个。

如果想要实现借用已经创建的元素当容器，让内部元素可以刷新，就要在创建之前，模拟可刷新元素的清空操作：

```python3
from nicegui import ui
from datetime import datetime

@ui.refreshable
def time_box(container:ui.element):
    container.clear()
    with container:
        ui.label(datetime.now())

card1 =ui.card()
time_box(card1)

ui.button('refresh1',on_click=time_box.refresh)

ui.run(native=True)
```

### 4.4 `ui.button`

1，想要在定义之后修改按钮的颜色，但是`bg-*`的TailWindCSS样式没有用，怎么实现？

按钮的默认颜色由Quasar控制，而Quasar的颜色应用使用最高优先级的`!important`，TailWindCSS的颜色样式默认比这个低，所以无法成功。如果想修改颜色，可以修改按钮的`color`属性。或者使用`!bg-*`来强制应用。代码如下：

```python3
from nicegui import ui

ui.button('button').props('color="red-10"')
#或者强制应用TailWindCSS
ui.button('button').classes('!bg-red-700')

ui.run(native=True)
```

注意：Quasar的颜色体系和TailWindCSS的颜色体系不同。Quasar中，使用`color-[1-14]`来表示颜色，数字表示颜色程度，可选。TailWindCSS中，使用`type-color-[50-950]`表示颜色，type为功能类别，数字表示颜色程度，可选。需要注意代码中不同方式使用的颜色体系。

2，不擅长CSS的话，怎么用`ui.button`实现一个 Floating Action Button？

Floating Action Button是特定最小尺寸的圆角按钮，如果熟悉CSS样式的话，可以将普通的按钮改成类似样式，但是，`ui.button`自带一个`fab`属性（`props`），可以一步完成，省去调整CSS的过程，代码如下：

```python3
from nicegui import ui

ui.button(icon='home', on_click=lambda: ui.notify('home')).props('fab')

ui.run(native=True)
```

3，如何实现按钮点击后才执行特定操作？

使用异步等待。

```python3
from nicegui import ui

@ui.page('/')
async def index():
    b = ui.button('Step')
    await b.clicked()
    ui.label('One')
    await b.clicked()
    ui.label('Two')
    await b.clicked()
    ui.label('Three')

ui.run()
```

4，如何实现嵌入按钮的图标，点击图标并不触发按钮的点击事件？

使用JavaScript中对应事件的`stopPropagation()`方法阻止事件穿透即可。

```python3
from nicegui import ui

with ui.button('Item').classes('w-96') as button:
    button.on_click(lambda :ui.notify('button'))
    ui.space()
    icon = ui.icon('delete')
    icon.on('click',js_handler='(e)=>{e.stopPropagation()}')
    icon.on('click',lambda :ui.notify('icon'))
    
ui.run(native=True)
```

### 4.5 `ui.page`

1，如何通过传参的形式动态修改页面内容？

使用参数注入，基于FastAPI的https://fastapi.tiangolo.com/tutorial/path-params/ 和 https://fastapi.tiangolo.com/tutorial/query-params/ 或者 https://fastapi.tiangolo.com/advanced/using-request-directly/ ，可以捕获url传入的参数，并用在Python程序中。

```python3
from nicegui import ui

@ui.page('/icon/{icon}')
def icons(icon: str, amount: int = 1):
    ui.label(icon).classes('text-h3')
    with ui.row():
        [ui.icon(icon).classes('text-h3') for _ in range(amount)]
ui.link('Star', '/icon/star?amount=5')
ui.link('Home', '/icon/home')
ui.link('Water', '/icon/water_drop?amount=3')

ui.run()
```

### 4.6 `ui.stepper`

1，如何使用其他控件模拟`ui.step`？

给控件增加`.props["name"]`和`.props["title"]`即可。

```python3
from nicegui import ui

with ui.stepper(
    value='First',
    on_value_change=lambda e: ui.notify(e.value),
    keep_alive=True
).classes('w-full') as stepper:
    with ui.card() as first:
        first.props.update(dict(name='First', title='First step', icon='home'))
        ui.label('Do it fisrt.')
        with ui.stepper_navigation(wrap=True):
            ui.button('Next', on_click=stepper.next)
    with ui.card() as second:
        second.props.update(dict(name='Second', title='Second step', icon='home'))
        ui.label('Do it second.')
        with ui.stepper_navigation(wrap=True):
            ui.button('Next', on_click=stepper.next)
            ui.button('Back', on_click=stepper.previous).props('flat')
    with ui.card() as last:
        last.props.update(dict(name='last', title='Last step', icon='home'))
        ui.label('Do it last.')
        with ui.stepper_navigation(wrap=True):
            ui.button('Done', on_click=lambda: ui.notify(
                'Done!', type='positive'))
            ui.button('Back', on_click=stepper.previous).props('flat')

ui.run(native=True)
```

2，将`ui.stepper`的控制按钮放置在外，如何识别第一步和最后一步？

遍历其中控件的`name`，或者直接指定中间变量存储第一步和最后一步的`name`，并绑定按钮的可见性或者使用`refreshable`装饰。

方法一：

```python3
from nicegui import ui

def navigation_bar(stepper:ui.stepper=None,on_finish=None,container=None):
    @ui.refreshable
    def navigation():
        with container or ui.element(),ui.row():
            step_name_list = [i.props['name'] for i in stepper]
            first_name = step_name_list[0]
            is_first = stepper.value == first_name
            is_not_first = not is_first
            last_name = step_name_list[-1]
            is_last = stepper.value == last_name
            is_not_last = not is_last
            next_btn = ui.button('Next', on_click=stepper.next)
            next_btn.bind_visibility_from(locals(),'is_not_last')
            last_btn = ui.button('Done')
            last_btn.bind_visibility_from(locals(),'is_last')
            if callable(on_finish):
                if len(on_finish.__code__.co_varnames) == 0:
                    last_btn.on_click(on_finish)
                else:
                    last_btn.on_click(lambda e:on_finish(e))
            else:
                last_btn.on_click(lambda: ui.notify('Done!', type='positive'))
            back_btn = ui.button('Back', on_click=stepper.previous).props('flat')
            back_btn.bind_visibility_from(locals(),'is_not_first')
    if stepper:
        navigation()
    stepper.on_value_change(navigation.refresh)

with ui.stepper(
    value='First',
    keep_alive=True
).classes('w-full') as stepper:
    with ui.step(name='First', title='First step', icon='home') as first:
        ui.label('Do it fisrt.')
    with ui.step(name='Second', title='Second step', icon='home') as second:
        ui.label('Do it second.')
    with ui.step(name='Last', title='Last step', icon='home') as last:
        ui.label('Do it last.')

with ui.card():
    navigation_bar(stepper)

ui.run(native=True)
```

方法二：

```python3
from nicegui import ui

with ui.stepper(
    value='First',
    keep_alive=True
).classes('w-full') as stepper:
    with ui.step(name='First', title='First step', icon='home') as first:
        ui.label('Do it fisrt.')
    with ui.step(name='Second', title='Second step', icon='home') as second:
        ui.label('Do it second.')
    with ui.step(name='Last', title='Last step', icon='home') as last:
        ui.label('Do it last.')

with ui.card(),ui.row():
    next_btn = ui.button('Next', on_click=stepper.next)
    next_btn.bind_visibility_from(stepper,'value',lambda x:x!=last.props['name'])
    last_btn = ui.button('Done')
    last_btn.bind_visibility_from(stepper,'value',lambda x:x==last.props['name'])
    last_btn.on_click(lambda: ui.notify('Done!', type='positive'))
    back_btn = ui.button('Back', on_click=stepper.previous).props('flat')
    back_btn.bind_visibility_from(stepper,'value',lambda x:x!=first.props['name'])

ui.run(native=True)
```

### 4.7 `ui.icon`

1，想用自定义的LOGO图片（SVG格式）当图标行不行？

可以，使用`'img:path/to/some_image.png'`这样的语法（适用于`ui.icon`控件或者其他支持`icon`参数的控件），比如`'img:https://cdn.quasar.dev/logo-v2/svg/logo.svg'`：

```python3
from nicegui import ui

ui.button(text='LOGO',icon='img:https://cdn.quasar.dev/logo-v2/svg/logo.svg')

ui.run(native=True)
```

### 4.8 `ui.carousel`

1，如何自定义轮播图的控制控件？

修改`'control'`slot（`add_slot('control')`），API参考[Quasar官网](https://quasar.dev/vue-components/carousel#qcarouselcontrol-api)。

```python3
from nicegui import ui

with ui.carousel(animated=True, arrows=True, navigation=True).props('height=180px').classes('bg-green-400') as carousel:
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/30/270/180').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/31/270/180').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/32/270/180').classes('w-[270px]')
    with carousel.add_slot('control') ,ui.element('q-carousel-control').props('position="top-right"'):
        ui.button('prev',on_click=carousel.previous)
        ui.button('next',on_click=carousel.next)

ui.run(native=True)
```

### 4.9 `ui.tree`

1，如何实现点击树形图的文字部分也能展开子节点？

可以在`on('click')`的响应操作中添加对当前节点是否展开的判断，然后展开、收起当前节点。

简洁版：

```python3
from nicegui import ui

# 调用JavaScript接口来展开、收起当前节点
def expand_node_js(e):
    if e.sender.props['selected'] in e.sender.props['expanded']:
        e.sender.run_method('setExpanded',e.sender.props['selected'],False)
    else:
        e.sender.run_method('setExpanded',e.sender.props['selected'],True)

ui.tree([
    {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
    {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
], label_key='id').classes('w-full').props('no-selection-unset').on('click',expand_node_js)


# 调用Python接口展开、收起当前节点
def expand_node_py(e):
    if e.sender.props['selected'] in e.sender.props['expanded']:
        e.sender.collapse([e.sender.props['selected']])
    else:
        e.sender.expand([e.sender.props['selected']])

ui.tree([
    {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
    {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
], label_key='id').classes('w-full').props('no-selection-unset').on('click',expand_node_py )

ui.run(native=True)
```

短小精悍防裁员版：

```python3
from nicegui import ui

ui.tree([
    {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
    {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
], label_key='id').classes('w-full').props('no-selection-unset').on('click',lambda e:e.sender.run_method('setExpanded',e.sender.props['selected'],False if e.sender.props['selected'] in e.sender.props['expanded'] else True ))

ui.tree([
    {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
    {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
], label_key='id').classes('w-full').props('no-selection-unset').on('click',lambda e:e.sender.collapse([e.sender.props['selected']]) if e.sender.props['selected'] in e.sender.props['expanded'] else e.sender.expand([e.sender.props['selected']]) )

ui.run(native=True)
```

### 4.10 `ui.video`

1，如何获取视频播放的进度？

目前NiceGUI没有实现视频控件的`currentTime`属性，但是可以使用JavaScript代码获取，示例如下：

```python3
from nicegui import ui

@ui.page('/')
async def index():
    v = ui.video(src='https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4',
             controls=True, autoplay=False, muted=False, loop=False)
    
    label = ui.label(f'当前播放进度为 {0} 秒。')
    async def get_current_time():
        time = await ui.run_javascript(f'getHtmlElement({v.id}).currentTime')
        label.set_text(f'当前播放进度为 {int(time)} 秒。')
    timer = ui.timer(0.1,get_current_time,immediate=False)
    v.on('play', lambda _:setattr(timer,'active',True))
    v.on('pause', lambda _:setattr(timer,'active',False))
    v.on('ended', lambda _:setattr(timer,'active',False))

ui.run(native=True)
```







NiceGUI 2.20.0 新增自定义程序内报错的响应页面

以下示例包含程序内报错和HTTP报错的自定义响应页面：

```python3
from nicegui import ui, app

# 自定义程序内报错的响应页面
@app.on_page_exception
def error_handler(exception: Exception) -> None:
    ui.label(f'触发的异常为 {exception}')

@ui.page('/')
def index():
    raise Exception('错误')

# 自定义HTTP报错的响应页面
from nicegui import ui, Client
from fastapi import Request

@app.exception_handler(404)
def exception_handler_404(request:Request, exception: Exception):
    from urllib.parse import urlparse
    with Client(ui.page('/404'),request=request) as client:
        ui.label(f'页面 {urlparse(str(request.url)).path[1:]} 不存在')
    return client.build_response(request, 404)

ui.run()
```





（以上为2025年更新的部分）

（以下为2026年更新的部分，2025年的将会存档（保存在nicegui_plus_2025.md）或者折叠起来）
