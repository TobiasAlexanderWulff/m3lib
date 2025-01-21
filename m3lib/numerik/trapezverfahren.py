import numpy as np
import fractions

def trapezverfahren(f, a, b, n, display="default"):
    """
    Berechnet das bestimmte Integral von f(x) von a bis b
    
    Parameter:
    f : function
        Integrand
    a : float
        Untere Grenze
    b : float
        Obere Grenze
    n : int
        Anzahl der Teilintervalle/Säulen (Stützstellen - 1)
    display : str
        Anzeigeoptionen für die Rückgabe
        "default" - Standardanzeige
        "fraction" - Bruchan
    
    Rückgabe:
    float
        Näherung des bestimmten Integrals
    """
    if display is "fraction":
        np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
    h = (b - a) / n # Schrittweite
    x = np.linspace(a, b, n + 1) # Stützstellen
    y = f(x) 
    return (h / 2) * (y[0] + y[-1] + 2 * np.sum(y[1:-1]))
