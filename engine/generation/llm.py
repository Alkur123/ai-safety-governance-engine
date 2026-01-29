from transformers import pipeline

gen = pipeline(
    task="text-generation",
    model="google/flan-t5-base",
    max_new_tokens=256
)

def generate(prompt: str) -> str:
    out = gen(prompt, do_sample=False)
    return out[0]["generated_text"]
