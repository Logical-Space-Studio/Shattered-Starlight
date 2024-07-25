### 目前的设计

本仓库属于制作组的 organization 名下。

本 `README.md` 现在用来记录工作情况，以及一些具体的工作任务，一些需要商讨的设计方案 等。

#### 仓库结构

计划本仓库除了 `README.md` 以外，仅存放一个以游戏英文名命名的目录。（命名：用下划线代替空格）

该游戏英文名命名的目录为游戏项目的根目录。

计划项目完成时，本 `README.md` 将删除，重写为游戏的 `README.md`。

# 偶像幻灭

偶像幻灭视觉小说企划

英文名（暂定）：Shattered Starlight

## 制作组

制作组：[Logical Space Studio](https://github.com/Logical-Space-Studio)

人员分组（14）：

- 监督 1
- 系列构成 1
- 顾问 2
- 角色原案 1
- 脚本 4
- 音声 1
- 美工 1
- CG 画师 1
- 程序 3

## 制作

引擎：[Ren’Py](https://doc.renpy.cn/zh-CN/)



---
---

# 程序设计

- [ ] 建立工程文件，开始正式编写游戏代码
- [ ] 与美术协商分辨率等问题
- [ ] GUI 设计
- [ ] 打包发布

# 程序以外

- [ ] 游戏英文名
- [ ] 画质、分辨率等设定
- [ ] LICENSE

# 其他

比如关于 GitHub organization 的一些信息设置问题

- [x] 工作室英文名
- [ ] 工作室 Logo
- [ ] 工作室描述

------

------

# Note

以下内容需要与其他组商讨决定。

*重要性*指该项的紧急程度。

### 确定模式

- [ ] ADV 模式
- [ ] NVL 模式

#### 介绍

视觉小说中总共有两种表现形式。

ADV 模式下使用界面底部的一个窗口显示对话和旁白，每次显示一行， 更接近台本 ；
NVL 模式下使用几乎占据整个界面的一个窗口，每次能在界面上显示多行对话和旁白，更接近小说 。 

此处仅供参考，建议再另外自行了解二者区别。

#### 重要性   非常高

直接关系到程序的基本结构，正式开始编写后几乎无法修改。

## 资源文件

请美术、音声老师一定留意。

### 分辨率

（待补充）

### 图片

#### 用途

- 角色头像
- 角色立绘
  - 各种表情等
- 背景
  - 主界面
  - 启动界面
  - 加载界面
  - 场景
- 图标
- 某些按键图标
- 鼠标光标

（未完待续...）

#### 支持的格式

- AVIF
- Webp
- Png
- Jpg
- SVG（矢量图）

### 音频

#### 用途

- 音乐
- 音效
- 语音

#### 支持的格式

- Opus
- Ogg Vorbis
- MP3
- MP2
- FLAC
- WAV（未压缩的有符号 16bit 型 PCM 编码格式）

### 视频

#### 用途

举个例子，启动时播放，或者完线后播放 ed。

#### 支持的格式

- AV1
- VP9
- VP8
- Theora
- MPEG-4 part 2（包括 Xvid 和 DivX）
- MPEG-2
- MPEG-1

注意某些格式可能需要专利许可证书。没有把握的情况下，我们推荐使用 AV1、VP9、VP8 或者 Theora、Opus、Vorbis，以及 WebM、Matroska 或者 Ogg。 

### 字体

支持 TrueType / OpenType 字体和字体集，以及基于图形的字体。 

字体资源从网上下载。

## 可以实现的一些功能

### 文本输入

#### 介绍

允许用户输入文本，具体来说可以用来实现很多功能，比如玩家角色起名。

#### 风险

工作量很少。

#### 重要性   高

其实要看具体想实现什么功能。

比如如果打算让玩家给自己起名，就需要一开始就决定，因为会影响到脚本和程序设计。

### 气泡式台词

- [ ] 使用
- [ ] 不使用

#### 介绍

将对话以气泡式台词形式显示。气泡式台词可以使用交互式设计，指定在界面上显示的位置。
该功能可以是 ADV 模式游戏下文本框或 NVL 模式下全屏对话框之外，一种新的对话表现形式。 

#### 风险

估计工作量不少。

#### 重要性   高

要和正文一起做。

### 画廊

- [ ] 使用
- [ ] 不使用

#### 介绍

画廊是一个专门的界面，允许用户解锁并查看图片。该界面有一个或多个相关联的按钮，每个按钮都有对应的图片。按钮和图片的状态取决于是否已被解锁。 

可以播放幻灯片。

#### 风险

估计工作量少。

#### 重要性   较低

考虑到工作量，不能拖到最后才开始做。

### 音乐空间

- [ ] 使用
- [ ] 不使用

#### 介绍

与画廊类似，但是音乐。

音乐空间是允许用于选择和播放游戏内音轨的界面。这些音轨可能在用户刚开始玩时是锁定的，随着游戏进度的推进逐步解锁。 

#### 风险

估计工作量少。

#### 重要性   较低

考虑到工作量，不能拖到最后才开始做。

### 回放

- [ ] 使用
- [ ] 不使用

#### 介绍

从主菜单或游戏菜单回放某个场景的。这可以用来创建一个“场景画廊”或者“回忆画廊”，允许用户重复重要的场景。

该功能不能由用户指定要回放的场景。

#### 风险

估计工作量很少。

#### 重要性   低

其他的都做完了，最后阶段来写也可以。

### 成就系统

- [ ] 使用
- [ ] 不使用

#### 介绍

可以在一定阶段向玩家显示完成进度。

额外功能：如果 Steam 平台支持可用并且被启用，成就信息会自动与 Steam 同步。 

#### 风险

工作量跟成就数量线性正相关。

#### 重要性   较低

其他的都做完了，最后阶段来写也可以。

### Live2D Cubism

- [ ] 使用
- [ ] 不使用

#### 介绍

懂的都懂

#### 风险

- 大大增加程序和美术的工作量
- 需要额外安装相关插件（库）
  - x86_64 的安卓平台不支持 Live2D，因为对应平台缺乏某个动态连接库。这也表示在安卓模拟器和 ChromeOS 上运行可能会有问题。
  - Web 平台也不支持 Live2D。
  - 在 iOS 平台安装 Live2D 时，需要手工将静态库复制到自己的 iOS 项目中。
-  如果该商业项目年收入达到了某个下限，将需要购买一个 Live2D 使用许可证。 

#### 重要性   高

因为工作量太高。

### Splash Screen

- [ ] 使用
- [ ] 不使用

#### 介绍

游戏首次运行，在主菜单出现前，的内容。

比如可以放一段视频，也可以推进一部分游戏内容。

#### 风险

工作量很小。

#### 重要性   高

视具体内容而定，主要是可能影响到剧本安排。





待续...