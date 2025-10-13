# ---------------------------------------------------------
# File: Slack_bot.py
# Author: Ahtesham Shaikh
# Description: Part of AI Engineer Assignment – Slackbot Content Pipeline
# ---------------------------------------------------------

import os
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request
from content_pipeline import group_keywords, generate_outline_for_group, generate_post_idea
from pdf_generator import build_pdf_report
from utils.data_cleaning import clean_keywords

app = Flask(__name__)
SLACK_BOT_TOKEN = "fake-token"
SLACK_SIGNING_SECRET = "fake-secret"

bolt_app = App(
    token="dummy-token",
    signing_secret="dummy-secret",
    token_verification_enabled=False
)

@bolt_app.command('/generate')
def handle_generate(ack, respond, command):
    ack('Processing your request...')
    text = command.get('text','').strip()
    if not text:
        respond('Please provide keywords or upload a CSV file with keywords.')
        return
    keywords = [k.strip() for k in text.split(',') if k.strip()]
    cleaned, groups = group_keywords(keywords, n_clusters=5)
    outlines = {}
    ideas = {}
    for gid, kws in groups.items():
        outlines[gid] = generate_outline_for_group(' / '.join(kws[:3]), kws)
        ideas[gid] = generate_post_idea(' / '.join(kws[:3]), outlines[gid])
    report_path = build_pdf_report(cleaned, groups, outlines, ideas, output_path='report.pdf')
    client = bolt_app.client
    channel_id = command.get('channel_id')
    client.files_upload(channels=channel_id, file=report_path, title='Content Research Report')
    respond('Report generated and uploaded.')
    return

handler = SlackRequestHandler(bolt_app)

from flask import jsonify

from content_generator import generate_report
from flask import send_file

@app.route('/slack/events', methods=['POST'])
def slack_events():
    # Print request data for debugging
    print("Incoming request received!")
    print(request.get_json())

    # Simulate Slack event handling locally
    data = request.get_json()

    if data and "event" in data:
        user_message = data["event"].get("text", "")
        if "report" in user_message.lower():
            # extract a short topic string (you can improve parsing later)
            topic_text = user_message
            pdf_path = generate_report(topic_text)
            print("Generated PDF:", pdf_path)
            # Optionally return path in JSON so test script can find it
            return jsonify({"message": "Report generated successfully", "pdf": pdf_path}), 200

    return jsonify({"error": "invalid request"}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
