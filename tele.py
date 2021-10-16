import telebot
from pytube import  YouTube
import  os
import  datetime

# url = input("Input url from youtube: ")



# YouTube(url).streams.first().download('vid')
# vid  =YouTube(url).streams.get_by_resolution('480')
# vid.download()
# print(datetime.datetime.now())
current_path = os.path.abspath(os.getcwd())
token = '2090591774:AAFUVgZVsa2AGvsNRP0iZXdgSQmQSaWO6M8'
bot =telebot.TeleBot(token)

@bot.message_handler(commands=['start','старт'])
def start_message(message):
    username = message.from_user.first_name
    mess = 'Привет  ' + username + '  просто отправь мне ссылку на видео из YouTube и скачаю его!!'
    bot.send_message(message.chat.id, mess)
    # bot.send_message(message.chat.id, 'Привет', username, 'просто отправь мне ссылку на видео из YouTube и скачаю его!!!')


@bot.message_handler(content_types='text')
def downloader(message):


    url_from_youtube= message.text
    dow_path =current_path+'/videos'
    filename =str(datetime.datetime.now())
    yout = YouTube(url_from_youtube)
    bot.send_message(message.chat.id,'Пожалуйста подождите! \n ваше видео уже в пути..')
    # yout2=yout.streams.get_by_resolution('480p')
    # yout2.download(filename=filename, output_path=dow_path)
    # print(current_path+'/videos')
    YouTube(url_from_youtube).streams.filter(res="720p").first().download(filename=filename,
    output_path=dow_path)
    # url_from_youtube = message.text
    # YouTube(url_from_youtube).streams.first()
    path_url = dow_path + '/'+filename
    # vid = open(path_url,'rb')
    bot.send_message(message.chat.id, 'It is downloading!')
    vid = open(path_url,'rb')
    bot.send_video(message.chat.id,vid)
    

print('Bot is waiting!')
bot.infinity_polling()