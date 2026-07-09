# MediaKit MCP Server

MediaKit MCP Server is a standard AI capability plugin for Volcano Engine AI MediaKit. It is built on the MCP (Model Context Protocol) protocol and exposes cloud media capabilities such as video editing, audio processing, subtitle processing, and video enhancement as tools that can be called by AI agents. With MediaKit MCP, developers can use natural language to drive intelligent media production workflows.

| Field       | Value                                                                               |
| ----------- | ----------------------------------------------------------------------------------- |
| Version     | v1.0.0                                                                              |
| Description | MediaKit MCP intelligent media assistant                                            |
| Categories  | Media cloud, audio/video editing, video enhancement, image processing               |
| Tags        | MCP, MediaKit, video editing, audio processing, video enhancement, image processing |

## Tool Overview

MediaKit MCP provides tools that cover the full workflow from asynchronous task query to deep media editing, video enhancement and understanding, audio processing, and image processing. All tools support dynamic loading by group or by tool name to optimize agent reasoning efficiency.

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Group</th>
      <th>Tool</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Shared</b></td>
      <td>shared</td>
      <td>query_task</td>
      <td><b>Task query</b>: Query asynchronous task status and results after submitting an asynchronous task. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/shared.py#L37">query_task</a>.
      </td>
    </tr>
    <tr>
      <td rowspan="17"><b>Video editing</b></td>
      <td rowspan="17">editing</td>
      <td>add_image_to_video</td>
      <td><b>Add image to video</b>: Overlay an image on a video, commonly used for image watermarks. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L44">add_image_to_video</a>.
      </td>
    </tr>
    <tr>
      <td>add_subtitle_to_video</td>
      <td><b>Add subtitles to video</b>: Burn subtitle files or subtitle text into a video. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L66">add_subtitle_to_video</a>.
      </td>
    </tr>
    <tr>
      <td>adjust_video_speed</td>
      <td><b>Adjust video speed</b>: Change video playback speed for fast or slow motion effects. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L87">adjust_video_speed</a>.
      </td>
    </tr>
    <tr>
      <td>concat_audio</td>
      <td><b>Concatenate audio</b>: Merge multiple audio clips into a single audio file. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L103">concat_audio</a>.
      </td>
    </tr>
    <tr>
      <td>concat_video</td>
      <td><b>Concatenate video</b>: Merge multiple video clips into a new video with optional transitions. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L118">concat_video</a>.
      </td>
    </tr>
    <tr>
      <td>extract_audio</td>
      <td><b>Extract audio</b>: Separate the audio stream from a video and save it as an independent audio file. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L134">extract_audio</a>.
      </td>
    </tr>
    <tr>
      <td>flip_video</td>
      <td><b>Flip video</b>: Flip a video horizontally or vertically. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L150">flip_video</a>.
      </td>
    </tr>
    <tr>
      <td>image_to_video</td>
      <td><b>Image to video</b>: Create an animated video from multiple images with optional transitions. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L167">image_to_video</a>.
      </td>
    </tr>
    <tr>
      <td>mux_audio_video</td>
      <td><b>Mux audio and video</b>: Combine a video track and an audio track into one video file. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L183">mux_audio_video</a>.
      </td>
    </tr>
    <tr>
      <td>trim_audio</td>
      <td><b>Trim audio</b>: Trim an audio file by start and end time. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L203">trim_audio</a>.
      </td>
    </tr>
    <tr>
      <td>trim_video</td>
      <td><b>Trim video</b>: Trim a video by start and end time. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L220">trim_video</a>.
      </td>
    </tr>
    <tr>
      <td>adjust_audio_speed</td>
      <td><b>Adjust audio speed</b>: Change audio playback speed for fast or slow effects. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L237">adjust_audio_speed</a>.
      </td>
    </tr>
    <tr>
      <td>adjust_video_volume</td>
      <td><b>Adjust video volume</b>: Change video volume, including muting. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L253">adjust_video_volume</a>.
      </td>
    </tr>
    <tr>
      <td>apply_video_filter</td>
      <td><b>Apply video filter</b>: Add a preset filter style to a video. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L269">apply_video_filter</a>.
      </td>
    </tr>
    <tr>
      <td>fade_audio</td>
      <td><b>Fade audio</b>: Apply fade-in and fade-out effects to an audio file. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L285">fade_audio</a>.
      </td>
    </tr>
    <tr>
      <td>fade_video_audio</td>
      <td><b>Fade video audio</b>: Apply fade-in and fade-out effects to a video's audio track. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L302">fade_video_audio</a>.
      </td>
    </tr>
    <tr>
      <td>mix_audio</td>
      <td><b>Mix audio</b>: Mix multiple audio files (background music, sound effects, vocals) into one audio file. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/editing.py#L320">mix_audio</a>.
      </td>
    </tr>
    <tr>
      <td rowspan="14"><b>Video enhancement &amp; understanding</b></td>
      <td rowspan="14">video</td>
      <td>analyze_video_highlights</td>
      <td><b>Analyze video highlights</b>: Detect emotional peaks and key actions and output highlight metadata (timestamps, scores, OCR text, scene descriptions). For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L38">analyze_video_highlights</a>.
      </td>
    </tr>
    <tr>
      <td>analyze_video_storyline</td>
      <td><b>Analyze video storyline</b>: Parse film/TV content into a structured storyline of chronological clips and aggregated highlights. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L58">analyze_video_storyline</a>.
      </td>
    </tr>
    <tr>
      <td>asr_subtitles</td>
      <td><b>Speech to subtitles</b>: Run speech recognition on a video or audio and output timestamped subtitle segments. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L77">asr_subtitles</a>.
      </td>
    </tr>
    <tr>
      <td>enhance_video</td>
      <td><b>Enhance video</b>: Improve video quality for AIGC, UGC, short drama, education, gaming, and old film restoration scenarios. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L99">enhance_video</a>.
      </td>
    </tr>
    <tr>
      <td>enhance_video_generative</td>
      <td><b>Generative video restoration</b>: Diffusion-model based restoration that reconstructs details and generates high-fidelity content. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L122">enhance_video_generative</a>.
      </td>
    </tr>
    <tr>
      <td>erase_video_subtitle</td>
      <td><b>Erase video subtitles</b>: Detect and erase existing hard subtitles while preserving the original background. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L140">erase_video_subtitle</a>.
      </td>
    </tr>
    <tr>
      <td>erase_video_subtitle_pro</td>
      <td><b>Erase video subtitles (pro)</b>: Remove subtitles or text from a video with high-quality restoration. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L156">erase_video_subtitle_pro</a>.
      </td>
    </tr>
    <tr>
      <td>generate_highlights_microdrama</td>
      <td><b>Microdrama highlights</b>: Extract highlights from microdramas and produce promotional cut videos. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L175">generate_highlights_microdrama</a>.
      </td>
    </tr>
    <tr>
      <td>generate_highlights_minigame</td>
      <td><b>Minigame highlights</b>: Identify core gameplay and highlight events in minigame recordings and generate marketing video assets. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L199">generate_highlights_minigame</a>.
      </td>
    </tr>
    <tr>
      <td>matte_greenscreen_video</td>
      <td><b>Green screen matting</b>: Matte videos with a green screen or solid-color background to produce a transparent-background video. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L219">matte_greenscreen_video</a>.
      </td>
    </tr>
    <tr>
      <td>matte_portrait_video</td>
      <td><b>Portrait matting</b>: Identify the human subject and remove the background to produce a transparent-background video. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L237">matte_portrait_video</a>.
      </td>
    </tr>
    <tr>
      <td>probe_video_metadata</td>
      <td><b>Probe video metadata</b>: Probe a video URL and output standardized media metadata (container, video stream, audio stream). For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L255">probe_video_metadata</a>.
      </td>
    </tr>
    <tr>
      <td>segment_scenes</td>
      <td><b>Segment scenes</b>: Automatically split a video into scenes based on transitions and visual changes. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L272">segment_scenes</a>.
      </td>
    </tr>
    <tr>
      <td>video_ocr</td>
      <td><b>Video OCR</b>: Recognize subtitles/text in video frames and output timestamped subtitle segments. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/video.py#L293">video_ocr</a>.
      </td>
    </tr>
    <tr>
      <td rowspan="2"><b>Audio processing</b></td>
      <td rowspan="2">audio</td>
      <td>separate_voice</td>
      <td><b>Separate voice</b>: Separate vocals and background sound into two independent tracks. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/audio.py#L32">separate_voice</a>.
      </td>
    </tr>
    <tr>
      <td>probe_audio_metadata</td>
      <td><b>Probe audio metadata</b>: Retrieve detailed audio metadata (container and audio stream). For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/audio.py#L51">probe_audio_metadata</a>.
      </td>
    </tr>
    <tr>
      <td rowspan="5"><b>Image processing</b></td>
      <td rowspan="5">image</td>
      <td>image_ocr</td>
      <td><b>Image OCR</b>: Recognize general printed text and return editable text, bounding boxes, and confidence. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/image.py#L32">image_ocr</a>.
      </td>
    </tr>
    <tr>
      <td>erase_image</td>
      <td><b>Erase image</b>: Detect and erase icons, text, or specified regions with intelligent background inpainting. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/image.py#L48">erase_image</a>.
      </td>
    </tr>
    <tr>
      <td>remove_image_background</td>
      <td><b>Remove image background</b>: Keep the subject and remove the background to produce a transparent-background image. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/image.py#L67">remove_image_background</a>.
      </td>
    </tr>
    <tr>
      <td>enhance_image</td>
      <td><b>Enhance image</b>: Improve image resolution, sharpness, and color based on content understanding. For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/image.py#L89">enhance_image</a>.
      </td>
    </tr>
    <tr>
      <td>evaluate_image_quality</td>
      <td><b>Evaluate image quality</b>: Score image quality and aesthetics (subjective and objective). For detailed input and output parameters, see
        <a href="https://github.com/volcengine/mcp-server/blob/main/server/mcp_server_mediakit/src/mediakit/mcp_tools/image.py#L108">evaluate_image_quality</a>.
      </td>
    </tr>
  </tbody>
</table>

# Quick Start in Trae

Trae is an AI-native IDE with strong agent collaboration capabilities. By connecting MediaKit MCP, you can call cloud media processing capabilities in Trae with natural language and quickly complete tasks such as video editing, subtitle processing, audio processing, and video enhancement.

## Prerequisites

- Prepare a valid MediaKit API key.
- Install the [Trae client](https://www.trae.com.cn/).
- For local mode or self-hosted cloud mode, make sure `uvx` is installed in your local environment. Run `uvx --version` to check. If it is not installed, follow the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

## Steps

### Step 1: Choose an Access Mode

Choose one of the following modes based on your usage scenario:

| Mode                        | Best for                                                           | Access method                                                                                  |
| --------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| **Local Mode (JSON Local)** | Personal debugging, quick trials, no self-hosted service required. | Use `uvx` to launch MediaKit MCP directly from the `mcp-server` repository subdirectory.       |
| **Cloud Mode (JSON URL)**   | Team sharing, long-term usage, centralized operations.             | Deploy MediaKit MCP Server yourself, then connect using the deployed Streamable HTTP endpoint. |

### Step 2: Add MCP Configuration

1. Open Trae and click the settings button in the top-right corner.
2. In the MCP tab, click **Add** > **Add Manually**.
3. Copy the JSON configuration for your selected mode and replace the fields as described below.

#### Local Mode (JSON Local)

Copy the following JSON and replace the fields as needed. Trae uses `uvx` to fetch the remote code and run it locally.

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

**Field replacement notes:**

- `mediakit_mcp`: The MCP service name. You can customize it.
- `MEDIAKIT_API_KEY`: Replace with your MediaKit API key.
- `MCP_DOMAINS`: Load tools by group, for example `editing,video,audio,image`. To load tools by exact tool name, use `MCP_TOOLS` instead.

To load by tool name, use a configuration like this:

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

#### Cloud Mode (JSON URL)

Cloud mode does not provide a prebuilt deployment URL. Before using this mode, you need to deploy MediaKit MCP Server yourself and make sure the service is reachable through Streamable HTTP. After deployment, record the service URL, for example `https://your-domain/mcp`, and then connect it in Trae as shown below.

A simple startup example is:

```bash
export MEDIAKIT_API_KEY="your-api-key"
export MCP_SERVER_HOST="0.0.0.0"
export MCP_SERVER_PORT="8000"
export STREAMABLE_HTTP_PATH="/mcp"

uvx --from "git+https://github.com/volcengine/mcp-server.git#subdirectory=server/mcp_server_mediakit"   mcp-server-mediakit   --transport streamable-http
```

After deployment, copy the following JSON and replace the fields as needed:

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

**Field replacement notes:**

- `mediakit_mcp`: The MCP service name. You can customize it.
- `url`: Replace with your self-hosted MediaKit MCP Streamable HTTP URL, such as `https://your-domain/mcp`.
- `x-amk-api-key`: Replace with your MediaKit API key.
- `x-mcp-domains`: Load tools by group, for example `editing,video,audio,image`. To load tools by exact tool name, use `x-mcp-tools` instead.

To load by tool name, use a configuration like this:

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

4. Make sure the MCP status is shown as active in Trae.

### Step 3: Start Agent Conversations

Open the chat panel in Trae and switch the agent mode to one that supports MCP. Then you can directly issue natural language instructions such as:

- Trim this video to the first 10 seconds and output a new video.
- Add Chinese subtitles to this video with font size 28.
- Remove the subtitles at the bottom of this video, then enhance the processed video quality.
- Concatenate these two audio files, and if the task is asynchronous, continue querying until the final result is ready.

## Usage Notes

- Synchronous tasks return results directly.
- Asynchronous tasks return a `task_id`, and you need to call `query_task` to get task status and results.
- Idempotency is enabled by default. Requests from the same account with the same core parameters within 2 days return the first task result instead of creating duplicate tasks.
- To control idempotency explicitly, pass `client_token`. Reuse the same value for retries and use a new unique value to force a new task.
- `client_token` is generated by the client and must not exceed 64 characters.

## MCP Configuration Reference

The table below lists the core MediaKit MCP configuration fields for cloud mode and local mode.

<table>
  <thead>
    <tr>
      <th>Cloud header</th>
      <th>Local environment variable</th>
      <th>Example</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>x-amk-api-key</td>
      <td>MEDIAKIT_API_KEY</td>
      <td>your-api-key</td>
      <td>MediaKit API key used for authentication.</td>
    </tr>
    <tr>
      <td>x-mcp-domains</td>
      <td>MCP_DOMAINS</td>
      <td>editing,video,audio,image</td>
      <td>Load tools by group. Separate multiple groups with commas.</td>
    </tr>
    <tr>
      <td>x-mcp-tools</td>
      <td>MCP_TOOLS</td>
      <td>trim_video,query_task</td>
      <td>Load tools by tool name. Separate multiple tool names with commas.</td>
    </tr>
  </tbody>
</table>

For self-hosted cloud mode, you can also configure the following startup parameters:

| Environment variable   | Default value | Description                 |
| ---------------------- | ------------- | --------------------------- |
| `MCP_SERVER_HOST`      | `0.0.0.0`     | MCP service bind address.   |
| `MCP_SERVER_PORT`      | `8000`        | MCP service listening port. |
| `STREAMABLE_HTTP_PATH` | `/mcp`        | Streamable HTTP path.       |

## License

This project is open-sourced under the **MIT License**.

At runtime, this software calls the MediaKit cloud APIs. Using these APIs is subject to the following agreements:

- `https://www.volcengine.com/docs/6448/79646?lang=zh`
- `https://www.volcengine.com/docs/6448/104992?lang=zh`
- `https://www.volcengine.com/docs/6448/79648?lang=zh`
