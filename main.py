from utils.botproc import BotProc
import utils.configs as config
from buildsheet import BuildSheet
import csv


if __name__ == '__main__':

    config = config.read_config()
    search_list = []
    with open('patients.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            search_list.append(row[0])
        print(search_list)

    bot = BotProc(config)
    bot.login()
    output_list = bot.process_search_list(search_list)
    for i in output_list:
        print(i)

    bs = BuildSheet()

    bs.insert_data(bs.creds, output_list, config)









