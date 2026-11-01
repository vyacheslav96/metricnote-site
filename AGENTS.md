# Vision
Лендинг для приложение для руковдителей небольших фирм. Оно позволяет с минимальными влложениями строить отчеты по данным из API. Данные тянутся в формате JSON.  Идея в том что бы настройками определять поля группировок и измерений. Выводы в формате таблицы, графиков.

# Mandates
Жесткие запреты и обязательные правила.
- Никогда не используй глобальные переменные.
- Всегда используй интерфейсы для внешних зависимостей.

# Workflow
Как мы работаем.
- Коммиты только в формате Conventional Commits.

# Documentation
#Требования к комментариям и документации.

## Project Overview

This is a Next.js 15 application with a Python FastAPI backend.
The frontend uses TypeScript, Tailwind CSS, and Zustand for state management.
The backend uses SQLAlchemy with PostgreSQL.

## Coding Standards

- Use functional components with hooks (no class components)
- All API endpoints must include input validation using Pydantic
- Write tests for every new function using pytest (backend) and Vitest (frontend)
- Use conventional commit messages: feat:, fix:, refactor:, docs:, test:

## Architecture

- Frontend routes are in src/app/ (App Router)
- API routes are in backend/api/routes/
- Database models are in backend/models/
- Shared types are in shared/types/

## Constraints

- Do not modify the database schema without explicit approval
- Do not add new dependencies without noting them in the PR description
- All environment variables must be documented in .env.example
