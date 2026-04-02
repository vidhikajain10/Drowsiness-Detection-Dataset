# Driver Drowsiness Detection System

## Overview

This project is a simple real-time drowsiness detection system built using computer vision. It monitors eye activity through a webcam and alerts the user when signs of fatigue are detected.

## Motivation

While observing long-distance driving scenarios, it became clear that fatigue is a major factor behind road accidents. This project was created to explore how a basic vision-based system can help detect drowsiness early.

## How It Works

* The system captures video using a webcam
* Face is detected using Haar Cascade
* Eye detection is performed within the face region
* If eyes remain closed for a certain number of frames, an alert is triggered

## Features

* Real-time detection
* Lightweight and fast
* Audio alert system
* Easy to run and modify

## Tech Stack

* Python
* OpenCV
* NumPy

## Setup Instructions

1. Install dependencies:
   pip install -r requirements.txt

2. Make sure the following files are present:

   * models/haarcascade_frontalface_default.xml
   * models/haarcascade_eye.xml
   * assets/alarm.wav

3. Run the program:
   python main.py

## Output

* Webcam feed opens
* If eyes remain closed for a few seconds, a warning message and alarm is triggered

## Future Improvements

* Use deep learning for better accuracy
* Add mobile notification system
* Deploy on embedded devices like Raspberry Pi
