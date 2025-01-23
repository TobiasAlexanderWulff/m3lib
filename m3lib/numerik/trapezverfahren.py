import numpy as np
import fractions

def trapezverfahren(f, a, b, n):
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
    
    Rückgabe:
    float
        Näherung des bestimmten Integrals
    """
    h = (b - a) / n # Schrittweite
    x = np.linspace(a, b, n + 1) # Stützstellen
    y = f(x) 
    return (h / 2) * (y[0] + y[-1] + 2 * np.sum(y[1:-1]))

def max_feher_trapezverfahren(f2, a, b, n):
    """
    Berechnet den maximalen Fehler des Trapezverfahrens
    
    Parameter:
    f2 : function 
        Zweite Ableitung des Integranden
    a : float
        Untere Grenze
    b : float
        Obere Grenze
    n : int
        Anzahl der Teilintervalle/Säulen (Stützstellen - 1)
        
    Rückgabe:
    float
        Fehler des Trapezverfahrens
    """
    h = (b - a) / n # Schrittweite
    x = np.linspace(a, b, n + 1) # Stützstellen
    return ((b - a) / 12) * h**2 * np.max(np.abs(f2(x)))
