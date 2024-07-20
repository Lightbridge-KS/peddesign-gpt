def read_markdown_file(file_path):
    from pathlib import Path
    file_path = Path(file_path)
    try:
        # Open the markdown file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire file content into a string
            markdown_content = file.read()
            return markdown_content
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")