import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Habilita o logging para vermos o que acontece
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia uma mensagem de boas-vindas quando o comando /start é emitido."""
    user = update.effective_user
    await update.message.reply_text(f"Olá, {user.first_name}! Eu sou seu bot educacional. Como posso ajudar?")

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia uma mensagem de ajuda."""
    await update.message.reply_text("Comandos disponíveis:\n/start - Inicia o bot\n/ajuda - Mostra esta mensagem")

def main() -> None:
    """Inicia o bot."""
    # O token é lido de uma variável de ambiente por segurança
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise ValueError("A variável de ambiente BOT_TOKEN não foi definida.")

    application = Application.builder().token(token).build()

    # Adiciona os "handlers" para os comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ajuda", ajuda))

    # Inicia o bot (polling)
    application.run_polling()

if __name__ == "__main__":
    main()
