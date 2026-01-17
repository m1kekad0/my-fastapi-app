# FastAPI Vercel App

FastAPI を使用した Vercel デプロイ用のバックエンドアプリケーションです。
パッケージ管理には [uv](https://github.com/astral-sh/uv) を使用しています。

**デモ URL**: [https://my-fastapi-app-sigma.vercel.app/](https://my-fastapi-app-sigma.vercel.app/)

## 開発環境のセットアップ

```bash
# uv のインストール (未導入の場合)
brew install uv

# Python 3.12 のインストールと固定
uv python install 3.12
uv python pin 3.12

# 依存関係の同期
uv sync

# pre-commit の有効化 (コミット時に Ruff を自動実行)
uv run pre-commit install
```

## ローカルでの実行

```bash
# ローカルサーバー起動
uv run python3 -m uvicorn api.index:app --reload
```

## コード品質 (Linter/Formatter)

[Ruff](https://docs.astral.sh/ruff/) を使用しています。

```bash
# チェックと自動修正
uv run ruff check --fix

# 整形
uv run ruff format
```

## テストの実行

```bash
uv run pytest
```

## デプロイ手順 (Vercel)

Vercel は `pyproject.toml` を直接サポートしていないため、デプロイ前に `requirements.txt` を生成する必要があります。

### 1. 依存関係の追加・更新
新しいライブラリを追加した場合は、以下の手順を実施してください。

```bash
# 1. パッケージの追加
uv add <package_name>

# 2. requirements.txt の再生成 (重要)
uv run python3 generate_requirements.py
```

### 3. テスト
デプロイ前にテストが通ることを確認してください。

```bash
uv run pytest
```

### 2. デプロイの実行

```bash
# Vercel CLI を使用する場合
vercel --prod

# または GitHub にプッシュ (自動デプロイ設定済みの場合)
git add .
git commit -m "feat: add new feature"
git push
```

## プロジェクト構造

- `api/index.py`: FastAPI のエントリーポイント
- `generate_requirements.py`: `pyproject.toml` から `requirements.txt` を生成するスクリプト
- `vercel.json`: Vercel のデプロイ・ルーティング設定
- `pyproject.toml`: プロジェクト設定・依存関係管理
- `tests/`: テストコード
- `.gitmessage`: コミットメッセージのテンプレート
- `LICENSE`: MIT ライセンス

## ライセンス

[MIT License](LICENSE)