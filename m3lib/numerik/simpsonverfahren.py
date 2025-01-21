import numpy as np
import fractions

def simpsonverfahren(f, a, b, n):
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
        Anzahl der Teilintervalle/Doppelsäulen (Stützstellen - 1)
    
    Rückgabe:
    float
        Näherung des bestimmten Integrals
    """
    h = (b - a) / (2 * n) # Schrittweite (2n wegen Doppelsäulen)
    x = np.linspace(a, b, 2 * n + 1) # Stützstellen
    y = f(x) 
    return (h / 3) * (y[0] + y[-1] + 2 * np.sum(y[2:-2:2]) + 4 * np.sum(y[1:-1:2]))


def max_fehler_simpsonverfahren(f4, a, b, n):
    """
    Berechnet den maximalen Fehler des Simpsonverfahrens
    
    Parameter:
    f4 : function 
        Vierte Ableitung des Integranden
    a : float
        Untere Grenze
    b : float
        Obere Grenze
    n : int
        Anzahl der Teilintervalle/Doppelsäulen (Stützstellen - 1)
        
    Rückgabe:
    float
        Fehler des Simpsonverfahrens
    """
    h = (b - a) / (2 * n) # Schrittweite (2n wegen Doppelsäulen)
    x = np.linspace(a, b, 2 * n + 1) # Stützstellen
    return ((b - a) / 180) * h**4 * np.max(np.abs(f4(x)))
