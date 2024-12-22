![GPT-Neo Demo](./images/Mika.jpg)
# Misono Mika GPT-Neo with transformer BOT

This bot will act as a discord bot assistant that can have conversation and manage your server. Also, 
this project demonstrates how to use **GPT-Neo** (via Hugging Face's `transformers` library) to generate text responses using a conversational model.

---

## Prerequisites

To run this project, ensure you have the following installed on your system:

- **Python 3.8 or higher**
- **pip** (Python package installer)

Optional (for GPU support for faster processing):
- **CUDA**-enabled GPU drivers (if using PyTorch with GPU).

---

## Installation

Follow these steps to set up the project:

### 1. Clone this Repository

First, clone the repository to your local system (if applicable):

```bash
git clone https://github.com/pandoradox214/MikaGPT.git
cd MikaGPT
```

### 2. Create a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment to isolate dependencies:

**For Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies

Run the following command to install the required Python libraries:

```bash
pip install torch transformers discord.py
```

- **`torch`**: PyTorch library for loading and running models.
- **`transformers`**: Hugging Face's library for working with pre-trained models like `GPT-Neo`.
- **`discord.py`**: Library for interacting with the Discord API.

#### GPU Version of PyTorch (Optional for Faster Performance)
If you have a CUDA-enabled GPU and wish to run the model on it, install the GPU-accelerated version of PyTorch. Visit the [PyTorch installation page](https://pytorch.org/get-started/locally/) and use the proper installation command for your setup, or try the following:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

This will ensure that the model takes advantage of the GPU's computational power. If running on a CPU, no additional steps are required.

## Usage

1. Open the `main.py` (or whatever the name of the file is where the script resides).
2. Start the script in your terminal:
   ```bash
   python main.py
   ```
3. Follow the prompts to input your text and receive a response.

---

## Project Structure

- **`main.py`**: The main Python script containing the logic to load the GPT-Neo model, process user input, and generate responses.
- **`.gitignore`**: Ensures sensitive files (like `.env`) and unnecessary files (e.g., virtual environment folder) are not committed to Git.

---

## Notes

- The project uses the `transformers` library by Hugging Face to interface with the `EleutherAI/gpt-neo-1.3B` model.
- For better performance, make sure to load the model on a GPU if available.

---

## Troubleshooting

1. **ModuleNotFoundError**:
   - If you see an error like `ModuleNotFoundError: No module named 'transformers'`, ensure you’ve installed the required libraries by running:
     ```bash
     pip install transformers torch
     ```
   
2. **Slow Performance**:
   - If the model responds slowly, consider switching to a smaller model like `EleutherAI/gpt-neo-125M`. Simply replace the model name:
     ```python
     model_name = "EleutherAI/gpt-neo-125M"
     ```

3. **GPU Not Being Used**:
   - If you have a GPU but the model is still running on a CPU, ensure you installed the GPU-enabled version of PyTorch and confirm CUDA is available in Python:
     ```python
     import torch
     print(torch.cuda.is_available())  # Should return True if GPU is available
     ```

---