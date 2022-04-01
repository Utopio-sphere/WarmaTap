# WarmaTap

根据 Warma 的最新视频 [【warma】来一起上网冲浪！](https://www.bilibili.com/video/BV1Gq4y1e7ND?share_source=copy_web) 中的第一个网站 [MikuTap](https://aidn.jp/mikutap/) 更换上 Warma 视频中自己录制的音效而修改成的小网站，命名为 WarmaTap

网站源代码取自这个项目 [mikutap](https://github.com/HFIProgramming/mikutap)

## 使用说明

将 Site 目录部署到服务器上托管即可

目前已上载至腾讯云托管，网站地址 [WarmaTap](https://file-share-1304947651.cos.ap-guangzhou.myqcloud.com/WarmaTap_Site/index.html)

`Site/Data/main/main.json` 使用 base64 编码了音频，使用Python 运行 decode_audio.py 和 encode_audio.py 即可对js文件音频进行解码和编码

Warma 天下第一！