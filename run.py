import os
from pylib import ask_gpt3
from pylib import ocr_image

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))

    source_directory = os.path.join(base_dir, "Corpus", "Notice-of-Sale-21CV47908", "Source")
    output_directory = os.path.join(base_dir, "Corpus", "Notice-of-Sale-21CV47908", "Text")
    
    ocr_image.process_files_for_ocr(source_directory, output_directory)
