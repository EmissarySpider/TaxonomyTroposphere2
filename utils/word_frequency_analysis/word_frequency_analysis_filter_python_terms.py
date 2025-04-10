import re
import argparse
from collections import Counter
from pathlib import Path

def count_word_frequency(file_path, filter_words=None):
    if filter_words is None:
        filter_words = []
    filter_set = set(filter_words)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"Error: File not found -> {file_path}")
        return Counter()

    words = re.findall(r'\b\w+\b', text)
    filtered_words = (
        word for word in words
        if (
            word not in filter_set
            and len(word) >= 3
            and re.search(r'[a-zA-Z0-9]', word)
        )
    )
    return Counter(filtered_words)

def print_summary(counter):
    for word, count in counter.most_common():
        print(f"{word}: {count}")

def save_summary(counter, original_file_path):
    input_path = Path(original_file_path)
    output_filename = f"{input_path.stem}_word_frequency_results.txt"
    output_path = Path.cwd() / output_filename  # Save to current working dir

    with open(output_path, 'w', encoding='utf-8') as output_file:
        for word, count in counter.most_common():
            output_file.write(f"{word}: {count}\n")

    print(f"\nResults saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Count word frequency in a file.')
    parser.add_argument('file_path', help='Path to the target file')
    args = parser.parse_args()


    filter_words = {'self', 'init', '__init__', 'def', 'class', '__main__', '__name__', 'if', 'not', 'return', 'global', 'variable', 'type', 'none', 'from', 'for', 'in', 'while', 'str', 'split', 'splitlines', 'enumerate', 'with', 'try', 'except', 'exception', 'and', 'else', 'elif', 'os', 'system', 'enter', 'center', 'clear', 'open', 'read', 'write', 'lower', 'upper', 'out', 'path', 'input', 'or', 'random', 'choice', 'blue', 'gold', 'green', 'red', 'gray', 'white', 'yellow', 'colors', 'fg_color',
   
    'tk', 'customtkinter', 'grid', 'row', 'column', 'sticky', 'padx', 'pady',
    'width', 'height', 'place', 'relx', 'rely', 'anchor', 'pack',
    'font', 'command', 'state', 'title', 'image', 'value', 'text',
    'insert', 'replace', 'destroy', 'button', 'label', 'entry', 'checkbox',
    'scrollbar', 'text_color', 'text_color_disabled', 'hover_color',
    'corner_radius', 'border_width', 'border_color', 'transparent',
    'topmost', 'columnspan', 'weight',

    'ctkbutton', 'ctklabel', 'ctkcheckbox', 'ctkframe', 'ctkentry',
    'ctktextbox', 'ctkimage', 'ctkscrollableframe', 'ctkswitch', 'tabview',
    
    'grid_columnconfigure', 'grid_rowconfigure', 'grid_forget', 'configure',

    'true', 'false', 'onvalue', 'offvalue', 'disabled', 'default', 'normal',

    'text', 'txt', 'msg', 'usrmsg', 'console', 'consolelog', 'show_error', 'show_info',
    
    'utf', 'encoding', 'len', 'type', 'int', 'str', 'stringvar', 'booleanvar'
}

    word_freq = count_word_frequency(args.file_path, filter_words)

    print_summary(word_freq)
    save_summary(word_freq, args.file_path)

if __name__ == "__main__":
    main()
