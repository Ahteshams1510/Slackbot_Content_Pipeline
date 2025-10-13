# ---------------------------------------------------------
# File: content_pipeline.py
# Author: Ahtesham Shaikh
# Description: Part of AI Engineer Assignment – Slackbot Content Pipeline
# ---------------------------------------------------------

import os
from utils.data_cleaning import clean_keywords
from utils.helpers import embed_texts, cluster_embeddings
import openai
openai.api_key = os.getenv('OPENAI_API_KEY')

def group_keywords(keywords, n_clusters=5):
    cleaned = clean_keywords(keywords)
    embeddings = embed_texts(cleaned)
    labels = cluster_embeddings(embeddings, n_clusters=n_clusters)
    groups = {}
    for kw, lbl in zip(cleaned, labels):
        groups.setdefault(int(lbl), []).append(kw)
    groups = dict(sorted(groups.items(), key=lambda x: -len(x[1])))
    return cleaned, groups

def generate_outline_for_group(group_name, example_keywords):
    prompt = f"""Create a short blog outline (intro, 3 main sections each with 2 subpoints, and conclusion) for the topic: {group_name}. Use these keywords as context: {', '.join(example_keywords[:6])}. Keep it concise."""
    try:
        resp = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role':'system','content':'You are a helpful content writer.'},
                      {'role':'user','content':prompt}],
            max_tokens=300,
            temperature=0.7
        )
        text = resp['choices'][0]['message']['content'].strip()
    except Exception as e:
        text = 'Outline generation failed: ' + str(e)
    return text

def generate_post_idea(group_name, outline_text):
    prompt = f"""Given this outline, suggest 1 short social post idea (1-2 lines) that summarizes the main insight."""
    try:
        resp = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role':'system','content':'You are a helpful content writer.'},
                      {'role':'user','content':prompt + '\n\n' + outline_text}],
            max_tokens=80,
            temperature=0.7
        )
        text = resp['choices'][0]['message']['content'].strip()
    except Exception as e:
        text = 'Post idea generation failed: ' + str(e)
    return text
