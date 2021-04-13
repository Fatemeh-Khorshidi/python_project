# General book_list
book_list = []
magazine_list = []
podcast_list = []
audiobook_list = []

import sys

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

sys.setrecursionlimit(10 ** 6)

class Book:
    """
    this is parent class
    """
    def __init__(self, title, author, publish_year, pages, language, price, read_pages= None,state=None, read=None, progress = None):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.read = read
        self.read_pages = read_pages
        self.state = state
        self.progress = progress

    def get_data(self, *args, **kwargs):
        """
        this function get book informations from user
        get the input and split tem in the list
        """
        print("\n======BOOK INFORMATION=======\n")
        print(" please split them with '|'")

        book_infos = [item.strip() for item in input("Enter the title, author, publish_year, pages, "
                                                     "language, and price of book: \n ").split("|")]
        """
        defined the list items to the class objects 
        """
        title = book_infos[0]
        author = book_infos[1]
        publish_year = int(book_infos[2])
        pages = int(book_infos[3])
        language = book_infos[4]
        price = int(book_infos[5])

        book_info = Book(title, author, publish_year, pages, language, price)
        book_list.append(book_info)

    def read(self):
        """
        This function take the number of read and left pages of book
        :return: the number of readen pages and left pages
        """
        # Show bookshelf list
        print("Please select your book:")
        for item in book_list:
            print('-', item.title)

        selected_book = input("Your choice: ").strip()

        # find book
        flag = False  # for find
        for item in book_list:
            if item.title == selected_book:
                flag = True
                self.read_pages = int(input("\n OK, How many pages do you read till now? "))
                left_pages = int(item.pages) - self.read_pages

                if left_pages < 0:
                    print('Your input is more than book pages !!!')
                    menu()

                elif left_pages == 0:
                    print('Congrats, You finished the book !')
                    item.read = self.read_pages

                else:
                    print('You have read {} pages, and still {} pages remain to finish the book.'.format(self.read_pages, left_pages))
                    item.read = self.read_pages

                break
        if flag == False:
            print('Your book not found !')
            menu()

        return self.read_pages

    def get_status(self):

        """
            based on number of readen pages , return 3 status:
        """
        for item in book_list:
            if self.read_pages == 0:
                self.state = 'unread'
            elif int(self.read_pages) > 0 and int(self.read_pages) < int(item.pages):
                self.state = 'reading'
            elif int(self.read_pages) == int(item.pages):
                self.state = 'finished'
            else:
                print("error")

            print(f"your state is {self.state}")

    def progress(self):
        """
        This function calculate the percent of read or listen
        Becouse the data record to the total list, loop in the list items
        """
        for item in book_list:

            self.progress = round((self.read_pages / item.pages) * 100, 1)

            print(f'Your Progress of {item.title} is {self.progress} %')

    def __str__(self):

        return f'the book is "{self.title}" and writen by "{self.author}",this book published in {self.publish_year}' \
               f' and have {self.pages} pages. this book\'s language is "{self.language}"' \
               f' and it\'s price is {self.price} $ .'


class Magazine(Book):
    def __init(self, title, author, publish_year, pages, language, price, issue):
        super().__init__(self, title, author, publish_year, pages, language, price)
        self.issue = issue

    def get_magazine_data(self, *args, **kwargs):
        print("\n======MAGAZINE INFORMATION=======\n")
        print("\n please split them with '|'")
        magazine_infos = [item.strip() for item in input("Enter the title, author,publish_year, pages, language,"
                          " price and issue of magazine: \n ").split("|")]

        title = magazine_infos[0]
        author = magazine_infos[1]
        publish_year = int(magazine_infos[2])
        pages = int(magazine_infos[3])
        language = magazine_infos[4]
        price = int(magazine_infos[5])
        issue = magazine_infos[6]

        magazine_info = Magazine(title, author, publish_year, pages, language, price, issue)
        magazine_list.append(magazine_info)

        return magazine_list

    def __str__(self):

        return f'the magazine is "{self.title}" and writen by "{self.author}",' \
               f'this magazine published in {self.publish_year}' \
               f' and have {self.pages} pages. this magazine\'s language is "{self.language}"' \
               f' and it\'s price is {self.price} $ .'


class PodcastEpisode(Book):
    def __init__(self, title, speaker, publish_year, time, language, price, listened_time=None, left_times=None):
        super().__init__(title, speaker, publish_year, time, language, price)
        self.speaker = speaker
        self.time = time
        self.listened_time = listened_time
        self.left_times = left_times

    def get_podcast_data(self):

        print("\n======PODCAST INFORMATION=======\n")
        print("\n please split them with '|'")
        podcast_infos = [item.strip() for item in input("Enter the title, speaker, publish year, "
                                                        "time, language, and price of podcast: \n ").split("|")]

        title = podcast_infos[0]
        speaker = podcast_infos[1]
        publish_year = int(podcast_infos[2])
        time = int(podcast_infos[3])
        language = podcast_infos[4]
        price = int(podcast_infos[5])

        podcast_info = PodcastEpisode(title, speaker, time, publish_year, language, price)
        podcast_list.append(podcast_info)

        return podcast_list

    def listen(self):
        # Show bookshelf list
        print("Please select your podcast:")
        for item in podcast_list:
            print('-', item.title)

        selected_podcast = input("Your choice: ").strip()

        # find podcast
        flag = False  # for find
        for item in podcast_list:
            if item.title == selected_podcast:
                flag = True
                self.listened_time = int(input("\n OK, How much time do you listen till now? "))
                left_times = int(item.time) - self.listened_time

                if left_times < 0:
                    print('Your input is more than total podcast time !!!')
                    menu()

                elif left_times == 0:
                    print('Congrats, You finished the podcast !')
                    item.listen_time = self.listened_time

                else:
                    print(
                        'You have listen {} time, and still {} time remain to finish the podcast.'.format(self.listened_time,
                                                                                                       left_times))
                    item.listen_time = self.listened_time

                break
        if flag == False:
            print('Your podcast not found !')
            menu()

        return self.listened_time

    def get_status(self):

        """
            based on number of readen pages , return 3 status:
        """
        for item in podcast_list:
            if self.listened_time == 0:
                self.state = 'unread'
            elif int(self.listened_time) > 0 and int(self.listened_time) < int(item.time):
                self.state = 'reading'
            elif int(self.listened_time) == int(item.time):
                self.state = 'finished'
            else:
                print("error")

            print(f"your state is {self.state}")

    def __str__(self):

        return f'the podcast is "{self.title}" and speak by "{self.speaker}",' \
               f'this podcast published in {self.publish_year}' \
               f' and have {self.time} pages. this podcast\'s language is "{self.language}"' \
               f' and it\'s price is {self.price} $ .'


class Audiobook(Book):
    def __init__(self, title, speaker, author, publish_year, pages, time, book_language, audio_language, price, state=None):
        super().__init__(title, speaker, publish_year, time, book_language, price)
        self.book_language = book_language
        self.audio_language = audio_language
        self.state = state
        self.author = author
        self.pages = pages

        self.time = time
        self.speaker = speaker

    def get_audiobook_data(self):

        print()
        print("======AUDIOBOOK INFORMATION=======")
        print("\n please split them with '|'")
        audiobook_infos = [item.strip() for item in input("Enter the title, speaker, author, publish_year, pages, time,"
                                                          " book_language, audio_language, price of audiobook: \n ").split("|")]

        title = audiobook_infos[0]
        speaker = audiobook_infos[1]
        author = audiobook_infos[2]
        publish_year = int(audiobook_infos[3])
        pages = int(audiobook_infos[4])
        time = int(audiobook_infos[5])
        book_language = audiobook_infos[6]
        audio_language = audiobook_infos[7]
        price = int(audiobook_infos[8])

        audio_info = Audiobook(title, speaker, author, publish_year, pages, time, book_language, audio_language, price)
        audiobook_list.append(audio_info)

        return audiobook_list

    def __str__(self):

        return f'the audiobook is "{self.title} and its speaker is {self.speaker}.' \
               f' this audiobook is written by {self.author} and published in {self.publish_year}.' \
               f' the books pages are {self.pages} and its time is {self.time}' \
               f'also the book language and the audio language is {self.book_language} and ' \
               f'{self.audio_language} and the price is {self.price} $. '


def sorting(sorted_list):
    # note: all progress most be inserted to all list !!!
    sorted_list = sorted(sorted_list, key=lambda x: x[9], reverse=True)
    print("sorted of each group -->", sorted_list[:])
    return sorted_list[:]

"""
---------------- main part of code------------------
===================user menu========================
Sample of input: No Friend But the Mountains | Behrouz Boochani | 2018 | 374 | English | 10 $
read(23, index)
read(23, list[index)]
"""

print('***************************  Create Your Personal Bookshelf   ***************************\n'
      ' ***************************************************************************************')
def menu():

    print("===================\n"
          "    LIBRARY MENU\n"
          "====================\n")
    print("what do you do?")
    print("1. Add a Book/Magazine/Podcast_Episode/Audiobook")
    print("2. Show my bookshelf")
    print("3. Add read pages or time listen")
    print("4. Sort my bookshelf")
    print("5. Exit")

    try:
        choice = int(input("please select your option: "))
    except:
        print('invalid input !')

    if choice == 1:

        # chose between book, magazine, podcast, audiobook:
        choose_item = input("Which item do you want to add? \n"
                            "              - book \n"
                            "              - magazine \n"
                            "              - podcast \n"
                            "              - audiobook \n")

        if choose_item == "book":
            Book.get_data = classmethod(Book.get_data)
            Book.get_data()
            menu()

        elif choose_item == "magazine":
            Magazine.get_magazine_data = classmethod(Magazine.get_magazine_data)
            Magazine.get_magazine_data()
            menu()

        elif choose_item == "podcast":
            PodcastEpisode.get_podcast_data = classmethod(PodcastEpisode.get_podcast_data)
            PodcastEpisode.get_podcast_data()
            menu()

        elif choose_item == "audiobook":
            Audiobook.get_audiobook_data = classmethod(Audiobook.get_audiobook_data)
            Audiobook.get_audiobook_data()
            menu()

        """
        after get data, return to the menu
        """

    elif choice == 2:
        """
        show the total items of bookshelf
        """
        for item in book_list:
            print(item)

        for item in magazine_list:
            print(item)

        for item in audiobook_list:
            print(item)

        for item in podcast_list:
            print(item)

        menu()

    elif choice == 3:
        # chose between book, magazine, podcast, audiobook:
        choose_item = input("Which item do you want to read? \n"
                            "              - book \n"
                            "              - magazine \n"
                            "              - podcast \n"
                            "              - audiobook \n")

        if choose_item == "book":
            Book.read = classmethod(Book.read)
            Book.read()
            Book.get_status = classmethod(Book.get_status)
            Book.get_status()
            Book.progress = classmethod(Book.progress)
            Book.progress()
            menu()

        elif choose_item == "magazine":
            Magazine.read = classmethod(Magazine.read)
            Magazine.read()
            Magazine.get_status = classmethod(Magazine.get_status)
            Magazine.get_status()
            Magazine.progress = classmethod(Magazine.progress)
            Magazine.progress()
            menu()

        elif choose_item == "podcast":
            PodcastEpisode.listen = classmethod(PodcastEpisode.listen)
            PodcastEpisode.listen()
            PodcastEpisode.get_status = classmethod(PodcastEpisode.get_status)
            PodcastEpisode.get_status()
            PodcastEpisode.progress = classmethod(PodcastEpisode.progress)
            PodcastEpisode.progress()
            menu()

        elif choose_item == "audiobook":
            Audiobook.listen = classmethod(Audiobook.listen)
            Audiobook.listen()
            Audiobook.get_status = classmethod(Audiobook.get_status)
            Audiobook.get_status()
            Audiobook.progress = classmethod(Audiobook.progress)
            Audiobook.progress()
            menu()

        menu()

    elif choice == 4:
        sorting(book_list)
        menu()

    elif choice == 5:
        exit()

    else:
        print("You made an invalid choice!")


"""
****************call start menu function****************
"""
if __name__ == "__main__":
    menu()

# 1|2|3|4|5|6|7|8|9