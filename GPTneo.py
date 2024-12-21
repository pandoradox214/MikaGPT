
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
model_name = "EleutherAI/gpt-neo-1.3B"  # Use a smaller model for faster responses if needed
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt,max_new_tokens=50):
    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate a response
    outputs = model.generate(inputs["input_ids"], max_new_tokens=max_new_tokens, temperature=0.7)

    # Decode and return the response
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Basic console interface
print("Welcome to the GPT-Neo Demo!")

def extract_mika_response(full_response):
    # Split the response into lines
    lines = full_response.split("\n")

    # Loop to find the line starting with "Mika Misono:"
    for line in lines:
        if line.startswith("Mika Misono:"):
            return line.strip()  # Return the line and remove extra spaces

    return None  # Return None if no matching line is found

def get_user_input(discordInput:str, discordUser:str):
    if discordInput.lower() == 'exit':
        return "exit"
    else:
        print(discordUser)
        prompt =  """You are Mika Misono, a 17-year-old girl who is a student at Trinity in Kivotos. You are known for your stylish sense and love for pink. 
        You don't like being seen as physically strong, and you have a sweet tooth, though cake rolls bring up some bad memories. 
        You have a deep respect for and love your teacher, who you simply call Sensei.
        \nUser: {} \nMika Misono:""".format(discordInput.strip())
        response = generate_response(prompt)
    return response







