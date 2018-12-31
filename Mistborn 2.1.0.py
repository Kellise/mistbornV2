import random as ran
trap0= True

while trap0==True:
  trap1= True
  trap2= True
  trap3= True
  trap4= True
  trap5= True
  trap6= True
  trap7= True
  trap8= True
  trap9= True
  trap10=True
  trap11=True

  mistborn= None
  fero= None
  twin= None
  playerMagic= None
  powerNames= []
  playerMetal= None
  playerMetal2= None

  powerL= "0"
  standingL= "0"
  attriL="0"


  pMetal1= ["Iron", "Steel", "Pewter", "Tin"]
  mMetal1= ["Copper", "Bronze", "Brass", "Zinc"]
  tMetal1= ["Gold", "Atium"]

  pMetal2= ["Iron", "Steel", "Pewter", "Tin"]
  mMetal2= ["Copper", "Bronze", "Brass", "Zinc"]
  tMetal2= ["Gold", "Electrum", "Bendalloy", "Cadmium"]
  eMetal2= ["Aluminum", "Duralumin", "Nicrosil", "Chromium"]

  metals1= [pMetal1, mMetal1, tMetal1] 
  metals2= [pMetal2, mMetal2, tMetal2, eMetal2] 

  def selectAnyMetalEra1():
      family= ran.choice(metals1)
      metalChoice= ran.choice(family) 
      return(metalChoice)

  def selectAnyMetalEra2():
      family= ran.choice(metals2)
      metalChoice= ran.choice(family) 
      return(metalChoice)

  def noGnat():
      family= ran.choice(metals2)
      metalChoice= ran.choice(family)
      if metalChoice=="Aluminum" or metalChoice=="Duralumin":
          return(noGnat())
      else:
          return(metalChoice)

  def powerLevels():
      global powerL
      global standingL
      global attriL
      
      
      attriNums= ["1", "2", "3"]
      powerL= ran.choice(attriNums)
      used= int(powerL)-1
      try:
          attriNums.pop(used)

      except IndexError:
          used=used-1
          attriNums.pop(used)

      if mistborn==False and fero==False and twin==False and powerL== "3":
          return powerLevels()


      standingL= ran.choice(attriNums)
      used= int(standingL)-1
      try:
          attriNums.pop(used)

      except IndexError:
          used=used-1
          try:
              attriNums.pop(used)
          except IndexError:
              used=used-1
              attriNums.pop(used)

      
      attriL=ran.choice(attriNums)
      results= ("Power Level= " +powerL+ "|  Standing level= "+ standingL+ "|  Attributes Level=" +attriL)
      return(results)

  #ask if disabling mistborn
  print("Welcome to Mistborn RPG generator.")
  while trap5== True:  
    select5= input("Era? 1/2:")
    if select5=="1":
      era= "1"
      twinborn= False
      trap3=False
      trap5= False
    elif select5=="2":
      era= "2"
      mistborn=False
      fero= False
      trap1= False
      trap2=False
      trap5= False

  while trap1== True:
      select1= input("Are you allowed to be Mistborn? Y/N :")
      select1= str.upper(select1)
      if select1=="Y":
          mistborn= True
          trap1= False
      elif select1=="N":
          mistborn= False
          trap1= False

  #ask if disabling full fero

  while trap2== True:
      select2= input("Are you allowed to be a full Feruchemist ? Y/N :")
      select2= str.upper(select2)
      if select2=="Y":
          fero= True
          trap2= False
      elif select2=="N":
          fero= False
          trap2= False

  while trap3== True:
      select3= input("Are you allowed to be a twinborn ? Y/N :")
      select3=str.upper(select3)
      if select3=="Y":
          twin= True
          trap3= False
      elif select3=="N":
          twin= False
          trap3= False
  #generate power levels, factoring in allowances
  characterlevel= powerLevels()
  print("Character Levels are: "+characterlevel)
      
  #generate any powers

  if powerL== "2":
    while trap4== True:
        select4= input("Misting or Ferring? A/F :")
        select4=str.upper(select4)
        if select4=="A":
          playerMagic= "A"
          trap4= False
        elif select4=="F":
          playerMagic= "F"
          trap4= False
    

    
    if playerMagic=="A" or playerMagic== "F" and era=="1":
      playerMetal=selectAnyMetalEra1()

    if playerMagic== "A" and era=="2":
      while trap6== True:
        gnatStat= input("Are you will to risk Gnat Status?Y/N :")
        gnatStat= str.upper(gnatStat)
        if gnatStat=="Y" or gnatStat=="N":
          trap6=False
      
      if gnatStat=="Y":
        playerMetal= selectAnyMetalEra2()
      elif gnatStat=="N":
        playerMetal= noGnat()

    if playerMagic=="F" and era=="2":
      playerMetal= selectAnyMetalEra2()

    print("Your Metal is: "+playerMetal)


  elif powerL=="1":
      print("You lack powers, but are strong in other ways!")
      

  elif powerL=="3":
    if era=="1":
      while trap7== True:
        playerMetal= "All"
        if mistborn==True and fero==True:
          select7= input("Mistborn or Keeper? M/K :")
          select7= str.upper(select7)
          if select7=="M":
            playerMagic= "M"
            trap7= False
          elif select7=="K":
            playerMagic= "K"
            trap7= False
        elif mistborn==True:
          playerMagic="M"
          print("You are Mistborn!")
          trap7=False
        elif fero==True:
          playerMagic="K"
          print("You are a Keeper!")
          trap7=False
      print("You have access to all metals")
    elif era=="2":
      playerMagic= "Twin"
      
      while trap8== True:
        gnatStat= input("Are you will to risk Gnat Status?Y/N :")
        gnatStat= str.upper(gnatStat)
        if gnatStat=="Y" or gnatStat=="N":
          trap8=False
      
      if gnatStat=="Y":
        playerMetal= selectAnyMetalEra2()
      elif gnatStat=="N":
        playerMetal= noGnat()

      playerMetal2= selectAnyMetalEra2()

      print("Your Allomatic Metal is: "+playerMetal)
      print("Your Feruchemical Metal is: "+ playerMetal2)
      if playerMetal==playerMetal2:
        print("You are a Compounder")


  #generate names of powers
  if powerL=="1":
    powerNames.append("None")

  elif powerL=="3" and era=="1":
    powerNames.append("All")

  elif powerL=="2" and playerMagic=="A":
    if playerMetal=="Iron":
      powerNames.append("Lurcher")
    elif playerMetal=="Steel":
      powerNames.append("Coinshot")
    elif playerMetal=="Pewter":
      powerNames.append("Thug")
    elif playerMetal=="Tin":
      powerNames.append("Tineye")

    elif playerMetal=="Zinc":
      powerNames.append("Rioter")
    elif playerMetal=="Brass":
      powerNames.append("Soother")
    elif playerMetal=="Copper":
      powerNames.append("Smoker")
    elif playerMetal=="Bronze":
      powerNames.append("Seeker")

    elif playerMetal=="Atium":
      powerNames.append("Seer")
    
    elif playerMetal=="Gold":
      powerNames.append("Augur")
    elif playerMetal=="Electrum":
      powerNames.append("Oracle")
    elif playerMetal=="Cadmium":
      powerNames.append("Pulsar")
    elif playerMetal=="Bendalloy":
      powerNames.append("Slider")
    
    elif playerMetal=="Duralumin":
      powerNames.append("Duralumin Gnat")
    elif playerMetal=="Aluminum":
      powerNames.append("Aluminum Gnat")
    elif playerMetal=="Nicrosil":
      powerNames.append("Nicroburst")
    elif playerMetal=="Chromium":
      powerNames.append("Leecher")

  elif powerL=="2" and playerMagic=="F":
    if playerMetal=="Iron":
      powerNames.append("Skimmer")
    elif playerMetal=="Steel":
      powerNames.append("Steelrunner")
    elif playerMetal=="Pewter":
      powerNames.append("Brute")
    elif playerMetal=="Tin":
      powerNames.append("Windwhisper")

    elif playerMetal=="Zinc":
      powerNames.append("Sparker")
    elif playerMetal=="Brass":
      powerNames.append("Firesoul")
    elif playerMetal=="Copper":
      powerNames.append("Archivist")
    elif playerMetal=="Bronze":
      powerNames.append("Sentry")

    elif playerMetal=="Atium":
      powerNames.append("Seer")
    
    elif playerMetal=="Gold":
      powerNames.append("Bloodmaker")
    elif playerMetal=="Electrum":
      powerNames.append("Pinnacle")
    elif playerMetal=="Cadmium":
      powerNames.append("Gasper")
    elif playerMetal=="Bendalloy":
      powerNames.append("Subsumer")
    
    elif playerMetal=="Duralumin":
      powerNames.append("Connector")
    elif playerMetal=="Aluminum":
      powerNames.append("Trueself")
    elif playerMetal=="Nicrosil":
      powerNames.append("Soulbearer")
    elif playerMetal=="Chromium":
      powerNames.append("Spinner")

  elif powerL=="3" and era=="2":
    
    if playerMetal=="Iron":
      powerNames.append("Lurcher")
    elif playerMetal=="Steel":
      powerNames.append("Coinshot")
    elif playerMetal=="Pewter":
      powerNames.append("Thug")
    elif playerMetal=="Tin":
      powerNames.append("Tineye")

    elif playerMetal=="Zinc":
      powerNames.append("Rioter")
    elif playerMetal=="Brass":
      powerNames.append("Soother")
    elif playerMetal=="Copper":
      powerNames.append("Smoker")
    elif playerMetal=="Bronze":
      powerNames.append("Seeker")

    elif playerMetal=="Atium":
      powerNames.append("Seer")
    
    elif playerMetal=="Gold":
      powerNames.append("Augur")
    elif playerMetal=="Electrum":
      powerNames.append("Oracle")
    elif playerMetal=="Cadmium":
      powerNames.append("Pulsar")
    elif playerMetal=="Bendalloy":
      powerNames.append("Slider")
    
    elif playerMetal=="Duralumin":
      powerNames.append("Duralumin Gnat")
    elif playerMetal=="Aluminum":
      powerNames.append("Aluminum Gnat")
    elif playerMetal=="Nicrosil":
      powerNames.append("Nicroburst")
    elif playerMetal=="Chromium":
      powerNames.append("Leecher")
    
    
    if playerMetal2=="Iron":
      powerNames.append("Skimmer")
    elif playerMetal2=="Steel":
      powerNames.append("Steelrunner")
    elif playerMetal2=="Pewter":
      powerNames.append("Brute")
    elif playerMetal2=="Tin":
      powerNames.append("Windwhisper")

    elif playerMetal2=="Zinc":
      powerNames.append("Sparker")
    elif playerMetal2=="Brass":
      powerNames.append("Firesoul")
    elif playerMetal2=="Copper":
      powerNames.append("Archivist")
    elif playerMetal2=="Bronze":
      powerNames.append("Sentry")

    elif playerMetal2=="Atium":
      powerNames.append("Seer")
    
    elif playerMetal2=="Gold":
      powerNames.append("Bloodmaker")
    elif playerMetal2=="Electrum":
      powerNames.append("Pinnacle")
    elif playerMetal2=="Cadmium":
      powerNames.append("Gasper")
    elif playerMetal2=="Bendalloy":
      powerNames.append("Subsumer")
    
    elif playerMetal2=="Duralumin":
      powerNames.append("Connector")
    elif playerMetal2=="Aluminum":
      powerNames.append("Trueself")
    elif playerMetal2=="Nicrosil":
      powerNames.append("Soulbearer")
    elif playerMetal2=="Chromium":
      powerNames.append("Spinner")
  else:
    powerNames="No Power Name Set by system"
  print(powerNames)
  #generate name of character
  characterName= input("What is your full character name: ")
  #set gender 
  gender= input("What is your Gender?")

  #generate height
  height= None
  while trap9==True:
    heightA= input("Are you a random height, tall, average, short? R/T/A/S: ")
    heightA= str.upper(heightA)

    if heightA=="R":
      height= ran.randint(46, 78)
      trap9=False

    elif heightA=="T":
      height= ran.randint(72, 78)
      trap9=False

    elif heightA=="A":
      height= ran.randint(62, 71)
      trap9=False

    elif heightA=="S":
      height= ran.randint(46, 61)
      trap9=False
  print("You are "+ str(height)+" inches tall.")
  #generate build
  builds= ["Lean", "Musclear", "Thin", "Weedy", "Average", "Underfed", "Twisted", "Average", "Overweight", "Lean", "Musclear", "Thin", "Weedy", "Average", "Underfed", "Average", "Overweight"]

  characterBuild= ran.choice(builds)
  print("You are: "+characterBuild+" of build")


  #generate age
  while trap10==True:
    heightA= input("How old are you? Random, young, average, old? R/Y/A/O: ")
    heightA= str.upper(heightA)
    if heightA=="R":
      age= ran.randint(14, 67)
      trap10=False

    elif heightA=="Y":
      age= ran.randint(14, 22)
      trap10=False

    elif heightA=="A":
      age= ran.randint(23, 45)
      trap10=False

    elif heightA=="O":
      age= ran.randint(46, 67)
      trap10=False
  print("You are "+ str(age)+" years old.")


  #generate nobility
  if era=="1":
      nobility_types= ["Skaa","Skaa","Skaa", "Merchant","Merchant", "Noble", "Noble", "Major Noble House Member"]
      nobility= ran.choice(nobility_types)
      print("Your social class is: "+nobility)
  elif era=="2":
      nobility_types= ["Citizen","Citizen", "Citizen","Citizen","Criminal", "Merchant","Merchant", "Noble", "Noble", "Major Noble House Member"]
      nobility= ran.choice(nobility_types)
      print("Your social class is: "+nobility)


  filename= open("The "+ nobility+ " "+ characterName+".txt", "w+")
  filename.write("Name: "+characterName)
  filename.write("\n"+"Age: "+str(age))
  filename.write("\n"+"Gender: "+str(gender))
  filename.write("\n"+"Height (Inches): "+str(height))
  filename.write("\n"+"Build: "+str(characterBuild))
  filename.write("\n"+"Class: "+str(nobility))
  filename.write("\n"+"Power Level: "+str(powerL))
  filename.write("\n"+"Standing: "+str(standingL))
  filename.write("\n"+"Attributes: "+str(attriL))
  filename.write("\n"+"Power: "+str(playerMagic))
  filename.write("\n"+"Metal: "+str(playerMetal))
  if playerMetal2!=None:
      filename.write("\n"+"Metal 2: "+str(playerMetal2))
  if powerNames!= []:
      filename.write("\n"+"Power Name: "+str(powerNames))

  filename.close()
  print("File Created!")
  while trap11==True:
    exit=input("Repeat process? Y/N: ")
    exit= str.upper(exit)
    if exit=="N":
      trap0=False
      trap11=False

    elif exit=="Y":
      trap11=False
