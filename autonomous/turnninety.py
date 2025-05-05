import math

from commands2 import Command
from subsystems.drivetrain import Drivetrain
from wpimath.controller import PIDController

class TurnNinety(Command):
    def __init__(self, drivetrain):
        super().__init__()
        self.drivetrain = drivetrain
        self.Kp = 0.4
        self.Ki = 0
        self.Kd = 0
        self.pid_controller = PIDController(self.Kp, self.Ki, self.Kd)

    def initialize(self):
        self.drivetrain.resetGyro()
        self.pid_controller.setSetpoint(math.pi/2)
        self.pid_controller.setTolerance(math.pi/180)

    def execute(self):
        self.drivetrain.arcadeDrive(
            0, 
            self.pid_controller.calculate(
                self.drivetrain.getGyroAngleZ()
            )
        )

    def isFinished(self):
        return self.pid_controller.atSetpoint()

   
    def end(self, interrupted):
        self.drivetrain.arcadeDrive(0, 0)