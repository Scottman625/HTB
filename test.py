# 令牌生成模式分析
import re
observed_tokens = ["SbNwK9sFRtDQSIW7LlnALZHxeQAUfqz7", "5QvVk6Nx3yIiUGOy3IfhyooJTRzMxD0t"]
pattern = r'^[A-Za-z0-9]{32}$'  # 32位隨機字符模式
if all(re.match(pattern, t) for t in observed_tokens):
    print("CSRF令牌為高強度隨機值")
else:
    print("可能存在令牌預測漏洞")
