import cv2
import streamlit as st

st.title('Real-time Face Detection')

# Load the Haar cascade for smile detection
face_smile_file = 'haarcascade_smile.xml'
face_profile_file = 'haarcascade_profileface.xml'
face_profile = cv2.CascadeClassifier(face_profile_file)
face_smile = cv2.CascadeClassifier(face_smile_file)

# Function to detect smiles in the frame
def detect_smile(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    smiles = face_profile.detectMultiScale(gray, 1.3, 1)
    for x, y, w, h in smiles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    return frame

# Initialize session state for webcam status
if 'webcam_active' not in st.session_state:
    st.session_state.webcam_active = False

# Function to start the webcam
def start_webcam():
    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    
    while st.session_state.webcam_active:
        ret, frame = cap.read()
        if not ret:
            st.write("Failed to capture video")
            break

        # Detect smiles in the frame
        frame = detect_smile(frame)

        # Display the frame in Streamlit
        stframe.image(frame, channels='BGR')

    cap.release()
    cv2.destroyAllWindows()

# Button to start the webcam
if st.button("Start Webcam", key='start'):
    st.session_state.webcam_active = True
    start_webcam()

# Button to stop the webcam
elif st.button("Stop Webcam", key='stop'):
    st.session_state.webcam_active = False

