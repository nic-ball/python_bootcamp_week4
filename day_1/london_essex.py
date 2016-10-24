def main():
    # Call the london function
    london()
    # Call the essex function
    essex()


#Definition of the london function. It creates
#a local variable named birds
def london():
    birds = 500
    # Print('London has ', birds, 'birds')  # This indentation causes an error
    print('London has', birds, 'birds')  # this indentation does not cause error


# Definition of the essex function. It also
# Creates a local variable named birds
def essex():
    birds = 800
    # print('Essex has', birds, 'birds')  #indentation causes an error
    print('Essex has', birds, 'birds')

# Call the main function
main()