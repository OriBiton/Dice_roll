import streamlit as st
import random
from PIL import Image

# שמירת המצב של הניקוד
if 'total_score' not in st.session_state:
    st.session_state.total_score = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# עמוד שער
st.title("🎲 ברוכים הבאים למשחק הקובייה!")
st.write("""
החוקים פשוטים:
- אתה תגלגל קובייה כמה פעמים שתרצה.
- בכל פעם, המספר שיופיע על הקובייה יתווסף לניקוד הכולל שלך.
- אם הקובייה תראה 1, כל הניקוד שלך יתאפס!
- המטרה: להגיע לניקוד של לפחות 50 ולזכות ב-50$! 💰
- אתה יכול להפסיק לשחק בכל רגע.
""")

# התחלת המשחק
if st.session_state.game_over:
    st.write("המשחק נגמר. תודה ששיחקת!")
else:
    if st.button("🎲 לגלגל קובייה!"):
        # גלגול הקובייה
        dice = random.randint(1, 6)
        final_dice_image = Image.open(f"images/die_{dice}.png")
        st.image(final_dice_image, caption=f"התוצאה היא {dice}", width=150)
        
        if dice != 1:
            st.session_state.total_score += dice
            st.write(f"🌟 הניקוד שלך: {st.session_state.total_score}")
        else:
            st.write("😱 יצא 1! הניקוד שלך התאפס!")
            st.session_state.total_score = 0
        
        # בדיקת תנאי הניצחון
        if st.session_state.total_score >= 50:
            st.write("🎉 ניצחת וזכית ב-50$! מזל טוב!")
            st.session_state.game_over = True
    else:
        st.write(f"💡 הניקוד הנוכחי שלך: {st.session_state.total_score}")

# כפתור לסיום המשחק
if st.button("🚪 לצאת מהמשחק"):
    st.write("תודה ששיחקת! נתראה בפעם הבאה 🎮")
    st.session_state.game_over = True


