try:
    x=5
    y="8"
    s=x+y
    print(s)
except NameError:
    print("No se declaro variable!!")
except TypeError:
    print("Una de la variables tiene un formato distino!")
except:
    print("Algo salio mal!!")