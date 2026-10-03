class GWAcalculator:
  def __init__(self, name):
    self.__name = name
    self.__subjects = []
  def subjectslist(self, subjectlist):
    self.__subjects = subjectlist.copy()
  def get_subjects(self):
    return self.__subjects.copy()
  def calculateGWA(self):
    GWAtotal = 0.0
    Unittotal = 0.0
    for i in self.__subjects:
      unit = i.getunit()
      grade = i.getgrade()
      weightedgwa = grade * unit
      GWAtotal += weightedgwa
      Unittotal += unit
    if Unittotal == 0.0:
      return "No subject units. Please ensure that you've entered the units properly."
    return GWAtotal / Unittotal


class ScenarioCalculator:
  def __init__(self, calculator_instance, newsubj):
    self.calculator = calculator_instance
    self.newsubj = newsubj

  def calculateScenario(self):
    scenariolist = self.calculator.get_subjects()
    reallist = self.calculator.get_subjects()
    for index, i in enumerate(scenariolist):
      if i.getname() == self.newsubj.getname():
        scenariolist[index] = self.newsubj
        break
    temp_calc1 = GWAcalculator("Calculator")
    temp_calc1.subjectslist(reallist)
    result = temp_calc1.calculateGWA()
    temp_calc2 = GWAcalculator("Simulation")
    temp_calc2.subjectslist(scenariolist)
    newresult = temp_calc2.calculateGWA()
    if result > newresult:
      diff = result - newresult
      print(f"Your grade increased by {diff}")
    elif result < newresult:
      print(f"SHIT SHIT SHIT YOUR GRADE DROPPED BY {diff} !")
    elif result == newresult:
      print("Literally NOTHING changed! Good job")
