import re

# Global variables
file_name = "Art of Entrepreneurship"

#url = r"E:\Project\Anaconda\csv\vbc\data\Test.txt"
url = r"E:\Project\Anaconda\csv\vbc\data\\" + file_name + ".txt"
time_series = list()

# Data type convertion from string to integer
def str_to_int_convertion(list_=None, split_list=None, str_to_int=None):
    """1) This function get a list of one string element (eg: ['14:32']).
    2) Split a string into two string elements (eg: ['14', '32']).
    3) Converts string elements into integer elements (eg: [14, 32])
    4) return a tuple (eg: (14,32))
    """
    str_to_int = []
    split_list = list_[0].split(':')       # spliting
    type_conversion1 = int(split_list[0])  # type casting
    type_conversion2 = int(split_list[1])  # type casting
    str_to_int.extend([type_conversion1, type_conversion2])  # making list
    return tuple(str_to_int)  # return tuple

# time convertion from hours and minutes to minutes only
def minutes_and_seconds_to_seconds(minutes_and_seconds):
    """This function get a tuple (eg: (1,30)) which is 1 minute and 30 seconds
    and return an integer value 90 because there are 90 seconds in 1 minute 
    and 30 seconds.
    """
    minutes = minutes_and_seconds[0]
    seconds = minutes_and_seconds[1]
    total_seconds = (minutes * 60) + seconds
    return total_seconds

# Time conversion from minutes to minutes and hours.
def seconds_to_hours_minutes_and_seconds(seconds):
    '''This function counts how many hours,minutes and seconds
    in given number of seconds
    '''
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

# Reading file and Data Extraction
def main():
    
    with open(url) as file_handle:
        name = file_handle.name
        print(name)
        for line in file_handle:
            line = line.rstrip()
            if line:
                print("\nline: ",line)
                extracted_string = re.findall('[(]([0-9]+[:][0-9]+)[)]', line)
                print("extracted_string: ",extracted_string)
                if extracted_string:
                    converted_value = str_to_int_convertion(extracted_string)
                    print("converted_value: ",converted_value)
                    total_minutes = minutes_and_seconds_to_seconds(converted_value)
                    print("total_seconds: ",total_minutes)
                    time_series.append(total_minutes)
    h,m,s = seconds_to_hours_minutes_and_seconds(sum(time_series))
    print(f"Time_series in seconds: {time_series}")
    print('*'*100,"\n")
    print("\t\tInformation About Course\n")
    # print(f"Course Name:\t{name}")
    print(f"\nNo of videos:\t{len(time_series)}")
    # print("Average video time: ", sum(time_series)/len(time_series))
    # print("Time in minutes: ", sum(time_series))
    print(f"Time:\t\t{h} hours {m} minutes and {s} seconds")
    # print("or",end="")    
    print(f"*"*100)


if __name__ == "__main__":
    main()
