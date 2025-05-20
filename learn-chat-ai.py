#!/usr/bin/env python3

import openai
import readline

api_key = input("Enter your OpenAI API key: ")
client = openai.OpenAI(api_key=api_key)

# 会話の履歴管理（ChatGPT APIのmessages形式で）
history = [
    {"role": "system", "content": "あなたは英語学習用AIアシスタントです。"}
]

def ask_ai(prompt, messages=None):
    if messages is None:
        messages = history.copy()
    messages.append({"role": "user", "content": prompt})
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except openai.RateLimitError as e:
        print("⚠️ OpenAI APIの利用上限（無料枠または残高）を超えています。")
        print("OpenAIのUsageページ（https://platform.openai.com/usage）やBillingページで利用状況・課金状況を確認してください。")
        print("APIキーの無料枠が終了した場合は、OpenAIにログインして課金設定を行う必要があります。")
        return None
    except openai.OpenAIError as e:
        print("⚠️ OpenAI APIとの通信中にエラーが発生しました。詳細：", str(e))
        return None

def get_next_prompt():
    # 会話の流れ維持用
    prompt = """英語学習者に対し、英語で簡単な日常英会話で１つだけ質問をしてください。なるべく話の流れを保ち、親しみやすく。
    前回有効な返答がなかった場合や、同じような質問が続く場合には、質問を変えてください。
    ここでは英語教師として振舞わないでください。あくまでもロールプレイで、英語学習者に対して質問をしてください。
    例: What did you eat for breakfast today? など"""
    return ask_ai(prompt, history)

def evaluate_response(user_english):
    # 返答評価 & 言い換え例出力用のプロンプト
    prompt = f"""次の英文を英語教師として評価し、日本語で簡単に添削してください（回答の内容について評価する必要はありません）。
    1行開けて、同じ内容で異なる英語表現を2〜3個例示してください。例文には 1. 2. 3. のように番号を付けてください。
    有効な回答が得られなかった場合は、評価を控える旨のみ簡潔に返答してください。
    学習者の返答: {user_english}"""
    return ask_ai(prompt, history)

# REPL本体
while True:
    # 1. AIが質問
    ai_question = get_next_prompt()
    if ai_question is None:
        print("プログラムを終了します。")
        break
    print("--------")
    print("AI:", ai_question)
    history.append({"role": "assistant", "content": ai_question})

    # 2. ユーザーの返答
    user_input = input("あなた（英語）: ")
    history.append({"role": "user", "content": user_input})

    # 3. AIによる評価 & 言い換え例
    feedback = evaluate_response(user_input)
    if feedback is None:
        print("プログラムを終了します。")
        break
    print("--------")
    print("AIの評価:\n", feedback)

    # 4. 会話継続（historyにたまるので流れが保てる）
    # 途中で終了したい場合などは、breakを入れてもOK
