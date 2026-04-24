import random

class Torre:
    def __init__(self, nombre, vida_maxima):
        self.nombre = nombre
        self.vida = vida_maxima
        self.vida_maxima = vida_maxima
        self.esta_viva = True
    def mostrar_condicion(self):
        # Proporción de asteriscos basada en 20 espacios
        proporcion = self.vida / self.vida_maxima
        estrellas = int(proporcion * 20)
        espacios = 20 - estrellas
        # Gráfico solicitado: |**********----------|
        barra = "|" + ("*" * estrellas) + ("-" * espacios) + "|"
        print(f"\n>>> MONITOREO: {self.nombre} <<<")
        print(f"ESTRUCTURA: {barra} {self.vida}/{self.vida_maxima} HP")
        if proporcion > 0.8:
            print("ESTADO: [INTEGRO]")
        elif proporcion > 0.4:
            print("ESTADO: [DAÑADO]")
        elif proporcion > 0:
            print("ESTADO: [CRÍTICO]")
        else:
            print("ESTADO: [COLAPSADO]")
    def recibir_ataque(self, danio):
        self.vida -= danio
        if self.vida <= 0:
            self.vida = 0
            self.esta_viva = False
        print(f"[!] Impacto recibido: -{danio} HP")
    def reparar(self):
        """Método de recuperación de vida"""
        if self.vida < self.vida_maxima:
            recuperacion = random.randint(15, 25)
            self.vida += recuperacion
            # Aseguramos que no sobrepase el máximo
            if self.vida > self.vida_maxima:
                self.vida = self.vida_maxima
            print(f"[+] Protocolo de reparación: +{recuperacion} HP recuperados.")
        else:
            print("[i] La estructura ya está al máximo nivel.")

class Juego:
    def __init__(self):
        self.mi_torre = Torre("Fortaleza Phoenix", 100)
        self.turnos = 0
    def jugar(self):
        print("INICIANDO DEFENSA TERRITORIAL")
        while self.mi_torre.esta_viva:
            self.turnos += 1
            self.mi_torre.mostrar_condicion()
            print("\n¿Qué acción desea tomar?")
            print("1. Activar Escudos (Recibe poco daño)")
            print("2. Contraatacar (Recibe daño normal)")
            print("3. REPARAR ESTRUCTURA (Recupera HP, pero el enemigo ataca)")
            opcion = input("\nSeleccione comando: ")
            if opcion == "1":
                danio = random.randint(5, 10)
                self.mi_torre.recibir_ataque(danio)
            elif opcion == "2":
                danio = random.randint(15, 25)
                self.mi_torre.recibir_ataque(danio)
            elif opcion == "3":
                self.mi_torre.reparar()
                # El enemigo siempre ataca aunque repares
                print("El enemigo aprovecha tus reparaciones para atacar.")
                self.mi_torre.recibir_ataque(random.randint(5, 15))
            else:
                print("Error de comando: La torre queda indefensa.")
                self.mi_torre.recibir_ataque(30)
        self.mi_torre.mostrar_condicion()
        print("\n" + "="*35)
        print("   GAME OVER - LA TORRE HA CAÍDO")
        print(f"   Resistencia total: {self.turnos} turnos")
        print("="*35)

if __name__ == "__main__":
    partida = Juego()
    partida.jugar()