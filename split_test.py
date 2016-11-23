import  os
import  pickle
import  nesterMN

os.chdir('e:\\PythonLearning\\HeadFirstPython\\chapter3')

try:
#if os.path.exists('sketch.txt'):
    Man = []
    Woman = []
    data = open('sketch.txt')
    for data_line in data:
     #   if not data_line.find(':')==-1:
        try:
            (role,line_spoken) = data_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                Man.append(line_spoken)
            elif role == 'Woman':
                Woman.append(line_spoken)
        #    print(role,end='')
         #   print('  said:  ',end='')
          #  print('\t', end='')
           # print(line_spoken,end = '')
        except ValueError:
            pass
    data.close()
    try:
        man_data = open('mandata1.txt',"w")
        woman_data  = open('womandata1.txt',"w")
        print(Man,file = man_data)
        print(Woman,file = woman_data)
    except IOError as err:
        print('File error: '+str(err))
    finally:
        if man_data in locals():
            man_data.close()
        if woman_data in locals():
             woman_data.close()
except IOError:
#else:
     print('The data file is missing!')


try:
    with open('its.txt',"w") as data:
        print("Itis ....",file = data)
except IOError as err:
    print('File error:' + str(err))




try:
    with open('man_data.txt','w') as man_file,open('other_data.txt','w') as other_file:
        print(Man, file = man_file)
        print(Woman, file= other_file)

except IOError as err:
    print('File error:'+str(err))


try:
	with open('man_data.pickle','wb') as man_file, open('other_data.pickle','wb') as other_file:
		pickle.dump(Man,man_file)
        pickle.dump(Woman,other_file)
except IOError as err:
    print('File error:' + str(err))
except pickle.PickleError as perr:
    print('File error: ' + str(perr))

try:
    new_man = []
    new_other_man = []
    with open('man_data.pickle','rb') as new_man_file,open('other_data.file','rb') as new_other_file:
        new_man = pickle.load(new_man_file)
        new_other_file = pickle.load(new_other_file)
        nesterMN.print_list(new_man)
        nesterMN.print_list(new_other_man)
except IOError as err:
    print('File error : ' + str(err))
except pickle.PickleError as perr:
    print('File error : ' + str(perr) )

