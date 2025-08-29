import streamlit as st
from openai import OpenAI

def local_fallback(prompt: str, language: str) -> str:
    header = f"# Generated {language} program\n# Prompt: {prompt[:100]}\n\n"
    if language == "python":
        return header + f"""def main():
    print("This Python program was generated for: {prompt}")

if __name__ == "__main__":
    main()
"""
    elif language == "java":
        return header + f"""public class GeneratedProgram {{
    public static void main(String[] args) {{
        System.out.println("Generated for: {prompt}");
    }}
}}"""
    else:
        return header + f"""function main() {{
  console.log("Generated for: {prompt}");
}}

main();"""

client = OpenAI(api_key="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")

def generate_with_ai(prompt, language):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Write a {language} program: {prompt}"}]
    )
    return response.choices[0].message.content

st.title("🧑‍💻 AI → Code Generator")
st.write("Enter a prompt and get a generated program back.")

prompt = st.text_area("Enter your prompt:", placeholder="e.g. Create a Python program to calculate factorial.")
language = st.selectbox("Choose programming language:", ["python", "java", "javascript"])

if st.button("Generate Code"):
    if not prompt.strip():
        st.error("Please enter a prompt!")
    else:
        try:
            code = generate_with_ai(prompt, language)
        except Exception as e:
            st.warning(f"Using fallback because of error: {e}")
            code = local_fallback(prompt, language)
        st.code(code, language=language)
        st.download_button("Download Code", code, file_name=f"generated.{language[:2]}")
