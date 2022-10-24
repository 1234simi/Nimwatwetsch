import pytest
from Taschenrechner import berechnungen_machen
print("pytest Version: ",pytest.__version__)
print(" ")
# =============================================================================
# Zum testen, ob die Funktion 'berechnungen_machen()' auch importiert wurde:
# =============================================================================
berechnungen_machen(1,'q',2)
