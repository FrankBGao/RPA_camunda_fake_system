# RPA_camunda_fake_system
This project is a part of the RWTH-Aachen PADS group's RPA research.
This project adopts the BPMN engine camunda for generating a user interaction log.

We use a business process for the [process mining book](https://www.springer.com/de/book/9783662498507),
and designed a business process from the HR scenario. 


Here is the model for a process.
![alt text](https://raw.githubusercontent.com/FrankBGao/RPA_camunda_fake_system/master/pic/bpmn.JPG)

For each step in the process, camunda will generate an html form.
![alt text](https://raw.githubusercontent.com/FrankBGao/RPA_camunda_fake_system/master/pic/sreenshot.png)

We add a mechanism step before the human step, and another mechanism step after the human step. These mechanism steps collect event logs from the process. We use this event log to discover the process model as the grand truth.
![alt text](https://raw.githubusercontent.com/FrankBGao/RPA_camunda_fake_system/master/pic/pm4py_a_fake_process.JPG)


Then, we use the RPA action recorder to collect the user interactions from the front-end. Adopting this front-end event log, we discover a process model. 
![alt text](https://raw.githubusercontent.com/FrankBGao/RPA_camunda_fake_system/master/pic/Inductive%20Miner%20Result_pm4py.png)

However, this method is difficult to generate a process model that could guide RPA.
