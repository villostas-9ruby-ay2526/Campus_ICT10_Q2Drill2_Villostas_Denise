# Dance Club Name Verification

from pyscript import display, document

def grab_name(e):
    document.getElementById('the_div').innerHTML = ' '
    members_of_the_club = ['devon villostas', 'keona valdez', 'isabelle cabatu', 'leiane gabia', 'stephanie toralde', 'jade cabatingan']

    
    first_name = document.getElementById('namef').value.lower().strip()
    second_name = document.getElementById('namel').value.lower().strip()
    final_output = first_name + ' ' + second_name
    name_checker = final_output in members_of_the_club # True(1) or False(0)
    


    message_display = (f'{first_name}, you did not register yet!', 'Welcome to the Club! You finally made it!')  # to showcase whether input is on list
    display(message_display[name_checker], target='the_div')