from Authentication.Authenticate import service
from datetime import datetime, timedelta



def Create_Reminder(start_date_time, timezone = '+05:30', note = 'No Notes', duration = 60, description = None, location = None):
    start_time = start_date_time
    end_time = start_time + timedelta(minutes = duration)
    event = {
        'summary' : note,
        'location' : location,
        'description' : description,
        'start' : {
            'dateTime' : start_time.strftime("%Y-%m-%dT%H:%M:%S{0}".format(timezone)),
        },
        'end' : {
            'dateTime' : end_time.strftime("%Y-%m-%dT%H:%M:%S{0}".format(timezone)),
        },
        'reminders' : {
            'useDefault' : False,
            'overrides' : [
                {
                    'method' : 'email',
                    'minutes' : 24 * 60
                },
                {
                    'method' : 'popup',
                    'minutes' : 15
                }
            ]
        }
    }
    return service.events().insert(calendarId = 'primary', body = event).execute()


def Show_Reminder(start_date):
    page_token = None
    count = 0
    while True:
        events = service.events().list(calendarId = 'primary', pageToken = page_token).execute()
        for event in events['items']:
            if start_date in event['start']['dateTime']:
                count += 1
                print('\nReminder-{0}'.format(count))
                print (event['summary'])
                print ('Start: {0}'.format(event['start']['dateTime']))
                print ('End: {0}'.format(event['end']['dateTime']))
        page_token = events.get('nextPageToken')
        if not page_token:
            break
    if count == 0:
        print('No Reminders found on this date !')


def Delete_Reminder(start_date):
    event_id = ''
    page_token = None
    while True:
        events = service.events().list(calendarId='primary', pageToken = page_token).execute()
        for event in events['items']:
            if start_date in event['start']['dateTime']:
                event_id = event['id']
                service.events().delete(calendarId = 'primary', eventId = event_id).execute()
                print('1 Reminder Deleted.')
                return
        page_token = events.get('nextPageToken')
        if not page_token:
            break
    print('No Notes found on this date !')