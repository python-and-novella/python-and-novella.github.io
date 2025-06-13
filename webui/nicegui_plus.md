# NiceGUI拾遗

## 0 为什么要写这个系列

《NiceGUI的中文入门教程》完成后，NiceGUI一直处于不断更新中，同时《NiceGUI的中文入门教程》也不是完美的，需要不断补充、修改内容，这也导致该教程后续不断增补内容，影响教程的完整性，也不好写标题。为了和《NiceGUI的中文入门教程》的系统性教程做出区分，《NiceGUI拾遗》应运而生。《NiceGUI拾遗》采用线性编写原则，按照时间顺序编写《NiceGUI的中文入门教程》中的遗漏内容、NiceGUI的更新内容，采取想起哪些写哪些的原则，但是标题中会尽量简短地与内容关联，避免出现《NiceGUI的中文入门教程》中为了确保教程完整性不得不沿用原标题的情况。

此外，《NiceGUI的中文入门教程》中的具体示例也会放在这里继续更新，并在标题中体现示例的主要用途。

简而言之，本系列教程可以看作是《NiceGUI的中文入门教程》的续作，但是叙述上不再沿用系统性架构，而是采用类似于敏捷开发式叙述方式，随时补充新内容且不会在原始位置修改已发布的内容（但可能单开一节用于修订之前的内容）。

## 1 使用环境变量配置NiceGUI程序（更新中）

https://nicegui.io/documentation/section_configuration_deployment#environment_variables





You can set the following environment variables to configure NiceGUI:

- `MATPLOTLIB` (default: true) can be set to `false` to avoid the potentially costly import of Matplotlib. This will make `ui.pyplot` and `ui.line_plot` unavailable.
- `NICEGUI_STORAGE_PATH` (default: local ".nicegui") can be set to change the location of the storage files.
- `MARKDOWN_CONTENT_CACHE_SIZE` (default: 1000): The maximum number of Markdown content snippets that are cached in memory.
- `RST_CONTENT_CACHE_SIZE` (default: 1000): The maximum number of ReStructuredText content snippets that are cached in memory.
- `NICEGUI_REDIS_URL` (default: None, means local file storage): The URL of the Redis server to use for shared persistent storage.
- `NICEGUI_REDIS_KEY_PREFIX` (default: "nicegui:"): The prefix for Redis keys.