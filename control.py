
Kc=0.47
def getPoscillation(deltatime):
    Poscillation= -81.756*deltatime*deltatime + 18.069*deltatime-0.1803
    return Poscillation

def getkp():
    kp=0.6*Kc
    return kp

def getki(deltatime):
    Poscillation=getPoscillation(deltatime)
    ki=(0.6*Kc)/(0.5*Poscillation)
    return ki

def getkd(deltatime):
    Poscillation=getPoscillation(deltatime)
    kd=(0.125*Poscillation)*(0.6*Kc)
    return kd