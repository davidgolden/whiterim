import time
import schedule
from populate import populate_form

if __name__ == '__main__':
    print('scheduled populate')
    schedule.every().day.at("23:59:35").do(populate_form)
    while True:
        schedule.run_pending()
        time.sleep(1)

