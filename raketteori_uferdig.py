'''
Dette er et uferdig Python program for aa regne ut raketteori paa talentsenter 2018.

Python er et moderne programmeringsspraak som er lett og bruke.
Alt man kan gjore paa en datamaskin kan man gjore forholdvis enkelt i python.

Python kan lastes ned fra blant annet https://www.python.org/downloads/
Aapne denne filen i IDLE og trykk F5 (run).

Python tips:
- Det finnes ubegrenset med hjelp hvis man googler sine python problemer.
    Forumet "stackoverflow" er utrolig bra.
- Unngaa æ,ø,å. Da kan man mote uforstaaelige problemer som selv ikke stackoverflow kan svare paa.
- Punktum i stedet for komma naar det gjelder desimaltall.
- Tegn med # foran, blir ignorert av python
- Tegn mellom '''   ''' blir ignorert av python.
- Ikke rediger python code i Word. Bruk for eksembel IDLE, ATOM, xcode
- Moduler som numpy og matplotlib er helt legendarisk for matematiske utregninger og grafer.
'''


# importer modul(er)
import math as math

# definer en funksjon.
def hovedprogram_kanhetehvasomhelst():

    ############ Definer variabler i henhold til maalinger/tabeller #############
    F_thrust = 6.0 # Newton
    diameter = 0.03 # m
    halefinn_area_mean = 0.004*0.04 # m^2
    C_d = 0.7
    rho = 1.2 # kg/m3
    t_b = 1.6 # sekund
    m_rakett_uten_motor = 95 * 10**(-3) #kg         # 10**(3) = 1000 = 10^3
    m_motor_total = 2.0 * 10**(-3) #kg
    m_drifstoff = 11.0 * 10**(-3) #kg
    ############################################################################

    g_0 = 9.8 #m/s
    A_max = 3.14 * (diameter/2)**2 + 3*halefinn_area_mean
    beta = 0.5 * C_d * rho * A_max
    M = m_rakett_uten_motor + m_motor_total
    M_b = M - m_drifstoff

    M_mean = (M + M_b)*0.5
    q = math.sqrt((F_thrust - M_mean*g_0)/(beta))
    p = 2 * beta * q / M_mean
    v_max = q*((1-math.exp(-p*t_b))/(1+math.exp(-p*t_b)))

    q_a = math.sqrt(M_b*g_0/beta)

    arc_tan = math.atan(v_max/q_a)


    ###################### Print variabler #####################################

    print("A_max = %.10f" % (A_max))
    print("M_mean = %.2f" % (M_mean))
    print("V_max = %.2f" % (v_max))

    ############################################################################

# man kan kommentere ut disse linjene ved aa sette # foran print.
print("")
print("Raketteori, talentsenter 2018")
print("")

#execute funksjon
hovedprogram_kanhetehvasomhelst()
