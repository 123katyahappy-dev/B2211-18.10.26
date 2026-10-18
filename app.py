
import streamlit as st

st.title('всем привет')
st.write("сегодня я расскажу вам о совей жизни. жизнь моя очень интеоресная, наполнена активностями и друзьями. кроме того, я ещё хожу в школу, и про неё я расскажу вам сегодня! Но перед этим:")

user_name = st.text_input("Как тебя зовут?")
if st.button("Всё?"):
    if user_name:
        st.success(f"ПРИВЕТ ПРИВЕЕЕЕТ {user_name}!!!")

    else:
        st.warning('Write your name i beg ya')

st.subheader("show yourself bro")
uploaded_file = st.file_uploader("select smth", type=["png", "jpg", "jpeg"])
if uploaded_file:
  if uploaded_file is not None:
    st.image(uploaded_file, use_container_width=True)


