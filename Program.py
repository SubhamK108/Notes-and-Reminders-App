import BuildPackages.NotesLibrary as NL
import BuildPackages.RemindersLibrary as RL
import os
from datetime import datetime, timedelta



while True:
    os.system('clear')
    print('MENU'.center(95, '.'))
    print('1. CREATE A NOTE')
    print('2. VIEW A NOTE')
    print('3. DELETE A NOTE')
    print('4. CREATE A REMINDER')
    print('5. DISPLAY A REMINDER')
    print('6. DELETE A REMINDER')
    print('7. EXIT')

    option = int(input('Enter Option: '))

    if option == 1:
        d, m, y = input('Enter date (DD.MM.YYYY): ').split('.')
        file_name = d + m + y
        notes = input('Enter Note: ')
        notes += '\n'
        NL.Create_Notes(notes, file_name)
        print('Note Created.')

    elif option == 2:
        d, m, y = input('Enter date (DD.MM.YYYY): ').split('.')
        file_name = d + m + y
        note = NL.View_Notes(file_name)
        print('Notes created on {0}.{1}.{2}...\n'.format(d, m, y))
        print(note)

    elif option == 3:
        d, m, y = input('Enter date (DD.MM.YYYY): ').split('.')
        file_name = d + m + y
        NL.Delete_Note(file_name)
        print('Note Deleted.')

    elif option == 4:
        D, M, Y = map(int, input('Enter Starting Date (D.M.YYYY, Eg. 5.8.2019): ').split('.'))
        h, m = map(int, input('Enter Starting Time in 24 Hour Format (HH:MM, Eg. 17:30): ').split(':'))
        event_duration = int(input('Enter Duration of Event (in Minutes): '))
        try:
            start_info = datetime(Y, M, D, h, m, 00)
        except:
            print('Invalid Date or Time !')
            exit()
        notes = input('Add a Note: ')

        event = RL.Create_Reminder(start_info, note = notes, duration = event_duration)

        print('''{0} Event Added:
                Start: {1}
                End  : {2}'''.format(event['summary'], event['start']['dateTime'], event['end']['dateTime']))

    elif option == 5:
        date = input('Enter Date (YYYY-MM-DD, Eg. 2019-09-08): ')
        RL.Show_Reminder(date)

    elif option == 6:
        date = input('Enter Date (YYYY-MM-DD, Eg. 2019-09-08): ')
        RL.Delete_Reminder(date)

    elif option == 7:
        print('THANK YOU'.center(95, '.'))
        exit()

    else:
        print('Invalid Option !')

    e = input('Enter any key to continue... ')