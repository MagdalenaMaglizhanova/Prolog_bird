import streamlit as st
from pyswip import Prolog

# Initialize Prolog and add birds
prolog = Prolog()

prolog.assertz("bird('eagle', 'Eagle', 'A large bird of prey, symbol of power and freedom.')")
prolog.assertz("bird('sparrow', 'Sparrow', 'A small, common bird often found in cities.')")
prolog.assertz("bird('owl', 'Owl', 'A nocturnal bird known for sharp hearing and vision.')")
prolog.assertz("bird('peacock', 'Peacock', 'Famous for its bright plumage and large tail.')")
prolog.assertz("bird('parrot', 'Parrot', 'A colorful and intelligent bird often mimicking human speech.')")
prolog.assertz("bird('white_stork', 'White Stork', 'A large migratory bird known for its long legs and beak, often seen nesting on rooftops in Europe.')")

bird_images = {
    'eagle': 'https://upload.wikimedia.org/wikipedia/commons/1/19/Bald_eagle_portrait.jpg',
    'sparrow': 'https://upload.wikimedia.org/wikipedia/commons/4/45/House_sparrow04.jpg',
    'owl': 'https://upload.wikimedia.org/wikipedia/commons/1/1f/Siberian_owl.jpg',
    'peacock': 'https://upload.wikimedia.org/wikipedia/commons/6/6d/Peacock_Plumage.jpg',
    'parrot': 'https://upload.wikimedia.org/wikipedia/commons/3/32/Ara_macao_Tucson.jpg',
    'white_stork': 'https://upload.wikimedia.org/wikipedia/commons/3/3a/Ciconia_ciconia_in_flight_2_-_Budakeszi.jpg'
}

st.title("🦜 Bird Chatbot with Prolog and Streamlit")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def query_bird(user_text):
    user_text = user_text.lower()
    for bird_key in bird_images.keys():
        if bird_key in user_text:
            results = list(prolog.query(f"bird('{bird_key}', Name, Description)."))
            if results:
                return results[0]['Description'], bird_images[bird_key]
    return None, None

def add_message(sender, message, image_url=None):
    st.session_state.chat_history.append({'sender': sender, 'message': message, 'image': image_url})

def display_chat():
    for chat in st.session_state.chat_history:
        if chat['sender'] == 'User':
            st.markdown(f"**You:** {chat['message']}")
        else:
            st.markdown(f"**Chatbot:** {chat['message']}")
            if chat['image']:
                st.image(chat['image'], width=300)

with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Enter bird name:")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_input.strip():
    add_message('User', user_input)
    description, image_url = query_bird(user_input)
    if description:
        add_message('Bot', description, image_url)
    else:
        add_message('Bot', "I don't understand the question.")

display_chat()
