"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    with open(input_filename, "r", encoding="utf-8") as fin:
        with open(output_filename, "w", encoding="utf-8") as fout:
            table_string = create_schedule_string(fin.read())
            fout.write(table_string)


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    activities = {}
    for match in re.finditer(r"\s(\d{1,2})\D(\d{1,2})(\s+)([a-züõöäA-ZÜÕÖÄ]+)?", input_string):
        h = int(match.group(1))
        m = int(match.group(2))
        activity = str(match.group(4)).lower()
        if activity == 'none':
            continue
        if 0 <= h < 24 and 0 <= m < 60:
            timestr = f"{h:02}:{m:02}"  # h * 60 + m
            if timestr in activities:
                if activity not in activities[timestr] and activity != 'none':
                    activities[timestr].append(activity)
            else:
                activities[timestr] = [activity]

    sorted_activities = sorted(activities.items(), key=lambda x: x[0])

    formatted_activities = []
    max_time_width = 0
    max_activity_width = 0
    for activity_tuple in sorted_activities:
        formatted_time = get_formatted_time(activity_tuple[0])
        formatted_activities_str = ", ".join(activity_tuple[1])
        formatted_activities.append((formatted_time, formatted_activities_str))
        max_activity_width = max(max_activity_width, len(formatted_activities_str))
        if max_activity_width < 7:
            max_activity_width = 7
        max_time_width = max(max_time_width, len(formatted_time))

    # creating a table
    table = []
    if len(formatted_activities) == 0:
        table.append("-" * 20)
        table.append(f"| {'time': >{5}} | {'entries':<{8}} |")
        table.append("-" * 20)
        table.append("| No entries found |")
        table.append("-" * 20)
    else:

        table.append("-" * (max_time_width + max_activity_width + 7))
        table.append(f"| {'time':>{max_time_width}} | {'entries':<{max_activity_width}} |")
        table.append("-" * (max_time_width + max_activity_width + 7))
        for activity_tuple in formatted_activities:

            table.append(f"| {activity_tuple[0]:>{max_time_width}} | {activity_tuple[1]:<{max_activity_width}} |")
        table.append("-" * (max_time_width + max_activity_width + 7))

    return "\n".join(table)


def get_formatted_time(timestr: str) -> str:
    """Format 24 hour time to the 12 hour time."""
    h = int(timestr[:2])
    m = timestr[-2:]
    if h < 12:
        ampm = "AM"
        if h == 0:
            h = 12
    else:
        ampm = "PM"
        if h > 12:
            h = h - 12
    return f"{h}:{m} {ampm}"


if __name__ == '__main__':
    # print(get_formatted_time("00,15"))
    # print(create_schedule_string("  "))
    # print(create_schedule_string("jj  15:03 correct-b hj"))
    print(create_schedule_string("a 1:2 tere 1:2 tsau 1:2 tere"))
    # print(create_schedule_string("here 01:12 abc some more 01:12 def"))
    # print(create_schedule_string("here 01:12 def some more 01:12 abc 1:12 YES"))
    # print(create_schedule_string("x 00:59 incredible regex 0:0 midnight party 00:15 hippo 00:00 viego drinking water 0:00 incident"))
    # print(create_schedule_string("x 12:59 heroes of might and magic 3 12:21 macaroni and 12:21 cheese 12:00 lunch during midday"))
    # print(create_schedule_string(" midagi "))
    # print(create_schedule_string(" 12:00  jooks 12:00 "))
    # print(create_schedule_string("wat 11:00 teine tekst 11:00 jah ei 10:00 entries 10,00"))
    # print(create_schedule_file("schedule_input", "schedule_output.txt"))
