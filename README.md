## Inspiration
COVID-19 has forced all schools and colleges to shut down, and as a result all the teachers are hosting classes online. 
It is nearly impossible for a teacher to make sure that every student is paying attention to the class. For example, the student could just join the class and physically leave to to do something else or use his smartphone.
This is where Student-Sight comes in, it uses Computer Vision to keep the teacher notified about the amount of time that the student was actually paying attention to the ongoing class via telegram. 

## What it does
Our solution uses a Computer Vision script that works in harmony with a Telegram Bot that notifies the teacher about the amount of time the student is actually spending in front of the laptop. The amount of time spent on and off-screen for each student is logged and sent to the teacher using the telegram bot. 

## How we built it
<img src = "https://raw.githubusercontent.com/Mainakdeb/student-sight/main/images/student-sight.jpg">

The project was divided into 2 main parts:
* The computer vision pipeline uses the live webcam feed of the laptop and verified the physical presence of the student. It also logged the amount of time spent on and off screen.
* The telegram bot sends 2 kinds of messages to the teacher:
    1. When a student enters the class, it sends: 

        
        ```
    Spongebob {ID: hack101} just joined the class
    ```
    
    2. When a student leaves the class, it sends:

         
        ```
       Spongebob {ID: hack101} left the class 
       Uptime: 00:25:46 
       Downtime: 0:10:14
        ```
Note: The name and ID for each student can be changed by simply changing the `students.json` file. 

## Scalable out of the box
<img src = "https://raw.githubusercontent.com/Mainakdeb/student-sight/main/images/student-sight-scalable.jpg">

## Challenges we ran into
This was the first time we were building a telegram bot, it was a bit challenging at first, but we figured out our way through it thanks to the documentation. 

## Accomplishments that we're proud of
This was the first time that we were trying to deploy a computer vision pipeline on a platform like telegram. It also took us quite some time to figure out how to properly build the computer vision pipeline. 

## What we learned
We learnt how to build a telegram bot, and how to integrate it with other scripts to send messages in real time to the user. We also learned how to efficiently detect faces and eyes of any user using the live webcam feed using openCV. 

## What's next for Student-Sight
We would try to deploy this in our class and see how it goes :)
