# -*- coding: utf-8 -*-
import os
from application import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run('127.0.0.1', port=port)
