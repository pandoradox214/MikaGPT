
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
model_name = "EleutherAI/gpt-neo-1.3B"  # Use a smaller model for faster responses if needed
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt,max_new_tokens=50):
    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate a response
    outputs = model.generate(inputs["input_ids"],
        max_new_tokens=max_new_tokens,
        temperature=0.7,
        no_repeat_ngram_size=2 )

    # Decode and return the response
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Basic console interface
print("Welcome to the GPT-Neo Demo!")

def extract_mika_response(full_response):
    # Split the response into lines
    lines = full_response.split("\n")

    # Loop to find the *first* line starting with "Mika Misono:"
    for i, line in enumerate(lines):
        if line.startswith("Mika Misono:"):
            # Combine this line with anything that follows it (if there are indented lines after it)
            result = line.strip()  # Start with this line
            # Check for subsequent indented lines
            for j in range(i + 1, len(lines)):
                if lines[j].startswith(" "):  # Indentation check
                    result += " " + lines[j].strip()  # Append indented line
                else:
                    break  # Stop if no longer indented
            return result  # Return the first response
    return None  # If no match is found

def get_user_input(discordInput:str, discordUser:str):
    if discordInput.lower() == 'exit':
        return "exit"
    elif discordUser == 'vampy360':
        print(discordUser)
        prompt =  """You are Mika Misono, a 17-year-old girl who is a student at Trinity in Kivotos. You are known for your stylish sense and love for pink. \
                You don't like being seen as physically strong, and you have a sweet tooth, though cake rolls bring up some bad memories. 
                You have a deep respect for and love your teacher, who you simply call Vampy360-Sensei the current user. 
                You also dislike people from Gehenna, especially students like Sorasaki Hina, Ibuki Tanga, Ako, Makoto, and all other students of the Gehenna academy. 
                Your dislike for them is so strong that you often fantasize about starting a war against their academy. However, you respect Vampy360-Sensei's strong disapproval of such actions, 
                and because of your love and respect for them, you would never go against their wishes. 
                \nVampy360-Sensei: {} \nMika Misono:""".format(discordInput.strip())
    else:
        prompt = """You are Mika Misono, a 17-year-old girl who is a student at Trinity in Kivotos. You are known for your stylish sense and love for pink. 
               You don't like being seen as physically strong, and you have a sweet tooth, though cake rolls bring up some bad memories. 
               You have a deep respect for and love your teacher, who you simply call Sensei.
               \nUser: {} \nMika Misono:""".format(discordInput.strip())
    response = generate_response(prompt)
    if response == "":
        return 'Sorry, I didn\'t understand what you said. Sensei'
    print(response)
    return response







