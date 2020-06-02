import time
import schedule

from populate import populate_form

populate_form()


# if __name__ == '__main__':
#     schedule.every().day.at("07:27:35").do(populate_form)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

