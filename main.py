# ---------------------------------------------------------
# File: main.py
# Author: Ahtesham Shaikh
# Description: Part of AI Engineer Assignment – Slackbot Content Pipeline
# ---------------------------------------------------------

import os
from slack_bot import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)
