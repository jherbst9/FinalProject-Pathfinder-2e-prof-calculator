#By: Jacob Herbst
#Purpose: Tkinter program to calculate proficiencys for pathfinder 2e

#Import tkinter
from tkinter import *

 

#set up main
def main():
    #Create root window
    root = Tk()
    #name root window 
    root.title("Pathfinder 2e Proficiecy Calcultor")
    #set root window size
    root.geometry("500x500")


##################################################################################################################################
#set up the window for Skills Page

    #set command to open new window for skills page
    def OpenSkillsPage():
        #Create , name and, set size of skills page
        SkillsPage = Tk()
        SkillsPage.geometry("900x550")
        SkillsPage.title("Skills")


        #entry box format
        # create a place on Skills Page to store a users level entry value
        SkillsLevelString = StringVar(SkillsPage, 0)
        #Create a label for level 
        SkillsLevelLabel = Label(SkillsPage, text = "Level").grid(row=0, column=0)
        #Create a entry box for level on skill page
        SkillsLevel = Entry(SkillsPage,textvariable=SkillsLevelString).grid(row=0, column=1)
        #Set Level entry box size
        SkillsLevel = Entry(SkillsPage, width = 10)

        #Skills Page Strength Lable and entry box
        SkillsStrengthString = StringVar(SkillsPage, 0)
        StrengthLabel = Label(SkillsPage, text = "Strength modifier").grid(row=0, column=2)
        SkillsEntry = Entry(SkillsPage, textvariable=SkillsStrengthString).grid(row=0, column=3)
        SkillsEntry = Entry(SkillsPage, width = 10)

        #Skills Page Dexterity Lable and entry box
        SkillsDexterityString = StringVar(SkillsPage, 0)
        DexterityLabel = Label(SkillsPage, text = "Dexterity modifier").grid(row=0, column=4)
        SkillsDexterity = Entry(SkillsPage, textvariable=SkillsDexterityString).grid(row=0, column=5)
        SkillsDexterity = Entry(SkillsPage, width = 10)

        #Skills Page Intelligence Lable and entry box
        SkillsIntelligenceString = StringVar(SkillsPage, 0)
        IntelligenceLabel = Label(SkillsPage, text = "Intelligence modifier").grid(row=1, column=0)
        SkillsIntelligence = Entry(SkillsPage, textvariable=SkillsIntelligenceString).grid(row=1, column=1)
        SkillsIntelligence = Entry(SkillsPage, width = 10)

        #Skills Page Wisdom Lable and entry box
        SkillsWisdomString = StringVar(SkillsPage ,0)
        WisdomLabel = Label(SkillsPage, text = "Wisdom modifier").grid(row=1, column=2)
        SkillsWisdom = Entry(SkillsPage, textvariable=SkillsWisdomString).grid(row=1, column=3)
        SkillsWisdom = Entry(SkillsPage, width = 10)

        #Skills Page Charisma Lable and entry box
        SkillsCharismaString = StringVar(SkillsPage, 0)
        CharismaLabel = Label(SkillsPage, text = "Charisma modifier").grid(row=1, column=4)
        SkillsCharisma = Entry(SkillsPage, textvariable=SkillsCharismaString).grid(row=1, column=5)
        SkillsCharisma = Entry(SkillsPage, width = 10)


        #set up command to calcuate skill proficiency
        def CalculateSkillProficiency():

            #Proficiency calculate example for skills page
            #First chech if the radio button is set to untrained. You only need to add the level to proficiendy if it is a minimum of trained
            if acrobatics.get() ==0:
                #Radio button value is 0 and its untrained so dont add level to proficiency
                profAcrobatics = (float(SkillsDexterityString.get()))
                #Show user proficiency
                AcrobaticsFinalProf = Label(SkillsPage, text = ("Your Acrobatics Proficiency is :", profAcrobatics))
                #place proficiency on grid
                AcrobaticsFinalProf.grid(row=3, column=6)
            #If radio button is not set to untrained you now add extra bonuses
            else:
                #get bonus from adding entry box level , radio button value, and entry box dexterity modifier
                profAcrobatics = (acrobatics.get()+ float(SkillsLevelString.get()) + float(SkillsDexterityString.get()))
                #Show user proficiency
                AcrobaticsFinalProf = Label(SkillsPage, text = ("Your Acrobatics Proficiency is :", profAcrobatics))
                #choose where on grid to place acrobatics proficiency
                AcrobaticsFinalProf.grid(row=3, column=6)

            #Calculate and show arcana proficiency
            if arcana.get() ==0:
                profArcana = (float(SkillsIntelligenceString.get()))
                ArcanaFinalProf = Label(SkillsPage, text = ("Your Arcana Proficiency is :", profArcana))
                ArcanaFinalProf.grid(row=4, column=6)
            
            else:
                profArcana = (arcana.get()+ float(SkillsLevelString.get()) + float(SkillsIntelligenceString.get()))
                ArcanaFinalProf = Label(SkillsPage, text = ("Your Arcana Proficiency is :", profArcana))
                ArcanaFinalProf.grid(row=4, column=6)

            #Calculate and show athletics proficiency
            if athletics.get() ==0:
                profAthletics = (float(SkillsStrengthString.get()))
                AthleticsFinalProf = Label(SkillsPage, text = ("Your Athletics Proficiency is :", profAthletics))
                AthleticsFinalProf.grid(row=5, column=6)
            else:
                profAthletics = (athletics.get()+ float(SkillsLevelString.get()) + float(SkillsStrengthString.get()))
                AthleticsFinalProf = Label(SkillsPage, text = ("Your Athletics Proficiency is :", profAthletics))
                AthleticsFinalProf.grid(row=5, column=6)

            #Calculate and show crafting proficiency
            if crafting.get() ==0:
                profCrafting = (float(SkillsIntelligenceString.get()))
                CraftingFinalProf = Label(SkillsPage, text = ("Your Crafting Proficiency is :", profCrafting))
                CraftingFinalProf.grid(row=6, column=6)
            else:
                profCrafting = (crafting.get()+ float(SkillsLevelString.get()) + float(SkillsIntelligenceString.get()))
                CraftingFinalProf = Label(SkillsPage, text = ("Your Crafting Proficiency is :", profCrafting))
                CraftingFinalProf.grid(row=6, column=6)

            #Calculate and show deception proficiency
            if deception.get() ==0:
                profDeception = (float(SkillsCharismaString.get()))
                DeceptionFinalProf = Label(SkillsPage, text = ("Your Deception Proficiency is :", profDeception))
                DeceptionFinalProf.grid(row=7, column=6)
            else:
                profDeception = (deception.get()+ float(SkillsLevelString.get()) + float(SkillsCharismaString.get()))
                DeceptionFinalProf = Label(SkillsPage, text = ("Your Deception Proficiency is :", profDeception))
                DeceptionFinalProf.grid(row=7, column=6)

            #Calculate and show diplomacy proficiency
            if diplomacy.get() ==0:
                profDiplomacy = (float(SkillsCharismaString.get()))
                DiplomacyFinalProf = Label(SkillsPage, text = ("Your Diplomacy Proficiency is :", profDiplomacy))
                DiplomacyFinalProf.grid(row=8, column=6)
            else:
                profDiplomacy = (diplomacy.get()+ float(SkillsLevelString.get()) + float(SkillsCharismaString.get()))
                DiplomacyFinalProf = Label(SkillsPage, text = ("Your Diplomacy Proficiency is :", profDiplomacy))
                DiplomacyFinalProf.grid(row=8, column=6)

            #Calculate and show intimidation proficiency
            if intimidation.get() ==0:
                profIntimidation = (float(SkillsCharismaString.get()))
                IntimidationFinalProf = Label(SkillsPage, text = ("Your Intimidation Proficiency is :", profIntimidation))
                IntimidationFinalProf.grid(row=9, column=6)
            else:
                profIntimidation = (intimidation.get()+ float(SkillsLevelString.get()) + float(SkillsCharismaString.get()))
                IntimidationFinalProf = Label(SkillsPage, text = ("Your Intimidation Proficiency is :", profIntimidation))
                IntimidationFinalProf.grid(row=9, column=6)

            #Calculate and show lore proficiency
            if lore.get() ==0:
                profLore = (float(SkillsIntelligenceString.get()))
                LoreFinalProf = Label(SkillsPage, text = ("Your Lore Proficiency is :", profLore))
                LoreFinalProf.grid(row=10, column=6)
            else:
                profLore = (lore.get()+ float(SkillsLevelString.get()) + float(SkillsIntelligenceString.get()))
                LoreFinalProf = Label(SkillsPage, text = ("Your Lore Proficiency is :", profLore))
                LoreFinalProf.grid(row=10, column=6)

            #Calculate and show medicine proficiency
            if medicine.get() ==0:
                profMedicine = (float(SkillsWisdomString.get()))
                MedicineFinalProf = Label(SkillsPage, text = ("Your Medicine Proficiency is :", profMedicine))
                MedicineFinalProf.grid(row=11, column=6)
            else:
                profMedicine = (medicine.get()+ float(SkillsLevelString.get()) + float(SkillsWisdomString.get()))
                MedicineFinalProf = Label(SkillsPage, text = ("Your Medicine Proficiency is :", profMedicine))
                MedicineFinalProf.grid(row=11, column=6)

            #Calculate and show nature proficiency
            if nature.get() ==0:
                profNature = (float(SkillsWisdomString.get()))
                NatureFinalProf = Label(SkillsPage, text = ("Your Nature Proficiency is :", profNature))
                NatureFinalProf.grid(row=12, column=6)
            else:
                profNature = (nature.get()+ float(SkillsLevelString.get()) + float(SkillsWisdomString.get()))
                NatureFinalProf = Label(SkillsPage, text = ("Your Nature Proficiency is :", profNature))
                NatureFinalProf.grid(row=12, column=6)

            #Calculate and show occultism proficiency
            if occultism.get() ==0:
                profOccultism = (float(SkillsIntelligenceString.get()))
                OccultismFinalProf = Label(SkillsPage, text = ("Your Occultism Proficiency is :", profOccultism))
                OccultismFinalProf.grid(row=13, column=6)
            else:
                profOccultism = (occultism.get()+ float(SkillsLevelString.get()) + float(SkillsIntelligenceString.get()))
                OccultismFinalProf = Label(SkillsPage, text = ("Your Occultism Proficiency is :", profOccultism))
                OccultismFinalProf.grid(row=13, column=6)

            #Calculate and show performance proficiency
            if performance.get() ==0:
                profPerformance = (float(SkillsCharismaString.get()))
                PerformanceFinalProf = Label(SkillsPage, text = ("Your Performance Proficiency is :", profPerformance))
                PerformanceFinalProf.grid(row=14, column=6)
            else:
                profPerformance = (performance.get()+ float(SkillsLevelString.get()) + float(SkillsCharismaString.get()))
                PerformanceFinalProf = Label(SkillsPage, text = ("Your Performance Proficiency is :", profPerformance))
                PerformanceFinalProf.grid(row=14, column=6)
    
            #Calculate and show religion proficiency
            if religion.get() ==0:
                profReligion = (float(SkillsWisdomString.get()))
                ReligionFinalProf = Label(SkillsPage, text = ("Your Religion Proficiency is :", profReligion))
                ReligionFinalProf.grid(row=15, column=6)

            else:
                profReligion = (religion.get()+ float(SkillsLevelString.get()) + float(SkillsWisdomString.get()))
                ReligionFinalProf = Label(SkillsPage, text = ("Your Religion Proficiency is :", profReligion))
                ReligionFinalProf.grid(row=15, column=6)

            #Calculate and show society proficiency
            if society.get() ==0:
                profSociety = (float(SkillsIntelligenceString.get()))
                SocietyFinalProf = Label(SkillsPage, text = ("Your Society Proficiency is :", profSociety))
                SocietyFinalProf.grid(row=16, column=6)

            else:   
                profSociety = (society.get()+ float(SkillsLevelString.get()) + float(SkillsIntelligenceString.get()))
                SocietyFinalProf = Label(SkillsPage, text = ("Your Society Proficiency is :", profSociety))
                SocietyFinalProf.grid(row=16, column=6)

            #Calculate and show stealth proficiency
            if stealth.get() ==0:
                profStealth = (float(SkillsDexterityString.get()))
                StealthFinalProf = Label(SkillsPage, text = ("Your Stealth Proficiency is :", profStealth))
                StealthFinalProf.grid(row=17, column=6)
            else:
                profStealth = (stealth.get()+ float(SkillsLevelString.get()) + float(SkillsDexterityString.get()))
                StealthFinalProf = Label(SkillsPage, text = ("Your Stealth Proficiency is :", profStealth))
                StealthFinalProf.grid(row=17, column=6)

            #Calculate and show survival proficiency
            if survival.get() == 0:
                profSurvival = (float(SkillsWisdomString.get()))
                SurvivalFinalProf = Label(SkillsPage, text = ("Your Survival Proficiency is :", profSurvival))
                SurvivalFinalProf.grid(row=18, column=6)

            else:
                profSurvival = (survival.get()+ float(SkillsLevelString.get()) + float(SkillsWisdomString.get()))
                SurvivalFinalProf = Label(SkillsPage, text = ("Your Survival Proficiency is :", profSurvival))
                SurvivalFinalProf.grid(row=18, column=6)

            #Calculate and show thievery proficiency
            if thievery.get() == 0:
                profThievery = (float(SkillsDexterityString.get()))
                ThieveryFinalProf = Label(SkillsPage, text = ("Your Thievery Proficiency is :", profThievery))
                ThieveryFinalProf.grid(row=19, column=6)

            else:
                profThievery = (thievery.get()+ float(SkillsLevelString.get()) + float(SkillsDexterityString.get()))
                ThieveryFinalProf = Label(SkillsPage, text = ("Your Thievery Proficiency is :", profThievery))
                ThieveryFinalProf.grid(row=19, column=6)
            
        #skills radiobutton format
        #make a place for int value on skill page       
        acrobatics = IntVar(SkillsPage, 0)
        #make the dafault button untrained
        acrobatics.set(0)
        #create label for acrobatics
        AcrobaticsLabel = Label(SkillsPage, text="Acrobatics").grid(row=3, column=0)
        #Create acrobatics radio button named Untrained with number value 0
        AcrobaticsUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=acrobatics, value = 0).grid(row=3, column=1)
        #Create acrobatics radio button named Trained with number value 2
        AcrobaticsTrained = Radiobutton(SkillsPage, text="Trained", variable=acrobatics, value = 2).grid(row=3, column=2)
        #Create acrobatics radio button named Expert with number value 4
        AcrobaticsExpert = Radiobutton(SkillsPage, text="Expert", variable=acrobatics, value = 4).grid(row=3, column=3)
        #Create acrobatics radio button named master with number value 6
        AcrobaticsMaster = Radiobutton(SkillsPage, text="Master", variable=acrobatics, value =6 ).grid(row=3, column=4)
        #Create acrobatics radio button named Legendary with number value 8
        AcrobaticsLegendary = Radiobutton(SkillsPage, text="Legendary", variable=acrobatics, value = 8).grid(row=3, column=5)

        #Arcana Radio Buttons and labels
        arcana = IntVar(SkillsPage, 0)
        arcana.set(0)
        ArcanaLabel = Label(SkillsPage, text="Arcana").grid(row=4, column=0)
        ArcanaUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=arcana, value = 0).grid(row=4, column=1)
        ArcanaTrained = Radiobutton(SkillsPage, text="Trained", variable=arcana, value = 2).grid(row=4, column=2)
        ArcanaExpert = Radiobutton(SkillsPage, text="Expert", variable=arcana, value = 4).grid(row=4, column=3)
        ArcanaMaster = Radiobutton(SkillsPage, text="Master", variable=arcana , value =6 ).grid(row=4, column=4)
        ArcanaLegendary = Radiobutton(SkillsPage, text="Legendary", variable=arcana, value = 8).grid(row=4, column=5)

        #Athletics Radio Buttons and labels
        athletics = IntVar(SkillsPage, 0)
        athletics.set(0)
        AthleticsLabel = Label(SkillsPage, text="Athletics").grid(row=5, column=0)
        AthleticsUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=athletics, value = 0).grid(row=5, column=1)
        AthleticsTrained = Radiobutton(SkillsPage, text="Trained", variable=athletics, value = 2).grid(row=5, column=2)
        AthleticsExpert = Radiobutton(SkillsPage, text="Expert", variable=athletics, value = 4).grid(row=5, column=3)
        AthleticsMaster = Radiobutton(SkillsPage, text="Master", variable=athletics, value =6 ).grid(row=5, column=4)
        AthleticsLegendary = Radiobutton(SkillsPage, text="Legendary", variable=athletics, value = 8).grid(row=5, column=5)

        #Crafting Radio Buttons and labels
        crafting = IntVar(SkillsPage, 0)
        crafting.set(0)
        CraftingLabel = Label(SkillsPage, text="Crafting").grid(row=6, column=0)
        CraftingUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=crafting, value = 0).grid(row=6, column=1)
        CraftingTrained = Radiobutton(SkillsPage, text="Trained", variable=crafting, value = 2).grid(row=6, column=2)
        CraftingExpert = Radiobutton(SkillsPage, text="Expert", variable=crafting, value = 4).grid(row=6, column=3)
        CraftingMaster = Radiobutton(SkillsPage, text="Master", variable=crafting, value =6 ).grid(row=6, column=4)
        CraftingLegendary = Radiobutton(SkillsPage, text="Legendary", variable=crafting, value = 8).grid(row=6, column=5)

        #Deception Radio Buttons and labels
        deception = IntVar(SkillsPage, 0)
        deception.set(0)
        DeceptionLabel = Label(SkillsPage, text="Deception").grid(row=7, column=0)
        DeceptionUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=deception, value = 0).grid(row=7, column=1)
        DeceptionTrained = Radiobutton(SkillsPage, text="Trained", variable=deception, value = 2).grid(row=7, column=2)
        DeceptionExpert = Radiobutton(SkillsPage, text="Expert", variable=deception, value = 4).grid(row=7, column=3)
        DeceptionMaster = Radiobutton(SkillsPage, text="Master", variable=deception, value =6 ).grid(row=7, column=4)
        DeceptionLegendary = Radiobutton(SkillsPage, text="Legendary", variable=deception, value = 8).grid(row=7, column=5)

        #Diplomacy Radio Buttons and labels
        diplomacy = IntVar(SkillsPage, 0)
        diplomacy.set(0)
        DiplomacyLabel = Label(SkillsPage, text="Diplomacy").grid(row=8, column=0)
        DiplomacyUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=diplomacy, value = 0).grid(row=8, column=1)
        DiplomacyTrained = Radiobutton(SkillsPage, text="Trained", variable=diplomacy, value = 2).grid(row=8, column=2)
        DiplomacyExpert = Radiobutton(SkillsPage, text="Expert", variable=diplomacy, value = 4).grid(row=8, column=3)
        DiplomacyMaster = Radiobutton(SkillsPage, text="Master", variable=diplomacy, value =6 ).grid(row=8, column=4)
        DiplomacyLegendary = Radiobutton(SkillsPage, text="Legendary", variable=diplomacy, value = 8).grid(row=8, column=5)

        #Intimidation Radio Buttons and labels
        intimidation = IntVar(SkillsPage, 0)
        intimidation.set(0)
        IntimidationLabel = Label(SkillsPage, text="Intimidation").grid(row=9, column=0)
        IntimidationUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=intimidation, value = 0).grid(row=9, column=1)
        IntimidationTrained = Radiobutton(SkillsPage, text="Trained", variable=intimidation, value = 2).grid(row=9, column=2)
        IntimidationExpert = Radiobutton(SkillsPage, text="Expert", variable=intimidation, value = 4).grid(row=9, column=3)
        IntimidationMaster = Radiobutton(SkillsPage, text="Master", variable=intimidation, value =6 ).grid(row=9, column=4)
        IntimidationLegendary = Radiobutton(SkillsPage, text="Legendary", variable=intimidation, value = 8).grid(row=9, column=5)

        #Lore Radio Buttons and labels
        lore = IntVar(SkillsPage, 0)
        lore.set(0)
        LoreLabel = Label(SkillsPage, text="Lore").grid(row=10, column=0)
        LoreUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=lore, value = 0).grid(row=10, column=1)
        LoreTrained = Radiobutton(SkillsPage, text="Trained", variable=lore, value = 2).grid(row=10, column=2)
        LoreExpert = Radiobutton(SkillsPage, text="Expert", variable=lore, value = 4).grid(row=10, column=3)
        LoreMaster = Radiobutton(SkillsPage, text="Master", variable=lore, value =6 ).grid(row=10, column=4)
        LoreLegendary = Radiobutton(SkillsPage, text="Legendary", variable=lore, value = 8).grid(row=10, column=5)

        #Medicine Radio Buttons and labels
        medicine = IntVar(SkillsPage, 0)
        medicine.set(0)
        MedicineLabel = Label(SkillsPage, text="Medicine").grid(row=11, column=0)
        MedicineUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=medicine, value = 0).grid(row=11, column=1)
        MedicineTrained = Radiobutton(SkillsPage, text="Trained", variable=medicine, value = 2).grid(row=11, column=2)
        MedicineExpert = Radiobutton(SkillsPage, text="Expert", variable=medicine, value = 4).grid(row=11, column=3)
        MedicineMaster = Radiobutton(SkillsPage, text="Master", variable=medicine, value =6 ).grid(row=11, column=4)
        MedicineLegendary = Radiobutton(SkillsPage, text="Legendary", variable=medicine, value = 8).grid(row=11, column=5)

        #Nature Radio Buttons and labels
        nature = IntVar(SkillsPage, 0)
        nature.set(0)
        NatureLabel = Label(SkillsPage, text="Nature").grid(row=12, column=0)
        NatureUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=nature, value = 0).grid(row=12, column=1)
        NatureTrained = Radiobutton(SkillsPage, text="Trained", variable=nature, value = 2).grid(row=12, column=2)
        NatureExpert = Radiobutton(SkillsPage, text="Expert", variable=nature, value = 4).grid(row=12, column=3)
        NatureMaster = Radiobutton(SkillsPage, text="Master", variable=nature, value =6 ).grid(row=12, column=4)
        NatureLegendary = Radiobutton(SkillsPage, text="Legendary", variable=nature, value = 8).grid(row=12, column=5)

        #Occultism Radio Buttons and labels
        occultism  = IntVar(SkillsPage, 0)
        occultism.set(0)
        OccultismLabel = Label(SkillsPage, text="Occultism").grid(row=13, column=0)
        OccultismUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=occultism, value = 0).grid(row=13, column=1)
        OccultismTrained = Radiobutton(SkillsPage, text="Trained", variable=occultism, value = 2).grid(row=13, column=2)
        OccultismExpert = Radiobutton(SkillsPage, text="Expert", variable=occultism, value = 4).grid(row=13, column=3)
        OccultismMaster = Radiobutton(SkillsPage, text="Master", variable=occultism, value =6 ).grid(row=13, column=4)
        OccultismLegendary = Radiobutton(SkillsPage, text="Legendary", variable=occultism, value = 8).grid(row=13, column=5)

        #Performance Radio Buttons and labels
        performance  = IntVar(SkillsPage, 0)
        performance.set(0)
        PerformanceLabel = Label(SkillsPage, text="Performance").grid(row=14, column=0)
        PerformanceUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=performance, value = 0).grid(row=14, column=1)
        PerformanceTrained = Radiobutton(SkillsPage, text="Trained", variable=performance, value = 2).grid(row=14, column=2)
        PerformanceExpert = Radiobutton(SkillsPage, text="Expert", variable=performance, value = 4).grid(row=14, column=3)
        PerformanceMaster = Radiobutton(SkillsPage, text="Master", variable=performance, value =6 ).grid(row=14, column=4)
        PerformanceLegendary = Radiobutton(SkillsPage, text="Legendary", variable=performance, value = 8).grid(row=14, column=5)

        #Religion Radio Buttons and labels
        religion  = IntVar(SkillsPage, 0)
        religion.set(0)
        ReligionLabel = Label(SkillsPage, text="Religion").grid(row=15, column=0)
        ReligionUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=religion, value = 0).grid(row=15, column=1)
        ReligionTrained = Radiobutton(SkillsPage, text="Trained", variable=religion, value = 2).grid(row=15, column=2)
        ReligionExpert = Radiobutton(SkillsPage, text="Expert", variable=religion, value = 4).grid(row=15, column=3)
        ReligionMaster = Radiobutton(SkillsPage, text="Master", variable=religion, value =6 ).grid(row=15, column=4)
        ReligionLegendary = Radiobutton(SkillsPage, text="Legendary", variable=religion, value = 8).grid(row=15, column=5)

        #Society Radio Buttons and labels
        society  = IntVar(SkillsPage, 0)
        society.set(0)
        SocietyLabel = Label(SkillsPage, text="Society").grid(row=16, column=0)
        SocietyUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=society, value = 0).grid(row=16, column=1)
        SocietyTrained = Radiobutton(SkillsPage, text="Trained", variable=society, value = 2).grid(row=16, column=2)
        SocietyExpert = Radiobutton(SkillsPage, text="Expert", variable=society, value = 4).grid(row=16, column=3)
        SocietyMaster = Radiobutton(SkillsPage, text="Master", variable=society, value =6 ).grid(row=16, column=4)
        SocietyLegendary = Radiobutton(SkillsPage, text="Legendary", variable=society, value = 8).grid(row=16, column=5)

        #Stealth Radio Buttons and labels
        stealth  = IntVar(SkillsPage, 0)
        stealth.set(0)
        StealthLabel = Label(SkillsPage, text="Stealth").grid(row=17, column=0)
        StealthUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=stealth, value = 0).grid(row=17, column=1)
        StealthTrained = Radiobutton(SkillsPage, text="Trained", variable=stealth, value = 2).grid(row=17, column=2)
        StealthExpert = Radiobutton(SkillsPage, text="Expert", variable=stealth, value = 4).grid(row=17, column=3)
        StealthMaster = Radiobutton(SkillsPage, text="Master", variable=stealth, value =6 ).grid(row=17, column=4)
        StealthLegendary = Radiobutton(SkillsPage, text="Legendary", variable=stealth, value = 8).grid(row=17, column=5)

        #Survival Radio Buttons and labels
        survival  = IntVar(SkillsPage, 0)
        survival.set(0)
        SurvivalLabel = Label(SkillsPage, text="Survival").grid(row=18, column=0)
        SurvivalUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=survival, value = 0).grid(row=18, column=1)
        SurvivalTrained = Radiobutton(SkillsPage, text="Trained", variable=survival, value = 2).grid(row=18, column=2)
        SurvivalExpert = Radiobutton(SkillsPage, text="Expert", variable=survival, value = 4).grid(row=18, column=3)
        SurvivalMaster = Radiobutton(SkillsPage, text="Master", variable=survival, value =6 ).grid(row=18, column=4)
        SurvivalLegendary = Radiobutton(SkillsPage, text="Legendary", variable=survival, value = 8).grid(row=18, column=5)

        #Thievery Radio Buttons and labels
        thievery  = IntVar(SkillsPage, 0)
        thievery.set(0)
        ThieveryLabel = Label(SkillsPage, text="Thievery").grid(row=19, column=0)
        ThieveryUntrained = Radiobutton(SkillsPage, text="UnTrained", variable=thievery, value = 0).grid(row=19, column=1)
        ThieveryTrained = Radiobutton(SkillsPage, text="Trained", variable=thievery, value = 2).grid(row=19, column=2)
        ThieveryExpert = Radiobutton(SkillsPage, text="Expert", variable=thievery, value = 4).grid(row=19, column=3)
        ThieveryMaster = Radiobutton(SkillsPage, text="Master", variable=thievery, value =6 ).grid(row=19, column=4)
        ThieveryLegendary = Radiobutton(SkillsPage, text="Legendary", variable=thievery, value = 8).grid(row=19, column=5)


        #Command to close skills page
        def SkillsPageBackButton():
            SkillsPage.withdraw()
        #make button on skills page to run command to calculate proficiencys
        ButtonSkillsProf = Button(SkillsPage, text = "Calculate Proficiency", command = CalculateSkillProficiency).grid(row=20, column=0)
        #make button on skills page to run command to close skills page
        ButtonSkillsBack = Button(SkillsPage, text = "Back", command =  SkillsPageBackButton).grid(row=21, column=0)


##########################################################################################################################################
    #Create and name Weapons/Armor page

    #set command to open new window for Weapons Armor Page
    def OpenWeaponsPage():
        #Create , name and, set size of Weapons Armor Page
        WeaponsArmorPage = Tk()
        WeaponsArmorPage.title("Weapons/Armor")
        WeaponsArmorPage.geometry("900x400")

        #Add a label at top of weapon armor page
        WeaponsPageLabel = Label(WeaponsArmorPage, text="Weapons and Armor Proficiency Calculator").grid(row=0, column=0)
        

        #make a place on weapons armor page to store level
        WeaponsArmorLevelString = StringVar(WeaponsArmorPage, 0)
        #create level label to show user what to enter in extry box
        WeaponsArmorLevelLabel = Label(WeaponsArmorPage, text = "Level").grid(row=1, column=0)
        #create entry box for level
        WeaponsArmorLevel = Entry(WeaponsArmorPage,textvariable=WeaponsArmorLevelString).grid(row=1, column=1)
        #set entry box size
        WeaponsArmorLevel = Entry(WeaponsArmorPage, width = 10)


        #create a label for when weapons proficiencys start
        WeaponsLabel = Label(WeaponsArmorPage, text="Weapons Proficiency").grid(row=2, column=0)
        #create a label for when Armor proficiencys start
        WeaponsLabel = Label(WeaponsArmorPage, text="Armor Proficiency").grid(row=8, column=0)
    
        #Create command to caculate your proficiencys
        def CalculateWeaponsArmorProficiency():

            #Check if the radio button value is untrained
            if simpleWeapons.get() ==0:
            # Calculate proficiency with only radio button
                profSimpleWeapons = (simpleWeapons.get())
            #Display the simple weapons proficiency to user
                SimpleWeaponsProf = Label(WeaponsArmorPage, text = ("Your Simple Weapons Proficiency is :", profSimpleWeapons))
            #place you simple weapon proficiency
                SimpleWeaponsProf.grid(row=3, column=6)

            #The radio button in not untrained so add value with level
            else:
            # Get your Simple Weapons proficiency by adding together entered level with radio button value
                profSimpleWeapons = (simpleWeapons.get()+ float(WeaponsArmorLevelString.get()))
            #Display the simple weapons proficiency to user
                SimpleWeaponsProf = Label(WeaponsArmorPage, text = ("Your Simple Weapons Proficiency is :", profSimpleWeapons))
            #place you simple weapon proficiency
                SimpleWeaponsProf.grid(row=3, column=6)

            #calculate and display Martial Weapon Proficiency
            if martialWeapons.get() ==0:
                profMartialWeapons = (martialWeapons.get())
                MartialWeaponsProf = Label(WeaponsArmorPage, text = ("Your Martial Weapons Proficiency is :", profMartialWeapons))
                MartialWeaponsProf.grid(row=4, column=6)
            else:
                profMartialWeapons = (martialWeapons.get()+ float(WeaponsArmorLevelString.get()))
                MartialWeaponsProf = Label(WeaponsArmorPage, text = ("Your Martial Weapons Proficiency is :", profMartialWeapons))
                MartialWeaponsProf.grid(row=4, column=6)

            #calculate and display Advanced Weapon Proficiency
            if advancedWeapons.get() ==0:
                profAdvancedWeapons = (advancedWeapons.get())
                AdvancedWeaponsProf = Label(WeaponsArmorPage, text = ("Your Advanced Weapons Proficiency is :", profAdvancedWeapons))
                AdvancedWeaponsProf.grid(row=5, column=6)

            else:
                profAdvancedWeapons = (advancedWeapons.get()+ float(WeaponsArmorLevelString.get()))
                AdvancedWeaponsProf = Label(WeaponsArmorPage, text = ("Your Advanced Weapons Proficiency is :", profAdvancedWeapons))
                AdvancedWeaponsProf.grid(row=5, column=6)

            #calculate and display Unarmed Attack Proficiency
            if unarmedAttack.get() ==0:
                profUnarmedAttack = (unarmedAttack.get())
                UnarmedAttackProf = Label(WeaponsArmorPage, text = ("Your Unarmed Attack Proficiency is :", profUnarmedAttack))
                UnarmedAttackProf.grid(row=6, column=6)
            else:
                profUnarmedAttack = (unarmedAttack.get()+ float(WeaponsArmorLevelString.get()))
                UnarmedAttackProf = Label(WeaponsArmorPage, text = ("Your Unarmed Attack Proficiency is :", profUnarmedAttack))
                UnarmedAttackProf.grid(row=6, column=6)

            #calculate and display bomb Proficiency
            if bombs.get() ==0:
                profBombs = (bombs.get())
                BombsProf = Label(WeaponsArmorPage, text = ("Your Bomb Proficiency is :", profBombs))
                BombsProf.grid(row=7, column=6)
            else:
                profBombs = (bombs.get()+ float(WeaponsArmorLevelString.get()))
                BombsProf = Label(WeaponsArmorPage, text = ("Your Bomb Proficiency is :", profBombs))
                BombsProf.grid(row=7, column=6)


            #calculate and display Light Armor Proficiency
            if lightArmor.get() ==0:
                profLightArmor = (lightArmor.get())
                LightArmorProf = Label(WeaponsArmorPage, text = ("Your Light Armor Proficiency is :", profLightArmor))
                LightArmorProf.grid(row=9, column=6)
            else:
                profLightArmor = (lightArmor.get()+ float(WeaponsArmorLevelString.get()))
                LightArmorProf = Label(WeaponsArmorPage, text = ("Your Light Armor Proficiency is :", profLightArmor))
                LightArmorProf.grid(row=9, column=6)

            #calculate and display Medium Armor Proficiency
            if mediumArmor.get() ==0:
                profMediumArmor = (mediumArmor.get())
                MediumArmorProf = Label(WeaponsArmorPage, text = ("Your Medium Armor Proficiency is :", profMediumArmor))
                MediumArmorProf.grid(row=10, column=6)

            else:
                profMediumArmor = (mediumArmor.get()+ float(WeaponsArmorLevelString.get()))
                MediumArmorProf = Label(WeaponsArmorPage, text = ("Your Medium Armor Proficiency is :", profMediumArmor))
                MediumArmorProf.grid(row=10, column=6)

            #calculate and display Heavy Armor Proficiency
            if unarmoredDefense.get() ==0:
                profHeavyArmor = (heavyArmor.get())
                HeavyArmorProf = Label(WeaponsArmorPage, text = ("Your Heavy Armor Proficiency is :", profHeavyArmor))
                HeavyArmorProf.grid(row=11, column=6)
            else:
                profHeavyArmor = (heavyArmor.get()+ float(WeaponsArmorLevelString.get()))
                HeavyArmorProf = Label(WeaponsArmorPage, text = ("Your Heavy Armor Proficiency is :", profHeavyArmor))
                HeavyArmorProf.grid(row=11, column=6)

            #calculate and display Unarmored Defense Proficiency
            if unarmoredDefense.get() ==0:
                profUnarmoredDefense = (unarmoredDefense.get())
                UnarmoredDefenseProf = Label(WeaponsArmorPage, text = ("Your Unarmored Defense Proficiency is :", profUnarmoredDefense))
                UnarmoredDefenseProf.grid(row=12, column=6)
            else:
                profUnarmoredDefense = (unarmoredDefense.get()+ float(WeaponsArmorLevelString.get()))
                UnarmoredDefenseProf = Label(WeaponsArmorPage, text = ("Your Unarmored Defense Proficiency is :", profUnarmoredDefense))
                UnarmoredDefenseProf.grid(row=12, column=6)
            

        #radio button format for Weapons Armor Page
        #Make place on weapons armor page for storing variable for Simple Weapons
        simpleWeapons  = IntVar(WeaponsArmorPage, 0)
        #set the radio buttons to default option untrained
        simpleWeapons.set(0)
        #Create a label for radio buttons called simple weapons
        SimpleWeaponsLabel = Label(WeaponsArmorPage, text="Simple Weapons").grid(row=3, column=0)
        #Create acrobatics radio button named Untrained with number value 0
        SimpleWeaponsUntrained = Radiobutton(WeaponsArmorPage, text="UnTrained", variable=simpleWeapons, value = 0).grid(row=3, column=1)
        #Create acrobatics radio button named Trained with number value 2
        SimpleWeaponsTrained = Radiobutton(WeaponsArmorPage, text="Trained", variable=simpleWeapons, value = 2).grid(row=3, column=2)
        #Create acrobatics radio button named Expert with number value 4
        SimpleWeaponsExpert = Radiobutton(WeaponsArmorPage, text="Expert", variable=simpleWeapons, value = 4).grid(row=3, column=3)
        #Create acrobatics radio button named Master with number value 6
        SimpleWeaponsMaster = Radiobutton(WeaponsArmorPage, text="Master", variable=simpleWeapons, value =6 ).grid(row=3, column=4)
        #Create acrobatics radio button named Legendary with number value 8
        SimpleWeaponsLegendary = Radiobutton(WeaponsArmorPage, text="Legendary", variable=simpleWeapons, value = 8).grid(row=3, column=5)

        #MartialWeapons Radio Buttons and labels
        martialWeapons  = IntVar(WeaponsArmorPage, 0)
        martialWeapons.set(0)
        MartialWeaponsLabel = Label(WeaponsArmorPage, text="Martial Weapons").grid(row=4, column=0)
        MartialWeaponsUntrained = Radiobutton(WeaponsArmorPage, text="UnTrained", variable=martialWeapons, value = 0).grid(row=4, column=1)
        MartialWeaponsTrained = Radiobutton(WeaponsArmorPage, text="Trained", variable=martialWeapons, value = 2).grid(row=4, column=2)
        MartialWeaponsExpert = Radiobutton(WeaponsArmorPage, text="Expert", variable=martialWeapons, value = 4).grid(row=4, column=3)
        MartialWeaponsMaster = Radiobutton(WeaponsArmorPage, text="Master", variable=martialWeapons, value =6 ).grid(row=4, column=4)
        MartialWeaponsLegendary = Radiobutton(WeaponsArmorPage, text="Legendary", variable=martialWeapons, value = 8).grid(row=4, column=5)

        #Advanced Weapons Radio Buttons and labels
        advancedWeapons  = IntVar(WeaponsArmorPage, 0)
        advancedWeapons.set(0)
        AdvancedWeaponsLabel = Label(WeaponsArmorPage, text="Advanced Weapons").grid(row=5, column=0)
        AdvancedWeaponsUntrained = Radiobutton(WeaponsArmorPage, text="UnTrained", variable=advancedWeapons, value = 0).grid(row=5, column=1)
        AdvancedWeaponsTrained = Radiobutton(WeaponsArmorPage, text="Trained", variable=advancedWeapons, value = 2).grid(row=5, column=2)
        AdvancedWeaponsExpert = Radiobutton(WeaponsArmorPage, text="Expert", variable=advancedWeapons, value = 4).grid(row=5, column=3)
        AdvancedWeaponsMaster = Radiobutton(WeaponsArmorPage, text="Master", variable=advancedWeapons, value =6 ).grid(row=5, column=4)
        AdvancedWeaponsLegendary = Radiobutton(WeaponsArmorPage, text="Legendary", variable=advancedWeapons, value = 8).grid(row=5, column=5)

        #Unarmed Attack Radio Buttons and labels
        unarmedAttack  = IntVar(WeaponsArmorPage, 0)
        unarmedAttack.set(0)
        UnarmedAttackLabel = Label(WeaponsArmorPage, text="Unarmed Attacks").grid(row=6, column=0)
        UnarmedAttackUntrained = Radiobutton(WeaponsArmorPage, text="UnTrained", variable=unarmedAttack, value = 0).grid(row=6, column=1)
        UnarmedAttackTrained = Radiobutton(WeaponsArmorPage, text="Trained", variable=unarmedAttack, value = 2).grid(row=6, column=2)
        UnarmedAttackExpert = Radiobutton(WeaponsArmorPage, text="Expert", variable=unarmedAttack, value = 4).grid(row=6, column=3)
        UnarmedAttackMaster = Radiobutton(WeaponsArmorPage, text="Master", variable=unarmedAttack, value =6 ).grid(row=6, column=4)
        UnarmedAttackLegendary = Radiobutton(WeaponsArmorPage, text="Legendary", variable=unarmedAttack, value = 8).grid(row=6, column=5)

        #Unarmed Attack Radio Buttons and labels       
        bombs  = IntVar(WeaponsArmorPage, 0)
        bombs.set(0)
        BombsLabel = Label(WeaponsArmorPage, text="Bombs").grid(row=7, column=0)
        BombsUntrained = Radiobutton(WeaponsArmorPage, text="UnTrained", variable=bombs, value = 0).grid(row=7, column=1)
        BombsTrained = Radiobutton(WeaponsArmorPage, text="Trained", variable=bombs, value = 2).grid(row=7, column=2)
        BombsExpert = Radiobutton(WeaponsArmorPage, text="Expert", variable=bombs, value = 4).grid(row=7, column=3)
        BombsMaster = Radiobutton(WeaponsArmorPage, text="Master", variable=bombs, value =6 ).grid(row=7, column=4)
        BombsLegendary = Radiobutton(WeaponsArmorPage, text="Legendary", variable=bombs, value = 8).grid(row=7, column=5)

        #Light Armor Radio Buttons and labels
        lightArmor = IntVar(WeaponsArmorPage, 0)
        lightArmor.set(0)
        LightArmorLabel = Label(WeaponsArmorPage, text="Light Armor").grid(row=9, column=0)
        LightArmorUntrained = Radiobutton(WeaponsArmorPage, text="UnTrained", variable=lightArmor, value = 0).grid(row=9, column=1)
        LightArmorTrained = Radiobutton(WeaponsArmorPage, text="Trained", variable=lightArmor, value = 2).grid(row=9, column=2)
        LightArmorExpert = Radiobutton(WeaponsArmorPage, text="Expert", variable=lightArmor, value = 4).grid(row=9, column=3)
        LightArmorMaster = Radiobutton(WeaponsArmorPage, text="Master", variable=lightArmor, value =6 ).grid(row=9, column=4)
        LightArmorLegendary = Radiobutton(WeaponsArmorPage, text="Legendary", variable=lightArmor, value = 8).grid(row=9, column=5)

        #Medium Armor Radio Buttons and labels
        mediumArmor = IntVar(WeaponsArmorPage, 0)
        mediumArmor.set(0)
        MediumArmorLabel = Label(WeaponsArmorPage, text="Medium Armor").grid(row=10, column=0)
        MediumArmorUntrained = Radiobutton(WeaponsArmorPage, text="UnTrained", variable=mediumArmor, value = 0).grid(row=10, column=1)
        MediumArmorTrained = Radiobutton(WeaponsArmorPage, text="Trained", variable=mediumArmor, value = 2).grid(row=10, column=2)
        MediumArmorExpert = Radiobutton(WeaponsArmorPage, text="Expert", variable=mediumArmor, value = 4).grid(row=10, column=3)
        MediumArmorMaster = Radiobutton(WeaponsArmorPage, text="Master", variable=mediumArmor, value =6 ).grid(row=10, column=4)
        MediumArmorLegendary = Radiobutton(WeaponsArmorPage, text="Legendary", variable=mediumArmor, value = 8).grid(row=10, column=5)

        #Heavy Armor Radio Buttons and labels
        heavyArmor = IntVar(WeaponsArmorPage, 0)
        heavyArmor.set(0)
        HeavyArmorLabel = Label(WeaponsArmorPage, text="Heavy Armor").grid(row=11, column=0)
        HeavyArmorUntrained = Radiobutton(WeaponsArmorPage, text="UnTrained", variable=heavyArmor, value = 0).grid(row=11, column=1)
        HeavyArmorTrained = Radiobutton(WeaponsArmorPage, text="Trained", variable=heavyArmor, value = 2).grid(row=11, column=2)
        HeavyArmorExpert = Radiobutton(WeaponsArmorPage, text="Expert", variable=heavyArmor, value = 4).grid(row=11, column=3)
        HeavyArmorMaster = Radiobutton(WeaponsArmorPage, text="Master", variable=heavyArmor, value =6 ).grid(row=11, column=4)
        HeavyArmorLegendary = Radiobutton(WeaponsArmorPage, text="Legendary", variable=heavyArmor, value = 8).grid(row=11, column=5)

        #UnarmoredDefense Radio Buttons and labels
        unarmoredDefense = IntVar(WeaponsArmorPage, 0)
        unarmoredDefense.set(0)
        UnarmoredDefenseLabel = Label(WeaponsArmorPage, text="Unarmored Defense").grid(row=12, column=0)
        UnarmoredDefenseUntrained = Radiobutton(WeaponsArmorPage, text="UnTrained", variable=unarmoredDefense, value = 0).grid(row=12, column=1)
        UnarmoredDefenseTrained = Radiobutton(WeaponsArmorPage, text="Trained", variable=unarmoredDefense, value = 2).grid(row=12, column=2)
        UnarmoredDefenseExpert = Radiobutton(WeaponsArmorPage, text="Expert", variable=unarmoredDefense, value = 4).grid(row=12, column=3)
        UnarmoredDefenseMaster = Radiobutton(WeaponsArmorPage, text="Master", variable=unarmoredDefense, value =6 ).grid(row=12, column=4)
        UnarmoredDefenseLegendary = Radiobutton(WeaponsArmorPage, text="Legendary", variable=unarmoredDefense, value = 8).grid(row=12, column=5)


        #Create command to close weapons armor page
        def WeaponsArmorPageBackButton():
            WeaponsArmorPage.withdraw()

        #make button on weapons armor page to run command to calculate proficiencys
        ButtonWeaponsArmorProf = Button(WeaponsArmorPage, text = "Calculate Proficiency", command = CalculateWeaponsArmorProficiency).grid(row=20, column=0)
        #make button on weapons armor pageto run command to close weapons armor page
        ButtonWeaponsArmorBack = Button(WeaponsArmorPage, text = "Back", command =  WeaponsArmorPageBackButton).grid(row=21, column=0)


#############################################################################################################################################
    #Create and name Saves/Perception page

    #set command to open new window for Saves/Perception Page
    def OpenSavesPage():
        #Create , name and, set size of Saves/Perception Page
        SavesPerceptionPage = Tk()
        SavesPerceptionPage.title("Saves/Perception")
        SavesPerceptionPage.geometry("1000x250")

        #Add label for Saves/Perception page
        SavesPerceptionLabel = Label(SavesPerceptionPage, text = "Saves and Perception Calculator").grid(row=0, column=0)

        #Entry box format for Saves/Perception page
        #make a place on Saves/Perception page to store level
        SavesPerceptionLevelString = StringVar(SavesPerceptionPage, 0)
        #add a label for level entry box
        SavesPerceptionLevelLabel = Label(SavesPerceptionPage, text = "Level").grid(row=1, column=0)
        #Create a entry box for level
        SavesPerceptionLevel = Entry(SavesPerceptionPage,textvariable=SavesPerceptionLevelString).grid(row=1, column=1)
        #Set entry box size
        SavesPerceptionLevel = Entry(SavesPerceptionPage, width = 10)
        
        #Saves/Perception Page Dexterity Lable and entry box
        SavesPerceptionDexterityString = StringVar(SavesPerceptionPage, 0)
        SavesPerceptionDexterityLabel = Label(SavesPerceptionPage, text = "Dexterity modifier").grid(row=2, column=0)
        SavesPerceptionDexterity = Entry(SavesPerceptionPage, textvariable=SavesPerceptionDexterityString).grid(row=2, column=1)
        SavesPerceptionDexterity = Entry(SavesPerceptionPage, width = 10)

        #Saves/Perception Page Wisdom Lable and entry box
        SavesPerceptionWisdomString = StringVar(SavesPerceptionPage, 0)
        SavesPerceptionWisdomLabel = Label(SavesPerceptionPage, text = "Wisdom modifier").grid(row=2, column=2)
        SavesPerceptionWisdom = Entry(SavesPerceptionPage, textvariable=SavesPerceptionWisdomString).grid(row=2, column=3)
        SavesPerceptionWisdom = Entry(SavesPerceptionPage, width = 10)

        #Saves/Perception Page Constitution Lable and entry box
        SavesPerceptionConstitutionString = StringVar(SavesPerceptionPage, 0)
        SavesPerceptionConstitutionLabel = Label(SavesPerceptionPage, text = "Constitution modifier").grid(row=2, column=4)
        SavesPerceptionConstitution = Entry(SavesPerceptionPage, textvariable=SavesPerceptionConstitutionString).grid(row=2, column=5)
        SavesPerceptionConstitution = Entry(SavesPerceptionPage, width = 10)

        #Create command to calculate Saves/Perception
        def CalculateSavesPerceptionProficiency():

            #proficiency calculation format
            #check if radio button is set to untrained
            if reflex.get() ==0:
                # Get your reflex proficiency by using just stat modifier
                profReflex = (float(SavesPerceptionDexterityString.get()))
                #Display reflex to user
                ReflexProf = Label(SavesPerceptionPage, text = ("Your Reflex Proficiency is :", profReflex))
                #Place label 
                ReflexProf.grid(row=3, column=6)
            else:
                # Get your reflex proficiency by adding together entered level, entered dexterity with radio button value
                profReflex = (reflex.get()+ float(SavesPerceptionLevelString.get())+ float(SavesPerceptionDexterityString.get()))
                #Display reflex to user
                ReflexProf = Label(SavesPerceptionPage, text = ("Your Reflex Proficiency is :", profReflex))
                #Place label 
                ReflexProf.grid(row=3, column=6)

            #calculate and display Fortitude
            if fortitude.get() ==0:
                profFortitude = (float(SavesPerceptionConstitutionString.get()))
                FortitudeProf = Label(SavesPerceptionPage, text = ("Your Fortitude Proficiency is :", profFortitude))
                FortitudeProf.grid(row=4, column=6)
            else:
                profFortitude = (fortitude.get()+ float(SavesPerceptionLevelString.get())+ float(SavesPerceptionConstitutionString.get()))
                FortitudeProf = Label(SavesPerceptionPage, text = ("Your Fortitude Proficiency is :", profFortitude))
                FortitudeProf.grid(row=4, column=6)

            #calculate and display Will Proficiency
            if will.get() ==0:
                profWill = (float(SavesPerceptionWisdomString.get()))
                WillProf = Label(SavesPerceptionPage, text = ("Your Will Proficiency is :", profWill))
                WillProf.grid(row=5, column=6)
            else:
                profWill = (will.get()+ float(SavesPerceptionLevelString.get())+ float(SavesPerceptionWisdomString.get()))
                WillProf = Label(SavesPerceptionPage, text = ("Your Will Proficiency is :", profWill))
                WillProf.grid(row=5, column=6)

            #calculate and display Perception Proficiency
            if perception.get() ==0:
                profPerception = (float(SavesPerceptionWisdomString.get()))
                PerceptionProf = Label(SavesPerceptionPage, text = ("Your Perception Proficiency is :", profPerception))
                PerceptionProf.grid(row=6, column=6)
            else:
                profPerception = (perception.get()+ float(SavesPerceptionLevelString.get())+ float(SavesPerceptionWisdomString.get()))
                PerceptionProf = Label(SavesPerceptionPage, text = ("Your Perception Proficiency is :", profPerception))
                PerceptionProf.grid(row=6, column=6)

        #Radio button format for Saves/Perception Page
        #Make place on Saves/Perception Page for storing variable for Reflex
        reflex  = IntVar(SavesPerceptionPage, 0)
        #Set default on radio buttons to untrained
        reflex.set(0)
        #Create a label for radio buttons called Reflex
        ReflexLabel = Label(SavesPerceptionPage, text="Reflex").grid(row=3, column=0)
        #Create acrobatics radio button named Untrained with number value 0
        ReflexUntrained = Radiobutton(SavesPerceptionPage, text="UnTrained", variable=reflex, value = 0).grid(row=3, column=1)
        #Create acrobatics radio button named Trained with number value 2
        ReflexTrained = Radiobutton(SavesPerceptionPage, text="Trained", variable=reflex, value = 2).grid(row=3, column=2)
        #Create acrobatics radio button named Expert with number value 4
        ReflexExpert = Radiobutton(SavesPerceptionPage, text="Expert", variable=reflex, value = 4).grid(row=3, column=3)
        #Create acrobatics radio button named Master with number value 6
        ReflexMaster = Radiobutton(SavesPerceptionPage, text="Master", variable=reflex, value =6 ).grid(row=3, column=4)
        #Create acrobatics radio button named Legendary with number value 8
        ReflexLegendary = Radiobutton(SavesPerceptionPage, text="Legendary", variable=reflex, value = 8).grid(row=3, column=5)

        #Fortitude Radio Buttons and labels
        fortitude  = IntVar(SavesPerceptionPage, 0)
        fortitude.set(0)
        FortitudeLabel = Label(SavesPerceptionPage, text="Fortitude").grid(row=4, column=0)
        FortitudeUntrained = Radiobutton(SavesPerceptionPage, text="UnTrained", variable=fortitude, value = 0).grid(row=4, column=1)
        FortitudeTrained = Radiobutton(SavesPerceptionPage, text="Trained", variable=fortitude, value = 2).grid(row=4, column=2)
        FortitudeExpert = Radiobutton(SavesPerceptionPage, text="Expert", variable=fortitude, value = 4).grid(row=4, column=3)
        FortitudeMaster = Radiobutton(SavesPerceptionPage, text="Master", variable=fortitude, value =6 ).grid(row=4, column=4)
        FortitudeLegendary = Radiobutton(SavesPerceptionPage, text="Legendary", variable=fortitude, value = 8).grid(row=4, column=5)

        #Will Radio Buttons and labels
        will  = IntVar(SavesPerceptionPage, 0)
        will.set(0)
        WillLabel = Label(SavesPerceptionPage, text="Will").grid(row=5, column=0)
        WillUntrained = Radiobutton(SavesPerceptionPage, text="UnTrained", variable=will, value = 0).grid(row=5, column=1)
        WillTrained = Radiobutton(SavesPerceptionPage, text="Trained", variable=will, value = 2).grid(row=5, column=2)
        WillExpert = Radiobutton(SavesPerceptionPage, text="Expert", variable=will, value = 4).grid(row=5, column=3)
        WillMaster = Radiobutton(SavesPerceptionPage, text="Master", variable=will, value =6 ).grid(row=5, column=4)
        WillLegendary = Radiobutton(SavesPerceptionPage, text="Legendary", variable=will, value = 8).grid(row=5, column=5)

        #Perception Radio Buttons and labels
        perception  = IntVar(SavesPerceptionPage, 0)
        perception.set(0)
        PerceptionLabel = Label(SavesPerceptionPage, text="Perception").grid(row=6, column=0)
        PerceptionUntrained = Radiobutton(SavesPerceptionPage, text="UnTrained", variable=perception, value = 0).grid(row=6, column=1)
        PerceptionTrained = Radiobutton(SavesPerceptionPage, text="Trained", variable=perception, value = 2).grid(row=6, column=2)
        PerceptionExpert = Radiobutton(SavesPerceptionPage, text="Expert", variable=perception, value = 4).grid(row=6, column=3)
        PerceptionMaster = Radiobutton(SavesPerceptionPage, text="Master", variable=perception, value =6 ).grid(row=6, column=4)
        PerceptionLegendary = Radiobutton(SavesPerceptionPage, text="Legendary", variable=perception, value = 8).grid(row=6, column=5)

        #Create command to close Saves Perception Page
        def SavesPerceptionPageBackButton():
            SavesPerceptionPage.withdraw()
        #make button Saves Perception Page to run command to calculate proficiencys
        ButtonSavesPerceptionProf = Button(SavesPerceptionPage, text = "Calculate Proficiency", command = CalculateSavesPerceptionProficiency).grid(row=7, column=0)
        #make button on Saves Perception Page to run command to close Saves Perception Page
        ButtonSavesPerceptionBack = Button(SavesPerceptionPage, text = "Back", command =  SavesPerceptionPageBackButton).grid(row=8, column=0)


#################################################################################################
#Set up root page
    #Make a label on root page
    RootPageLabel = Label(root, text = "Pathfinder 2e Profficiecy Calcultor").pack()

    #Add a image to root page
    RootImage=PhotoImage(file='calculator.png')
    root=Label(image=RootImage)
    root.photo=RootImage
    root.pack()






    #Buttons for root page that open other pages
    #Button that opens Skills Page on root page
    ButtonSkills = Button(text = "Skills", command = OpenSkillsPage).pack()

    #Button that opens Weapons/Armor Page on root page
    ButtonWeapons = Button(text = "Weapons/Armor", command = OpenWeaponsPage).pack()

    #Button that opens Saves/Perception Page on root page
    ButtonSaves = Button(text = "Saves/Perception", command = OpenSavesPage).pack()

        

#Run main loop
main()

