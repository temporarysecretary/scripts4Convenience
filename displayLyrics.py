# Building on the random lyric generator I made a bit ago,
# I decided that, rather than editing in the lyrics I wrote myself,
# I would like the lyrics to be displayed when triggered by a MIDI signal
# I wrote this program to do just that :)

# By the way, that song can be found at
# 

# YES, I KNOW THIS IS BAD PRACTICE. I plan on getting more acquainted with tkinter
# in the future...
import mido
from tkinter import *
from tkinter import ttk

# Open a MIDI port.
inPort = mido.open_input("loopMIDI Port 1")

# Create window
root = Tk()
root.title("words and music and words and music and words and music and words and music and ")
root.geometry("600x600")

# Delay time to avoid magic numbers.
delayTime = 1

# This long ass string of characters was randomly generated
lyrics = "ぱひこつむぞたぬきえせてぼるおはだでもかとろもぼずかとぞさごぴひなけどぼへらおぼへぬぎぞのずほぐぶくたぷずしとひうつのうりがゆむなけすあいすせよしおぶぬがらうべうづごほのゆしあぱめめきぷれきびわまあぱすどごそおもへぷひごぬぽつえるぼぼぴぶりさてねがぢだぺぎりみよみさみとぜせぎもへばじりぐうぽぬさざぷえよやそほつとぢひやぱぺにみがにべずおめばほぬすくずぷきぱほにちぴずげろぬとじうぺがごらひだぞにきめぶきだてあだだぞぜあぞぎやぺみうどげおみえずだじるよゆせれだかごぴぎのぜげだべごそじどぬほぎゆせうべみけづがごみかそきよぞぎじやぴせべでこらぐみとふるちぱごこひぢきじにのぜざぜのじだこぐわぞとめみだせぜぐうあぷくおなぎろぞみぺはいぬべぐねはぺまぢらちせぱびぴにでまぺらせがぽつたもとぱらふえせぴばへづばよむがでずえぶらづうだぬちきれぐけどやびぱぷだざのとかちびべれけばぼれろざるじどめがざぴぱぶださぱるたばぽたぱずすすぱみまもつりねざびひまらちけなみけざまぽえぐがろだしえむこたべやええぷてぷぶづうかずぬながげじでちえかずはてれぎむゆややはどめけれつぷぎせぶへふぴばけるづもぞろすせぺちごりぶがちぽそとはあつけりごもさおもめめねざもたぎもわづごばとすせべすよぴけらりづやつあびべびぢげけぜゆていきひきねかづかてれびげたざみぢにめれのにばぽえさねとこげまじろあへずちるぞぽばちもらおもぽだざぱえりしびなまぺよばぺくぶつばれなずぢしぽゆまにしけわべゆぢぶぺざびなぬりつばぞのぢぶみめげべぺだすつてのるあぶてたせりへあえぐもぎもぬりみやねとどきだうろるぜきだげぶめやりちざへぶづくめぞざざきうぢみいみりまぐひぺわもよさぺうぞうべどらるうのげべつけくゆわひまぎはへぞきまあぺめぐるけじわそぱぽぼにじぽなごらひぐくろゆぬるやぐぼなじるさほかかせおざさめぺくさでむとあすづぷがしぺぺひまぐついざれらぬなぴじやぬぴぼわみぷとずぼかぬわわげうがゆおわつげそへただどぽずたるみけへであぱそさべいぬづぽめごじのねめぜらぶだべぜめぐぷぱおぜくほぴひなよがこざやおばでなぜあたつきえひそわぽぢちまばぞでぷずてわづごらいけるざぼはぐづざぜまよもぼげぺきめにぺふめめむすぼぴぜらぢぷぴゆえぽだものふぷおろみびぼよぐでぜさざかそなとべぱざぺぬがぜろついらそつあおぢじぢやもはれむひふほわぶるううがそどむぽがけわくぬせへぽぽわめりぽはなひはねぴぶよなぢかもりしげへががてげさ"
iterator_lyrics = iter(lyrics)

# Initialize text variables & labels
tetoSpeech = StringVar(root, "707c")
tetoLabel = Label(root, textvariable=tetoSpeech, height = 600)
tetoLabel.config(font=("Arial", 192))
tetoLabel.pack()

# Define the midiCallback: i.e., what happens to the labels when
# a MIDI note is received
def midiCallback():
    # Check if there is a MIDI message
    msg = inPort.poll()

    # If not, do nothing and reschedule this function
    if msg is None:
        print("No message, waiting")
        root.after(delayTime, midiCallback)
    # If there is, first check and see that it's the kind we want
    else:
        print("There is a message!")
        # If it is, update the label and make it say the next syllable in the lyric sheet
        if msg.type == 'note_on':
            tetoSpeech.set(next(iterator_lyrics, -1))
            root.after(delayTime, midiCallback)
        # If it isn't, do nothing and reschedule this function
        else:
            root.after(delayTime, midiCallback)

# Define the "destructor" function that will close our mido port for us
def onClose():
    print("Closing!!")
    inPort.close()
    root.destroy()

# Tell tkinter what's up
root.protocol("WM_DELETE_WINDOW", onClose)
root.after(1, midiCallback)
root.mainloop()
