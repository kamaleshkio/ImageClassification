import gradio as gr
from classify_tool import classify_image

def classify_image_gradio(image):
    image.save("input.jpg")
    return classify_image("input.jpg")

gr.Interface(
    fn=classify_image_gradio,
    inputs="image",
    outputs="text",
    title="Oil Drop Stage Classifier"
).launch()