import os

import translation_agent as ta


if __name__ == "__main__":
    source_lang, target_lang, country = "English", "Chinese", "China"

    # relative_path = "sample-texts/sample-short1.txt"
    relative_path = "sample-texts/sample-long1.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))

    full_path = os.path.join(script_dir, relative_path)

    with open(full_path, encoding="utf-8") as file:
        source_text = file.read()

    print(f"Source text:\n\n{source_text}\n------------\n")

    translation = ta.translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        model_provider="deepseek",
        # model_provider="llama3",
        country=country,
    )

    print(f"Translation:\n\n{translation}")
