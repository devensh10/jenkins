import gradio as gr
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyAgxQjN7mNKpeDswKbgJwk3D0sNSNkA2Y0") 

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")  # Confirm the exact model name you're using

# Function to generate itinerary
def generate_itinerary(dest, budget, days, prefs):
    prompt = f"""
    Plan a {days}-day trip to {dest} with a budget of {budget}. Preferences: {prefs}.
    Include a day-wise plan, hotels, food suggestions, and a packing list.
    """
    response = model.generate_content(prompt)
    
    # Get the generated text safely
    return response.text if hasattr(response, 'text') else response.candidates[0]['content']

# Gradio interface
gr.Interface(
    fn=generate_itinerary,
    inputs=[
        gr.Textbox(label="Destination"),
        gr.Textbox(label="Budget"),
        gr.Number(label="Days", value=3),
        gr.Textbox(label="Preferences")
    ],
    outputs=gr.Textbox(label="Generated Itinerary"),
    title="Travel Itinerary Generator"
).launch()
