<img src="assets/banner.svg" alt="Omar Fkih Hassen — AI engineer building evidence-grounded agent systems" width="100%" />

<p align="center">
  <a href="https://www.linkedin.com/in/omar-fkihhassen/"><img src="https://img.shields.io/badge/LinkedIn-0A1526?style=flat-square&logo=linkedin&logoColor=38BDF8" alt="LinkedIn" /></a>
  <img src="https://img.shields.io/badge/Tunis%2C%20Tunisia-0A1526?style=flat-square&logo=googlemaps&logoColor=38BDF8" alt="Tunis, Tunisia" />
  <img src="https://img.shields.io/badge/AI%20%26%20Computer%20Engineering-0A1526?style=flat-square&logo=openai&logoColor=38BDF8" alt="AI and Computer Engineering" />
</p>

I build AI systems for problems where **a plausible answer is not enough** — governed data changes, retail operations, environmental risk, finance, nutrition, and accessibility.

The signature across my work is a closed engineering loop: **retrieve evidence → let specialized agents reason → enforce critical rules in code → keep a human at the authority boundary → observe and evaluate the result.** The model is one component inside a typed, testable system; it is never the whole system.

<img src="assets/metrics.svg" alt="Measured evidence across Omar's AI engineering projects" width="100%" />

## Selected work

### [LineageGuard AI](https://github.com/omarfh111/LineageGuard-AI) &nbsp;·&nbsp; Governed agents for DataHub

An evidence-first agent system for schema-change impact analysis, verified catalog answers, and human-approved documentation write-back. Vector search can nominate a candidate; only live DataHub MCP reads can establish a fact. A deterministic engine computes blast radius and remediation, two independent judges review the immutable dossier, and the human owns the only write path.

<img src="assets/pipe-lineage.svg" alt="LineageGuard flow: request, retrieval, live DataHub evidence, deterministic impact analysis, independent review, human approval and scoped write-back" width="100%" />

| | |
|:--|:--|
| **Authority model** | Read-only by default; model agents cannot call the isolated writer |
| **Evidence** | Exact URNs, live schemas and multi-hop lineage from DataHub MCP |
| **Safety** | Double review, capability checks, idempotency, compare-and-swap and uncertain-outcome reconciliation |
| **Reproducibility** | Docker Compose, deterministic tests, browser E2E, CI and a public judge guide |

<img src="https://img.shields.io/badge/LangGraph-0A1526?style=flat-square&logo=langchain&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/DataHub%20MCP-0A1526?style=flat-square&logo=datahub&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/FastAPI-0A1526?style=flat-square&logo=fastapi&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/Qdrant-0A1526?style=flat-square&logo=qdrant&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/React-0A1526?style=flat-square&logo=react&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/Docker-0A1526?style=flat-square&logo=docker&logoColor=38BDF8" />

**[▶ Live demo](https://lineageguard.hackdev.tech)** &nbsp;·&nbsp; [Testing guide](https://github.com/omarfh111/LineageGuard-AI/blob/main/docs/judge-testing.md) &nbsp;·&nbsp; [Repository](https://github.com/omarfh111/LineageGuard-AI)

<br />

### [BaronsMarket](https://github.com/omarfh111/BaronsMarket) &nbsp;·&nbsp; Multimodal AI for smart retail

A complete retail system: a Flutter shopping experience, an employee operations console, and a GPU-ready FastAPI backend orchestrating **12 AI and computer-vision services**. The platform connects perception to operations — product recognition, freshness, queues, theft events, document integrity, employee access, semantic search, checkout and analytics.

<img src="assets/pipe-barons.svg" alt="BaronsMarket flow: mobile and employee interfaces, FastAPI orchestration, computer vision and RAG services, operational results" width="100%" />

| | |
|:--|:--|
| **Perception** | YOLO, CLIP, OCR, liveness, face matching and PyTorch/CUDA inference |
| **Retrieval** | FAISS for visual similarity and Qdrant for catalog-grounded semantic search |
| **Agent design** | Router and specialist agents constrained to products in the real catalog |
| **Product surface** | Flutter mobile app, employee dashboard, async video jobs and store analytics |

<img src="https://img.shields.io/badge/PyTorch-0A1526?style=flat-square&logo=pytorch&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/YOLO-0A1526?style=flat-square&logo=yolo&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/Flutter-0A1526?style=flat-square&logo=flutter&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/FastAPI-0A1526?style=flat-square&logo=fastapi&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/Qdrant-0A1526?style=flat-square&logo=qdrant&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/Supabase-0A1526?style=flat-square&logo=supabase&logoColor=38BDF8" />

[Repository](https://github.com/omarfh111/BaronsMarket)

<br />

### [Gabesi AIGuardian](https://github.com/omarfh111/Gabesi-AIGuardian) &nbsp;·&nbsp; Environmental and emergency intelligence

A regional decision-support platform for Gabès, Tunisia. It joins scientific RAG, live NASA and atmospheric data, geospatial analysis, deterministic environmental models, community alerts, energy projections, and medical triage — without pretending every problem should be solved by an LLM.

<img src="assets/pipe-gabesi.svg" alt="Gabesi AIGuardian flow: live and scientific evidence, specialist modules, guardrails, deterministic models and operator-facing decisions" width="100%" />

| | |
|:--|:--|
| **Grounding** | 1,718 scientific chunks across 21 documents plus live external signals |
| **Determinism** | FAO-56 irrigation, P80/P95 pollution bands, Haversine proximity and zero-LLM orchestration where appropriate |
| **Safety** | Four-layer guardrails, faithfulness verification and confidence-gated medical routing |
| **Validation** | 56 passing tests; Top 8 at H12 Innovation 3.0 — AI Healing Gabès |

<img src="https://img.shields.io/badge/LangGraph-0A1526?style=flat-square&logo=langchain&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/NASA%20POWER-0A1526?style=flat-square&logo=nasa&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/Qdrant-0A1526?style=flat-square&logo=qdrant&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/GeoAI-0A1526?style=flat-square&logo=openstreetmap&logoColor=38BDF8" /> <img src="https://img.shields.io/badge/React-0A1526?style=flat-square&logo=react&logoColor=38BDF8" />

[Repository](https://github.com/omarfh111/Gabesi-AIGuardian)

## The engineering signature

| Stage | What repeats across the projects |
|:--|:--|
| **1 · Observe** | PDFs, images, video, catalog metadata, satellite feeds, APIs and user context enter through explicit schemas. |
| **2 · Ground** | RAG narrows the search space; authoritative tools or datasets establish the evidence. Similarity is never treated as truth. |
| **3 · Orchestrate** | Specialized agents run in bounded sequential or fan-out/fan-in graphs, with structured outputs and explicit failure states. |
| **4 · Enforce** | Deterministic code owns thresholds, scoring, permissions, routing gates, idempotency and other load-bearing decisions. |
| **5 · Verify** | Tests, retrieval evaluations, traces, independent review and human approval close the loop. |

This is the common architecture behind the portfolio: **AI that can explain what it used, code that defines what it may do, and evidence that shows what actually happened.**

## More systems

| Project | Engineering evidence |
|:--|:--|
| [NutriAI](https://github.com/omarfh111/NutriAI) | Nutrition RAG over 18,601 dishes; 51 generated-and-refined QA pairs; 0.780 context relevance and 0.771 faithfulness |
| [MarketLens](https://github.com/omarfh111/MarketLens) | Product retrieval, campaign generation and a nine-agent retail analytics pipeline; Top 4 at Lunar Hack 2.0 |
| [TerraGuard](https://github.com/omarfh111/TerraGuard) | Nine-agent climate audit against GRI, TCFD, IFRS and IPCC evidence; 28/28 retrieval checks |
| [FairTrace](https://github.com/omarfh111/FairTrace) | Explainable credit decisions through parallel debate, dense + sparse retrieval and RRF |
| [Engineering Copilot](https://github.com/omarfh111/engineering-copilot-ai) | React, Spring Boot and FastAPI behind explicit trust boundaries, CI and human-reviewed AI findings |
| [DeepDrive](https://github.com/omarfh111/DeepDrive) | Automotive computer vision, specialized agents and full transaction workflows |

## Activity

<img src="assets/activity.svg" alt="Omar Fkih Hassen's public GitHub contribution activity over the last 12 months" width="100%" />

<sub>Self-hosted in this repository and refreshed daily by <a href=".github/workflows/profile-activity.yml">GitHub Actions</a>. No third-party statistics widget.</sub>

## Stack

| | |
|:--|:--|
| **Languages** | Python · TypeScript · Java · SQL · C |
| **Agents & LLM** | LangGraph · LangChain · CrewAI · MCP · OpenAI · Ollama |
| **Retrieval & ML** | Qdrant · FAISS · ChromaDB · PyTorch · YOLO · CLIP · scikit-learn |
| **Backend & Data** | FastAPI · Django · Spring Boot · PostgreSQL · Supabase · SQLite |
| **Product** | React · Next.js · Vite · Tailwind CSS · Flutter |
| **Delivery & Quality** | Docker · GitHub Actions · Pytest · Playwright · LangSmith · SSE |

## Background

- AI & Computer Engineering student at **ESPRIT**, Tunisia
- AI engineering internship experience at **Capgemini Engineering**
- Hackathon builder: **Lunar Hack 2.0 — Top 4**, **H12 Innovation 3.0 — Top 8**, **Vectors in Orbit — finalist**
- Interested in agent reliability, multimodal systems, RAG evaluation and human-controlled automation

<p align="center">
  <a href="https://www.linkedin.com/in/omar-fkihhassen/"><img src="https://img.shields.io/badge/Let's%20build%20AI%20that%20holds%20up-Connect%20on%20LinkedIn-0A1526?style=for-the-badge&logo=linkedin&logoColor=38BDF8" alt="Connect on LinkedIn" /></a>
</p>


