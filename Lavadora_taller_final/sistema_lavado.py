from lavadoras_hijas import Lavadora_estandar, Lavadora_inteligente 

class sistema_lava_smart:

   #Clase que maneja la lógica general del sistema de lavadoras.
   #Desde aquí se atiende a los clientes, se crean las lavadoras (estándar o inteligentes)
   #y se van sumando los datos para el reporte del administrador
   

   def __init__(self):
      # Contadores y acumuladores para la parte administrativa
      self._total_clientes = 0
      self._total_iva = 0
      self._total_ganancia = 0
      # Aquí voy guardando lo que paga cada cliente
      self._total_facturado_por_cliente = []

   def _crear_lavadora(self, tipo_lavadora, kilos, tipo_ropa, estrato):
      #Método interno que decide qué tipo de lavadora crear según la opción del usuario
      if tipo_lavadora == "estandar":
         # Retorno una instancia de Lavadora_estandar
         return Lavadora_estandar(kilos, tipo_ropa, estrato)
      elif tipo_lavadora == "inteligente":
         # Retorno una instancia de Lavadora_inteligente
         return Lavadora_inteligente(kilos, tipo_ropa, estrato)
      else:
         # Valido que el tipo de lavadora sea correcto
         raise ValueError("Tipo de lavadora no válido")

   def atender_cliente(self):
      nombre_cliente = input("Nombre del cliente: ")
      # Manejo de errores al convertir los kilos a número
      try:
         kilos = float(input("Kilos de ropa (5 a 40): "))
      except ValueError:
         print("Entrada inválida para kilos.")
         return

      tipo_ropa = input("Tipo de prenda (ej: diario, interior, pijamas, vestidos): ")

      # Manejo de errores al convertir el estrato a entero
      try:
         estrato = int(input("Estrato (2, 3, 4, 5): "))
      except ValueError:
         print("Entrada inválida para estrato.")
         return

      # Menú para escoger el tipo de lavadora que se va a usar
      print("Seleccione tipo de lavadora:")
      print("1. Estandar")
      print("2. Inteligente")
      opcion = input("Opción: ")

      if opcion == "1":
         tipo_lavadora = "estandar"
      elif opcion == "2":
         tipo_lavadora = "inteligente"
      else:
         print("Opción no válida.")
         return

      # Aquí uso el método que crea la lavadora según la opción del usuario
      lavadora = self._crear_lavadora(tipo_lavadora, kilos, tipo_ropa, estrato)

      # Pregunto si el cliente quiere secar la ropa además de lavarla
      desea_secar = input("¿Desea secar? (s/n): ").lower() == "s"

      # Ejecuto todo el ciclo de la lavadora. Este método viene de la clase base.
      resumen = lavadora.ciclo_terminado(nombre_cliente, tipo_lavadora, desea_secar)

      # Si hubo algún error, resumen será None y salgo del método
      if resumen is None:
         return

      # Acumulo los valores para el reporte del administrador
      self._total_clientes += 1
      self._total_iva += resumen["iva_cobrado"]
      self._total_ganancia += resumen["utilidad_empresario"]
      self._total_facturado_por_cliente.append({
         "nombre_cliente": resumen["nombre_cliente"],
         "total_pagar": resumen["total_pagar"],
      })

   def mostrar_reporte_administrador(self):
      """Muestra por pantalla un resumen de todos los clientes atendidos."""
      print("\n===== REPORTE ADMINISTRADOR =====")
      print(f"Total de clientes atendidos: {self._total_clientes}")
      print(f"IVA cobrado: {self._total_iva:.0f}")
      print(f"Ganancia neta (30%): {self._total_ganancia:.0f}")
      print("Total facturado por cliente:")
      for factura in self._total_facturado_por_cliente:
         print(f"- {factura['nombre_cliente']}: {factura['total_pagar']:.0f}")
