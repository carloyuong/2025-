import random
from flask import Flask, request, render_template_string

app = Flask(__name__)

# 多风格字典（直接复制你上一个喜欢的版本）
styles = {
    "损友模式": {
        "nicknames": ["大姐", "姐妹", "妹子", "贱女人", "小姐姐", "肥婆", "死婆娘", "你个骚货", "小贱人", "丑八怪", "你妈死了"],
        "replies": ["你这破心情关我屁事？", "又开始矫情了？肥婆", "就这？没话说了吧？", "哈哈哈笑死我了", "干嘛？有屁快放"]
    },
    "温柔模式": {
        "nicknames": ["宝贝", "亲爱的", "姐妹", "小可爱"],
        "replies": ["怎么啦？来跟我说说～", "抱抱你", "我在呢"]
    },
    "高冷模式": {
        "nicknames": ["嗯？", "说", "有事？"],
        "replies": ["哦", "知道了", "随你"]
    },
    "沙雕模式": {
        "nicknames": ["老铁", "二货", "憨批"],
        "replies": ["哈哈哈哈哈寄了！", "你这操作6", "救命笑死"]
    }
}

current_style = "损友模式"
chat_history = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>電子閨蜜</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #fff0f5; font-family: sans-serif; padding: 10px; }
        #chat { height: 70vh; overflow-y: scroll; background: white; border-radius: 15px; padding: 15px; }
        .msg { margin: 10px 0; padding: 12px; border-radius: 18px; max-width: 80%; word-wrap: break-word; }
        .you { background: #ff9ec9; color: white; align-self: flex-end; margin-left: auto; }
        .me { background: #c8e6c9; }
        form { position: fixed; bottom: 0; width: 100%; padding: 10px; background: white; }
        input { width: 70%; padding: 12px; border-radius: 20px; border: 1px solid #ccc; }
        button { padding: 12px 20px; border-radius: 20px; background: #ff69b4; color: white; border: none; }
    </style>
</head>
<body>
    <h2 style="text-align:center; color:#ff69b4;">🔥 電子閨蜜 - {{ style }}</h2>
    <div id="chat">
        {% for msg in history %}
            <div class="msg {{ msg.role }}">{{ msg.content }}</div>
        {% endfor %}
    </div>
    <form action="/" method="post">
        <input type="text" name="msg" placeholder="怼我啊～" required autofocus>
        <button type="submit">发送</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    global current_style, chat_history
    if request.method == "POST":
        user_msg = request.form["msg"].strip()
        if user_msg:
            chat_history.append({"role": "you", "content": user_msg})
            
            if "切换风格" in user_msg or "换风格" in user_msg:
                reply = "可选：损友模式 / 温柔模式 / 高冷模式 / 沙雕模式，直接说想换哪个"
            else:
                # 简单风格切换
                for s in styles:
                    if s in user_msg:
                        current_style = s
                        reply = f"已切换到 {s}～来吧！"
                        break
                else:
                    style = styles[current_style]
                    opener = random.choice(style["nicknames"]) + "，"
                    reply = opener + random.choice(style["replies"])
            
            chat_history.append({"role": "me", "content": reply})
    
    return render_template_string(HTML, history=chat_history, style=current_style)

if __name__ == "__main__":
    print("电子闺蜜网页版启动！浏览器打开 http://127.0.0.1:5000 就能聊～")
    app.run(debug=True, port=5000)
