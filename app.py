import streamlit as st

# ---------- FLAMES LOGIC ----------
def flames_result(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    list1 = list(name1)
    list2 = list(name2)

    # Remove common letters
    for char in name1:
        if char in list2:
            list1.remove(char)
            list2.remove(char)

    count = len(list1) + len(list2)

    flames = ["F", "L", "A", "M", "E", "S"]

    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            flames = flames[index+1:] + flames[:index]
        else:
            flames = flames[:len(flames)-1]

    return flames[0]


# ---------- FEEDBACK ----------
def flames_feedback(letter):
    feedback = {
        "F": ("🤝 FRIEND", "You both share a strong friendship bond filled with trust and fun."),
        "L": ("❤️ LOVE", "There is love in the air! A deep emotional connection exists."),
        "A": ("😊 AFFECTION", "You both care deeply for each other with warmth and respect."),
        "M": ("💍 MARRIAGE", "A perfect match! This bond has long-term commitment potential."),
        "E": ("⚔️ ENEMY", "Opposites clash! But hey, sometimes enemies turn into friends 😉"),
        "S": ("👧 SISTER", "A pure and protective bond like siblings.")
    }
    return feedback[letter]


# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="FLAMES Game", page_icon="🔥")

st.title("🔥 FLAMES Relationship Game")
st.write("Enter **Male & Female names** to find your relationship 💖")

male_name = st.text_input("👦 Male Name")
female_name = st.text_input("👧 Female Name")

if st.button("💘 Check FLAMES"):
    if male_name and female_name:
        result = flames_result(male_name, female_name)
        title, message = flames_feedback(result)

        st.success(f"### Result: {title}")
        st.info(message)

    else:
        st.warning("⚠️ Please enter both names!")
