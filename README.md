# 📚 Story World – AI Story & Cover Generator

An interactive **Streamlit web app** that lets you create short stories with **GPT-4o** and (optionally) generate a matching **cover illustration** with **OpenAI Images (DALL·E)**.

---

## ✨ Features

- 🖊️ **Custom Story Generation**  
  Enter a character, topic, location, mood, and choose length/style. GPT-4o creates a full, self-contained story.

- 🎨 **Optional Cover Image**  
  Generate a cinematic illustration for your story using OpenAI’s latest image model.

- 💾 **Download Support**  
  Save your story as a `.txt` file and the cover as a `.png`.

- 🖥️ **Simple UI**  
  Built with [Streamlit](https://streamlit.io/) for fast, shareable apps.

---

## 🚀 Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/story-generator-app.git
cd story-generator-app
```

### 2. Create & activate a virtual environment (optional)
```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

```
# Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set your API key
```
Create .env 

cd story-generator -> .env

Add your OpenAI API key:

OPENAI_API_KEY=sk-xxxx
```

### 5. Run the app
```
streamlit run app.py
```

## ⚠️ Notes & Gotchas

### 🖼️ Image Generation (gpt-image-1 / DALL·E 3)
- Requires your **OpenAI account/organization to be identity verified**.  
- If you see a `403: organization must be verified` error, go to  
  [OpenAI Org Settings → General](https://platform.openai.com/settings/organization/general)  
  and complete verification.

### 💰 API Costs
- Both **GPT-4o** and **DALL·E** are **paid API calls**.  
- Monitor your usage in the [OpenAI dashboard](https://platform.openai.com/).


## 🙌 Acknowledgements

- [OpenAI GPT-4o](https://platform.openai.com/) – for storytelling  
- [OpenAI Images (DALL·E)](https://platform.openai.com/docs/guides/images) – for cover art  
- [Streamlit](https://streamlit.io/) – for the UI  
