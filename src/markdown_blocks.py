from htmlnode import *
from textnode import *
from inline_markdown import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown):
    unformatted = markdown.split("\n\n")
    formatted = []
    for block in unformatted:
        if block == "":
            continue
        block = block.strip()
        formatted.append(block)

    return formatted

def block_to_blocktype(markdown):
    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE
    if markdown.startswith((">", "> ")):
        return BlockType.QUOTE
    splitsies = markdown.splitlines()
    is_ordered, is_unordered = True, True
    for i in range(1, len(splitsies) + 1):
        line = splitsies[i - 1]
        if not line.startswith("- "):
            is_unordered = False
        if not line.startswith(f"{i}. "):
            is_ordered = False
    if is_unordered:
        return BlockType.UNORDERED_LIST
    if is_ordered:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

# def get_block_tag(text_node):
#     if not isinstance(text_node, TextNode):
#         raise Exception("Error: TextNode expected")

#     if text_node.text_type == BlockType.QUOTE:
#         node = LeafNode("blockquote", text_node.text)

    # elif text_node.text_type == BlockType.PARAGRAPH:
    #     node = LeafNode("p", text_node.text)

    # elif text_node.text_type == BlockType.HEADING:
    #     hash = "#"
    #     count = 1
    #     while text_node.text.startswith(hash):
    #         hash += "#"
    #         count += 1
    #     node = LeafNode(f"h{count}", text_node.text)

    # elif text_node.text_type == BlockType.QUOTE:
    #     node = LeafNode("a", text_node.text, {"href": text_node.url})

    # elif text_node.text_type == BlockType.QUOTE:
    #     node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text} )


    # else:
    #     raise Exception("TextType not valid")

    # return tag


def text_to_children(string):
    node_list = text_to_textnodes(string)
    child_list = []
    for node in node_list:
        child_list.append(text_node_to_html_node(node))
    return child_list



def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)

    root_children = []

    for block in block_list:
        block_type = block_to_blocktype(block)


        if block_type == BlockType.PARAGRAPH:
            normalized = block.replace("\n", " ")
            children = text_to_children(normalized)
            node = ParentNode("p", children)
            root_children.append(node)

        elif block_type == BlockType.CODE:

            lines = block.split("\n")

            inner_lines = []
            for line in lines:
                # drop lines that are only ``` (with or without spaces)
                if line.strip() == "```":
                    continue
                inner_lines.append(line)

            code_text = "\n".join(inner_lines)

            if not code_text.endswith("\n"):
                code_text += "\n"
            code_node = LeafNode("code", code_text)
            pre_node = ParentNode("pre", [code_node])
            root_children.append(pre_node)

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = []
            for line in lines:
                if line.startswith("> "):
                    cleaned_lines.append(line[2:])  # remove "> "
                elif line.startswith(">"):
                    cleaned_lines.append(line[1:])  # remove ">"
                else:
                    cleaned_lines.append(line)

            # Join like a paragraph: spaces instead of newlines
            cleaned = " ".join(cleaned_lines)

            children = text_to_children(cleaned)
            node = ParentNode("blockquote", children)
            root_children.append(node)

        elif block_type == BlockType.HEADING:
            count = 0
            for ch in block:
                if ch == "#":
                    count += 1
                else:
                    break
            htag = f"h{count}"
            cleaned = block[count + 1:]
            children = text_to_children(cleaned)
            node = ParentNode(htag, children)
            root_children.append(node)
        
        elif block_type == BlockType.UNORDERED_LIST:
            splitsies = block.split("\n")
            li_nodes = []
            for line in splitsies:
                if not line.strip():
                    continue
                item_text = line[2:]
                children = text_to_children(item_text)
                li_node = ParentNode("li", children)
                li_nodes.append(li_node)
            ul_node = ParentNode("ul", li_nodes)
            root_children.append(ul_node)

        elif block_type == BlockType.ORDERED_LIST:
            splitsies = block.split("\n")
            li_nodes = []
            for line in splitsies:
                if not line.strip():
                    continue
                dot_index = line.find(". ")
                item_text = line[dot_index + 2 :] 
                children = text_to_children(item_text)

                li_node = ParentNode("li", children)
                li_nodes.append(li_node)

            ol_node = ParentNode("ol", li_nodes)
            root_children.append(ol_node)


    root = ParentNode("div", root_children)
    return root



























# def testytest(block_list):
#     print("Testing now...")
    
#     for item in block_list:
#         expected = item[0]
#         block = item[1]
#         print(f"Expected: {expected}")
#         print(f"Type: {block_to_blocktype(block)}")

#     print("Done")

# testers = [
#     ("heading", "### this is a heading"),
#     ("paragraph", "Nothing special here"),
#     ("unordered list", "- a line \n- and another line \n- and another line"),
#     ("code", "```\n Some code or something ```"),
#     ("quote", "> 'To be or not to be'"),
#     ("ordered list", "1. First thing's first \n2. Second is second \n3. And then a third")
# ]

# testytest(testers)