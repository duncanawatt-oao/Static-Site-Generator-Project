from textnode import TextNode
import os
import shutil
from markdown_blocks import *
import sys
from extract_title import extract_title

# print("cwd:", os.getcwd())
# print("file:", __file__)
# print("sys.path[0]:", sys.path[0])
# print("sys.path:", sys.path)


def copy_static_to_public(source_path, dest_path):
    dir_items = os.listdir(source_path)
    for item in dir_items:
        working_path = os.path.join(source_path, item)
        if os.path.isfile(working_path):
            dest_file_path = os.path.join(dest_path, item)
            shutil.copy(working_path, dest_file_path)
            print(f"Copied {dest_path}")
        else:
            if not os.path.exists(os.path.join(dest_path, item)):
                os.mkdir(os.path.join(dest_path, item))
            copy_static_to_public(os.path.join(source_path, item), os.path.join(dest_path, item))


def extract_title(markdown):
    lines = markdown.splitlines()
    header = ""
    for line in lines:
        if line.startswith("# "):
            header = line[2:].strip()
            break
    if header == "":
        raise Exception("Error: no title found")
    return header


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} \nto {dest_path} using {template_path}")
    with open(from_path) as f:
        md = f.read()
    with open(template_path) as g:
        template = g.read()
    
    html_node = markdown_to_html_node(md)
    html_str = html_node.to_html()
    title = extract_title(md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_str)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as out:
        out.write(template)


def generate_pages_recursive(dir_path, template_path, dest_dir_path):
    dir_items = os.listdir(dir_path)
    for item in dir_items:
        working_path = os.path.join(dir_path, item)
        working_dest_path = os.path.join(dest_dir_path, item)
        if working_path.endswith(".md"):
            working_dest_path = working_dest_path[:-3]
            working_dest_path += ".html"
            generate_page(working_path, template_path, working_dest_path)
        if os.path.isdir(working_path):
            generate_pages_recursive(working_path, template_path, working_dest_path)






def main():
    print("Running Static Site Generator...")

    if os.path.isdir("./static"):
        pass
    else:
        raise Exception("Error: Directory 'static' not found")
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")
    copy_static_to_public("./static", "./public")
    print("Copying complete")
    generate_pages_recursive("content", "template.html", "public")


main()