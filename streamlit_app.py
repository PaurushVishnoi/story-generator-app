import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_message = ("You are a wonderful and an award winning story teller."
                  "You use simple English as a narrative language."
                  "Your endings are always emotionally satisfying."
                  "You keep the story self‑contained."
                  )


st.set_page_config(page_title="Story World", page_icon="📚", layout="wide")
st.title("📚 Create Stories in your way ...")
st.caption("GPT‑4o for text, OpenAI Images for a matching cover.")


with st.form("story_form"):
    character = st.text_input("Choose your main Character", placeholder="e.g.: HanumanJi, Batman")
    topic = st.text_input("Whats the main theme", placeholder="e.g. : fighting from demons")
    location = st.text_input("Whats the location", placeholder="e.g. : Heaven , Earth")
    mood = st.text_input("Mood of Story", placeholder="romantic, comedy, tense")

    
    col1, col2, col3 = st.columns(3)
    with col1:
        length = st.selectbox("Length", ["Short (~200 words)", "Medium (~800 words)", "Long (~1500 words)"])
    with col2:
        temperature = st.slider("Creativity", 0.0, 1.2, 0.9, 0.05)
    with col3:
        make_image = st.checkbox("Generate cover image", value=True)
    submitted = st.form_submit_button("Generate ✨")
    
if submitted:
    
    if not os.getenv("OPENAI_API_KEY"):
        st.error("Missing OPENAI_API_KEY. Add it to your .env file.")
        st.stop()


    if not any([character, location, mood, topic]):
        st.warning("Please provide at least one field.")
        st.stop()


    target_length = {
        "Short (~200 words)": "~200 words",
        "Medium (~800 words)": "~800 words",
        "Long (~1500 words)": "~1500 words",
    }[length]

    user_message = (
        f"Write a complete short story in a very creative way that attracts the user attention.\n"
        f"Character(s): {character or 'you choose—interesting and fresh'}\n"
        f"Topic: {topic or 'you choose—hot topic now a days'}\n"
        f"Location: {location or 'you choose—any good famous location'}\n"
        f"Mood: {mood or 'you choose—cohesive to the setting'}\n"
        f"Length: {target_length}.\n"
        "Avoid cliches; show, don’t tell; keep continuity."
    )
    
    with st.spinner("Generating your story..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ]
        )
        story = response.choices[0].message.content
        
    st.subheader("Your Story")
    st.write(story)
    
    st.download_button(
        label="Download as .txt",
        data=story.encode("utf-8"),
        file_name="story.txt",
        mime="text/plain",
    )
    
        # --- Image generation ---
    if make_image:
        with st.spinner("Generating cover image..."):
            try:
                img_resp = client.images.generate(
                    model="gpt-image-1",
                    prompt=(
                        "Create a cinematic book cover illustration for the story below. "
                        "Do not include any text in the image. "
                        f"Story: {story[:500]}..."  # limit prompt length
                    ),
                    size="1024x1536"
                )
                import base64
                b64 = img_resp.data[0].b64_json
                binary = base64.b64decode(b64)
                cover_img = Image.open(BytesIO(binary)).convert("RGB")

                st.image(cover_img, caption="Cover Illustration", use_container_width=True)

                buf = BytesIO()
                cover_img.save(buf, format="PNG")
                st.download_button(
                    label="Download cover image",
                    data=buf.getvalue(),
                    file_name="cover.png",
                    mime="image/png",
                )
            except Exception as e:
                st.error(f"Image generation failed: {e}")