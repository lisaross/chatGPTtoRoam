import json

# Assign user name variable here
user_name = "Lisa Ross"

with open("conversations.json", "r") as read_file:
    data = json.load(read_file)

roam_pages = []

for conversation in data:
    block_map = {}  # To hold blocks with their content and relationships

    # Process each node in the mapping
    for node_id, node_details in conversation['mapping'].items():
        message = node_details.get('message')
        parent_id = node_details.get('parent')
        children_ids = node_details.get('children', [])

        # Initialize block content
        block_content = ""

        # Check if the message exists and has parts
        if message and 'content' in message and 'parts' in message['content']:
            author_role = message['author']['role']
            content_parts = message['content']['parts']

            # Determine the prefix based on the author's role
            block_prefix = f"[[{user_name}]]: " if author_role == 'user' else "[[ChatGPT]]: "

            # Concatenate all parts of the message
            for part in content_parts:
                if isinstance(part, dict) and 'text' in part:
                    block_content += part['text']
                elif isinstance(part, str):
                    block_content += part

            # Prepend the author prefix if there's content to add
            if block_content:
                block_content = block_prefix + block_content

        # Add the block to the map if there's content
        if block_content:
            block_map[node_id] = {
                "string": block_content,
                "uid": node_id,
                "children": [],
                "parent": parent_id
            }

    # Build the parent-child relationships
    for node_id, block in block_map.items():
        if block['parent'] in block_map:
            block_map[block['parent']]['children'].append(block)

    # Extract top-level blocks (those without a parent or whose parent isn't in block_map)
    top_level_blocks = [block for node_id, block in block_map.items() if not block['parent'] or block['parent'] not in block_map]

    # Construct the Roam page for this conversation
    if top_level_blocks:
        conversation_link = f"[{conversation['title']} Link](https://chat.openai.com/c/{conversation['id']})"
        roam_page = {
            "title": conversation['title'],
            "children": top_level_blocks
        }
        # Optionally, add the conversation link to the first block or as a separate block
        roam_page['children'][0]['string'] += "\n" + conversation_link
        roam_pages.append(roam_page)

# Write the output to a file
with open('roamimport.json', 'w') as outfile:
    json.dump(roam_pages, outfile, indent=4)

print("File processed successfully. The output was saved as roamimport.json")
