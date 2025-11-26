import time
from datetime import datetime
import winsound
import os


class Lavadora_base:
   def __init__(self, kilos, tipo_ropa, estrato, tiempo_lavado=45, potencia_kw=0.5):
      # Atributos "protegidos" (por convención, un guion bajo) que puedo usar
      # tanto en esta clase como en las clases hijas.
      self._kilos = kilos
      self._tipo_ropa = tipo_ropa

      # Atributo privado solo se debe acceder dentro de esta clase.
      self.__estado = "apagada"

      self._tiempo_lavado = tiempo_lavado
      self._precio_kilo = 10000
      self._aumento_especial = 0.05
      self._iva = 0.19
      self._potencia_kw = potencia_kw
      self._estrato = estrato

      # Variables internas para ir guardando los cálculos del servicio
      self._costo_sin_iva = 0
      self._costo_aumento = 0
      self._iva_valor = 0
      self._costo_total_servicio = 0
      self._consumo_kwh = 0
      self._costo_energia = 0
      self._utilidad_empresario = 0
      self._total_pagar = 0

   def encender(self):
      #Enciende la lavadora y reproduce el sonido de encendido.

      if self.__estado == "encendida":
         # Si ya está encendida, solo muestro un mensaje y salgo
         print("La lavadora ya está encendida.")
         return
      # Cambio el estado interno a encendida
      self.__estado = "encendida"
      print("Encendido")
      # Busco el archivo de sonido en la misma carpeta donde está este archivo .py
      base_dir = os.path.dirname(__file__)
      sound_path = os.path.join(base_dir, "lavadora_encendido.wav")
      # Reproduzco el sonido de encendido de forma asíncrona
      winsound.PlaySound(
         sound_path,
         winsound.SND_FILENAME | winsound.SND_ASYNC
      )
      time.sleep(2)
      # Detengo el sonido
      winsound.PlaySound(None, 0)

   def _validar_kilos(self):
      #Método interno para validar que los kilos estén en el rango permitido
      if self._kilos < 5 or self._kilos > 40:
         raise ValueError("Los kilos deben estar entre 5 y 40.")

   def _llenar(self):
      #Simula el llenado de la lavadora con agua y reproduce el sonido respectivo
      print("Llenando la lavadora...")
      base_dir = os.path.dirname(__file__)
      sound_path = os.path.join(base_dir, "lavadora_llenado.wav")
      winsound.PlaySound(
         sound_path,
         winsound.SND_FILENAME | winsound.SND_ASYNC
      )
      time.sleep(6)
      winsound.PlaySound(None, 0)

   def lavar(self):
      #Método genérico de lavado de la clase base.

      #Las clases hijas pueden sobreescribir este método (polimorfismo) para
      #personalizar el tipo de lavado, pero en todos los casos se puede reutilizar
      #este comportamiento básico.

      print("Lavando...")
      base_dir = os.path.dirname(__file__)
      sound_path = os.path.join(base_dir, "lavadora.wav")
      winsound.PlaySound(
         sound_path,
         winsound.SND_FILENAME | winsound.SND_ASYNC
      )
      time.sleep(6)
      winsound.PlaySound(None, 0)

   def _enjuagar(self):
      #Simula el enjuague de la ropa y reproduce el sonido correspondiente
      print("Enjuagando la ropa...")
      base_dir = os.path.dirname(__file__)
      sound_path = os.path.join(base_dir, "lavadora_enjuagado.wav")
      try:
         winsound.PlaySound(
            sound_path,
            winsound.SND_FILENAME | winsound.SND_ASYNC
         )
         time.sleep(6)
         winsound.PlaySound(None, 0)
      except Exception:
         # Si hay algún problema con el sonido, no detengo el programa
         pass

   def _secar(self):
      #Simula el secado de la ropa y reproduce el sonido de secado
      print("Secando la ropa...")
      base_dir = os.path.dirname(__file__)
      sound_path = os.path.join(base_dir, "lavadora_secado.wav")
      winsound.PlaySound(
         sound_path,
         winsound.SND_FILENAME | winsound.SND_ASYNC
      )
      time.sleep(5)
      winsound.PlaySound(None, 0)

   def __calcular_costos(self):
      #Método privado que calcula los costos del servicio de lavado
      self._costo_sin_iva = self._kilos * self._precio_kilo

      tipos_especiales = ["interior", "pijamas", "vestidos"]
      if self._tipo_ropa.lower() in tipos_especiales:
         self._costo_aumento = self._costo_sin_iva * self._aumento_especial
      else:
         self._costo_aumento = 0
      #aplica el iva para el tipo de ropa especial, valida cual es y luego lo aplica
      subtotal = self._costo_sin_iva + self._costo_aumento
      self._iva_valor = subtotal * self._iva
      self._costo_total_servicio = subtotal + self._iva_valor

      # La utilidad del empresario es el 30% del costo total
      self._utilidad_empresario = self._costo_total_servicio * 0.30

   def __calcular_consumo_energia(self):
      #Método privado que calcula el consumo de energía y su costo
      self._consumo_kwh = self._potencia_kw * (self._tiempo_lavado / 60)

      tarifas = {
         2: 867.8,
         3: 737.6,
         4: 867.8,
         5: 1041,
      }

      # Obtengo la tarifa según el estrato, si no existe uso un valor por defecto
      valor_kwh = tarifas.get(self._estrato, 737.6)
      self._costo_energia = self._consumo_kwh * valor_kwh

   def _mostrar_reporte_cliente(self, nombre_cliente, metodo_lavado):
      #Imprime en pantalla el reporte completo para el cliente
      fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      self._total_pagar = self._costo_total_servicio + self._costo_energia

      print("\n----- REPORTE CLIENTE -----")
      print(f"Fecha y hora: {fecha_hora}")
      print(f"Nombre del cliente: {nombre_cliente}")
      print(f"Kilos lavados: {self._kilos}")
      print(f"Tipo de prenda: {self._tipo_ropa}")
      print(f"Método de lavado: {metodo_lavado}")
      print(f"Costo por kilo: {self._precio_kilo}")
      print(f"Costo total sin IVA: {self._costo_sin_iva:.0f}")
      print(f"Costo adicional 5%: {self._costo_aumento:.0f}")
      print(f"IVA (19%): {self._iva_valor:.0f}")
      print(f"Costo total servicio (con IVA): {self._costo_total_servicio:.0f}")
      print(f"Consumo de energía (kWh): {self._consumo_kwh:.2f}")
      print(f"Costo energético: {self._costo_energia:.0f}")
      print(f"Consumo total (energía + servicios): {self._total_pagar:.0f}")
      print(f"Total a pagar: {self._total_pagar:.0f}")
      print("Gracias por usar Lava Smart")

   def ciclo_terminado(self, nombre_cliente, metodo_lavado, desea_secar=True):
      #Orquesta todo el ciclo de la lavadora encender, lavar, secar, etc.
      #Aquí también se ve el polimorfismo, porque cuando llamo self.lavar(), en tiempo
      #de ejecución se usará la versión de lavar() de la clase hija estándar o
      #inteligente
      try:
         # Primero enciendo la lavadora
         self.encender()
         # Valido que los kilos estén en el rango permitido
         self._validar_kilos()
         print(f"Tipo de ropa seleccionada: {self._tipo_ropa}")
         print(f"Costo por kilo: {self._precio_kilo}")
         # Lleno la lavadora
         self._llenar()
         # Llamo al método lavar. Gracias al polimorfismo, si el objeto es una
         # LavadoraEstandar o una LavadoraInteligente, se ejecuta su propia versión
         # de lavar(), aunque este método esté definido aquí en la clase base.
         self.lavar()
         # Enjuago la ropa
         self._enjuagar()
         # Si el cliente quiere, también seco la ropa
         if desea_secar:
            self._secar()
         # Calculo los costos del servicio y el consumo de energía
         self.__calcular_costos()
         self.__calcular_consumo_energia()
         # Muestro el reporte final al cliente
         self._mostrar_reporte_cliente(nombre_cliente, metodo_lavado)

         # Retorno un diccionario con toda la información para el módulo administrador
         return {
            "nombre_cliente": nombre_cliente,
            "kilos": self._kilos,
            "tipo_ropa": self._tipo_ropa,
            "metodo_lavado": metodo_lavado,
            "costo_sin_iva": self._costo_sin_iva,
            "costo_aumento": self._costo_aumento,
            "iva_cobrado": self._iva_valor,
            "costo_total_servicio": self._costo_total_servicio,
            "consumo_kwh": self._consumo_kwh,
            "costo_energia": self._costo_energia,
            "total_pagar": self._total_pagar,
            "utilidad_empresario": self._utilidad_empresario,
         }
      except ValueError as error:
         # Capturo errores de validación (por ejemplo, kilos fuera de rango)
         print(f"Error en el ciclo de lavado: {error}")
         return None

