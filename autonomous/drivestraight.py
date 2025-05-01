from commands2 import Command

class DriveStraight(Command):
    def __init__(self, drivetrain, distance_in_inches = 72):
        super().__init__()
        self.drivetrain = drivetrain
        self.distance = distance_in_inches
        self.addRequirements(drivetrain)

    def initialize(self):
        self.drivetrain.resetEncoders()
    
    def execute(self):
        left = self.drivetrain.getLeftDistanceInch()
        right = self.drivetrain.getRightDistanceInch()
        error = right - left
        self.drivetrain.arcadeDrive(-0.7, 0.6 * error)

    def isFinished(self):
        return self.drivetrain.getAverageDistanceInch() >= self.distance
    
    def end(self, interrupted):
        self.drivetrain.arcadeDrive(0, 0)