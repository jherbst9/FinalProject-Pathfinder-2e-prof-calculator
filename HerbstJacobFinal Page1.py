#By: Jacob Herbst
#Purpose: 

#Import tkinter
from tkinter import *

#Create starting page name it
root = Tk()
root.title("Pathfinder 2e Profficiecy Calcultor")


#Create and name skills page
def OpenSkillsPage():
    SkillsPage = Tk()
    SkillsPage.title("Skills")

    SkillsLevelLabel = Label(SkillsPage, text = "Level")
    SkillsLevelLabel.pack()
    SkillsLevel = Entry(SkillsPage)
    SkillsLevel = Entry(SkillsPage, width = 20)
    SkillsLevel.pack()
    
    StrengthLabel = Label(SkillsPage, text = "Strength modifier")
    StrengthLabel.pack()
    SkillsEntry = Entry(SkillsPage)
    SkillsEntry = Entry(SkillsPage, width = 20)
    SkillsEntry.pack()
    
    DexterityLabel = Label(SkillsPage, text = "Dexterity modifier")
    DexterityLabel.pack()
    SkillsDexterity = Entry(SkillsPage)
    SkillsDexterity = Entry(SkillsPage, width = 20)
    SkillsDexterity.pack()

    IntelligenceLabel = Label(SkillsPage, text = "Intelligence modifier")
    IntelligenceLabel.pack()
    SkillsIntelligence = Entry(SkillsPage)
    SkillsIntelligence = Entry(SkillsPage, width = 20)
    SkillsIntelligence.pack()

    WisdomLabel = Label(SkillsPage, text = "Wisdom modifier")
    WisdomLabel.pack()
    SkillsWisdom = Entry(SkillsPage)
    SkillsWisdom = Entry(SkillsPage, width = 20)
    SkillsWisdom.pack()

    CharismaLabel = Label(SkillsPage, text = "Charisma modifier")
    CharismaLabel.pack()
    SkillsCharisma = Entry(SkillsPage)
    SkillsCharisma = Entry(SkillsPage, width = 20)
    SkillsCharisma.pack()





#Create and name Weapons/Armor page   
def OpenWeaponsPage():
    WeaponsArmorPage = Tk()
    WeaponsArmorPage.title("Weapons/Armor")

    WeaponsLevelLabel = Label(WeaponsArmorPage, text = "Level")
    WeaponsLevelLabel.pack()
    WeaponsLevel = Entry(WeaponsArmorPage)
    WeaponsLevel = Entry(WeaponsArmorPage, width = 20)
    WeaponsLevel.pack()









#Create and name Saves/Perception page    
def OpenSavesPage():
    SavesPerceptionPage = Tk()
    SavesPerceptionPage.title("Saves/Perception")

    SavesLevelLabel = Label(SavesPerceptionPage, text = "Level")
    SavesLevelLabel.pack()
    SavesLevel = Entry(SavesPerceptionPage)
    SavesLevel = Entry(SavesPerceptionPage, width = 20)
    SavesLevel.pack()
    

    
    DexterityLabel2 = Label(SavesPerceptionPage, text = "Dexterity modifier")
    DexterityLabel2.pack()
    SavesDexterity = Entry(SavesPerceptionPage)
    SavesDexterity = Entry(SavesPerceptionPage, width = 20)
    SavesDexterity.pack()

    ConstitutionLabel = Label(SavesPerceptionPage, text = "Constitution modifier")
    ConstitutionLabel.pack()
    Constitution = Entry(SavesPerceptionPage)
    Constitution = Entry(SavesPerceptionPage, width = 20)
    Constitution.pack()


    WisdomLabel2 = Label(SavesPerceptionPage, text = "Wisdom modifier")
    WisdomLabel2.pack()
    SavesWisdom = Entry(SavesPerceptionPage)
    SavesWisdom = Entry(SavesPerceptionPage, width = 20)
    SavesWisdom.pack()






#Buttons for Root Page to open other pages
#Button that opens Skills Page
ButtonSkills = Button(text = "Skills", command = OpenSkillsPage)
ButtonSkills.pack()

#Button that opens Weapons/Armor
ButtonWeapons = Button(text = "Weapons/Armor", command = OpenWeaponsPage)
ButtonWeapons.pack()

#Button that opens Saves/Perception
ButtonSaves = Button(text = "Saves/Perception", command = OpenSavesPage)
ButtonSaves.pack()











#Run main loop
root.mainloop()

