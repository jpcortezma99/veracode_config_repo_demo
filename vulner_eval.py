# archivo: vulnerable_eval.py

def main():
    print("=== Calculadora rápida ===")
    print("Puedes escribir operaciones como 2+2 o 10/5")

    expresion = input("Ingresa una operación: ")

    try:
        # ⚠️ VULNERABILIDAD: ejecuta cualquier código ingresado
        resultado = eval(expresion)
        print("Resultado:", resultado)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()