#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv

def main():
    """Run administrative tasks."""

    if os.path.exists("../.env"):
        dotenv.read_dotenv("../.env") #在根目录放一个.env文件，里面是settings中需要用到的不应该公开的参数

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forum.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
