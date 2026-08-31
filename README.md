<img src="assets/banner.svg" alt="Omar Fkih Hassen — dependable AI systems" width="100%" />

<p align="center">
  <a href="https://www.linkedin.com/in/omar-fkihhassen/"><img src="https://img.shields.io/badge/LinkedIn-160D24?style=flat-square&logo=linkedin&logoColor=2DD4BF" alt="LinkedIn" /></a>
  <a href="mailto:fkihhassen.omar111@gmail.com"><img src="https://img.shields.io/badge/Email-fkihhassen.omar111%40gmail.com-160D24?style=flat-square&logo=gmail&logoColor=F59E0B" alt="Email Omar Fkih Hassen" /></a>
  <img src="https://img.shields.io/badge/Tunis%2C%20Tunisia-160D24?style=flat-square&logo=googlemaps&logoColor=2DD4BF" alt="Tunis, Tunisia" />
  <img src="https://img.shields.io/badge/AI%20%26%20Computer%20Engineering-160D24?style=flat-square&logo=openai&logoColor=2DD4BF" alt="AI and Computer Engineering" />
</p>

I build AI systems for problems where **a plausible answer is not enough** — governed data changes, retail operations, environmental risk, finance, nutrition, and accessibility.

The signature across my work is a closed engineering loop: **retrieve evidence → let specialized agents reason → enforce critical rules in code → keep a human at the authority boundary → observe and evaluate the result.** The model is one component inside a typed, testable system; it is never the whole system.

<img src="assets/metrics.svg" alt="Measured evidence across Omar's AI engineering projects" width="100%" />

<table>
  <tr>
    <td align="center" width="16.6%"><a href="https://github.com/omarfh111/LineageGuard-AI"><img src="https://raw.githubusercontent.com/omarfh111/LineageGuard-AI/main/frontend/public/lineageguard-logo.png" height="62" alt="LineageGuard AI logo" /><br /><sub><b>LineageGuard</b></sub></a></td>
    <td align="center" width="16.6%"><a href="https://github.com/omarfh111/BaronsMarket"><img src="https://raw.githubusercontent.com/omarfh111/BaronsMarket/main/frontend/assets/logo_app.png" height="62" alt="BaronsMarket logo" /><br /><sub><b>BaronsMarket</b></sub></a></td>
    <td align="center" width="16.6%"><a href="https://github.com/omarfh111/Gabesi-AIGuardian"><img src="https://raw.githubusercontent.com/omarfh111/Gabesi-AIGuardian/main/logo.png" height="62" alt="Gabesi AIGuardian logo" /><br /><sub><b>Gabesi</b></sub></a></td>
    <td align="center" width="16.6%"><a href="https://github.com/omarfh111/FairTrace"><img src="https://raw.githubusercontent.com/omarfh111/FairTrace/main/frontend/public/logo1.png" height="62" alt="FairTrace logo" /><br /><sub><b>FairTrace</b></sub></a></td>
    <td align="center" width="16.6%"><a href="https://github.com/omarfh111/MarketLens"><img src="https://raw.githubusercontent.com/omarfh111/MarketLens/main/frontend/assistant/public/logo.svg" height="62" alt="MarketLens logo" /><br /><sub><b>MarketLens</b></sub></a></td>
    <td align="center" width="16.6%"><a href="https://github.com/omarfh111/NutriAI"><img src="https://raw.githubusercontent.com/omarfh111/NutriAI/main/frontend/public/nutrilens-logo.svg" height="62" alt="NutriAI logo" /><br /><sub><b>NutriAI</b></sub></a></td>
  </tr>
</table>

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

<img src="https://img.shields.io/badge/LangGraph-160D24?style=flat-square&logo=langchain&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/DataHub%20MCP-160D24?style=flat-square&logo=datahub&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/FastAPI-160D24?style=flat-square&logo=fastapi&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Qdrant-160D24?style=flat-square&logo=qdrant&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/React-160D24?style=flat-square&logo=react&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Docker-160D24?style=flat-square&logo=docker&logoColor=2DD4BF" />

**[▶ Live demo](https://lineageguard.hackdev.tech)** &nbsp;·&nbsp; [Evidence dossier](https://github.com/omarfh111/LineageGuard-AI/blob/main/docs/live-writeback-proof.md) &nbsp;·&nbsp; [Testing guide](https://github.com/omarfh111/LineageGuard-AI/blob/main/docs/judge-testing.md) &nbsp;·&nbsp; [Repository](https://github.com/omarfh111/LineageGuard-AI)

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

<img src="https://img.shields.io/badge/PyTorch-160D24?style=flat-square&logo=pytorch&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/YOLO-160D24?style=flat-square&logo=yolo&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Flutter-160D24?style=flat-square&logo=flutter&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/FastAPI-160D24?style=flat-square&logo=fastapi&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Qdrant-160D24?style=flat-square&logo=qdrant&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Supabase-160D24?style=flat-square&logo=supabase&logoColor=2DD4BF" />

[Demo evidence](https://github.com/omarfh111/BaronsMarket/tree/main/docs/screenshots) &nbsp;·&nbsp; [Architecture](https://github.com/omarfh111/BaronsMarket#architecture) &nbsp;·&nbsp; [Repository](https://github.com/omarfh111/BaronsMarket)

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

<img src="https://img.shields.io/badge/LangGraph-160D24?style=flat-square&logo=langchain&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/NASA%20POWER-160D24?style=flat-square&logo=nasa&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Qdrant-160D24?style=flat-square&logo=qdrant&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/GeoAI-160D24?style=flat-square&logo=openstreetmap&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/React-160D24?style=flat-square&logo=react&logoColor=2DD4BF" />

[Architecture](https://github.com/omarfh111/Gabesi-AIGuardian#2-system-overview) &nbsp;·&nbsp; [Design decisions](https://github.com/omarfh111/Gabesi-AIGuardian#design-decisions--tradeoffs) &nbsp;·&nbsp; [Repository](https://github.com/omarfh111/Gabesi-AIGuardian)

## How I build — the engineering signature

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

## Selected collaborations

These are shared builds whose canonical repository belongs to a teammate. They are listed separately to make ownership and collaboration explicit.

| Project | Contribution context | Proof and references |
|:--|:--|:--|
| **Splunk Sentinel** | Collaborator on an autonomous SOC investigation platform: six agents, ReAct reconstruction, Splunk-native evidence and 425 passing tests | [▶ Demo](https://youtu.be/vdQYQY1cXFA) · [Devpost](https://devpost.com/software/splunk-sentinel) · [Canonical repository](https://github.com/Asembris/splunk-sentinel) |
| **CareerPath Compass** | Collaborator on agentic career guidance grounded in O\*NET, BLS and Neo4j; 83.3% RAG grounded pass rate with a documented ablation | [▶ Live demo](https://careerpath-compass.vercel.app) · [Evidence](https://github.com/Asembris/CareerPathCompass#impact-metrics) · [Canonical repository](https://github.com/Asembris/CareerPathCompass) |
| **IBSAR** | Team Barons build for voice-first banking and shopping accessibility, created with the IBSAR association | [Project context](https://github.com/Asembris/EspritMaratech2026-Barons#-présentation-du-projet) · [Canonical repository](https://github.com/Asembris/EspritMaratech2026-Barons) |

## Activity

<img src="assets/activity.svg" alt="Omar Fkih Hassen's public GitHub contribution activity over the last 12 months" width="100%" />

<sub>Self-hosted in this repository and refreshed daily by <a href=".github/workflows/profile-activity.yml">GitHub Actions</a>. No third-party statistics widget.</sub>

## Stack

| | |
|:--|:--|
| **Languages** | <img src="https://img.shields.io/badge/Python-160D24?style=flat-square&logo=python&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/TypeScript-160D24?style=flat-square&logo=typescript&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Java-160D24?style=flat-square&logo=openjdk&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/SQL-160D24?style=flat-square&logo=postgresql&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/C-160D24?style=flat-square&logo=c&logoColor=2DD4BF" /> |
| **Agents & LLM** | <img src="https://img.shields.io/badge/LangGraph-160D24?style=flat-square&logo=langchain&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/LangChain-160D24?style=flat-square&logo=langchain&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/CrewAI-160D24?style=flat-square" /> <img src="https://img.shields.io/badge/MCP-160D24?style=flat-square" /> <img src="https://img.shields.io/badge/OpenAI-160D24?style=flat-square&logo=openai&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Ollama-160D24?style=flat-square&logo=ollama&logoColor=2DD4BF" /> |
| **Retrieval & ML** | <img src="https://img.shields.io/badge/Qdrant-160D24?style=flat-square&logo=qdrant&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/FAISS-160D24?style=flat-square" /> <img src="https://img.shields.io/badge/ChromaDB-160D24?style=flat-square&logo=chroma&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/PyTorch-160D24?style=flat-square&logo=pytorch&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/YOLO-160D24?style=flat-square" /> <img src="https://img.shields.io/badge/scikit--learn-160D24?style=flat-square&logo=scikitlearn&logoColor=2DD4BF" /> |
| **Backend & Data** | <img src="https://img.shields.io/badge/FastAPI-160D24?style=flat-square&logo=fastapi&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Django-160D24?style=flat-square&logo=django&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Spring%20Boot-160D24?style=flat-square&logo=springboot&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/PostgreSQL-160D24?style=flat-square&logo=postgresql&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Supabase-160D24?style=flat-square&logo=supabase&logoColor=2DD4BF" /> |
| **Product & Delivery** | <img src="https://img.shields.io/badge/React-160D24?style=flat-square&logo=react&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Next.js-160D24?style=flat-square&logo=nextdotjs&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Flutter-160D24?style=flat-square&logo=flutter&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Docker-160D24?style=flat-square&logo=docker&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/GitHub%20Actions-160D24?style=flat-square&logo=githubactions&logoColor=2DD4BF" /> |
| **Observability & Quality** | <img src="https://img.shields.io/badge/LangSmith-160D24?style=flat-square&logo=langchain&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Langfuse-160D24?style=flat-square" /> <img src="https://img.shields.io/badge/Pytest-160D24?style=flat-square&logo=pytest&logoColor=2DD4BF" /> <img src="https://img.shields.io/badge/Playwright-160D24?style=flat-square&logo=playwright&logoColor=2DD4BF" /> |

## Background

- AI & Computer Engineering student at **ESPRIT**, Tunisia
- AI engineering internship experience at **Capgemini Engineering**
- Hackathon builder: **Lunar Hack 2.0 — Top 4**, **H12 Innovation 3.0 — Top 8**, **Vectors in Orbit — finalist**
- Interested in agent reliability, multimodal systems, RAG evaluation and human-controlled automation

<p align="center">
  <a href="https://www.linkedin.com/in/omar-fkihhassen/"><img src="https://img.shields.io/badge/Let's%20build%20AI%20that%20holds%20up-Connect%20on%20LinkedIn-160D24?style=for-the-badge&logo=linkedin&logoColor=2DD4BF" alt="Connect on LinkedIn" /></a>
  <a href="mailto:fkihhassen.omar111@gmail.com"><img src="https://img.shields.io/badge/Email-fkihhassen.omar111%40gmail.com-160D24?style=for-the-badge&logo=gmail&logoColor=F59E0B" alt="Email Omar Fkih Hassen" /></a>
</p>

