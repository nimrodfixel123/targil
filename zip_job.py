import os
import zipfile

# a. Create an array of a,b,c,d
my_array = ['a', 'b', 'c', 'd']

# b. Based on this array create txt files (a.txt,b.txt….)
for item in my_array:
    with open(f'{item}.txt', 'w') as f:
        f.write(item)

# c. Make sure all txt files created and if not - fail the script
for item in my_array:
    if not os.path.exists(f'{item}.txt'):
        raise Exception(f'Error: {item}.txt not found')

# d. Create zip files with names based on array + VERSION environment variable, that each one will have one txt file inside (a_1.2.0.zip should include a.txt, b_1.2.0.zip should include b.txt and so on)
version = os.environ['VERSION']
for item in my_array:
    with zipfile.ZipFile(f'{item}_{version}.zip', 'w') as myzip:
        myzip.write(f'{item}.txt')

# e. Make sure all zip files created and if not - fail the script
for item in my_array:
    if not os.path.exists(f'{item}_{version}.zip'):
        raise Exception(f'Error: {item}_{version}.zip not found')

# Print a message indicating that all files were created successfully
print('All files created successfully:')
for item in my_array:
    print(f'- {item}.txt')
    print(f'- {item}_{version}.zip')
