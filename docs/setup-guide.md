# 🚀 Discord Bot セットアップガイド

このガイドでは、Pythonで作成された最小構成のDiscordボットをセットアップする詳細な手順を説明します。

## 📋 前提条件

### 必要な環境
- **Python 3.8以上** がインストールされていること
- **インターネット接続** があること
- **Discordアカウント** を持っていること
- **基本的なコマンドライン操作** ができること

### 推奨環境
- **Python 3.10以上** （最新の安定版を推奨）
- **Git** （バージョン管理用）
- **テキストエディタ** （VS Code、PyCharm等）

## 🔧 ステップ1: Discordアプリケーションの作成

### 1.1 Discord Developer Portalにアクセス
1. [Discord Developer Portal](https://discord.com/developers/applications) にアクセス
2. Discordアカウントでログイン

### 1.2 新しいアプリケーションの作成
1. **"New Application"** ボタンをクリック
2. アプリケーション名を入力（例：「My First Bot」）
3. **"Create"** をクリック

### 1.3 ボットユーザーの作成
1. 左サイドバーから **"Bot"** を選択
2. **"Add Bot"** をクリック
3. **"Yes, do it!"** で確認

### 1.4 ボット設定の調整
1. **"Privileged Gateway Intents"** セクションで以下を有効化：
   - ✅ **Message Content Intent** （重要！）
   - ⚠️ **Server Members Intent** （オプション）
   - ⚠️ **Presence Intent** （オプション）

### 1.5 ボットトークンの取得
1. **"Token"** セクションで **"Copy"** をクリック
2. トークンを安全な場所にメモ（**絶対に他人に教えないでください！**）

### 1.6 ボットの招待URL作成
1. 左サイドバーから **"OAuth2"** → **"URL Generator"** を選択
2. **"Scopes"** で `bot` にチェック
3. **"Bot Permissions"** で以下を選択：
   - ✅ Send Messages
   - ✅ Read Message History
   - ✅ Use Slash Commands
   - ✅ Embed Links
4. 生成されたURLをコピー

### 1.7 ボットをテストサーバーに招待
1. 作成したURLをブラウザで開く
2. ボットを招待するサーバーを選択
3. **"認証"** をクリック

## 📦 ステップ2: プロジェクトのセットアップ

### 2.1 プロジェクトのクローン
```bash
git clone https://github.com/Sunwood-ai-labs/py-discord-bot.git
cd py-discord-bot
```

### 2.2 仮想環境の作成（推奨）
```bash
# Python venv を使用
python -m venv venv

# 仮想環境のアクティベート
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2.3 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 2.4 環境変数ファイルの設定
```bash
# .env.example を .env にコピー
cp .env.example .env
```

### 2.5 .envファイルの編集
テキストエディタで `.env` ファイルを開き、以下を設定：

```env
# 必須設定
DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE

# オプション設定
COMMAND_PREFIX=!
BOT_NAME=MyDiscordBot
BOT_VERSION=1.0.0
BOT_DESCRIPTION=私の最初のDiscordボット
```

⚠️ **重要**: `YOUR_BOT_TOKEN_HERE` を実際のボットトークンに置き換えてください。

## 🚀 ステップ3: ボットの起動

### 3.1 ボットの実行
```bash
python bot.py
```

### 3.2 成功時の表示
以下のようなメッセージが表示されれば成功です：
```
INFO:__main__:ボットを起動しています...
INFO:__main__:MyDiscordBot がDiscordにログインしました！
INFO:__main__:ボットID: 123456789012345678
```

### 3.3 ボットのテスト
Discordサーバーで以下のコマンドを試してください：
- `!hello` - 挨拶メッセージ
- `!ping` - レスポンス時間測定
- `!info` - ボット情報表示
- `!help` - コマンド一覧

## 🔧 カスタマイズ

### コマンドプレフィックスの変更
`.env` ファイルの `COMMAND_PREFIX` を変更：
```env
COMMAND_PREFIX=?  # ? を使用
COMMAND_PREFIX=bot!  # bot! を使用
```

### ボット名の変更
`.env` ファイルの `BOT_NAME` を変更：
```env
BOT_NAME=私の素敵なボット
```

### 新しいコマンドの追加
`commands/basic.py` ファイルに新しいコマンドを追加できます。

## 🛠️ 開発環境の設定

### VS Code拡張機能（推奨）
- Python
- Python Docstring Generator
- GitLens

### コードフォーマッター
```bash
# Black のインストール
pip install black

# コードのフォーマット
black .
```

## 📚 次のステップ

1. **機能の拡張**: `commands/` ディレクトリに新しいコマンドファイルを追加
2. **データベース連携**: SQLiteやPostgreSQLとの連携
3. **Web API連携**: 外部APIとの連携機能
4. **スラッシュコマンド**: モダンなスラッシュコマンドの実装
5. **デプロイ**: Heroku、Railway、VPSでのホスティング

## 🆘 トラブルシューティング

問題が発生した場合は、[troubleshooting.md](troubleshooting.md) を参照してください。

## 📞 サポート

- 🐛 **バグ報告**: [GitHub Issues](https://github.com/Sunwood-ai-labs/py-discord-bot/issues)
- 💬 **質問・相談**: [GitHub Discussions](https://github.com/Sunwood-ai-labs/py-discord-bot/discussions)
- 📧 **その他**: プロジェクトの README を参照

---

🎉 **おめでとうございます！** Discordボットのセットアップが完了しました。楽しいボット開発をお楽しみください！