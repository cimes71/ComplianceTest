from utils.botproc import BotProc
import csv


if __name__ == '__main__':


    search_list = []
    with open('patients.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            search_list.append(row[0])
        print(search_list)

    bot = BotProc()
    bot.login()
    bot.process_search_list(search_list)







