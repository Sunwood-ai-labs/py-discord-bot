<div align="center">

<img src="docs/header.png" width="100%" alt="py discord bot header"/>

<h1>🤖 Python Discord Bot - 最小構成</h1>

<p>
  <img alt="GitHub" src="https://img.shields.io/github/license/Sunwood-ai-labs/py-discord-bot">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-blue">
  <img alt="discord.py" src="https://img.shields.io/badge/discord.py-2.3.0%2B-7289da">
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/Sunwood-ai-labs/py-discord-bot">
  <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/Sunwood-ai-labs/py-discord-bot">
</p>

<p>
  Pythonで作成する<b>最小構成のDiscordボット</b>のサンプルコード集✨<br>
  初心者でも簡単に学習できる、わかりやすい実装とドキュメントを提供します！
</p>

<p>
  <a href="README_EN.md">🇺🇸 English</a> | 
  <a href="README.md">🇯🇵 日本語</a>
</p>

</div>

## 📋 概要

このプロジェクトは、**Discord Bot開発の入門者**が簡単に学習・理解できる最小構成のDiscordボットです。基本的なコマンド機能を実装し、セキュリティベストプラクティスに従った設計になっています。

### 🎯 対象ユーザー
- Discord Bot開発の初心者
- Pythonプログラミングの基礎知識を持つ開発者
- 教育目的でDiscord Botを学習したい学生・教員

## ✨ 主な機能

### 🚀 基本コマンド
- `!hello [ユーザー名]` - 挨拶メッセージを送信
- `!ping` - ボットのレスポンス時間を測定
- `!info` - ボットの詳細情報を表示
- `!help [コマンド名]` - コマンドのヘルプを表示

### 🔒 セキュリティ機能
- 環境変数によるトークン管理
- 適切なエラーハンドリング
- セキュアな設定ファイル管理

### 📚 学習支援
- 初心者向けの詳細なコメント
- ステップバイステップのセットアップガイド
- 豊富なドキュメントとトラブルシューティング

## 🛠️ 技術スタック

| 技術 | バージョン | 用途 |
|------|------------|------|
| Python | 3.8+ | メイン言語 |
| discord.py | 2.3.0+ | Discord API連携 |
| python-dotenv | 1.0.0+ | 環境変数管理 |
| aiohttp | 3.8.0+ | 非同期HTTP通信 |

## 📁 プロジェクト構造

```
py-discord-bot/
├── 📄 README.md              # このファイル
├── 📄 requirements.txt       # Python依存関係
├── 📄 .env.example          # 環境変数テンプレート
├── 📄 .gitignore           # Git除外設定
├── 🐍 bot.py               # メインボットファイル
├── ⚙️ config.py            # 設定管理
├── 📦 commands/            # コマンドモジュール
│   ├── __init__.py
│   └── basic.py            # 基本コマンド
└── 📚 docs/                # ドキュメント
    ├── setup-guide.md      # 詳細セットアップガイド
    └── troubleshooting.md  # トラブルシューティング
```

## 🚀 クイックスタート

### 📋 前提条件
- Python 3.8以上
- インターネット接続環境
- Discordアカウント

### ⚡ 5分でセットアップ

1. **リポジトリのクローン**
   ```bash
   git clone https://github.com/Sunwood-ai-labs/py-discord-bot.git
   cd py-discord-bot
   ```

2. **依存関係のインストール**
   ```bash
   pip install -r requirements.txt
   ```

3. **環境設定**
   ```bash
   cp .env.example .env
   # .envファイルを編集してDISCORD_TOKENを設定
   ```

4. **ボットの起動**
   ```bash
   python bot.py
   ```

### 🔑 Discord Botトークンの取得

1. [Discord Developer Portal](https://discord.com/developers/applications) にアクセス
2. "New Application" → アプリケーション名を入力
3. "Bot" → "Add Bot" → トークンをコピー
4. `.env` ファイルに `DISCORD_TOKEN=your_token_here` を設定

> 📖 **詳細な手順**: [setup-guide.md](docs/setup-guide.md) を参照

## 💻 使用方法

### 基本的なコマンド例

```bash
# 挨拶
!hello
# 出力: 👋 こんにちは、@ユーザー名さん！

# 特定のユーザーに挨拶
!hello Alice
# 出力: 👋 こんにちは、Aliceさん！

# レスポンス時間チェック
!ping
# 出力: 🏓 Pong! レスポンス時間: 45.67ms

# ボット情報
!info
# 出力: ボットの詳細情報（バージョン、統計など）

# ヘルプ
!help
# 出力: 利用可能なコマンド一覧
```

### カスタマイズ例

```python
# .env ファイルでカスタマイズ
COMMAND_PREFIX=?          # コマンドプレフィックスを変更
BOT_NAME=MyCustomBot      # ボット名を変更
BOT_DESCRIPTION=My Bot    # ボットの説明を変更
```

## 🎓 学習リソース

### 📚 ドキュメント
- [📖 詳細セットアップガイド](docs/setup-guide.md) - ステップバイステップの導入手順
- [🛠️ トラブルシューティング](docs/troubleshooting.md) - よくある問題と解決方法

### 🔧 コード解説
- **bot.py**: メインボット機能とイベントハンドリング
- **config.py**: 設定管理と環境変数の処理
- **commands/basic.py**: 基本コマンドの実装とEmbed使用例

### 🚀 次のステップ
1. **新しいコマンドの追加** - `commands/` ディレクトリに機能を追加
2. **データベース連携** - SQLiteやPostgreSQLとの連携
3. **Web API連携** - 外部APIとの連携機能
4. **スラッシュコマンド** - モダンなスラッシュコマンドの実装

## 🤝 コントリビューション

プロジェクトへの貢献を歓迎します！

### 貢献方法
1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

### 開発ガイドライン
- PEP 8に従ったコーディングスタイル
- 初心者にわかりやすいコメント
- 適切なエラーハンドリング
- セキュリティベストプラクティスの遵守

## 🛡️ セキュリティ

### 重要な注意事項
- **絶対にボットトークンを公開しないでください**
- `.env` ファイルは既に `.gitignore` に含まれています
- 環境変数で機密情報を管理してください

### 推奨事項
- 定期的にトークンを再生成
- 最小限の権限でボットを運用
- ログに機密情報を出力しない

## 🆘 サポート

### 問題が発生した場合
1. [トラブルシューティング](docs/troubleshooting.md) を確認
2. [GitHub Issues](https://github.com/Sunwood-ai-labs/py-discord-bot/issues) で問題を報告
3. [GitHub Discussions](https://github.com/Sunwood-ai-labs/py-discord-bot/discussions) で質問

### コミュニティ
- **Discord.py公式**: [Discord Server](https://discord.gg/dpy)
- **Python Discord**: [Discord Server](https://discord.gg/python)

## 📄 ライセンス

このプロジェクトは [MIT License](LICENSE) の下で公開されています。

## 🙏 謝辞

- [discord.py](https://github.com/Rapptz/discord.py) - 素晴らしいDiscord APIライブラリ
- Discord開発者コミュニティ - 継続的なサポートと知識共有
- すべてのコントリビューター - プロジェクトの改善への貢献

---

<div align="center">

**🎉 Happy Bot Building! 🎉**

*Pythonと一緒に素晴らしいDiscordボットを作りましょう！*

</div>