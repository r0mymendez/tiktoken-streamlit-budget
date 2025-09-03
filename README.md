[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support%20my%20work-FFDD00?style=flat&labelColor=101010&logo=buy-me-a-coffee&logoColor=white)](https://www.buymeacoffee.com/r0mymendez)

---

# 🔤 Tokenization Demo with tiktoken

This project is a simple Streamlit app that demonstrates how text is tokenized using **[tiktoken](https://github.com/openai/tiktoken)**, the official tokenization library developed by **OpenAI**.  

`tiktoken` is used by OpenAI models to split text into tokens — the fundamental units that language models process.  
With this app, you can:  
- Enter any text and see how it is divided into tokens.  
- Visualize tokens with colors for better readability.  
- Check token IDs and bytes.  
- Estimate costs based on a per-token price.  

![img-center](https://github.com/r0mymendez/tiktoken-streamlit-budget/blob/main/demo.png?raw=true)



---

## ⚙️ Installation

Clone the repository and install the dependencies:

```bash
pip install streamlit tiktoken
```
---

## 🚀 Usage

Run the Streamlit app with:
```bash
streamlit run app.py
```


## 📚 About tiktoken

**Tiktoken** is a fast and efficient library created by OpenAI to ensure that tokenization is consistent with their models. It is essential for:
* Counting tokens in prompts and responses.
* Estimating usage costs.
* Validating that text fits within the model’s maximum context length.

For more information, see the official [tiktoken repository](https://github.com/openai/tiktoken?utm_source=chatgpt.com)



