from sistema_lavado import sistema_lava_smart

def main():
   # Creo una instancia de SistemaLavaSmart, que es la clase que coordina todo
   sistema = sistema_lava_smart()

   # Bucle principal del programa, se repite hasta que el usuario decida salir
   while True:
      print("\n===== SISTEMA LAVA SMART =====")
      print("1. Atender nuevo cliente")
      print("2. Mostrar reporte administrador y salir")
      # Leo la opción del usuario por teclado
      opcion = input("Seleccione una opción: ")

      if opcion == "1":
         # Llamo al método que pide los datos del cliente y procesa el ciclo de lavado
         sistema.atender_cliente()
      elif opcion == "2":
         # Muestro el reporte final del administrador y salgo del programa
         sistema.mostrar_reporte_administrador()
         break
      else:
         # Mensaje de validación cuando la opción no es correcta
         print("Opción no válida.")


# Punto de entrada del programa. Solo se ejecuta main() si corro este archivo directamente
if __name__ == "__main__":
   main()


