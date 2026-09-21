import streamlit as st
import secrets
import string

# パスワード生成関数（選択された文字セットに応じて生成）
def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=False):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        return None  # 少なくとも1つの文字種が必要
    return ''.join(secrets.choice(characters) for _ in range(length))


st.title("パスワード生成アプリ")
st.write("スライダーとチェックボックスで設定し、「パスワード生成」ボタンを押してください。")

# パスワード長を選択
length = st.slider("パスワードの長さ", min_value=4, max_value=32, value=12, step=1)

# 文字種のチェックボックス
st.write("含める文字種:")
col1, col2 = st.columns(2)
with col1:
    use_lowercase = st.checkbox("英小文字 (a-z)", value=True)
    use_digits = st.checkbox("数字 (0-9)", value=True)
with col2:
    use_uppercase = st.checkbox("英大文字 (A-Z)", value=True)
    use_symbols = st.checkbox("記号 (!@#...)", value=False)

# 生成ボタン
generate = st.button("パスワード生成")

# メイン処理
if generate:
    # すべてのチェックボックスがOFFならエラー
    if not (use_lowercase or use_uppercase or use_digits or use_symbols):
        st.error("少なくとも1つの文字種を選択してください。")
    else:
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
        if password:
            st.success("生成されたパスワード:")
            st.code(password, language=None)
            st.button("パスワードをコピー", on_click=lambda: st.session_state.update({'_clipboard': password}))
            st.caption("ボタンを押すとクリップボードにコピーされます（動作しない場合は手動でコピーしてください）")
        else:
            st.error("少なくとも1つの文字種を選択してください。")
 