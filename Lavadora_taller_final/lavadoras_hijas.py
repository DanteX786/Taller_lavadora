from Lavadora_padre import Lavadora_base # Importo la clase base de la cual heredan las lavadoras hijas


class Lavadora_estandar(Lavadora_base):
   #Clase que representa una lavadora estándar.
   #Hereda de Lavadora_base y sobreescribe el método lavar para personalizar el mensaje.
   #Aquí se ve el uso de polimorfismo porque tiene su propia versión de lavar().

   def lavar(self):
      # Sobreescribo el método lavar de la clase base solo para mantener la estructura,
      # pero delego completamente el comportamiento al método de la clase padre.
      # Así, el mensaje que se muestra es el genérico "Lavando..." definido en Lavadora_base.
      super().lavar()


class Lavadora_inteligente(Lavadora_base):
   #Clase que representa una lavadora inteligente.
   #Hereda de Lavadora_base y además simula el uso de sensores para detectar
   #el tipo de ropa antes de realizar el ciclo de lavado completo.

   def __init__(self, kilos, tipo_ropa, estrato, tiempo_lavado=45, potencia_kw=0.5): 
      # Llamo al constructor de la clase base para inicializar los atributos comunes
      super().__init__(kilos, tipo_ropa, estrato, tiempo_lavado, potencia_kw)

   def detectar_tipo_ropa(self):
      # Este método simula el uso de sensores para detectar el tipo de prenda.
      # Muestro también el tipo de ropa que el usuario ingresó.
      print(f"Detectando con sensores tipo de ropa: {self._tipo_ropa}")

   def lavar(self):
      # Reutilizo directamente el comportamiento de lavado general de la clase base,
      # que muestra el mensaje genérico "Lavando..." y reproduce el sonido.
      super().lavar()

   def ciclo_terminado(self, nombre_cliente, metodo_lavado, desea_secar=True):
      #En la lavadora inteligente mantengo el mismo ciclo que en Lavadora_base,
      #pero después de encender y validar kilos uso los sensores para detectar
      #el tipo de ropa antes de mostrar la información al usuario.

      try:
         # Primero enciendo la lavadora (igual que en la clase base)
         self.encender()
         # Valido que los kilos estén en el rango permitido
         self._validar_kilos()
         # Aquí uso los sensores para detectar el tipo de ropa
         self.detectar_tipo_ropa()
         # Luego muestro la información general igual que en la clase base
         print(f"Tipo de ropa seleccionada: {self._tipo_ropa}")
         print(f"Costo por kilo: {self._precio_kilo}")
         # Lleno la lavadora
         self._llenar()
         # Llamo al método lavar (gracias al polimorfismo se usará la versión de esta clase)
         self.lavar()
         # Enjuago la ropa
         self._enjuagar()
         # Si el cliente quiere, también seco la ropa
         if desea_secar:
            self._secar()
         # Calculo los costos del servicio y el consumo de energía
         self._Lavadora_base__calcular_costos()
         self._Lavadora_base__calcular_consumo_energia()
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

