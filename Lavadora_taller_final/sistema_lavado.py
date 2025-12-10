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
      while True:
         nombre_cliente= input("Nombre del cliente: ").strip()
         if nombre_cliente:
            break
         print("El nombre del cliente no puede estar vacío.")
   
      while True:
         try:
            
            entrada = input("Kilos de ropa (5 a 40): ").strip()
            kilos = float(entrada) 
            
            if kilos < 5 or kilos > 40:
               print(f"Error: {kilos} kg está fuera del rango (5-40 kg)")
               continue
            break 
            
         except ValueError:
            print("Error: Debe ingresar un número válido.")
      
      tipos_permitidos = ["diario", "interior", "pijamas", "vestidos"]
      while True:
         tipo_ropa = input("Tipo de prenda (ej: diario, interior, pijamas, vestidos): ").strip().lower()
         if tipo_ropa in tipos_permitidos:
            break
         print(f"Tipo de prenda no válido. Debe ser uno de: {', '.join(tipos_permitidos)}")
      # Manejo de errores al convertir el estrato a entero
      
      while True:
         entrada_estrato = input("Estrato (2, 3, 4, 5): ").strip()
         if entrada_estrato in ["2", "3", "4", "5"]: 
            estrato = int(entrada_estrato)
            break  
         print("Error: Debe ingresar 2, 3, 4 o 5. Intente nuevamente.")
      while True:
        print("\nSeleccione tipo de lavadora:")
        print("1. Estandar")
        print("2. Inteligente")
        opcion = input("Opción (1 o 2): ").strip()
        
        if opcion == "1":
            tipo_lavadora = "estandar"
            break  
        elif opcion == "2":
            tipo_lavadora = "inteligente"
            break 
        print("Error: Debe ingresar 1 o 2. Intente nuevamente.")

        
      # Pregunto si el cliente quiere secar la ropa además de lavarla
      while True:
        respuesta = input("¿Desea secar? (s/n): ").strip().lower()
        if respuesta in ["s", "si", "sí"]:
            desea_secar = True
            break 
        elif respuesta in ["n", "no"]:
            desea_secar = False
            break 
        print("Error: Responda 's' para SÍ o 'n' para NO. Intente nuevamente.")


      # Aquí uso el método que crea la lavadora según la opción del usuario
      lavadora = self._crear_lavadora(tipo_lavadora, kilos, tipo_ropa, estrato)

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
