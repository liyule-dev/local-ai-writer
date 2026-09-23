# StoryMemory — 长篇小说创作智能体

> 基于 RAG 与结构化记忆的 AI 应用后端，解决大模型在长篇创作中“遗忘设定、前后矛盾”的问题。

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](LICENSE)
[![Status](https://img.shields.io/badge/Status-开发中-orange)]()

---

## 项目简介

通用大模型写短篇尚可，但写到几十万字后，角色性格会漂移、伏笔会丢失、设定会矛盾。

StoryMemory 通过以下方式为 AI 创作助手提供“长期记忆”：

- 结构化设定存储
- 向量检索（RAG）
- 一致性校验

本项目是面向 **AI 应用开发岗位** 的求职作品。

---

## 技术栈

- **后端**：Python、FastAPI
- **AI**：LangChain、智谱 API
- **向量数据库**：Chroma
- **关系数据库**：SQLite + SQLAlchemy
- **前端**：Streamlit
- **部署**：Docker

---

## 目录结构

```text
story-memory/
├── app/          # FastAPI 后端
├── frontend/     # Streamlit 前端
├── data/         # 运行时数据（git 忽略）
├── tests/        # 测试
├── scripts/      # 辅助脚本
├── docs/         # 详细文档
├── .env.example
├── requirements.txt
└── README.md
```

---

## 快速开始

> 项目仍在开发中，命令会随 MVP 完成情况更新。

```bash
git clone https://github.com/liyule-dev/story-memory.git
cd story-memory

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env       # 填入智谱 API Key
```

---

## 开发路线图

- [x] 项目骨架搭建
- [ ] 设定管理 CRUD
- [ ] RAG 检索（Chroma）
- [ ] 续写生成接口
- [ ] 一致性校验
- [ ] Streamlit 前端
- [ ] Docker 部署

---

## License

[Apache License 2.0](LICENSE)