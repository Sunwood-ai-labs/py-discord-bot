"""
🚀 基本コマンドモジュール

このファイルはDiscordボットの基本的なコマンドを実装します。
初心者向けの簡単なコマンドを提供し、ボットの基本機能を学習できます。

実装コマンド:
- !hello: 挨拶メッセージ
- !ping: レスポンス時間測定
- !info: ボット情報表示
- !help: ヘルプメッセージ
"""

import discord
from discord.ext import commands
import time
from config import Config

class BasicCommands:
    """基本コマンドクラス
    
    ボットの基本的なコマンド機能を提供するクラスです。
    初心者が理解しやすいシンプルなコマンドを実装しています。
    """
    
    def __init__(self, bot):
        """初期化
        
        Args:
            bot: Discordボットインスタンス
        """
        self.bot = bot
    
    def register_commands(self):
        """コマンドの登録
        
        各コマンドをボットに登録します。
        """
        
        @self.bot.command(name='hello')
        async def hello_command(ctx, *, user_name: str = None):
            """挨拶コマンド
            
            ボットが挨拶メッセージを返します。
            ユーザー名を指定すると、個人的な挨拶をします。
            
            使用例:
                !hello
                !hello Alice
            
            Args:
                ctx: コマンドコンテキスト
                user_name: 挨拶対象のユーザー名（オプション）
            """
            if user_name:
                # ユーザー名が指定された場合
                message = f"👋 こんにちは、{user_name}さん！\n✨ 今日も素敵な一日をお過ごしください！"
            else:
                # ユーザー名が指定されていない場合
                message = f"👋 こんにちは、{ctx.author.mention}さん！\n🎉 私は{Config.BOT_NAME}です。よろしくお願いします！"
            
            # Embedを使用して見栄えの良いメッセージを作成
            embed = discord.Embed(
                title="🌟 ご挨拶",
                description=message,
                color=0x00ff00  # 緑色
            )
            embed.set_footer(text=f"{Config.BOT_NAME} v{Config.BOT_VERSION}")
            
            await ctx.send(embed=embed)
        
        @self.bot.command(name='ping')
        async def ping_command(ctx):
            """pingコマンド
            
            ボットのレスポンス時間を測定します。
            ネットワークの遅延やボットの応答性を確認できます。
            
            使用例:
                !ping
            
            Args:
                ctx: コマンドコンテキスト
            """
            # レスポンス時間の計算開始
            start_time = time.time()
            
            # 一時的なメッセージを送信
            message = await ctx.send("🏓 Pong! 計算中...")
            
            # レスポンス時間の計算終了
            end_time = time.time()
            response_time = (end_time - start_time) * 1000  # ミリ秒に変換
            
            # Discord APIのレイテンシも取得
            api_latency = self.bot.latency * 1000  # ミリ秒に変換
            
            # Embedでレスポンス時間を表示
            embed = discord.Embed(
                title="🏓 Pong!",
                color=0x0099ff  # 青色
            )
            embed.add_field(
                name="⚡ レスポンス時間",
                value=f"`{response_time:.2f}ms`",
                inline=True
            )
            embed.add_field(
                name="🌐 APIレイテンシ",
                value=f"`{api_latency:.2f}ms`",
                inline=True
            )
            
            # パフォーマンスの評価
            if response_time < 100:
                performance = "🟢 優秀"
            elif response_time < 500:
                performance = "🟡 良好"
            else:
                performance = "🔴 改善の余地あり"
            
            embed.add_field(
                name="📊 パフォーマンス",
                value=performance,
                inline=False
            )
            
            embed.set_footer(text=f"{Config.BOT_NAME} v{Config.BOT_VERSION}")
            
            # メッセージを更新
            await message.edit(content="", embed=embed)
        
        @self.bot.command(name='info')
        async def info_command(ctx):
            """情報コマンド
            
            ボットの詳細情報を表示します。
            バージョン、機能、開発者情報などを確認できます。
            
            使用例:
                !info
            
            Args:
                ctx: コマンドコンテキスト
            """
            # ボットの情報を取得
            guild_count = len(self.bot.guilds)
            user_count = len(self.bot.users)
            
            # Embedで情報を整理して表示
            embed = discord.Embed(
                title=f"🤖 {Config.BOT_NAME} 情報",
                description=Config.BOT_DESCRIPTION,
                color=0xff9900  # オレンジ色
            )
            
            # 基本情報
            embed.add_field(
                name="📋 基本情報",
                value=f"**バージョン:** `{Config.BOT_VERSION}`\n"
                      f"**プレフィックス:** `{Config.COMMAND_PREFIX}`\n"
                      f"**言語:** Python 3.8+",
                inline=True
            )
            
            # 統計情報
            embed.add_field(
                name="📊 統計",
                value=f"**サーバー数:** {guild_count}\n"
                      f"**ユーザー数:** {user_count}",
                inline=True
            )
            
            # 利用可能なコマンド
            commands_list = [
                f"`{Config.COMMAND_PREFIX}hello` - 挨拶メッセージ",
                f"`{Config.COMMAND_PREFIX}ping` - レスポンス時間測定",
                f"`{Config.COMMAND_PREFIX}info` - ボット情報表示",
                f"`{Config.COMMAND_PREFIX}help` - ヘルプメッセージ"
            ]
            
            embed.add_field(
                name="🛠️ 利用可能なコマンド",
                value="\n".join(commands_list),
                inline=False
            )
            
            # 技術情報
            embed.add_field(
                name="⚙️ 技術情報",
                value=f"**フレームワーク:** discord.py\n"
                      f"**ホスト:** Python Runtime\n"
                      f"**ライセンス:** MIT License",
                inline=False
            )
            
            # ボットのアバターをサムネイルに設定
            if self.bot.user.avatar:
                embed.set_thumbnail(url=self.bot.user.avatar.url)
            
            embed.set_footer(text=f"開発: 初心者向けDiscordボット | {Config.BOT_NAME} v{Config.BOT_VERSION}")
            
            await ctx.send(embed=embed)
        
        @self.bot.command(name='help')
        async def help_command(ctx, command_name: str = None):
            """ヘルプコマンド
            
            利用可能なコマンドとその使用方法を表示します。
            特定のコマンド名を指定すると、詳細なヘルプを表示します。
            
            使用例:
                !help
                !help ping
            
            Args:
                ctx: コマンドコンテキスト
                command_name: 詳細を表示するコマンド名（オプション）
            """
            if command_name:
                # 特定のコマンドのヘルプを表示
                command = self.bot.get_command(command_name)
                if command:
                    embed = discord.Embed(
                        title=f"📖 {Config.COMMAND_PREFIX}{command.name} コマンドヘルプ",
                        description=command.help or "このコマンドの説明はありません。",
                        color=0x9966ff  # 紫色
                    )
                    
                    # 使用方法を追加
                    usage = f"{Config.COMMAND_PREFIX}{command.name}"
                    if command.signature:
                        usage += f" {command.signature}"
                    
                    embed.add_field(
                        name="💡 使用方法",
                        value=f"`{usage}`",
                        inline=False
                    )
                else:
                    embed = discord.Embed(
                        title="❌ エラー",
                        description=f"コマンド `{command_name}` が見つかりません。",
                        color=0xff0000  # 赤色
                    )
            else:
                # 全コマンドのヘルプを表示
                embed = discord.Embed(
                    title=f"📚 {Config.BOT_NAME} ヘルプ",
                    description=f"利用可能なコマンド一覧です。\n詳細は `{Config.COMMAND_PREFIX}help <コマンド名>` で確認できます。",
                    color=0x9966ff  # 紫色
                )
                
                # 基本コマンド
                basic_commands = [
                    f"`{Config.COMMAND_PREFIX}hello [ユーザー名]` - 挨拶メッセージを送信",
                    f"`{Config.COMMAND_PREFIX}ping` - ボットのレスポンス時間を測定",
                    f"`{Config.COMMAND_PREFIX}info` - ボットの詳細情報を表示",
                    f"`{Config.COMMAND_PREFIX}help [コマンド名]` - このヘルプを表示"
                ]
                
                embed.add_field(
                    name="🚀 基本コマンド",
                    value="\n".join(basic_commands),
                    inline=False
                )
                
                # 使用例
                examples = [
                    f"`{Config.COMMAND_PREFIX}hello` - 基本的な挨拶",
                    f"`{Config.COMMAND_PREFIX}hello Alice` - Aliceさんに挨拶",
                    f"`{Config.COMMAND_PREFIX}ping` - レスポンス時間チェック"
                ]
                
                embed.add_field(
                    name="💡 使用例",
                    value="\n".join(examples),
                    inline=False
                )
                
                # サポート情報
                embed.add_field(
                    name="🆘 サポート",
                    value="質問やバグ報告は開発者までお気軽にどうぞ！\n"
                          "このボットは学習目的で作成されています。",
                    inline=False
                )
            
            embed.set_footer(text=f"{Config.BOT_NAME} v{Config.BOT_VERSION}")
            await ctx.send(embed=embed)