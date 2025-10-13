# ---------------------------------------------------------
# File: main.py
# Author: Ahtesham Shaikh
# Description: Part of AI Engineer Assignment – Slackbot Content Pipeline
# ---------------------------------------------------------

from slack_bot import app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
