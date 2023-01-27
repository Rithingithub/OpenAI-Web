from django.shortcuts import render
import openai

def generate_text(request):
    # Set the API key
    openai.api_key = "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"

    # Define the prompt
    prompt = (f"Write an article about the benefits of AI")

    # Generate text
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the generated text
    generated_text = completions.choices[0].text

    # Render the template with the generated text
    return render(request, 'openaiapp/generated_text.html', {'generated_text': generated_text})
