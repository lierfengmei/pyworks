import  os
os.chdir('e:\\PythonLearning\\HeadFirstPython\\chapter5')

def santitize(time_string):
    if '-' in time_string:
        (mins,secs) = time_string.split('-',1)
    elif ':' in time_string:
        (mins,secs) =  time_string.split(':',1)
    else:
        (mins,secs) = time_string.split('.',1)
    return (mins + '.' + secs)



def get_coach_data(func_name):
    try:
        with open(func_name) as file:
            data = file.readline().strip().split(',')
            return {'Name':data.pop(0),
                    'DOB':data.pop(0),
                    'FastestScore':str(sorted(set([santitize(eachnum) for eachnum in data]))[0:3])}
    except IOError as err:
        print("File error:" + str(err))
        return (None)


sarah = get_coach_data("sarah2.txt")
print(sarah['Name'] + "'s fastest times are :" + sarah['FastestScore'])

