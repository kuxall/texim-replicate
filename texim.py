import replicate
import streamlit as st

REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]
REPLICATE_MODEL_ENDPOINTSTABILITY = st.secrets["REPLICATE_MODEL_ENDPOINTSTABILITY"]

# Main app layout
st.title("Text-to-Image Generator")

prompt = st.text_area(
    ":orange[**Start Using your Prompts...**]",
    value="An astronaut riding a rainbow unicorn, cinematic, dramatic")

width = st.number_input("Width of output image", value=1024)
height = st.number_input("Height of output image", value=1024)
num_outputs = st.slider(
    "Number of images to output", value=1, min_value=1, max_value=4)
negative_prompt = st.text_area(
    ":red[**Hey!, you don't want this...**]",
    value="the absolute worst quality, distorted features",
    help="This is a negative prompt, basically type what you don't want to see in the generated image")

if prompt:
    with st.spinner("Generating image..."):
        try:
            # Call the model to generate images
            output = replicate.run(
                REPLICATE_MODEL_ENDPOINTSTABILITY,
                input={
                    "prompt": prompt,
                    "width": width,
                    "height": height,
                    "num_outputs": num_outputs,
                    "negative_prompt": negative_prompt
                }
            )

            # Display generated images
            for image in output:
                st.image(image, caption="Generated Image")

        except Exception as e:
            st.error(f"Error: {e}")
