# MediaKit MCP Server

MediaKit MCP 是火山引擎 AI MediaKit 面向 AI 时代推出的标准能力插件。它基于 MCP（Model Context Protocol）协议，将云端专业的视频剪辑、音频处理、字幕处理、画质增强等原子能力封装为智能体可直观调用的工具。通过 MediaKit MCP，开发者可直接以自然语言驱动 AI 智能体完成复杂的云端媒体处理任务。

| 字段 | 取值                                                  |
| ---- | ----------------------------------------------------- |
| 版本 | v1.0.0                                                |
| 描述 | MediaKit MCP 智能媒体助手                             |
| 分类 | 视频云、音视频编辑、画质增强、图像处理                |
| 标签 | MCP、MediaKit、视频剪辑、音频处理、画质增强、图像处理 |

## 工具概览

MediaKit MCP 已开放的能力覆盖了从异步任务查询到深度媒体编辑、视频增强与理解、音频处理、图像处理的全流程。所有工具均支持通过“分组（Group）”或“工具名”进行动态加载，以优化智能体的推理效率。

<table>
  <thead>
    <tr>
      <th>分类</th>
      <th>分组名称</th>
      <th>工具</th>
      <th>说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>通用能力</b></td>
      <td>shared</td>
      <td>query_task</td>
      <td><b>任务查询</b>：查询异步任务状态和结果。提交异步任务后，使用该工具获取处理进度和最终产物。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/shared.py#L37">query_task</a>。
      </td>
    </tr>
    <tr>
      <td rowspan="17"><b>视频剪辑</b></td>
      <td rowspan="17">editing</td>
      <td>add_image_to_video</td>
      <td><b>视频加图片</b>：在视频画面上叠加图片，常用于添加图片水印。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L44">add_image_to_video</a>。
      </td>
    </tr>
    <tr>
      <td>add_subtitle_to_video</td>
      <td><b>视频加字幕</b>：将字幕文件或字幕文本压制到视频画面中。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L66">add_subtitle_to_video</a>。
      </td>
    </tr>
    <tr>
      <td>adjust_video_speed</td>
      <td><b>视频播放调速</b>：调整视频播放速度，实现快放或慢放效果。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L87">adjust_video_speed</a>。
      </td>
    </tr>
    <tr>
      <td>concat_audio</td>
      <td><b>音频拼接</b>：将多个音频片段拼接为一个新的音频文件。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L103">concat_audio</a>。
      </td>
    </tr>
    <tr>
      <td>concat_video</td>
      <td><b>视频拼接</b>：将多个视频片段拼接为一个新视频，支持添加转场效果。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L118">concat_video</a>。
      </td>
    </tr>
    <tr>
      <td>extract_audio</td>
      <td><b>音频提取</b>：从视频文件中分离音频流，并保存为独立音频文件。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L134">extract_audio</a>。
      </td>
    </tr>
    <tr>
      <td>flip_video</td>
      <td><b>画面翻转</b>：对视频画面进行水平或垂直镜像翻转。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L150">flip_video</a>。
      </td>
    </tr>
    <tr>
      <td>image_to_video</td>
      <td><b>图片合成视频</b>：将多张图片合成为动画视频，支持转场效果。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L167">image_to_video</a>。
      </td>
    </tr>
    <tr>
      <td>mux_audio_video</td>
      <td><b>音画合成</b>：将视频轨道与音频轨道合成一个视频文件。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L183">mux_audio_video</a>。
      </td>
    </tr>
    <tr>
      <td>trim_audio</td>
      <td><b>音频裁剪</b>：按起止时间点裁剪音频，生成新的音频片段。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L203">trim_audio</a>。
      </td>
    </tr>
    <tr>
      <td>trim_video</td>
      <td><b>视频裁剪</b>：按起止时间点裁剪视频，生成新的视频片段。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L220">trim_video</a>。
      </td>
    </tr>
    <tr>
      <td>adjust_audio_speed</td>
      <td><b>音频播放调速</b>：调整音频播放速度，实现快放或慢放效果。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L237">adjust_audio_speed</a>。
      </td>
    </tr>
    <tr>
      <td>adjust_video_volume</td>
      <td><b>视频音量调整</b>：调整视频音量大小，支持静音。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L253">adjust_video_volume</a>。
      </td>
    </tr>
    <tr>
      <td>apply_video_filter</td>
      <td><b>视频滤镜</b>：为视频添加指定的预设滤镜效果。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L269">apply_video_filter</a>。
      </td>
    </tr>
    <tr>
      <td>fade_audio</td>
      <td><b>音频淡入淡出</b>：对输入音频实现淡入淡出效果。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L285">fade_audio</a>。
      </td>
    </tr>
    <tr>
      <td>fade_video_audio</td>
      <td><b>视频声轨淡入淡出</b>：对输入视频的声轨实现淡入淡出效果。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L302">fade_video_audio</a>。
      </td>
    </tr>
    <tr>
      <td>mix_audio</td>
      <td><b>音频混音</b>：将多个音频文件（背景音乐、音效、人声等）混音生成一个新的音频文件。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L320">mix_audio</a>。
      </td>
    </tr>
    <tr>
      <td rowspan="14"><b>视频增强与理解</b></td>
      <td rowspan="14">video</td>
      <td>analyze_video_highlights</td>
      <td><b>视频高光分析</b>：智能捕捉视频情绪波峰与关键动作，输出时间戳、高光打分、OCR 文本和画面描述等元数据。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L38">analyze_video_highlights</a>。
      </td>
    </tr>
    <tr>
      <td>analyze_video_storyline</td>
      <td><b>视频剧情线分析</b>：智能解析影视剧内容，生成由时序剧情片段与聚合高光组成的结构化剧情线。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L58">analyze_video_storyline</a>。
      </td>
    </tr>
    <tr>
      <td>asr_subtitles</td>
      <td><b>语音识别字幕</b>：对输入视频或音频进行语音识别，输出带时间戳的字幕片段。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L77">asr_subtitles</a>。
      </td>
    </tr>
    <tr>
      <td>enhance_video</td>
      <td><b>画质增强</b>：面向 AIGC、UGC、短剧、教育、游戏、老片修复等场景提升视频画质。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L99">enhance_video</a>。
      </td>
    </tr>
    <tr>
      <td>enhance_video_generative</td>
      <td><b>生成式视频修复</b>：基于扩散大模型的生成式视频修复技术，补全细节、生成高保真视频内容。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L122">enhance_video_generative</a>。
      </td>
    </tr>
    <tr>
      <td>erase_video_subtitle</td>
      <td><b>视频字幕擦除</b>：智能检测并擦除视频画面中已有的硬字幕，保留原始背景。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L140">erase_video_subtitle</a>。
      </td>
    </tr>
    <tr>
      <td>erase_video_subtitle_pro</td>
      <td><b>视频字幕擦除（Pro）</b>：针对视频中的字幕或文本进行高质量无痕擦除。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L156">erase_video_subtitle_pro</a>。
      </td>
    </tr>
    <tr>
      <td>generate_highlights_microdrama</td>
      <td><b>短剧高光智剪</b>：深度理解短剧角色、剧情与故事线，自动提取高光片段并混剪成投流视频。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L175">generate_highlights_microdrama</a>。
      </td>
    </tr>
    <tr>
      <td>generate_highlights_minigame</td>
      <td><b>小游戏高光智剪</b>：识别小游戏录屏中的核心玩法与高光事件，快速生成买量视频素材。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L199">generate_highlights_minigame</a>。
      </td>
    </tr>
    <tr>
      <td>matte_greenscreen_video</td>
      <td><b>绿幕抠像</b>：对绿幕或纯色背景视频抠图，移除背景生成背景透明的视频。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L219">matte_greenscreen_video</a>。
      </td>
    </tr>
    <tr>
      <td>matte_portrait_video</td>
      <td><b>人像抠像</b>：自动识别人物主体并移除背景，生成背景透明的视频。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L237">matte_portrait_video</a>。
      </td>
    </tr>
    <tr>
      <td>probe_video_metadata</td>
      <td><b>视频元信息探测</b>：探测视频 URL，输出标准化媒资元信息（容器层、视频流层、音频流层）。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L255">probe_video_metadata</a>。
      </td>
    </tr>
    <tr>
      <td>segment_scenes</td>
      <td><b>场景切分</b>：依据视频转场与画面变化自动切分场景，输出切片时间轴和（可选）切片文件。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L272">segment_scenes</a>。
      </td>
    </tr>
    <tr>
      <td>video_ocr</td>
      <td><b>视频 OCR</b>：识别视频画面中的字幕/文字内容，输出带时间戳的字幕片段。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L293">video_ocr</a>。
      </td>
    </tr>
    <tr>
      <td rowspan="2"><b>音频处理</b></td>
      <td rowspan="2">audio</td>
      <td>separate_voice</td>
      <td><b>人声分离</b>：将音频中的人声与背景音精准分离，输出为两个独立音轨。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/audio.py#L32">separate_voice</a>。
      </td>
    </tr>
    <tr>
      <td>probe_audio_metadata</td>
      <td><b>音频元信息探测</b>：获取音频详细元信息，输出容器层信息与音频流元信息。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/audio.py#L51">probe_audio_metadata</a>。
      </td>
    </tr>
    <tr>
      <td rowspan="5"><b>图像处理</b></td>
      <td rowspan="5">image</td>
      <td>image_ocr</td>
      <td><b>图片 OCR</b>：识别图片中的通用印刷体文字，返回可编辑文本、文字框坐标和置信度。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/image.py#L32">image_ocr</a>。
      </td>
    </tr>
    <tr>
      <td>erase_image</td>
      <td><b>图像擦除</b>：自动检测并擦除图片中的图标、文字或指定区域，并对擦除区域进行背景智能填充。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/image.py#L48">erase_image</a>。
      </td>
    </tr>
    <tr>
      <td>remove_image_background</td>
      <td><b>图像背景移除</b>：自动识别并保留图像主体，移除背景生成背景透明的图片，支持通用、人像、商品场景。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/image.py#L67">remove_image_background</a>。
      </td>
    </tr>
    <tr>
      <td>enhance_image</td>
      <td><b>图像画质增强</b>：基于图像内容理解智能决策，提升图片分辨率、清晰度与色彩表现。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/image.py#L89">enhance_image</a>。
      </td>
    </tr>
    <tr>
      <td>evaluate_image_quality</td>
      <td><b>图像质量评估</b>：对图片进行主客观画质与美学评分，支持标准版多维评分与专业版大模型评分。详细输入和输出参数请见
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/image.py#L108">evaluate_image_quality</a>。
      </td>
    </tr>
  </tbody>
</table>

# 快速体验：在 Trae 中配置

Trae 是一款 AI 原生 IDE，提供了强大的智能体协作能力。通过接入 MediaKit MCP，您可以直接在 Trae 对话框中以自然语言方式调用云端媒体处理能力，快速完成视频剪辑、字幕处理、音频处理和画质增强等任务。

## 前提条件

- 已准备可用的 MediaKit API Key。
- 已安装 [Trae 客户端](https://www.trae.com.cn/)。
- 使用本地模式或云端自部署模式时，需确保本地开发环境已安装 `uvx`。可通过 `uvx --version` 检查；若提示未安装，请参考 [uv 官方安装文档](https://docs.astral.sh/uv/getting-started/installation/)。

## 操作步骤

### 步骤 1：选择接入模式

根据您的使用场景，选择以下两种接入模式之一：

| 模式                       | 适用场景                           | 接入方式                                                                  |
| -------------------------- | ---------------------------------- | ------------------------------------------------------------------------- |
| **本地模式（JSON Local）** | 个人调试、快速试用、无需自建服务。 | 通过 `uvx` 直接从 `mcp-server` 仓库子目录拉起 MediaKit MCP。              |
| **云端模式（JSON URL）**   | 团队共享、长期稳定使用、统一运维。 | 先自行部署 MediaKit MCP Server，再使用部署后的 Streamable HTTP 地址接入。 |

### 步骤 2：添加 MCP 配置

1. 打开 Trae，单击窗口右上角“设置”按钮。
2. 在 MCP 页签下，单击**添加** > **手动添加**。
3. 根据您在步骤 1 中选择的模式，复制对应 JSON 配置，并按下方说明替换参数。

#### 本地模式（JSON Local）

复制以下 JSON 并根据下方文字说明进行替换。Trae 会通过 `uvx` 自动拉取远程代码并在本地运行。

```json
{
  "mcpServers": {
    "mediakit_mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/volcengine/mcp-server.git#subdirectory=server/mcp_server_mediakit",
        "mcp-server-mediakit"
      ],
      "env": {
        "MEDIAKIT_API_KEY": "your-api-key",
        "MCP_DOMAINS": "editing,video,audio,image"
      }
    }
  }
}
```

**字段替换说明：**

- `mediakit_mcp`：MCP 服务名称，您可以根据需要自定义。
- `MEDIAKIT_API_KEY`：请替换为您的 MediaKit API Key。
- `MCP_DOMAINS`：按分组加载工具，例如 `editing,video,audio,image`。如需按工具名精确加载，可改用 `MCP_TOOLS`。

如需按工具名加载，可参考以下写法：

```json
{
  "mcpServers": {
    "mediakit_mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/volcengine/mcp-server.git#subdirectory=server/mcp_server_mediakit",
        "mcp-server-mediakit"
      ],
      "env": {
        "MEDIAKIT_API_KEY": "your-api-key",
        "MCP_TOOLS": "trim_video,query_task"
      }
    }
  }
}
```

#### 云端模式（JSON URL）

云端模式不提供现成的部署链接。使用该模式前，您需要先自行部署 MediaKit MCP Server，并确保服务可通过 Streamable HTTP 方式访问。部署完成后，请记录可访问的服务地址，例如 `https://your-domain/mcp`，然后在 Trae 中按如下方式接入。

一种简单的启动示例如下：

```bash
export MEDIAKIT_API_KEY="your-api-key"
export MCP_SERVER_HOST="0.0.0.0"
export MCP_SERVER_PORT="8000"
export STREAMABLE_HTTP_PATH="/mcp"

uvx --from "git+https://github.com/volcengine/mcp-server.git#subdirectory=server/mcp_server_mediakit"   mcp-server-mediakit   --transport streamable-http
```

完成部署后，复制以下 JSON 并根据下方文字说明进行替换：

```json
{
  "mcpServers": {
    "mediakit_mcp": {
      "url": "https://your-domain/mcp",
      "headers": {
        "x-amk-api-key": "your-api-key",
        "x-mcp-domains": "editing,video,audio,image"
      }
    }
  }
}
```

**字段替换说明：**

- `mediakit_mcp`：MCP 服务名称，您可以根据需要自定义。
- `url`：请替换为您自行部署后的 MediaKit MCP Streamable HTTP 地址，例如 `https://your-domain/mcp`。
- `x-amk-api-key`：请替换为您的 MediaKit API Key。
- `x-mcp-domains`：按分组加载工具，例如 `editing,video,audio,image`。如需按工具名精确加载，可改用 `x-mcp-tools`。

如需按工具名加载，可参考以下写法：

```json
{
  "mcpServers": {
    "mediakit_mcp": {
      "url": "https://your-domain/mcp",
      "headers": {
        "x-amk-api-key": "your-api-key",
        "x-mcp-tools": "trim_video,query_task"
      }
    }
  }
}
```

4. 确认该 MCP 的状态显示为绿色激活。

### 步骤 3：启用智能体对话

在 Trae 主界面打开对话面板，将底部智能体切换为支持 MCP 的模式。随后，您可以直接下达自然语言指令，例如：

- 帮我把这个视频裁剪为前 10 秒，并输出一个新视频。
- 帮我给这个视频添加中文字幕，字号设置为 28。
- 帮我擦除视频底部字幕，并对处理后的视频做画质增强。
- 帮我把两段音频拼接起来，如果任务是异步的，请继续帮我查询最终结果。

## 使用说明

- 同步任务会直接返回结果。
- 异步任务会返回 `task_id`，需要调用 `query_task` 查询任务状态和结果。
- 默认开启幂等：相同账户和核心请求参数在 2 天内重复提交时，服务会直接返回首次任务结果，不会重复创建任务。
- 如需主动控制幂等，可传 `client_token`；请求重试时复用同一值，强制重新执行时必须传新的唯一值。
- `client_token` 由客户端生成，长度不超过 64 个字符。

## MCP 配置参数说明

下表列出 MediaKit MCP 的核心配置项，区分云端模式与本地模式。请根据您的实际接入场景选择对应字段。

<table>
  <thead>
    <tr>
      <th>云端 Header 字段</th>
      <th>本地环境变量名</th>
      <th>示例</th>
      <th>说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>x-amk-api-key</td>
      <td>MEDIAKIT_API_KEY</td>
      <td>your-api-key</td>
      <td>MediaKit API Key，用于请求鉴权。</td>
    </tr>
    <tr>
      <td>x-mcp-domains</td>
      <td>MCP_DOMAINS</td>
      <td>editing,video,audio,image</td>
      <td>按工具分组加载，多个分组用英文逗号分隔。</td>
    </tr>
    <tr>
      <td>x-mcp-tools</td>
      <td>MCP_TOOLS</td>
      <td>trim_video,query_task</td>
      <td>按工具名加载，多个工具名用英文逗号分隔。</td>
    </tr>
  </tbody>
</table>

云端自部署时，还可按需使用以下服务启动参数：

| 环境变量               | 默认值    | 说明                   |
| ---------------------- | --------- | ---------------------- |
| `MCP_SERVER_HOST`      | `0.0.0.0` | MCP 服务监听地址。     |
| `MCP_SERVER_PORT`      | `8000`    | MCP 服务监听端口。     |
| `STREAMABLE_HTTP_PATH` | `/mcp`    | Streamable HTTP 路径。 |

## 许可证

本项目基于 **MIT 许可证** 开源。

该软件运行时会调用 MediaKit 云端 API，使用这些 API 需要遵守如下协议：

- `https://www.volcengine.com/docs/6448/79646?lang=zh`
- `https://www.volcengine.com/docs/6448/104992?lang=zh`
- `https://www.volcengine.com/docs/6448/79648?lang=zh`
