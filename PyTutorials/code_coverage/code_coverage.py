from os import system

print('Output of file:')
system('coverage run sample_file.py')
print('')
print('Output of report:')
system('coverage report')