"""
⚙️ 設定管理ファイル

このファイルはボットの設定を一元管理するためのモジュールです。
環境変数からの設定読み込みと、デフォルト値の設定を行います。
"""

import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv()

class Config:
    """設定クラス
    
    ボットの動作に必要な設定値を管理するクラスです。
    環境変数から値を取得し、デフォルト値を提供します。
    """
    
    # Discord関連の設定
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    """Discordボットのトークン
    
    Discord Developer Portalで取得したボットのトークンを設定します。
    セキュリティのため、環境変数から読み込みます。
    """
    
    # ボット動作設定
    COMMAND_PREFIX = os.getenv('COMMAND_PREFIX', '!')
    """コマンドプレフィックス
    
    ボットコマンドの先頭に付ける文字です。
    デフォルトは '!' ですが、環境変数で変更可能です。
    """
    
    # ボット情報
    BOT_NAME = os.getenv('BOT_NAME', 'DiscordBot')
    """ボット名
    
    ボットの表示名です。info コマンドなどで使用されます。
    """
    
    BOT_VERSION = os.getenv('BOT_VERSION', '1.0.0')
    """ボットバージョン
    
    現在のボットのバージョン情報です。
    """
    
    BOT_DESCRIPTION = os.getenv('BOT_DESCRIPTION', 'Pythonで作成された最小構成のDiscordボット')
    """ボットの説明
    
    ボットの機能や目的を説明するテキストです。
    """
    
    @classmethod
    def validate_config(cls):
        """設定値の検証
        
        必須の設定値が正しく設定されているかチェックします。
        
        Returns:
            bool: 設定が有効な場合True、無効な場合False
        """
        if not cls.DISCORD_TOKEN:
            print("❌ エラー: DISCORD_TOKENが設定されていません。")
            print("   .envファイルにDISCORD_TOKEN=your_token_here を追加してください。")
            return False
        
        if len(cls.DISCORD_TOKEN) < 50:
            print("❌ エラー: DISCORD_TOKENが無効な形式です。")
            print("   正しいトークンを設定してください。")
            return False
        
        return True
    
    @classmethod
    def print_config_info(cls):
        """設定情報の表示
        
        現在の設定値を表示します（トークンは除く）。
        デバッグ時に有用です。
        """
        print("📋 現在の設定:")
        print(f"   ボット名: {cls.BOT_NAME}")
        print(f"   バージョン: {cls.BOT_VERSION}")
        print(f"   コマンドプレフィックス: {cls.COMMAND_PREFIX}")
        print(f"   説明: {cls.BOT_DESCRIPTION}")
        
        # トークンは最初の数文字のみ表示（セキュリティのため）
        if cls.DISCORD_TOKEN:
            token_preview = cls.DISCORD_TOKEN[:10] + "..."
            print(f"   トークン: {token_preview}")
        else:
            print("   トークン: 未設定")