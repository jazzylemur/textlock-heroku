#!/usr/bin/env python
import os
import sys
import imp

APPS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'root', 'apps'))
if APPS_DIR not in sys.path:
    sys.path.insert(0, APPS_DIR)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ancient-ravine-5775.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
