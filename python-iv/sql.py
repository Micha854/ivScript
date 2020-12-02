import MySQLdb
import time
import json

class pokemon():
  def getPokemon(self,value,language):
    data = open('json/Pokemon.json').read()
    switch = json.loads(data)
    return switch[str(value)][language]

class Sql():
  encounter_id = []
  calc_endminsec = []
  pokemon_id = []
  individual_attack = []
  individual_defense = []
  individual_stamina = []
  disappear_time = []
  cp = []
  cp_multiplier = []
  shortattack = []
  loadattack = []
  gender = []
  longitude = []
  latitude = []
  form = []
  costume = []
  weather_boosted_condition = []

  def startSQL(self,cfg,modul):
    #Verbindungsaufbau zur MySQL-Datenbank
    try:
      connection = MySQLdb.connect(host=cfg.host,db=cfg.database,user=cfg.user, passwd=cfg.password)
      cursor = connection.cursor()
    except:
      print("Kein Verbindungsaufbau zur Datenbank, probiere es in 15 Sekunden erneut\n")
      time.sleep(15)
      return self.startSQL(cfg,modul)
    self.encounter_id.clear()
    self.calc_endminsec.clear()
    self.pokemon_id.clear()
    self.individual_attack.clear()
    self.individual_defense.clear()
    self.individual_stamina.clear()
    self.disappear_time.clear()
    self.cp.clear()
    self.cp_multiplier.clear()
    self.shortattack.clear()
    self.loadattack.clear()
    self.gender.clear()
    self.longitude.clear()
    self.latitude.clear()
    self.form.clear()
    self.costume.clear()
    self.weather_boosted_condition.clear()

    poke_class = pokemon()
    pokeID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,862,863,865,866,867]
    pokeID.sort(key=lambda x: poke_class.getPokemon(value=x, language=cfg.language))
    sort_pokemon = str(pokeID).replace("[", "").replace("]", "")

    if sort_pokemon and cfg.sort_pokemon == True:
      pokemon_sort = "FIELD(p.pokemon_id," + sort_pokemon + "), form, costume"
    else:
      pokemon_sort = "''"

    #Abfragen der Daten aus der Datenbank
    if modul == "0er":

      cursor.execute("SELECT p.encounter_id,s.calc_endminsec,p.pokemon_id,p.individual_attack,p.individual_defense,p.individual_stamina,p.disappear_time,p.cp,p.cp_multiplier,p.move_1,p.move_2,p.gender,p.longitude,p.latitude,p.form,p.costume,p.weather_boosted_condition FROM pokemon p LEFT JOIN trs_spawn s ON p.spawnpoint_id = s.spawnpoint WHERE disappear_time > utc_timestamp() ORDER BY " + pokemon_sort + ", round(((`individual_attack` + `individual_defense` + `individual_stamina` ) / 45) *100) DESC, disappear_time DESC")
      all = list(cursor.fetchall())
      i = 0
      try:
        while i < len(all):
          self.encounter_id.append(all[i][0])
          self.calc_endminsec.append(all[i][1])
          self.pokemon_id.append(all[i][2])
          self.individual_attack.append(all[i][3])
          self.individual_defense.append(all[i][4])
          self.individual_stamina.append(all[i][5])
          self.disappear_time.append(all[i][6])
          self.cp.append(all[i][7])
          self.cp_multiplier.append(all[i][8])
          self.shortattack.append(all[i][9])
          self.loadattack.append(all[i][10])
          self.gender.append(all[i][11])
          self.longitude.append(all[i][12])
          self.latitude.append(all[i][13])
          self.form.append(all[i][14])
          self.costume.append(all[i][15])
          self.weather_boosted_condition.append(all[i][16])
          i +=1

      except Exception as e:
        outF = open(cfg.areaName+"error.txt","w")
        ausgabe = "Passierte in der SQL.py\n"
        ausgabe += "encounter_id: " + str(self.encounter_id.__len__) + "\n"
        ausgabe += "calc_endminsec: " + str(self.calc_endminsec.__len__) + "\n"
        ausgabe += "pokemon_id: " + str(self.pokemon_id.__len__) + "\n"
        ausgabe += "individual_attack: " + str(self.individual_attack.__len__) + "\n"
        ausgabe += "individual_defense: " + str(self.individual_defense.__len__) + "\n"
        ausgabe += "individual_stamina: " + str(self.individual_stamina.__len__) + "\n"
        ausgabe += "disappear_time: " + str(self.disappear_time.__len__) + "\n"
        ausgabe += "cp: " + str(self.cp.__len__) + "\n"
        ausgabe += "cp_multiplier: " + str(self.cp_multiplier.__len__) + "\n"
        ausgabe += "shortattack: " + str(self.shortattack.__len__) + "\n"
        ausgabe += "loadattack: " + str(self.loadattack.__len__) + "\n"
        ausgabe += "gender: " + str(self.gender.__len__) + "\n"
        ausgabe += "longitude: " + str(self.longitude.__len__) + "\n"
        ausgabe += "latitude: " + str(self.latitude.__len__) + "\n"
        ausgabe += "form: " + str(self.form.__len__) + "\n"
        ausgabe += "costume: " + str(self.costume.__len__) + "\n"
        ausgabe += "Wert i" + str(i) + "\n"
        ausgabe += "All Variable: " + str(len(all))
        outF.writelines(ausgabe + str(e))
        outF.close()

    cursor = cursor.close()
    connection.close()