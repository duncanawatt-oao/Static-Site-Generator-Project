def extract_title(markdown):
    lines = markdown.splitlines()
    header = ""
    for line in lines:
        if line.startswith("#")  and not line.startswith("##"):
            header = line[1:].strip()
            break
    if header == "":
        raise Exception("Error: no title found")
    return header

# md_one = """This is not a header
# nor is this
# But someday
# # aha maybe this is a header
# ## but this shouldn't be
# and more lines"""

# md_two = """#   A header here   
# and some more text
# # that shouldn't get 
# # picked up"""

# def test_extract_title(md_one, md_two):
#     print("testing...")
#     print(extract_title(md_one))
#     print(extract_title(md_two))
#     print("Should see two headers")


# test_extract_title(md_one, md_two)