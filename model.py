import streamlit as st
import modelhelper
import time


st.set_page_config(page_title="LangChain: Model Karşılaştırma", layout="wide")
st.title("LangChain: Model Karşılaştırma")
st.divider()

col_prompt, col_settings = st.columns((2,3))

with col_prompt:
    prompt = st.text_input(label="Sorunuzu giriniz:")
    st.divider()
    submit_btn = st.button("Sor")

with col_settings:
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
    max_tokens = st.slider(label="Maximum Tokens", min_value=10, max_value=500, value=200, step=10)

st.divider()

col_gpt, col_gemini, col_claude, col_command = st.columns(4)

with col_gpt:
    if submit_btn:
        with st.spinner("GPT Yanıtlıyor..."):
            st.success("GPT-4 Turbo") #yesıl arka plan
            start_time = time.perf_counter()
            st.write(modelhelper.ask_gpt(prompt=prompt, temperature=temperature, max_tokens=max_tokens))
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} saniye")


with col_gemini:
    if submit_btn:
        with st.spinner("Gemini Yanıtlıyor..."):
            st.info("Gemini Pro") #mavi arka plan
            start_time = time.perf_counter()
            st.write(modelhelper.ask_gemini(prompt=prompt, temperature=temperature))  #gemını'da max_tokens kullanmıyoruz!
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} saniye")


with col_claude:
    if submit_btn:
        with st.spinner("Claude Yanıtlıyor..."):
            st.error("Claude 2.1") #kırmızı arka plan
            start_time = time.perf_counter()
            st.write(modelhelper.ask_claude(prompt=prompt, temperature=temperature, max_tokens=max_tokens))
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} saniye")


with col_command:
    if submit_btn:
        with st.spinner("Command Yanıtlıyor..."):
            st.warning("Command")
            start_time = time.perf_counter()
            st.write(modelhelper.ask_command(prompt=prompt, temperature=temperature, max_tokens=max_tokens))
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} saniye")