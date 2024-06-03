import argparse


def gen_command(name: str) -> None:

    imports = ["from config import BOT\n", "from utils import LOG\n", "from telebot.types import Message\n"]

    decorator = f"\n\n@BOT.message_handler(commands=['{name}'])\n"

    func = f"""def get_{name}(message: Message) -> None:
    LOG.debug("🛞 Run: {name}")
    BOT.reply_to(message, "Edite seu comando!")
"""

    with open(f"app/commands/{name}.py", "w") as f:
        f.writelines(imports)
        f.writelines(decorator)
        f.writelines(func)

    with open("app/commands/__init__.py", "a") as constructor:
        constructor.write(f"from commands.{name} import get_{name}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str, help="nome do arquivo de comando que deseja criar.")

    args = parser.parse_args()
    gen_command(args.name)
