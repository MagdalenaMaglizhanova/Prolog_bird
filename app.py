import streamlit as st

# Данни за птиците
birds = {
    'white_stork': {
        'name': 'White Stork',
        'description': 'A large bird known for its long legs and migratory habits.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/7/7c/Ciconia_ciconia_-_Portugal_02.jpg'
    },
    'bald_eagle': {
        'name': 'Bald Eagle',
        'description': 'A bird of prey found in North America, symbol of the United States.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/e/e5/Bald_Eagle_Portrait.jpg'
    },
    'peacock': {
        'name': 'Peacock',
        'description': 'Known for its iridescent tail feathers that fan out in a spectacular display.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/2/22/Peacock_Plumage.jpg'
    },
    # Добави още птици ако искаш
}

# Streamlit интерфейс
st.title("Bird Encyclopedia ChatBot")

chat_container = st.container()
input_container = st.container()

if 'chat' not in st.session_state:
    st.session_state.chat = []

def add_message(sender, text, image_url=None):
    st.session_state.chat.append({'sender': sender, 'text': text, 'image': image_url})

def get_bird_info(message):
    message = message.lower()
    for key, info in birds.items():
        if key in message or info['name'].lower() in message:
            return info['description'], info['image']
    return None, None

# Покажи чат съобщенията
with chat_container:
    for msg in st.session_state.chat:
        if msg['sender'] == 'User':
            st.markdown(f"**You:** {msg['text']}")
        else:
            st.markdown(f"**Bot:** {msg['text']}")
            if msg['image']:
                st.image(msg['image'], width=300)

# Въвеждане на ново съобщение
with input_container:
    user_input = st.text_input("Enter bird name or question:")

    if st.button("Send"):
        if user_input.strip() != '':
            add_message('User', user_input)
            description, image_url = get_bird_info(user_input)
            if description:
                add_message('Bot', description, image_url)
            else:
                add_message('Bot', "Sorry, I don't understand the question.")

            # За презареждане на чата
            st.experimental_rerun()
