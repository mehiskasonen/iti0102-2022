"""Mr Roboto, tomi aragoto."""

from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(15)
    robot.sleep(5)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(30)
    while robot.get_left_line_sensor and robot.get_right_line_sensor() > 5:
        robot.sleep(0.1)

    robot.set_wheels_speed(0)
    robot.set_wheels_speed(20)
    robot.sleep(1)
    robot.done()


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(20)
    robot.sleep(1)

    while robot.get_left_line_sensor() < 100 and robot.get_right_line_sensor() < 100:
        robot.set_wheels_speed(80)
        robot.sleep(0.01)
        print(robot.get_line_sensors())
        if robot.get_second_line_sensor_from_left() > robot.get_second_line_sensor_from_right() or \
                robot.get_third_line_sensor_from_left() > robot.get_third_line_sensor_from_right():

            print("left greater")
            while robot.get_second_line_sensor_from_left() > robot.get_second_line_sensor_from_right():
                # robot.get_third_line_sensor_from_left() > robot.get_third_line_sensor_from_right():

                robot.set_wheels_speed(0)
                robot.sleep(0.01)
                robot.set_left_wheel_speed(-12)
                robot.set_right_wheel_speed(12)
                robot.sleep(0.1)
                print(robot.get_line_sensors())
                print("turned right")
        if robot.get_second_line_sensor_from_right() > robot.get_second_line_sensor_from_left() or \
                robot.get_third_line_sensor_from_right() > robot.get_third_line_sensor_from_left():

            print("right greater")
            while robot.get_second_line_sensor_from_right() > robot.get_second_line_sensor_from_left():
                # robot.get_third_line_sensor_from_right() > robot.get_third_line_sensor_from_left():
                robot.set_wheels_speed(0)
                robot.sleep(0.01)
                robot.set_left_wheel_speed(12)
                robot.set_right_wheel_speed(-12)
                robot.sleep(0.1)
                print(robot.get_line_sensors())
                print("turned left")

    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    pass


if __name__ == '__main':
    robot = FollowerBot()
