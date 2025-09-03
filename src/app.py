import streamlit as st
import tiktoken


st.set_page_config(page_title="Tokenization Demo", page_icon="🔤", layout="wide")

st.title("🔤 Tokenization Demo with tiktoken")

with st.form("token_form"):
    c1, c2, c3, c4 = st.columns([4, 1.2, 1.2, 0.9])
    with c1:
        texto = st.text_area("✍️ Write your text here:",
                             "Talk is cheap. Show me the code. — Linus Torvalds",
                             height=80)
    with c2:
        modelo = st.selectbox("🤖 Model", ["gpt-4o", "gpt-4", "gpt-3.5-turbo"], index=0)
    with c3:
        costo_por_token = st.number_input("💲 Cost per token (USD)",
                                          value=0.00001, step=0.00001, format="%.5f")
    with c4:
        submitted = st.form_submit_button("Calculate", type="primary", use_container_width=True)

# --------- RESULTADOS ---------
if submitted and texto.strip():
    enc = tiktoken.encoding_for_model(modelo)
    tokens = enc.encode(texto)
    num_tokens = len(tokens)
    token_bytes = [enc.decode_single_token_bytes(t) for t in tokens]
    token_strs = [b.decode("utf-8", errors="replace") for b in token_bytes]
    costo_total = num_tokens * costo_por_token

    st.success("✅ The process is complete")

    # KPI
    m1, m2, m3 = st.columns(3)
    m1.metric("Token Number", num_tokens)
    m2.metric("Estimated Cost", f"${costo_total:.5f}")
    m3.metric("Model", modelo)

    # Tokens con colores
    st.markdown("**✏️ Tokenized Text:**")
    colors = [
        "#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF",
        "#D5BAFF", "#FFBAED", "#BAFFD9", "#FFD6BA", "#BAFFC9"
    ]
    colored_text = ""
    for i, token in enumerate(token_strs):
        color = colors[i % len(colors)]
        safe_token = (token.replace("&", "&amp;")
                           .replace("<", "&lt;")
                           .replace(">", "&gt;")
                           .replace(" ", "&nbsp;"))
        colored_text += (
            f"<span style='background-color:{color}; padding:4px 8px; border-radius:6px; "
            f"margin:2px; display:inline-block; font-size:0.95rem;'>{safe_token}</span>"
        )
    st.markdown(f"<div style='margin-bottom:16px'>{colored_text}</div>", unsafe_allow_html=True)

    
    st.markdown("**🔎 Token Details:**")
    st.dataframe(
        {
            "Index": list(range(1, num_tokens + 1)),
            "Token ID": tokens,
            "Token Text": token_strs,
            "Bytes": [str(b) for b in token_bytes],
        },
        hide_index=True,
        use_container_width=True,
        height=200,
    )
