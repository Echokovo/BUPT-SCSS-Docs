# 互联网舆情发现系统

## 项目简介

本项目是基于 Python 和 selenium 的网络舆情分析系统，主要功能包括：爬取微博平台的内容（根据主题/用户）、识别负面文本、统计与可视化分析。

## 运行说明

### 1. 安装依赖

系统内需要安装 `chrome`

```bash
pip install -r requirements.txt
```

### 2. 清理爬取到的旧 json 文件

注意，该操作会删除项目文件夹中 Keywords, Topics, User 文件夹中的 json 文件

```bash
python cleanJSON.py
```

### 3. 设置爬取主题与用户

可在 `config.py` 中自定义主题与用户

### 4. 爬取主题与用户主页

```bash
python topic.py
python user.py
```

### 5. 获取关键词表

```bash
python getKeywords.py
```

### 6. 分析结果

```bash
python analysis.py
```

## 注意事项

- 本项目仅供学习目的，请勿用于非法用途
- 进行爬虫时请遵守各平台的 robots 协议
