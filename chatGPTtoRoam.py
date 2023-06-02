import json

# Assign user name variable here
user_name = "Lisa Ross"

with open("conversations.json", "r") as read_file:
    data = json.load(read_file)

roam_pages = []

for conversation in data:
    roam_blocks = []
    block_map = {}  # To hold parent-child relationships

    for current_node, node_details in conversation['mapping'].items():
        message = node_details.get('message')

        if message:
            author_role = message['author']['role']

            if author_role in ['user', 'assistant', 'system']:
                if 'parts' in message['content']:
                    content_parts = message['content']['parts']

                    # Create Roam block
                    block_string = ""
                    for part in content_parts:
                        block_string += part

                    block_prefix = f"[[{user_name}]]: " if author_role == 'user' else "[[ChatGPT]]: "
                    block_string = block_prefix + block_string

                    block_map[current_node] = {"string": block_string, "uid": current_node, "children": []}

    # Attach blocks to their parents
    for node_id, node_details in block_map.items():
        parent_id = node_details.get('parent')
        if parent_id and parent_id in block_map:
            block_map[parent_id]['children'].append(block_map[node_id])

    # Filter out only top level blocks
    top_level_blocks = [block for block_id, block in block_map.items() if not node_details.get('parent')]

    # Add link to the conversation in the first block
    if top_level_blocks:
        conversation_link = f"[{conversation['title']} Link](https://chat.openai.com/c/{conversation['id']})"
        top_level_blocks[0]['string'] += "\n" + conversation_link

    # Add this conversation to the Roam pages
    if top_level_blocks:
        roam_page = {"title": conversation['title'], "children": top_level_blocks}
        roam_pages.append(roam_page)

with open('roamimport.json', 'w') as outfile:
    json.dump(roam_pages, outfile)

print("File processed successfully. The output was saved as roamimport.json")
