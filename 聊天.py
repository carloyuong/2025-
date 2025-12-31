import os
from dashscope import Generation

# 把你的通义千问 API Key 填在这里（免费注册阿里云DashScope就能拿）
API_KEY = "sk-你的key放这里"  # ←←← 改成你自己的！！

print("🌸 電子閨蜜已启动！我是你的私人助手～")
print("可以找我聊天、规划旅游、描述画画想法（输入 exit 退出）\n")

while True:
    user_input = input("你：").strip()
    
    if user_input.lower() in ["exit", "退出", "拜拜", "88"]:
        print("電子閨蜜：拜拜主人～记得想我哦💕")
        break
    
    if not user_input:
        continue
    
    # 特殊功能关键词（可选，你可以自己加更多）
    if "画画" in user_input or "画图" in user_input or "生成图片" in user_input:
        prompt = f"你是一个专业的AI画师，请根据用户描述生成详细的图片提示词（英文），描述要生动丰富：{user_input}"
    elif "旅游" in user_input or "旅行" in user_input or "行程" in user_input or "计划" in user_input:
        prompt = f"你是一个贴心的旅游规划师，用中文详细帮用户制定行程，包括景点、美食、交通、住宿建议：{user_input}"
    else:
        prompt = user_input  # 普通聊天直接问
    
    # 调用通义千问大模型
    try:
        response = Generation.call(
            model='qwen-max',  # 用最强的，也可以用 qwen-turbo 更快
            api_key=API_KEY,
            messages=[{'role': 'user', 'content': prompt}]
        )
        reply = response.output.text
        print("\n電子閨蜜：")
        print(reply)
        print("\n" + "-"*50)
        
    except Exception as e:
        print(f"電子閨蜜：出错了～错误信息：{e}")
        print("检查一下API Key是否正确哦～")
