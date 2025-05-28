"""
🤖 Pythonで作成する最小構成のDiscordボット

このファイルはメインボットファイルです。
Discord.pyを使用してボットの基本機能を実装しています。

主な機能:
- ボットの起動とログイン
- 基本的なイベントハンドリング
- コマンド処理の基盤
"""

import discord
from discord.ext import commands
import asyncio
import logging
from config import Config
from commands.basic import BasicCommands

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DiscordBot:
    """メインボットクラス
    
    Discordボットの核となる機能を管理するクラスです。
    ボットの起動、コマンド登録、イベント処理などを行います。
    """
    
    def __init__(self):
        """ボットの初期化
        
        Intentsの設定とボットインスタンスの作成を行います。
        """
        # Intentsの設定（メッセージ内容を読み取るために必要）
        intents = discord.Intents.default()
        intents.message_content = True
        
        # ボットインスタンスの作成
        self.bot = commands.Bot(
            command_prefix=Config.COMMAND_PREFIX,
            intents=intents,
            help_command=None  # デフォルトのhelpコマンドを無効化
        )
        
        # イベントとコマンドを登録
        self._register_events()
        self._register_commands()
    
    def _register_events(self):
        """イベントハンドラーの登録
        
        ボットの起動時やメッセージ受信時のイベント処理を設定します。
        """
        
        @self.bot.event
        async def on_ready():
            """ボット起動時の処理
            
            ボットがDiscordに正常に接続された時に実行されます。
            """
            logger.info(f'{self.bot.user} がDiscordにログインしました！')
            logger.info(f'ボットID: {self.bot.user.id}')
            
            # ボットのアクティビティ設定
            activity = discord.Game(name=f"{Config.COMMAND_PREFIX}help でヘルプを表示")
            await self.bot.change_presence(activity=activity)
            
        @self.bot.event
        async def on_command_error(ctx, error):
            """コマンドエラー時の処理
            
            コマンド実行中にエラーが発生した場合の処理を行います。
            
            Args:
                ctx: コマンドコンテキスト
                error: 発生したエラー
            """
            if isinstance(error, commands.CommandNotFound):
                # 存在しないコマンドの場合
                await ctx.send("❌ そのコマンドは存在しません。`!help` でコマンド一覧を確認してください。")
            elif isinstance(error, commands.MissingRequiredArgument):
                # 必須引数が不足している場合
                await ctx.send(f"❌ 必要な引数が不足しています。`{Config.COMMAND_PREFIX}help {ctx.command}` で使い方を確認してください。")
            else:
                # その他のエラー
                logger.error(f"コマンドエラーが発生しました: {error}")
                await ctx.send("❌ コマンドの実行中にエラーが発生しました。")
    
    def _register_commands(self):
        """コマンドの登録
        
        基本コマンドをボットに登録します。
        """
        basic_commands = BasicCommands(self.bot)
        basic_commands.register_commands()
    
    async def start_bot(self):
        """ボットの起動
        
        設定されたトークンを使用してボットをDiscordに接続します。
        """
        try:
            logger.info("ボットを起動しています...")
            await self.bot.start(Config.DISCORD_TOKEN)
        except discord.LoginFailure:
            logger.error("❌ Discordトークンが無効です。.envファイルのDISCORD_TOKENを確認してください。")
        except Exception as e:
            logger.error(f"❌ ボットの起動中にエラーが発生しました: {e}")

async def main():
    """メイン実行関数
    
    ボットインスタンスを作成して起動します。
    """
    discord_bot = DiscordBot()
    await discord_bot.start_bot()

if __name__ == "__main__":
    # ボットの実行
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("ボットが停止されました。")