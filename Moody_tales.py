#Here we are importing the  liabrary for the functions
import random #Random for creating random words
from playsound import playsound
import os




name = random.choice(["Gabriel", "Thor", "Jasper", "Raketh", "Tebbius", "David"])
mood = random.choice(["bright", "dark", "evil"])

import random
theme=random.choice(["real world","high fantasy","space sci-fi","alt-history","cyberpunk"])


if mood == "bright":
  adj = ["vast", "beautiful", "magestic", "colourful", "seemingly enchanted", "glittering", "magical", "seemingly peaceful", "peaceful"]
  enemy = random.choice(["Pokemon", "cat", "cuddly soft toy", "kangaroo", "koala"])



elif mood == "dark":
  adj = ["forboding", "imposing", "terrifying", "deathly", "cold", "desolate"]
  enemy = random.choice(["crow", "tiger", "swarm of wasps", "snake"])



elif mood == "evil":
  adj = ["evil", "cursed", "terrifying", "deathly", "frozen", "desolate", "horrific"]
  enemy = random.choice(["sorcerer", "necromancer", "zombie", "terminator", "army of aliens"])






# gens setting
if theme == "real world":
    subsetting=random.choice(["the USA","China","Europe","North Korea","Africa","the Middle East","Japan","Australia","the Bahamas"])
    setting=random.choice(["a small town in ","a big city in ","a farm in ","a school in ","the wilderness in ","the suburbs in ","the slums in ","the ocean""the entire world"])
  
  
    if setting != "the ocean" or "the entire world":
        setting=setting+subsetting
    age=random.choice(["newborn ","toddler ","child ","pre-teen ","teenager ","young adult ","adult ","middle aged ","elder "])
    race=random.choice(["africian ","africian ","hispanic ","arabic ","asian "])
    gengender=random.randint(0,100)


    if gengender <= 10:
         gender = ("transgender ")


    if gengender >= 9:
         if gengender >= 47:
             gender = ("male ")
         if gengender <= 46:
             gender = ("female ")


    protagonist=age+race+gender
    antagonist=random.choice(["a female","a male","a dictator","a corporation","a government","a tragic event","traffic","religion","a disease","a rival","the law","an old friend","a dog"])
if theme == "high fantasy":


    setting=random.choice(["The Great Empire","a vast desert","a dark corrupted land","a magic swamp","a unending labryinth","floating islands","a mystical forest","a frozen wasteland","a dangerous jungle land"])
    gender=random.choice(["male ","male ","male ","female ","female ","female ","magical transgender ","agender ","third gender "])
    race=random.choice(["human ","human ","elf ","orc ","dwarf ","gnome ","demon ","angel ","kitsune ","dark elf ","troll ","unicorn "])
    classs=random.choice(["marksmen ","warrior ","wizard ","bard ","thief ","merchant","knight ","spellsword ","peasant ","necromancer ","preist ","bandit ","monarch"])
    protagonist = gender+race+classs
    antagonist=random.choice(["a female","a male","an entire race","a god","an evil mage","an order of knights","evil itself","a giant","an invading army","a tyrant","magic","a greedy merchant","a monster","a dragon"])
if theme == "space sci-fi":


    setting=random.choice(["the deep void of space","an asteroid belt","an ice planet","a lava planet","a gas giant","an alien home world","future Earth","another galaxy, far far away","the multiverse"])
    protagonist=random.choice(["human","robot","hive mind","alien","alien","blob","human"])
    antagonist=random.choice(["a female","a male","an entire alien race","a starfleet","an alien","an artifical intellgence","a galactic federation","a glitch in space-time","an invading army","a incredibly infectious space fungus","the limits of science","a robot"])


if theme == "alt-history":
    setting=random.choice(["America","Religion","the Classical Era","the Middle Ages","the Renaissance","the Industrial Era","World War I","World War II","the Modern Era"])
    if setting == "America":
        figures=["Abraham Lincoln","George W. Bush Jr.","Benjamin Franklin","Donald Trump","Ronald Reagan","John Adams","Hilary Clinton","King George III","King George Washington","Andrew Jackson","Thomas Edison","Steve Jobs"]
        figure=random.choice(figures)
        antagonist=random.choice(figures)
    
    
    if setting == "Religion":
        figure=random.choice(["Jesus","Muhammad","Buddha","Krishna","Moses","L. Ron Hubbard","Joseph Smith","Zeus","Ra","Thor"])
        antagonist=random.choice(["Christianity","Islam","Hinduism","Buddhism","Greek mythology","Scientology","the Mormons","Paganism","Heresies"])
  
  
    if setting == "the Classical Era":
        figures=["Alexander The Great","Julius Caesar","Aristotle","King Tut","Qin Shi Huang","Homer","Augustus","Plato","Cleopatra","Ashoka","Attila the Hun","Leonidas"]
        figure=random.choice(figures)
        antagonist=random.choice(figures)
    
    
    if setting == "the Middle Ages":
        figures=["Charlemagne","Ghenghis Khan","Saladin","William the Conqueror","Ragnar Lodbrok","Oda Nobunaga","King Richard III","William Wallace","El Cid","Eleanor of Aquitaine","Erik the Red","Vlad the Impaler"]
        figure=random.choice(figures)
        antagonist=random.choice(figures)
  
  
    if setting == "the Renaissance":
        figures=["Marco Polo","Joan of Arc","Christopher Columbus","Blackbeard","Leonardo da Vinci","William Shakespeare","Henry VIII","Michelangelo","Donatello","Galileo","Admiral Yi Sun-sin","Suleiman the Magnificent"]
        figure=random.choice(figures)
        antagonist=random.choice(figures)
   
   
    if setting == "the Industrial Era":
        figures=["Henry Ford","Karl Marx","Charles Dickens","John D. Rockefeller","Thomas Edison","Nikola Tesla","Amelia Earheart","Frank C. Mars","Albert Einstein","Napoleon","Ghandi","Mark Twain"]
        figure=random.choice(figures)
        antagonist=random.choice(figures)
   
   
    if setting == "World War I":
        figure=random.choice(["Woodrow Wilson","Winston Churchill","Tsar Nicholas II","Lenin","Paul von Hindenburg","Ataturk"])
        antagonist=random.choice(["the Ottoman Empire","Germany","the United States","Britain","Austria-Hungary","France"])
  
  
    if setting == "World War II":
       figure=random.choice(["Hitler","Queen Elizabeth","Franklin D. Roosevelt","Joseph Stalin","Harry Truman","General Hideki Tojo"])
       antagonist=random.choice(["the United States","Germany","the Soviet Union","the United Kingdom","Japan","Italy"])
   
   
    if setting == "the Modern Era":
        figures=["Obama","Putin","Kim Jong-un","Kanye West","Bill Gates","Guido van Rossum","The Beatles","ISIS","Pope Francis","Mike Tyson","Pewdiepie","Hilary Cliton"]
        figure=random.choice(figures)
        antagonist=random.choice(figures)
    afigure=("figure known as ")     
    protagonist= afigure+figure     


if theme == "cyberpunk":
    setting=random.choice(["high-tech Tokyo","New New York","a dystopia","a utopia","a computer simulation","the SuperWeb","Mega Silicon Valley","an underwater city","an extensive underground facility"])
    gender=random.choice(["male ","male ","female ","female ","robogender ","unigender ","agender ","mega genderfluid ","third gender "])
    classs=random.choice(["hacker","cyborg","DJ","technopath","engineer","bomber","corporate","street rat","anarchist"])
    protagonist=gender+classs
    
    antagonist=random.choice(["a large corporation","an evil AI","Python","a gang","a secret society","a new technology","robots","internet trolls","the most powerful cyborg"])

conflict=random.choice(["fell in love with ","fought against ","attempted to stop ","defended against ","tried to befriend ","explored with ","tried to evade ","competed with ","exceeded beyond ","sought revenge against "])
end=random.choice(["It did not end well.","It ended very well.","Died tragically.","Lived happily ever after.","It ended sadly.","It was glorious.","In the end, nothing changed.","It ended with a twist.","Gave up."])







from tkinter import *    #Tkinter for GUI application
from tkinter.ttk import *


#Working with tkinter for creating GUI to take input from the user;

root=Tk()
root.title("Story creator")

#create label in python
head_title=Label(root,text= 'Welcome You to this application where story can be created as per your mood demands ')
head_title.grid(row=0,column=0,padx=4,pady=7)
head_title.configure(foreground='Black',background='Yellow')

auto_title=Label(root,text= 'Auto mode:Let machine to choose')
head_title.grid(row=3,column=1,padx=2,pady=2,sticky=E)
head_title.configure(foreground='Black')

#create label in python
mood_title=Label(root,text= 'You can choose Your MOOD from this combo Box')
mood_title.grid(row=1,column=0,padx=2,pady=2,sticky=W)
mood_title.configure(foreground='BLUE')

theme_title=Label(root,text= 'You can choose Your THEME from this combo Box')
theme_title.grid(row=2,column=0,padx=2,pady=2,sticky=W)
theme_title.configure(foreground='BLUE')

#combo box
ur_mood_var=StringVar()
ur_mood_combobox=Combobox(root,width=14,textvariable=ur_mood_var,state='readonly')
ur_mood_combobox['values']=('bright','dark','evil')
ur_mood_combobox.grid(row=1,column=1)
ur_mood_combobox.current(0)

ur_theme_var=StringVar()
ur_theme_combobox=Combobox(root,width=14,textvariable=ur_theme_var,state='readonly')
ur_theme_combobox['values']=("real world","high fantasy","space sci-fi","alt-history","cyberpunk")
ur_theme_combobox.grid(row=2,column=1)
ur_theme_combobox.current(0)


checkbtn_var=IntVar()
checkbtn=Checkbutton(root,variable=checkbtn_var)
checkbtn.grid(row=3,column=0)

def autoyes():
    print('You choosen yes to auto, So here is a story suggested by machine: ')
    Save="In the"+theme+"setting of"+setting+", there was a"+ protagonist+ "who"+conflict+antagonist+"."
   
    from gtts import gTTS

# This module is imported so that we can
# play the converted audio
    import os

# The text that you want to convert to audio
    
# Language in which you want to convert
    language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
    myobj = gTTS(text=Save, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
    myobj.save("welcome.mp3")

# Playing the converted file
    file = "welcome.mp3"
    playsound(file)


user_mood=ur_mood_var.get()
user_theme=ur_theme_var.get()
user_auto= checkbtn_var.get()

def autono():
    print(f'You chossen mood', user_mood, 'and the theme is', user_theme, 'Well here is the story of your demand: \n')


def action():

    if checkbtn_var.get()==0:
        auto='No'
        autoyes()
    else:
        auto='Yes'
        autoyes()
        
    

    
submit_button= Button(root,text='Submit', command=action)
submit_button.grid(row=5,column=1,padx=3,pady=3)



root.mainloop()










