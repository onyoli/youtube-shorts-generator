from random import choice
# import g4f
# import g4f.client

# Preset content list for AI prompts
contentList = [
    "give me a 30-60 seconds amazing fact on a random topic, make sure to make it interesting",
    "give me a 40-60 seconds script on a real mystifying marvel of engineering, make sure to make it interesting",
]

positiveParameters = "Give a list of 4 keywords to search for short video clips from Pexels. Return plain text in this format: Output: <your output here> Keywords: <comma-separated keywords>"

def getQuoteListFromAI(topic=None):
    '''
    This function generates a list of quotes or facts from the AI.

    Args:
        topic (str): The topic to generate the quotes on. Default is None.

    Returns:
        str: The AI-generated response.
    '''

    if topic is None:
        topic = choice(contentList)

    # Uncomment this if using GPT-based API
    # engine = g4f.client.Client()
    # completion = engine.chat.completions.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": topic + "." + positiveParameters}]
    # )
    # output = completion.choices[0].message.content

    # Placeholder AI output for testing (remove this when using real AI responses)
    output = "Output: The Eiffel Tower is repainted every 7 years to prevent rust. Keywords: Paris, Tower, Engineering, Travel"

    return output


def cleanTextOut(inputText):
    '''
    This function formats the text output from the AI.

    Args:
        inputText (str): The text output from the AI.

    Returns:
        tuple: (output (str), keyword (list)) or (None, None) if an error occurs.
    '''

    inputText = "".join(inputText).strip().replace("*", "").replace("\n", "")

    # Debugging: Print input to check format
    print("DEBUG: Received input ->", inputText)

    # Check if required keywords are in input
    if "Output:" not in inputText or "Keywords:" not in inputText:
        print("\n❌ ERROR: Input format is incorrect! Expected 'Output:' and 'Keywords:'.")
        print("✅ Hint: Make sure your input follows this format:\n")
        print("Example:")
        print("Output: The Eiffel Tower is repainted every 7 years to prevent rust.")
        print("Keywords: Paris, Tower, Engineering, Travel\n")
        return None, None  # Avoid crashing, return default values

    try:
        output = inputText.split("Output:")[1].split("Keywords:")[0].strip()
        keyword = inputText.split("Keywords:")[1].strip().replace('"', '').replace("'", "").split(",")
    except IndexError:
        print("\n❌ ERROR: Could not parse the expected format!")
        return None, None

    return output, keyword
