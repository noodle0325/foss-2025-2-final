# foss-2025-2-final
# notion-git-doc-sync - foss-2025-1-final


# Notion과 Git을 연동한 협업 중심 개발 문서화 워크플로우 구축

## 1. 아이템 선정 동기

개발 현장에서 문서화는 협업에 있어 필수적인 요소입니다. 하지만 대부분의 문서 작성은 코드와 분리된 도구(Google Docs, Notion 등)에서 이루어지며, 다음과 같은 문제가 발생합니다.

- 문서 최신화 누락
- PR과 문서의 불일치
- 중복된 문서 저장 및 공유

이러한 문제를 해결하기 위해, **Git에서 관리하는 문서를 Notion에 자동으로 연동하는 워크플로우**를 만들고자 했습니다. 이를 통해 **코드와 문서 간의 싱크 문제를 줄이고 협업 효율을 높이는 환경**을 조성하고자 합니다.

---

## 2. 기대 효과

- Git 기반 버전 관리를 통한 문서 이력 추적
- Pull Request와 함께 문서 자동 업데이트
- Notion을 통한 직관적인 문서 협업
- 코드 변경 사항에 따른 문서 자동 반영

---

## 3. 구현 개요

- **언어/기술 스택**: Python, GitHub Actions, Notion API
- **동작 흐름**:
  1. 개발자가 Markdown 문서를 `docs/`에 커밋
  2. GitHub Actions가 해당 문서 감지
  3. Python 스크립트 실행 → Notion API 호출
  4. Notion의 문서 데이터베이스에 새 페이지 생성 또는 업데이트

- **구현 주요 파일**:
  - `scripts/sync_to_notion.py`: 문서를 Notion에 업로드하는 핵심 스크립트
  - `.github/workflows/sync-notion.yml`: GitHub Actions 자동화 구성
  - `docs/api.md`: 예시 문서 파일

---

## 4. 활용 시나리오

- 개발자가 API 변경 → `api.md` 수정 → 커밋
- GitHub Actions → 문서 자동 Notion에 업로드
- 팀원은 별도 공유 없이 최신 문서를 Notion에서 바로 확인
- 회의 준비 시 문서 공유 및 이력 확인 간소화

---

## 5. 향후 개선 방향

- Notion 페이지의 업데이트 감지 기능 추가
- PR 승인 시에만 문서 업데이트하도록 조건 설정
- 다중 문서 자동 분류 및 태그 지정 기능 도입

---

## 6. 실행 방법

```bash
# Notion API token 및 Database ID 환경 변수 설정
export NOTION_TOKEN=your_token_here
export NOTION_DATABASE_ID=your_database_id_here

# 문서 자동 등록 스크립트 실행
python scripts/sync_to_notion.py
