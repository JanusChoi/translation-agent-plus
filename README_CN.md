# 翻译Agent自动化

> 本项目基于吴恩达 [translation-agent](https://github.com/andrewyng/translation-agent) ，添加了以下功能。（目前是自用分享状态，后续视情况会持续更新。）
> 1. 增加 example/pdf_trans.py 用于整本pdf翻译
> 2. 增加 DeepSeek & Ollama 调用，详见 util.py 中的函数： `get_completion_openai`,`get_completion_deeps`,`get_completion_ollama`

个人的基本诉求就是当我有一些想要翻译过来发布的文章或书籍时，希望有一个强大的机器翻译版本，尽可能降低人工审校的时间成本。

****

## 个人探索记录

「AI小工具」翻译Agent体验

快速测了一下吴恩达前段时间做的翻译Agent：GitHub - andrewyng/translation-agent​
效果还是不行

案例如下：

原文：
My favorite and inevitable application of QPUs is the simulation of physics. Physics simulations are ubiquitous. Gamers will know this well. When you think of video games, you should think of virtual worlds. These worlds have physical laws, and the motion of the objects and characters in the world needs to be calculated—this is a simulation. Physics must be simulated when designing aircraft, bridges, and any other engineered system. Physics is simulated in science, too—entire galaxies have been simulated to understand their formation. But quantum physics has resisted simulation because CPUs are really bad at it.
------------
程序：
我最喜欢而且不可或缺的量子处理器应用是物理模拟。物理模拟无处不在，游戏玩家对此应该很熟悉。想到视频游戏，就应该想到虚拟世界。这些世界有自己的物理法则，世界中的物体和角色的运动需要被计算——这就是模拟。设计飞机、桥梁或其他工程系统时，都必须进行物理模拟。物理也在科学中被模拟——科学家们已模拟整个星系，以更好地理解它们的形成过程。但是量子物理一直难以被模拟，因为传统CPU在处理量子物理方面表现非常糟糕。
------------
我的（人类）翻译：
我偏向认为QPU必然会用于物理模拟——这是广泛存在的。如果你是游戏玩家就会明白，即便身处游戏中，你依然会想象那是一个虚拟的真实世界。那里有各种物理法则，需要计算各种对象和角色的运动——即模拟。在设计飞机、桥梁等工程系统时都需要进行物理模拟。科学领域也要模拟——为了更好的理解，甚至可以模拟出整个星系。但是量子物理一直难以被模拟因为CPUs的表现实在太糟糕了。
------------
在最新版Claude上用了之前宝玉分享的意译prompt效果也不错：

QPU 最令人兴奋且不可或缺的应用是物理模拟。物理模拟在我们的生活中无处不在。游戏玩家对此再熟悉不过了。想想看，电子游戏就是在创造虚拟世界。这些世界都有自己的物理法则，游戏中物体和角色的运动都需要通过计算来模拟。不仅如此，在设计飞机、桥梁和其他工程系统时，物理模拟也是必不可少的。科学研究中同样需要物理模拟，科学家们甚至模拟了整个星系的形成过程。然而，量子物理的模拟一直是个难题，因为传统的 CPU 在处理这类问题时表现得很糟糕。
------------

用FastGPT构建的这个翻译Agent的效果目前是测试到最好的一个，感觉可以投入实际翻译工作中去使用了。
参考：https://mp.weixin.qq.com/s/h_Oqlkd4b6vqAILUrERrJw

但效果好的本质是由Opus的能力带来的，若使用本项目的prompt而换用Opus，效果也不错，而且工作流中的第二个步骤仅仅是为了提取最后一段Markdown而浪费一次API调用完全没必要。

目前本地调用测试了LLama3和Qwen:14b，效果都非常差劲，在长文本情况下还会漏译，将整个段落整漏了。

因此结论是基础模型决定翻译效果。
