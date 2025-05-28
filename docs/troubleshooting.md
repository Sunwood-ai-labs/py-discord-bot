# 🛠️ トラブルシューティングガイド

Discordボット開発でよく遭遇する問題とその解決方法をまとめています。

## 🔍 よくある問題と解決方法

### 1. ボットが起動しない

#### ❌ エラー: `discord.errors.LoginFailure`
```
discord.errors.LoginFailure: Improper token has been passed.
```

**原因と解決方法:**
- ❌ **間違ったトークンを使用している**
  - ✅ Discord Developer Portalで正しいトークンをコピー
  - ✅ `.env` ファイルに正確に貼り付け
  - ✅ トークンの前後に余分なスペースがないか確認

- ❌ **トークンが再生成されている**
  - ✅ Discord Developer Portalで新しいトークンを生成
  - ✅ 古いトークンは無効になるため、新しいものを使用

- ❌ **環境変数が読み込まれていない**
  - ✅ `.env` ファイルがプロジェクトルートにあるか確認
  - ✅ ファイル名が正確に `.env` であることを確認

#### ❌ エラー: `ModuleNotFoundError: No module named 'discord'`
```
ModuleNotFoundError: No module named 'discord'
```

**解決方法:**
```bash
# 仮想環境がアクティベートされているか確認
pip install discord.py

# または requirements.txt から一括インストール
pip install -r requirements.txt
```

### 2. ボットがメッセージに反応しない

#### ❌ **Message Content Intent が無効**
ボットがメッセージを読み取れない最も一般的な原因です。

**解決方法:**
1. [Discord Developer Portal](https://discord.com/developers/applications) にアクセス
2. アプリケーションを選択 → "Bot" セクション
3. "Privileged Gateway Intents" で **Message Content Intent** を有効化
4. ボットを再起動

#### ❌ **ボットに適切な権限がない**
**確認方法:**
1. Discordサーバーでボットの役割を確認
2. 以下の権限が付与されているか確認：
   - 📨 メッセージを送信
   - 📖 メッセージ履歴を読む
   - 🔗 埋め込みリンク

**解決方法:**
```
サーバー設定 → 役割 → ボットの役割を編集 → 必要な権限を付与
```

### 3. コマンドが認識されない

#### ❌ **間違ったプレフィックスを使用**
**確認方法:**
- `.env` ファイルの `COMMAND_PREFIX` を確認
- デフォルトは `!` です

**例:**
```env
COMMAND_PREFIX=!  # この場合 !hello を使用
COMMAND_PREFIX=?  # この場合 ?hello を使用
```

#### ❌ **コマンド名の間違い**
**利用可能なコマンド:**
- `!hello [ユーザー名]`
- `!ping`
- `!info`
- `!help [コマンド名]`

### 4. パフォーマンスの問題

#### ⚠️ **高いレスポンス時間（500ms以上）**
**原因:**
- ネットワーク接続の問題
- サーバーリソース不足
- Discordサーバーの問題

**解決方法:**
1. **ネットワーク確認:**
   ```bash
   ping discord.com
   ```

2. **システムリソース確認:**
   ```bash
   # CPU使用率
   top
   
   # メモリ使用量
   free -h
   ```

3. **ボットの再起動:**
   ```bash
   # Ctrl+C でボットを停止
   python bot.py  # 再起動
   ```

### 5. エラーログの読み方

#### 📋 **一般的なエラーパターン**

```python
# 1. 接続エラー
aiohttp.client_exceptions.ClientConnectorError
→ インターネット接続を確認

# 2. 権限エラー
discord.errors.Forbidden
→ ボットの権限を確認

# 3. レート制限エラー
discord.errors.HTTPException: 429 Too Many Requests
→ コマンドの実行頻度を下げる

# 4. 設定ファイルエラー
FileNotFoundError: [Errno 2] No such file or directory: '.env'
→ .env ファイルの存在を確認
```

### 6. 開発環境の問題

#### ❌ **仮想環境の問題**
```bash
# 仮想環境の確認
which python
pip list

# 新しい仮想環境の作成
python -m venv new_venv
source new_venv/bin/activate  # Linux/macOS
new_venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

#### ❌ **Pythonバージョンの問題**
```bash
# Pythonバージョンの確認
python --version

# Python 3.8以上が必要です
# 古いバージョンの場合は更新してください
```

### 7. セキュリティ関連

#### ⚠️ **トークンの漏洩対策**
- ✅ `.env` ファイルを `.gitignore` に追加済み
- ✅ GitHubにトークンをコミットしない
- ✅ トークンを他人と共有しない

**もしトークンが漏洩した場合:**
1. Discord Developer Portalで即座にトークンを再生成
2. 古いトークンは自動的に無効化されます
3. 新しいトークンを `.env` ファイルに設定

### 8. デバッグテクニック

#### 🔍 **ログレベルの調整**
`bot.py` でより詳細なログを出力：

```python
import logging
logging.basicConfig(level=logging.DEBUG)  # より詳細なログ
```

#### 🧪 **テスト用コマンドの追加**
`commands/basic.py` にデバッグ用コマンドを追加：

```python
@self.bot.command(name='debug')
async def debug_command(ctx):
    """デバッグ情報を表示"""
    embed = discord.Embed(title="🔍 デバッグ情報")
    embed.add_field(name="ユーザーID", value=ctx.author.id)
    embed.add_field(name="チャンネルID", value=ctx.channel.id)
    embed.add_field(name="サーバーID", value=ctx.guild.id if ctx.guild else "DM")
    await ctx.send(embed=embed)
```

## 🆘 さらなるサポートが必要な場合

### 📞 サポートチャネル
1. **GitHub Issues**: [問題を報告](https://github.com/Sunwood-ai-labs/py-discord-bot/issues)
2. **GitHub Discussions**: [質問・相談](https://github.com/Sunwood-ai-labs/py-discord-bot/discussions)
3. **公式ドキュメント**: [discord.py docs](https://discordpy.readthedocs.io/)

### 📋 バグ報告時の情報
問題を報告する際は、以下の情報を含めてください：

```
## 環境情報
- OS: [例: Windows 10, macOS 12, Ubuntu 22.04]
- Python バージョン: [例: 3.10.5]
- discord.py バージョン: [例: 2.3.0]

## 問題の詳細
- 何をしようとしていたか
- 期待していた動作
- 実際に起こった動作
- エラーメッセージ（あれば）

## 再現手順
1. 
2. 
3. 

## 設定ファイル
- .env の内容（トークンは除く）
- カスタマイズした部分
```

### 🚀 コミュニティリソース
- **Discord.py 公式サーバー**: [Discord Server](https://discord.gg/dpy)
- **Python Discord**: [Discord Server](https://discord.gg/python)
- **Stack Overflow**: `discord.py` タグで検索

---

💡 **ヒント**: 問題解決のため、まずは最小限のコードで動作確認を行い、段階的に機能を追加していくことをお勧めします。