"""         Script variabler                """
global Createmodel,Savemodel,numCPU,Runjobs,linearAnalysis,nonLinearAnalysis,Increments
#numCPU = multiprocessing.cpu_count()
numCPU = 1

Newmodels = 1
Runjobs = 1
Stifftest = 1
Stresstest = 1

if Newmodels:
    Createmodel = 1
    Savemodel = 1
    openModel = 0
else:
    Createmodel = 0
    Savemodel = 0
    openModel = 1

if Stifftest:
    linearAnalysis = 1
    LinearpostPross = 1
else:
    linearAnalysis = 0
    LinearpostPross = 0

if Stresstest:
    nonLinearAnalysis = 1
    nonLinearpostPross = 1
else:
    nonLinearAnalysis = 1
    nonLinearpostPross = 1

Increments = {'maxNum': 50, 'initial': 1e-2, 'min': 0.8e-3, 'max': 0.1}



"""Material modeller"""

#Plasticitet
Yieldlim = 0.060

Plastlim = 0.061
PlasticStrain = 0.015
Epox=((Yieldlim, 0.0), (Plastlim, PlasticStrain))

Sizing =((Yieldlim, 0.0), (Plastlim, PlasticStrain))
"""Simuleringsvariabler """
global Atapt_Damp_Ratio,Dampening,Stabl_Magn,Singlepin,tripplepin

Dampening = 1
Stabl_Magn =2e-4
Atapt_Damp_Ratio = 0.05

Singlepin = 0                               #   Randbetingelse:    Laaser hjornenode mot forskyvning i 3 retninger
tripplepin = 0                              #   Randbetingelse:    Laaser to noder mot forskyvning. En sentrert kantnode i 2 retninger og midtnode i 1 retning

global MaterialDens, ConDmPlast
ConDmPlast = 0
MaterialDens  = 0                           #   Material Density




"""    RVEmodel variabler                                      """
global noFibertest,Fibervariation,rmean,Rstdiv,Interface,rinterface,ElementInterfaceT,id, Retning

noFibertest = 0                                     # ON/OFF Fiber i modellen.
Fibervariation = 1                                  # ON/OFF variasjon fiberradius. Mean and standard div. Kan paavirke Vf i endelig model.


rmean = 8.7096                              # Gjennomsnittradius pa fiber
Rstdiv = 0.6374                             # OStandard avvik fra gjennomsnittsradius

Interface = 1                                   # ON/OFF CohesiveInterface
rinterface = 0.0001                              # Interfacetykkelse ved Sketching. Verdi er relativ til radius.    0.01 = 1%
AdjustElementInterfaceT = 0                  # Interfacetykkelse paa elementene.  Verdi er relativ til radius.
ElementInterfaceT = 0


id   =   np.identity(6)          # Identity matrix. Good for normalised load cases.'Exx','Eyy','Ezz','Exy','Exz','Eyz'
Retning =    ['Exx', 'Eyy', 'Ezz', 'Exy', 'Exz', 'Eyz']





"""Meshsize"""
global FiberSirkelResolution,meshsize,tykkelse,tol

FiberSirkelResolution =  20                                # Meshresolution pa Fiber omkrets. 2*pi/FiberSirkelResolution
meshsize = rmean * 2 * pi / FiberSirkelResolution           # Meshsize fra resolution paa interface paa fiberomkrets

tykkelse = meshsize    # RVE tykkelse
tol = rinterface * 0.4  # Modelleringstoleranse - Mindre en minste modelleringsvariabel (rInterface)





"""RVE populasjon"""
global r,gtol,ytredodgrense,indredodgrense,iterasjonsgrense,Rclearing

Rclearing = 0.02  # Minimumsavstand mellom fiberkant og RVE kant. Verdi relativ til radius. Skal den settes lik meshsize?

r = rmean       #Fordi jeg skrev koden med r som radius foer radius variasjon ble introdusert
gtol = Rclearing * r  # Fibers relative dodsone klarering for toleranse
ytredodgrense = r + gtol  # Dodzone avstand, ytre grense fra kanter/hjorner
indredodgrense = r - gtol  # Dodzone avstand, indre grense fra kanter/hjorner

iterasjonsgrense = 10000  # iterasjonsgrense i Fiberutplassering loop





""" ABAQUS modelleringsnavn    """

global modelName,partName, meshPartName, instanceName,stepName, difstpNm
modelName = 'Model-1'
partName, meshPartName = 'Part-1', 'Part-1-mesh-1'
instanceName = 'PART-1-MESH-1-1'
stepName, difstpNm = 'Enhetstoyninger', 'Lasttoyinger'