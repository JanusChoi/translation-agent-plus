import PyPDF2
import re
import pdfplumber
import os
import translation_agent as ta

def read_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages[26:27]:
            text += page.extract_text()
    return text

def split_into_chapters(text):
    # 假设章节标题是以大写字母开头的段落
    chapter_titles = re.findall(r'\n[A-Z][^A-Z]*?\n', text)
    chapters = {}
    start_index = 0
    for title in chapter_titles:
        end_index = text.find(title) + len(title)
        chapters[title] = text[start_index:end_index].strip()
        start_index = end_index
    return chapters

def translate_text(source_text):
    translation = ta.translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        model_provider="deepseek",
        country=country,
    )
    return translation

def write_to_txt(chapter_translations, output_file):
    # for title, text in chapter_translations.items():
    with open(output_file, 'a+', encoding='utf-8') as file:
        file.write("\n\n")
        # file.write(text)
        file.write(chapter_translations)

def main(input_pdf, output_file):
    text = read_pdf(input_pdf)
    translation = translate_text(text)
    write_to_txt(translation, output_file)
    # chapters = split_into_chapters(text)
    # for title, text in chapters.items():
    #     chapter_translations = translate_text(text)
        # write_to_txt(chapter_translations, output_file)    
    # chapter_translations = {title: translate_text(text) for title, text in chapters.items()}
    
# 使用示例
source_lang, target_lang, country = "English", "Chinese", "China"
input_pdf = "/Users/januswing/Downloads/somnium.pdf"
output_file = "/Users/januswing/Downloads/somnium.txt"
main(input_pdf, output_file)
