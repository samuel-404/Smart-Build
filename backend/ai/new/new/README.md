<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# [Project Name] 🎯


## Basic Details
### Team Name: [Game of codes]


### Team Members
- Team Lead: [Linta George] - [College of Engineering Perumon]
- Member 2: [Irene Ann Thomas] - [College of Engineering Perumon]
- Member 3: [Name] - [College]

### Project Description
[Smile-to-Calculate – A Fun Twist on Math!
This project is an interactive web-based calculator that works only when you smile! Using OpenCV’s face detection and smile recognition features, the system checks if the user is smiling through their webcam. If a smile is detected, the calculator processes the input and displays the result. If not, it refuses to calculate — adding a playful challenge to the user.]

### The Problem (that doesn't exist)
[Traditional calculators are purely functional, offering no emotional engagement or interaction. This lack of engagement can make basic mathematical tasks feel monotonous, especially in learning environments. There is a need for a tool that makes calculation more enjoyable while encouraging positive emotions, such as smiling.]

### The Solution (that nobody asked for)
[How are you solving it? Keep it fun!]

## Technical Details
### Technologies/Components Used
For Software:
- [Languages used:-Python]
- [Frameworks used:-Opencv,Mediapipe]
- [Libraries used:-Opencv,Numpy,Mediapipe]
- [Tools used:-Webcam,command prompt,vscode,git,github]

For Hardware:
- [List main components]
- [List specifications]
- [List tools required]

### Implementation
For Software:-Solution

To make a calculator that works only when the user smiles, we combined real-time smile detection with calculator logic using OpenCV and Python.

1. Capture Live Video Feed

Access the webcam using OpenCV’s cv2.VideoCapture() function.

Convert each frame to grayscale to make detection faster.



2. Detect Faces & Smiles

Load Haar Cascade Classifiers (haarcascade_frontalface_default.xml and haarcascade_smile.xml).

Detect faces in the frame, then detect smiles inside the detected face region.



3. Trigger Calculator on Smile

If a smile is detected, prompt the user to enter two numbers and choose an operation.

Perform the calculation (addition, subtraction, multiplication, division).



4. Add Emoji Feedback

Display different emojis for different operations to make the interaction fun.



5. Display Result on Webcam Feed

Show the message “Smile Detected! Running Calculator…” when a smile is found.

Overlay the result and emoji directly on the webcam feed using cv2.putText().



6. Close Application

Once the calculation is done, release the webcam and close all OpenCV windows.
# Installation
[Opencv install:-pip install opencv-python]

# Run
[Program run:-Python program_name.py]

### Project Documentation
For Software:We propose the development of “Smile-to-Calculate”, a web-based calculator that operates only when the user smiles. By integrating OpenCV’s real-time smile detection with a responsive web interface, the system ensures calculations are performed exclusively in a positive mood. This playful approach not only adds fun to a mundane task but also promotes happiness, making it ideal for educational tools, lighthearted productivity applications, and interactive tech showcases.

# Screenshots (Add at least 3)
![Screenshot1:-c:\Users\IRENE ANN THOMAS\Pictures\Screenshots\Screenshot 2025-08-09 063915.png]
*first lines of code explaining calculator*

![Screenshot2 :-c:\Users\IRENE ANN THOMAS\Pictures\Screenshots\Screenshot 2025-08-09 063932.png]
*webcam code*

![Screenshot3 :- c:\Users\IRENE ANN THOMAS\Pictures\Screenshots\Screenshot 2025-08-09 063946.png]
*Documentation*

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add your demo video link here:-<video controls src="Screen Recording 2025-08-09 071832.mp4" title="Title"></video>]
*Explain what the video demonstrates*:-In this mood base calculator we have used mediapipe and when smiled the operation starts and closes and when not smiled it waits till smile is detected

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Linta George]: [Ideation,programming,documentation]
- [Irene Ann Thomas]: [Programming,Documentation,Presentation]
- [Name 3]: [Specific contributions]

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



