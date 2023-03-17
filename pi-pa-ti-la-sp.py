import random as R

class Gesto():
    PIEDRA = 1
    PAPEL = 2
    TIJERA = 3
    LAGARTO = 4
    SPOCK = 5
    def __init__(self):
        self.gesto = R.randint(Gesto.PIEDRA,Gesto.SPOCK)
        #self.PIEDRA = 1
        #self.PAPEL = 2
        #self.TIJERA = 3

    def __str__(self):
        if self.gesto == Gesto.PIEDRA:
            return "PIEDRA"
        else:
            if self.gesto == Gesto().PAPEL:
                return "PAPEL"
            else:
                if self.gesto == Gesto.TIJERA:
                    return "TIJERA"
                else:
                    if self.gesto == Gesto.LAGARTO:
                        return "LAGARTO"
                    else:
                        if self.gesto == Gesto.SPOCK:
                            return "SPOCK" 

class Jugador():
    def __init__(self,nombre="SHELDON"):
        self.nombre = nombre
        self.mano = Gesto()

    def __str__(self):
        return self.nombre

    def hacer_gesto(self):
        self.mano = Gesto()

class Humano():
    def __init__(self,nombre):
        self.nombre = nombre
        self.mano = " "

    def hacerGesto(self):
        print("---------------------------")
        print("PIEDRA --> PI\nPAPEL --> PA\nTIJERA --> TI\nLAGARTO --> LA\nSPOCK --> SP\n ")
        self.mano = input(self.nombre +" HAGA SU GESTO: ").upper()
        if self.mano == "PI":            
            self.mano = "PIEDRA" #+ " ✊"            
        else:
            if self.mano == "PA":
                self.mano = "PAPEL" #+ " ✋"                
            else:
                if self.mano == "TI":
                    self.mano = "TIJERA" #+ " ✌"             
                else:
                    if self.mano == "LA":
                        self.mano = "LAGARTO" #+  " 🐊"             
                    else:
                        if self.mano == "SP":
                            self.mano = "SPOCK" #+ " 🖖"
                        else:
                            print("EL VALOR INGRESADO NO ES CORRECTO VUELA A INTENTARLO.")
                            self.hacerGesto()


class Juego():
    def __init__(self,jugador1,jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
    
    def quienGana(self):
        
        # VERSION CORTA
        if str(self.jugador1.mano) == str(self.jugador2.mano):
            return None
        else:
            if str(self.jugador1.mano) == "PIEDRA" and str(self.jugador2.mano) == "TIJERA" or str(self.jugador1.mano) == "PIEDRA" and str(self.jugador2.mano) == "LAGARTO":
                return self.jugador1
            else:
                if str(self.jugador1.mano) == "PAPEL" and str(self.jugador2.mano) == "SPOCK" or str(self.jugador1.mano) == "PAPEL" and str(self.jugador2.mano) == "PIEDRA":
                    return self.jugador1                    
                else:
                    if str(self.jugador1.mano) == "TIJERA" and str(self.jugador2.mano) == "PAPEL" or str(self.jugador1.mano) == "TIJERA" and str(self.jugador2.mano) == "LAGARTO":
                        return self.jugador1
                    else:
                        if str(self.jugador1.mano) == "LAGARTO" and str(self.jugador2.mano) == "PAPEL" or str(self.jugador1.mano) == "LAGARTO" and str(self.jugador2.mano) == "SPOCK":
                            return self.jugador1
                        else:
                            if str(self.jugador1.mano) == "SPOCK" and str(self.jugador2.mano) == "PIEDRA" or str(self.jugador1.mano) == "SPOCK" and str(self.jugador2.mano) == "TIJERA":
                                return self.jugador1
                            else:
                                return self.jugador2        
                    
    def jugar(self):   
        cv1 = 0
        cv2 = 0
        jg = 0
        ronda = 1
        print("BIENVENIDOS A PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK")
        print("-----------------------------")
        print("REFERENCIAS:")
        print("PIEDRA: APLASTA TIJERA Y APLASTA LAGARTO")
        print("TIJERA: CORTA PAPEL Y DECAPITA LAGARTO")
        print("PAPEL: ENVUELVE PIEDRA Y DESAUTORIZA SPOCK")
        print("LAGARTO: ENVENENA SPOCK Y DEVORA PAPEL")
        print("SPOCK: ROMPE TIJERA Y VAPORIZA PIEDRA")
        print("-----------------------------")
        while cv1 < 2  and cv2 < 2:
           print("RONDA ",ronda) 
           self.jugador1.hacerGesto()
           print(self.jugador1.nombre," HACE ", self.jugador1.mano)
           print("-----------")
           self.jugador2.hacer_gesto()
           print(self.jugador2.nombre," HACE ", self.jugador2.mano)
           x = self.quienGana()
           if x == self.jugador1:
               cv1 += 1
               print("-----------------------------")
               print("GANA ", self.jugador1.nombre)
               print("-----------------------------")
               jg = 1
           else:
                if x == self.jugador2:
                    cv2 += 1
                    print("-----------------------------")
                    print("GANA ", self.jugador2.nombre)
                    print("-----------------------------")
                    jg = 2
                else:
                    print("-----------------------------")
                    print("EMPATARON")
                    print("-----------------------------")
           ronda += 1
        if jg == 1:
            print("GANADOR ",self.jugador1.nombre, " LE GANO ", cv1 , " a ", cv2)
        else:
            print("GANADOR ",self.jugador2.nombre, " LE GANO ", cv2 , " a ", cv1)
        


        


def main():
    jugador1 = Humano(input("ESCRIBA SU NOMBRE: "))
    jugador2 = Jugador("SHELDON")
    Juego(jugador1,jugador2).jugar()

main()
