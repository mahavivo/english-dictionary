import re

def clean_phx_block(match):
    """回调函数，清理 <phx> 块中 <pos> 标签内的内容。"""
    phx_content = match.group(0)
    cleaned_content = re.sub(r'<pos>.*</pos>', '', phx_content)
    return cleaned_content

def process_entry_content(content):
    """处理单个词条的HTML内容，移除不需要的部分并格式化。"""
    #  移除脚本和链接标签
    content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<link[^>]+>', '', content)

    # 使用回调函数，清理 <phx> 块中多余的词性信息
    content = re.sub(r'<phx>.*?</phx>', clean_phx_block, content, flags=re.DOTALL)
    
    # 仅移除第一个出现的主词头块
    content = re.sub(r'<hwd>.*?</hwd>', '', content, count=1, flags=re.DOTALL)
    content = re.sub(r'^\s*<rw><phr><pd>.*?</pd>', '', content, count=1, flags=re.DOTALL)

    # 移除例句、用法说明和词源
    content = re.sub(r'<ex>.*?</ex>', '', content, flags=re.DOTALL)
    content = re.sub(r'<uge>.*?</uge>', '', content, flags=re.DOTALL)
    content = re.sub(r'<ori>.*?</ori>', '', content, flags=re.DOTALL)

    # 移除英文释义
    content = re.sub(r'<en>.*?</en>', '', content, flags=re.DOTALL)
    
    # 在音标后添加 ※ 标记
    content = re.sub(r'</pho>', '</pho> ※', content)

    # 为衍生词添加 ► 标记
    content = re.sub(r'<phr>', '►', content)

    # 格式化主序号
    content = re.sub(r'<sqn>(\d+)</sqn>', r'\1.', content)
    
    # 格式化子序号
    content = re.sub(r'<sqa>([a-zA-Z])</sqa>', r'\1.', content)
    
    # 将剩余HTML标签替换为空格
    text = re.sub(r'<.*?>', ' ', content)
    
    # 清理空白字符
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s+([.,):;!?])', r'\1', text)
    text = re.sub(r'([)\]}])([a-zA-Z\d])', r'\1 \2', text)
    
    return text.strip()

def parse_dictionary_file(input_file_path, output_file_path):
    """解析整个词典文件，提取所需文本并格式化为单行输出。"""
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            full_content = f.read()
    except FileNotFoundError:
        print(f"错误：找不到文件 '{input_file_path}'")
        print("请确保文件名正确，并且该文件与Python脚本在同一个文件夹下。")
        return

    entries = full_content.strip().split('</>')
    
    processed_lines = []

    for entry in entries:
        if not entry.strip():
            continue
            
        lines = entry.strip().split('\n', 1)
        headword = lines[0].strip()
        
        if len(lines) == 1:
            processed_lines.append(headword)
            continue

        content = lines[1].strip()

        # 如果释义内容包含 @@@LINK=,或者 See main entry at 则跳过整个词条
        if '@@@LINK=' in content:
            continue
        if 'See main entry at' in content:
            continue
        
        full_html_content = f"<rw>{content}"
        cleaned_text = process_entry_content(full_html_content)
        
        if cleaned_text:
            processed_lines.append(f"{headword} ⇒ {cleaned_text}")

    output_content = "\n".join(processed_lines)
    
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(output_content)
    print(f"处理完成！结果已保存到 '{output_file_path}'。")


# --- 主程序入口 ---
if __name__ == "__main__":
	
    # --- 配置 ---
    input_filename = 'COD9-EC.txt'      # <-- 源文件名（底本：牛津现代英汉双解词典（第9版）双解切换 2022-10-18）
    output_filename = 'output.txt' # <-- 希望保存结果的文件名

    # --- 执行处理 ---
    print(f"开始处理文件: '{input_filename}'...")
    parse_dictionary_file(input_filename, output_filename)