from manim import *

class EcuacionSistemaBachillerato(Scene):
    def construct(self):
        # Configure for YouTube Shorts (1080x1920)
        self.camera.frame_center = ORIGIN + UP * 1.5  # Shift camera up to keep content visible
        
        # Título más formal con fuentes más grandes
        titulo = Text("Solución de Sistemas", font_size=48, color=BLUE)
        subtitulo = Text("Método de Eliminación", font_size=36, color=BLUE_B)
        titulo_grupo = VGroup(titulo, subtitulo).arrange(DOWN, buff=0.3)
        titulo_grupo.to_edge(UP, buff=0.4)
        
        self.play(Write(titulo))
        self.wait(0.5)
        self.play(Write(subtitulo))
        self.wait(1)

        # Contexto del problema con fuente más grande
        contexto = Text("Problema: Encontrar el par ordenado que satisface:", font_size=28)
        contexto.next_to(titulo_grupo, DOWN, buff=0.5)
        self.play(Write(contexto))
        self.wait(1)

        # Pares dados con formato de tabla y fuentes más grandes
        pares_titulo = Text("Pares a evaluar:", font_size=26, color=YELLOW)
        pares_titulo.next_to(contexto, DOWN, buff=0.4)
        self.play(Write(pares_titulo))
        
        pares_lista = MathTex(
            "A = [10,12] \\quad B = [12,18] \\\\",
            "C = [18,22] \\quad D = [22,30]",
            font_size=32
        )
        pares_lista.next_to(pares_titulo, DOWN, buff=0.3)
        self.play(Write(pares_lista))
        self.wait(2)

        # Limpiar elementos iniciales
        elementos_iniciales = VGroup(titulo_grupo, contexto, pares_titulo)
        self.play(FadeOut(elementos_iniciales))
        
        # Mover pares hacia arriba (más arriba para YouTube Shorts)
        self.play(pares_lista.animate.to_edge(UP, buff=0.5))
        
        # Explicación detallada de cada ecuación con fuentes más grandes
        explicacion1 = Text(
            "1° ecuación:", 
            font_size=24, 
            color=GREEN
        )
        explicacion1_desc = Text(
            "'Primero + mitad del segundo = 21'",
            font_size=20,
            color=GREEN
        )
        explicacion1_grupo = VGroup(explicacion1, explicacion1_desc).arrange(DOWN, buff=0.1)
        explicacion1_grupo.next_to(pares_lista, DOWN, buff=0.5)
        self.play(Write(explicacion1_grupo))
        
        ecuacion1_paso1 = MathTex("x + \\frac{1}{2}y = 21", font_size=36)
        ecuacion1_paso1.next_to(explicacion1_grupo, DOWN, buff=0.3)
        self.play(Write(ecuacion1_paso1))
        self.wait(2)

        explicacion2 = Text(
            "2° ecuación:",
            font_size=24, 
            color=GREEN
        )
        explicacion2_desc = Text(
            "'Tercera parte negativa del segundo'",
            font_size=18,
            color=GREEN
        )
        explicacion2_desc2 = Text(
            "'+ doble del primero = 18'",
            font_size=18,
            color=GREEN
        )
        explicacion2_grupo = VGroup(explicacion2, explicacion2_desc, explicacion2_desc2).arrange(DOWN, buff=0.1)
        explicacion2_grupo.next_to(ecuacion1_paso1, DOWN, buff=0.4)
        self.play(Write(explicacion2_grupo))
        
        ecuacion2_paso1 = MathTex("-\\frac{1}{3}y + 2x = 18", font_size=36)
        ecuacion2_paso1.next_to(explicacion2_grupo, DOWN, buff=0.3)
        self.play(Write(ecuacion2_paso1))
        self.wait(2)

        # Fade out ecuaciones individuales
        self.play(FadeOut(ecuacion1_paso1), FadeOut(ecuacion2_paso1))

        # Limpiar explicaciones y preparar sistema
        explicaciones = VGroup(explicacion1_grupo, explicacion2_grupo)
        self.play(FadeOut(explicaciones))
        
        sistema_titulo = Text("Sistema de ecuaciones:", font_size=28, color=YELLOW)
        sistema_titulo.next_to(pares_lista, DOWN, buff=0.6)
        self.play(Write(sistema_titulo))
        
        # Sistema con fuente más grande
        sistema_ecuaciones = MathTex(
            "\\begin{cases} "
            "x + \\dfrac{1}{2}y = 21 \\\\ "
            "2x - \\dfrac{1}{3}y = 18 "
            "\\end{cases}",
            font_size=40
        )
        sistema_ecuaciones.next_to(sistema_titulo, DOWN, buff=0.4)
        self.play(Write(sistema_ecuaciones))
        self.wait(2)

        # Limpiar para método de eliminación
        elementos_sistema = VGroup(pares_lista, sistema_titulo)
        self.play(FadeOut(elementos_sistema))
        
        paso1_titulo = Text("Paso 1: Eliminar denominadores", font_size=30, color=ORANGE)
        paso1_titulo.to_edge(UP, buff=0.6)
        self.play(Write(paso1_titulo))
        
        # Mover sistema hacia abajo
        self.play(sistema_ecuaciones.animate.next_to(paso1_titulo, DOWN, buff=0.6))
        
        paso1_explicacion = Text(
            "Multiplicamos para eliminar fracciones:",
            font_size=24
        )
        paso1_explicacion.next_to(sistema_ecuaciones, DOWN, buff=0.4)
        self.play(Write(paso1_explicacion))
        
        paso1_ecuacion1 = MathTex("\\text{Ec. 1} \\times 2: \\quad 2x + y = 42", font_size=32)
        paso1_ecuacion1.next_to(paso1_explicacion, DOWN, buff=0.3)
        self.play(Write(paso1_ecuacion1))
        
        paso1_ecuacion2 = MathTex("\\text{Ec. 2} \\times 3: \\quad 6x - y = 54", font_size=32)
        paso1_ecuacion2.next_to(paso1_ecuacion1, DOWN, buff=0.3)
        self.play(Write(paso1_ecuacion2))
        self.wait(2)

        # Limpiar para paso 2
        elementos_paso1 = VGroup(paso1_explicacion, sistema_ecuaciones)
        self.play(FadeOut(elementos_paso1))
        
        paso2_titulo = Text("Paso 2: Eliminación", font_size=30, color=ORANGE)
        paso2_titulo.to_edge(UP, buff=0.6)
        self.play(Transform(paso1_titulo, paso2_titulo))
        
        ecuaciones_sin_fracciones = VGroup(paso1_ecuacion1, paso1_ecuacion2)
        self.play(ecuaciones_sin_fracciones.animate.next_to(paso1_titulo, DOWN, buff=0.6))
        
        paso2_explicacion = Text("Sumamos para eliminar y:", font_size=24)
        paso2_explicacion.next_to(ecuaciones_sin_fracciones, DOWN, buff=0.4)
        self.play(Write(paso2_explicacion))
        
        suma_ecuaciones = MathTex(
            "(2x + y) + (6x - y) = 42 + 54",
            font_size=32
        )
        suma_ecuaciones.next_to(paso2_explicacion, DOWN, buff=0.3)
        self.play(Write(suma_ecuaciones))
        self.wait(1)
        
        suma_simplificada = MathTex("8x = 96", font_size=32)
        suma_simplificada.move_to(suma_ecuaciones.get_center())
        self.play(Transform(suma_ecuaciones, suma_simplificada))
        self.wait(1)
        
        solucion_x = MathTex("x = \\frac{96}{8} = 12", font_size=32, color=GREEN)
        solucion_x.next_to(suma_ecuaciones, DOWN, buff=0.3)
        self.play(Write(solucion_x))
        self.wait(2)

        # Limpiar para paso 3
        elementos_paso2 = VGroup(paso2_explicacion, suma_ecuaciones)
        self.play(FadeOut(elementos_paso2))
        
        paso3_titulo = Text("Paso 3: Sustitución", font_size=30, color=ORANGE)
        paso3_titulo.to_edge(UP, buff=0.6)
        self.play(Transform(paso1_titulo, paso3_titulo))
        
        # Mover ecuaciones y x=12
        grupo_actual = VGroup(ecuaciones_sin_fracciones, solucion_x)
        self.play(grupo_actual.animate.next_to(paso1_titulo, DOWN, buff=0.6))
        
        paso3_explicacion = Text("Sustituimos x = 12:", font_size=24)
        paso3_explicacion.next_to(solucion_x, DOWN, buff=0.4)
        self.play(Write(paso3_explicacion))
        
        sustitucion = MathTex("2(12) + y = 42", font_size=32)
        sustitucion.next_to(paso3_explicacion, DOWN, buff=0.3)
        self.play(Write(sustitucion))
        self.wait(1)
        
        sustitucion2 = MathTex("24 + y = 42", font_size=32)
        sustitucion2.move_to(sustitucion.get_center())
        self.play(Transform(sustitucion, sustitucion2))
        self.wait(1)
        
        sustitucion3 = MathTex("y = 42 - 24 = 18", font_size=32, color=GREEN)
        sustitucion3.move_to(sustitucion.get_center())
        self.play(Transform(sustitucion, sustitucion3))
        self.wait(2)

        # Limpiar para solución final
        elementos_paso3 = VGroup(paso3_explicacion, ecuaciones_sin_fracciones)
        self.play(FadeOut(elementos_paso3))
        
        solucion_titulo = Text("Solución encontrada:", font_size=32, color=YELLOW)
        solucion_titulo.to_edge(UP, buff=0.8)
        self.play(Transform(paso1_titulo, solucion_titulo))
        
        solucion_grupo = VGroup(solucion_x, sustitucion)
        self.play(solucion_grupo.animate.arrange(RIGHT, buff=1.0).next_to(paso1_titulo, DOWN, buff=0.6))
        
        par_ordenado = MathTex("\\therefore (x, y) = (12, 18)", font_size=38, color=GREEN)
        par_ordenado.next_to(solucion_grupo, DOWN, buff=0.5)
        self.play(Write(par_ordenado))
        self.wait(2)

        # Limpiar para verificación
        self.play(FadeOut(solucion_grupo), FadeOut(par_ordenado))
        
        verificacion_titulo = Text("Verificación:", font_size=30, color=BLUE)
        verificacion_titulo.next_to(paso1_titulo, DOWN, buff=0.6)
        self.play(Write(verificacion_titulo))
        
        # Verificación ecuación 1 con fuentes más grandes
        verif1_texto = Text("Ecuación 1:", font_size=24)
        verif1_texto.next_to(verificacion_titulo, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(verif1_texto))
        
        verif1_pasos = MathTex(
            "12 + \\frac{1}{2}(18) = 12 + 9 = 21 \\quad \\checkmark",
            font_size=28,
            color=GREEN
        )
        verif1_pasos.next_to(verif1_texto, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(verif1_pasos))
        self.wait(1)
        
        # Verificación ecuación 2
        verif2_texto = Text("Ecuación 2:", font_size=24)
        verif2_texto.next_to(verif1_pasos, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(verif2_texto))
        
        verif2_pasos = MathTex(
            "2(12) - \\frac{1}{3}(18) = 24 - 6 = 18 \\quad \\checkmark",
            font_size=28,
            color=GREEN
        )
        verif2_pasos.next_to(verif2_texto, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(verif2_pasos))
        self.wait(2)

        # Limpiar para conclusión
        elementos_verificacion = VGroup(verificacion_titulo, verif1_texto, verif1_pasos, verif2_texto, verif2_pasos)
        self.play(FadeOut(elementos_verificacion), FadeOut(paso1_titulo))
        
        # CONCLUSIÓN FINAL - Centrada y con fuentes grandes
        respuesta_final = Text("RESPUESTA:", font_size=42, color=YELLOW, weight=BOLD)
        par_correcto = Text("[12, 18]", font_size=56, color=GREEN, weight=BOLD)
        explicacion_final = Text("Cumple ambas ecuaciones", font_size=32, color=BLUE)
        
        grupo_final = VGroup(respuesta_final, par_correcto, explicacion_final).arrange(DOWN, buff=0.4)
        grupo_final.move_to(ORIGIN + UP * 0.5)  # Mover todo hacia arriba
        
        self.play(Write(respuesta_final))
        self.wait(0.5)
        self.play(Write(par_correcto))
        self.wait(0.5)
        self.play(Write(explicacion_final))
        self.wait(2)
        
        # Enfatizar respuesta final
        self.play(
            par_correcto.animate.scale(1.2),
            respuesta_final.animate.set_color(ORANGE),
            explicacion_final.animate.set_color(WHITE)
        )
        self.wait(3)


if __name__ == "__main__":
    # Renderizar con: manim -pqh -r "1080,1920" archivo.py EcuacionSistemaBachillerato
    pass