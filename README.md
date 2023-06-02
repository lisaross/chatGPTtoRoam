# ChatGPT to Roam Importer

This script is designed to convert your chat history from [OpenAI's ChatGPT](https://openai.com/research/chatgpt) into a format that can be easily imported into [Roam Research](https://roamresearch.com/). It's perfect for those who want to keep a copy of their ChatGPT conversations in their personal knowledge management system.

## How to Use

1. Export your ChatGPT history following the instructions provided in this [OpenAI Help Article](https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data). You'll receive a JSON file that contains your conversations with ChatGPT.

2. Save your JSON file in the same directory as this script.

3. Edit the script to set the `user_name` variable to your name. This will be used to identify your responses in the conversation.

4. Run the script using a Python interpreter. Ensure that you have the necessary permissions to read and write files in the directory where the script is located.

```python
python chatgpt_to_roam.py
```

5. If the script runs successfully, it will generate a new file named `roamimport.json`. This file contains your ChatGPT conversations formatted for Roam Research import.

6. Import the `roamimport.json` file into Roam Research. Please follow the official Roam Research documentation on how to import files into your database.

![Import Screenshot Placeholder](./import_screenshot.png)

7. After importing, you will see each of your conversations as a separate page, with the questions and responses formatted as nested bullet points.

![Conversation Screenshot Placeholder](./conversation_screenshot.png)

## Note

The conversation link in Roam Research will take you back to the original conversation on the ChatGPT platform. You can use this link to continue the conversation in ChatGPT.

![Conversation Screenshot Placeholder](./conversation_screenshot.png)

## 🚨 Important Note 🚨

Before using this script, I strongly recommend the following precautions to protect your data:

1. **Backup your data**: Always have a recent backup of your data. This ensures that you can restore your information if something goes wrong.

2. **Test in a safe environment**: Before applying any conversion or import script on your main database or graph, test the process with a small subset of your data or in an empty Roam graph. This will allow you to verify the results without affecting your main data.

3. **Disclaimer**: This script is provided as is, and you use it at your own risk. I'm not responsible for any data loss or damage that may be caused by the use of this script. Please understand the script and the changes it will make before running it.

