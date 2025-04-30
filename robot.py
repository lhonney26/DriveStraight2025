

from wpilib import TimedRobot, Joystick
import os
from subsystems.drivetrain import Drivetrain
import ntcore

os.environ["HALSIMWS_HOST"] = "10.0.0.2"
os.environ["HALSIMWS_PORT"] = "3300"

class MyRobot(TimedRobot):

    def robotInit(self):
        '''This method is called as the robot turns on and is often used to setup the
        joysticks and other presets.'''
        self.controller=Joystick(0)
        self.drivetrain=Drivetrain()
        self.nt_drivetrain = ntcore.NetworkTableInstance.getDefault().getTable("Drivetrain")

    def robotPeriodic(self):
        '''This is called every cycle of the code. In general the code is loop
        through every .02 seconds.'''
        self.drivetrain.periodic()

    def autonomousInit(self):
        '''This is called once when the robot enters autonomous mode.'''
        self.drivetrain.resetEncoders()


    def autonomousPeriodic(self):
        '''This is called every cycle while the robot is in autonomous.'''
        if self.drivetrain.getAverageDistanceInch() < 12:
            # find the difference between the encoders
            left=self.drivetrain.getLeftDistanceInch()
            right=self.drivetrain.getRightDistanceInch()
            error=right-left
            self.drivetrain.arcadeDrive(-0.7,0.6*error)
        else:
            self.drivetrain.arcadeDrive(0,0)

    def teleopInit(self):
        '''This is called once at the start of Teleop.'''
        pass

    def teleopPeriodic(self):
        '''This is called once every cycle during Teleop'''
        forward = self.controller.getRawAxis(1)
        rotate = self.controller.getRawAxis(0)
        self.drivetrain.arcadeDrive(forward, rotate)



