import pygame
from pololu_drv8835_rpi import motors, MAX_SPEED

# Initialize Pygame
pygame.init()

# Set up the Xbox controller
joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    
left_speed = 0
right_speed = 0

lastSpeedEventValue = 0
leftWheelSpeedEventValue = 0
rightWheelSpeedEventValue = 0
right_trigger_event_value = 0
left_trigger_event_value = 0
turn_trigger_event_value = 0

# Main control loop
while True:
    forward = False
    backward = False
    turn = False


    events = pygame.event.get()

    
    for event in events: #starts at 0
        if event.axis == 4:
            forward = True
            right_trigger_event_value = event.value + 1
        if event.axis == 5:
            backward = True
            left_trigger_event_value = event.value + 1
        if event.axis == 0: #x axis on left
            turn = True
            turn_trigger_event_value = event.value + 1 #plus something .. whats its range... 0-2 wanted.. x axis
            #do calculation to get radius of turn and calculate 
            #use this event value eto change left and right speed 
            
    if (turn):
        print("turnn")
        lastSpeedEventValue = right_trigger_event_value - left_trigger_event_value
        #math with turn_trigger_event_value 
        leftWheelSpeedEventValue = lastSpeedEventValue*2/2*turn_trigger_event_value#math taht uses lastSpeedEventValue and the ratio of the currentTurnTriggerEWventValue
        rightWheelSpeedEventValue = 2-leftWheelSpeedEventValue#math
    elif (forward and backward):
        print("both triggers pressed")
        lastSpeedEventValue = right_trigger_event_value - left_trigger_event_value #vc of robot without turn
        leftWheelSpeedEventValue = lastSpeedEventValue
        rightWheelSpeedEventValue = leftWheelSpeedEventValue
    elif (forward):
        print("forward")
        lastSpeedEventValue = right_trigger_event_value - left_trigger_event_value #vc of robot without turn
        leftWheelSpeedEventValue = lastSpeedEventValue
        rightWheelSpeedEventValue = leftWheelSpeedEventValue
    elif (backward):
        print("backward")
        lastSpeedEventValue = right_trigger_event_value - left_trigger_event_value #vc of robot without turn
        leftWheelSpeedEventValue = lastSpeedEventValue
        rightWheelSpeedEventValue = leftWheelSpeedEventValue
        
    
    
    left_speed = int(-leftWheelSpeedEventValue/2 * 320)
    right_speed = int(rightWheelSpeedEventValue/2 * 320)
        
    motors.motor1.setSpeed(left_speed)
    motors.motor2.setSpeed(right_speed)
    
"""
    if event.type == pygame.JOYAXISMOTION:
            
    # Get datatype event with (controller inputs)
    for event in pygame.event.get():        
        if event.type == pygame.JOYAXISMOTION:
            
            
            if event.axis == 4:
                #going  forward
                right_trigger_event_value = event.value + 1
                forward = true
                
            elif event.axis == 5:
                #going backwards
            elif event.axis == 1:
                #left joystick
            
            
            if forward = true:
                
            
            if event.axis == 4:
                right_trigger_event_value = event.value + 1
                while(right_trigger_event_value >0):
                    left_speed = int(-right_trigger_event_value/2 *320)
                    right_speed = left_speed
            
            #Justin Sudo Code
            #we want to be locked in the forward direction 
            
            #if forward, stay in this loop until forward is 0
                #set speedL = speedR = trigger
                
                #if turn pressed, 
                    #speedLNew speedRNew = radius dependent 
                #else 
                    #speed/direction doesn't change
               
                
            #if backwards, stay in this loop until backwards = 0
                #set speedL = speedR = trigger
                
                #if turn pressed
                    #speedRNew speedLNew = radius dependent
                #else 
                    #nothing changes
           
                       
                        
            # Right Trigger controls both motors - forward
            if event.axis == 4:
                right_trigger_event_value = event.value + 1
                if 0 <= (right_trigger_event_value):
                    left_speed = int(-right_trigger_event_value/2 * 320)
                    right_speed = int(right_trigger_event_value/2 * 320)
                else:
                    left_speed = 0
                    right_speed = 0
                    
                    
            # Left Trigger controls both motors - backwards
            elif event.axis == 5:
                left_trigger_event_value = event.value + 1
                if 0.1 <= abs(left_trigger_event_value):
                    left_speed = int(left_trigger_event_value/2 * 320)
                    right_speed = int(-left_trigger_event_value/2 * 320)
                else:
                    left_speed = 0
                    right_speed = 0
                    
                    
            # Left joystick - Max command value is 480
            elif event.axis == 1:
                if abs(event.value) > 0.1:
                    left_speed = int(event.value * 200)
                else:
                    left_speed = 0
                    right_speed = 0
            # Right joystick
            elif event.axis == 3:
                if abs(event.value) > 0.1: 
                    right_speed = int(-event.value * 200)
                else:
                    left_speed = 0
                    right_speed = 0
                
        #elif event.type == pygame.JOYBUTTONDOWN:
            # Button press events can be used to trigger other robot behaviors
        
    # Update the motor commands
        motors.motor1.setSpeed(left_speed)
        motors.motor2.setSpeed(right_speed)"""