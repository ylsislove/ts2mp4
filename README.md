# 腾讯视频 TS 文件转 MP4

## 提取下载目录
腾讯视频缓存目录：`/Android/data/com.tencent.qqlive/files/videos_XXXXX/`

目录下每个`.hls`结尾的文件夹为一个视频的缓存

## 使用方法
将 `main.py` 和 `run.bat` 文件放置到文件夹根目录，例如一个视频`y0038k189n8.322013.hls`目录结构形如下:

```
├── main.py
├── run.bat
├── y0038k189n8.322013.hls_0_29
│   ├── 0.ts
│   ├── 1.ts
│   ├── ......
│   └── 29.ts
├── y0038k189n8.322013.hls_30_59
│   ├── 30.ts
│   ├── 31.ts
│   ├── ......
│   └── 59.ts
├── y0038k189n8.322013.hls_60_89
│   ├── 60.ts
│   ├── 61.ts
│   ├── ......
│   └── 89.ts
├── offline.m3u8
├── tpt
│   ├── y0038k189n8.322013.hls.1
│   ├── y0038k189n8.322013.hls.2
│   ├── ......
└── ......
```

双击 `run.bat` 文件即可运行，成功截图

![](http://image.aayu.today/2022/06/29/368358891e6c3.png)

## 注意事项
电脑需要 Python3.6 以上环境和 FFmpeg 命令行软件，安装方法自行百度~
