"""Mictlán levels 3–6 and 8 — rooms, items, and challenges."""

# ── ITEMS ─────────────────────────────────────────────────────────────────────

ITEMS_MICTLAN: dict[str, dict] = {
    # ── Nivel 3 — Iztepetl ────────────────────────────────────────────────────
    "fragmento_iztepetl": {
        "name": "Fragmento de Iztepetl",
        "description": (
            "Astilla de obsidiana del cerro que corta solo. "
            "Fría como hielo aunque el Mictlán no tiene temperatura. "
            "Guarda el eco de las visiones del tercer nivel."
        ),
        "type": "lore",
    },
    "espejo_iztepetl": {
        "name": "Espejo de Iztepetl",
        "description": (
            "Disco pulido de obsidiana negra. Refleja lo que hay "
            "detrás de las ilusiones, no lo que está enfrente. "
            "En el Nivel 8 puede romper velos."
        ),
        "type": "ritual",
        "use_msg": "El espejo absorbe la ilusión y la devuelve transparente.",
    },
    "corazon_obsidiana": {
        "name": "Corazón de Obsidiana",
        "description": (
            "Piedra tallada en forma de corazón. Pulsa suavemente "
            "con un ritmo que no es latido sino memoria. "
            "Guía en la niebla del Nivel 8."
        ),
        "type": "ritual",
        "use_msg": "El corazón pulsa con más fuerza, señalando el camino.",
    },
    "marca_cerro": {
        "name": "Marca del Cerro",
        "description": (
            "Cicatriz en la planta del pie, donde la obsidiana te cortó "
            "al descender descalzo. No duele. Solo recuerda."
        ),
        "type": "lore",
    },
    # ── Nivel 4 — Itzehecayan ─────────────────────────────────────────────────
    "piel_viento": {
        "name": "Piel del Viento",
        "description": (
            "Membrana transparente arrancada de un ser del viento. "
            "Pasiva: reduce el daño de cortadas en un punto. "
            "Diego nunca supo que existía."
        ),
        "type": "lore",
        "defense": 1,
    },
    "pluma_huitzilin": {
        "name": "Pluma de Huitzilin",
        "description": (
            "Pluma del colibrí del sol, traída al Mictlán por algún "
            "guerrero que murió admirando la luz. "
            "Resuena con otras plumas en el Nivel 6."
        ),
        "type": "ritual",
        "use_msg": "La pluma vibra con un zumbido apenas audible.",
    },
    "codice_viento": {
        "name": "Códice del Viento",
        "description": (
            "Rollo de corteza pintado con rutas de las corrientes del Mictlán. "
            "El Caminante lo usó para moverse sin ser cortado. "
            "Ahora es tuyo."
        ),
        "type": "lore",
    },
    "info_yaotl": {
        "name": "Perfil de Yaotl",
        "description": (
            "El Caminante conoció a Yaotl. Traicionado por un conquistador "
            "al que defendía. Cojea del pie izquierdo. Lleva treinta años "
            "atrapado en el Nivel 6. Puede ser aliado — si sabes cómo hablarle."
        ),
        "type": "lore",
    },
    # ── Nivel 5 — Pancuecuetlacayan ──────────────────────────────────────────
    "bandera_propia": {
        "name": "Bandera Propia",
        "description": (
            "Tela hecha de retazos: una ropa de tu madre, un pañuelo del abuelo, "
            "fibra del Mictlán. En ella está tu nombre en náhuatl y en español. "
            "Quien la lleva no olvida quién es."
        ),
        "type": "lore",
    },
    "bandera_heredero": {
        "name": "Bandera del Heredero",
        "description": (
            "La bandera de Diego, que no supo terminar. "
            "Mictlantecuhtli la reconoce: te trata como igual, "
            "no como intruso. Abre opciones de diálogo en el Nivel 9."
        ),
        "type": "key",
    },
    "hilo_bandera": {
        "name": "Hilo de la Bandera",
        "description": (
            "Un hilo que sobró al tejer. Lo llevas en la muñeca. "
            "Pasivo: en el Nivel 8 las ilusiones tardan más en formarse — "
            "el hilo te ancla al yo que eres."
        ),
        "type": "lore",
    },
    # ── Nivel 6 — Temiminaloyan ───────────────────────────────────────────────
    "punta_temiminaloyan": {
        "name": "Punta de Flecha del Temiminaloyan",
        "description": (
            "Flecha de pedernal del campo eterno. No corta carne — "
            "corta intenciones. Quien la lleva sabe reconocer mentiras."
        ),
        "type": "lore",
    },
    "arco_yaotl": {
        "name": "Arco de Yaotl",
        "description": (
            "Arco de madera negra del Mictlán con cuerda de tendón de jaguar. "
            "Las flechas que dispara hieren a seres etéreos. "
            "Yaotl lo entrega solo a quien le devuelve su dignidad."
        ),
        "type": "weapon",
        "damage": 8,
    },
    "bendicion_guerreros": {
        "name": "Bendición de los Guerreros",
        "description": (
            "Los guerreros caídos en el campo de flechas te reconocen "
            "como uno de los suyos. Pasivo: +1 defensa en combate."
        ),
        "type": "lore",
        "defense": 1,
    },
    # ── Nivel 7 — Teyollocualoyan ─────────────────────────────────────────────
    "roseta_itzcuintli": {
        "name": "Roseta de Itzcuintli",
        "description": (
            "Una de las rosetas del pelaje del jaguar guardián — "
            "las que brillan por dentro, como brasas bajo la piel. "
            "Tibia al tacto. Late levemente, como si tuviera pulso propio. "
            "Enciende fuego una sola vez cuando todo lo demás falle."
        ),
        "type": "ritual",
        "use_msg": "La roseta arde con un calor que viene de antes del mundo. El fuego que produce dura exactamente lo que necesitas.",
    },
    # ── Nivel 8 — Apochcaloca ─────────────────────────────────────────────────
    "cristal_niebla": {
        "name": "Cristal de la Niebla",
        "description": (
            "Fragmento de la oscuridad del octavo nivel, cristalizado "
            "por el frío. Dentro hay algo que se mueve. "
            "Recuerdo de lo que fue ilusión."
        ),
        "type": "lore",
    },
}

# ── ROOMS ─────────────────────────────────────────────────────────────────────

ROOMS_MICTLAN: dict[str, dict] = {
    # ── NIVEL 3 — Iztepetl ───────────────────────────────────────────────────
    "nivel3_entrada": {
        "name": "Iztepetl — Pie del Cerro",
        "description": (
            "Un cerro de obsidiana pura se alza ante ti hasta perderse en la oscuridad. "
            "La superficie brilla con un filo propio — cada arista, cada grano, un cuchillo. "
            "El viento que baja desde la cima corta la piel si lo miras de frente. "
            "Diego lo escaló. La sangre en las rocas lleva cincuenta años ahí."
        ),
        "exits": {"sur": "nivel2_cruce"},
        "locked_exits": {
            "norte": {
                "destination": "nivel3_cruce",
                "requires_challenge": "nivel3_iztepetl",
                "msg": "El cerro de obsidiana bloquea el paso. Debes escalar Iztepetl.",
            }
        },
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "cerro":   "Obsidiana en masa. Un cerro hecho de espejos rotos que cortan.",
            "sangre":  "Marcas oscuras en las piedras bajas — sangre de Diego, seca desde hace décadas.",
            "viento":  "Silba con un tono que parece una voz muy lejana intentando decir algo.",
        },
    },

    "nivel3_cruce": {
        "name": "Iztepetl — Descenso",
        "description": (
            "Has cruzado el cerro de obsidiana. El suelo al norte es más suave, "
            "hecho de ceniza que amortigua los pasos. "
            "Tus pies guardarán la memoria de lo que subiste."
        ),
        "exits": {"sur": "nivel3_entrada", "norte": "nivel4_entrada"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "ceniza": "Ceniza fina que registra cada huella. La tuya queda grabada al norte de la del cerro.",
            "cima":   "Desde aquí puedes ver la cima desde donde bajaste — oscura, afilada, silenciosa.",
        },
        "milestone": "nivel3_completado",
    },

    # ── NIVEL 4 — Itzehecayan ─────────────────────────────────────────────────
    "nivel4_entrada": {
        "name": "Itzehecayan — Corredor del Viento",
        "description": (
            "El viento no sopla — corta. Cada ráfaga lleva cuchillas de pedernal invisible. "
            "Las almas que llegaron sin preparación quedan reducidas a jirones. "
            "A lo lejos, algo camina entre las corrientes sin ser cortado: "
            "un Xolo negro del tamaño de un lobo, con ojos de brasas apagadas."
        ),
        "exits": {"sur": "nivel3_cruce"},
        "locked_exits": {
            "norte": {
                "destination": "nivel4_cruce",
                "requires_challenge": "nivel4_viento",
                "msg": "El viento de obsidiana bloquea el paso. Necesitas cruzar Itzehecayan.",
            }
        },
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "viento":   "Silba como un cuchillo contra piedra. Rítmico. Eterno. Implacable.",
            "xolo":     "El perro sin pelo te mira desde la corriente, inmune. Espera.",
            "jirones":  "En el suelo, ropa desgarrada de almas que no supieron cruzar.",
        },
    },

    "nivel4_cruce": {
        "name": "Itzehecayan — Calma",
        "description": (
            "Al otro lado del viento, la calma. El aire no se mueve. "
            "El silencio después de tantas cuchillas resulta casi doloroso. "
            "El Caminante que te ayudó desaparece hacia el norte con un gesto de despedida."
        ),
        "exits": {"sur": "nivel4_entrada", "norte": "nivel5_entrada"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "silencio": "Después del viento que corta, el silencio se siente como regalo.",
            "huellas":  "Las huellas del Caminante se pierden hacia el norte — fue aquí mucho tiempo.",
        },
        "milestone": "nivel4_completado",
    },

    # ── NIVEL 5 — Pancuecuetlacayan ──────────────────────────────────────────
    "nivel5_entrada": {
        "name": "Pancuecuetlacayan — El Campo del Olvido",
        "description": (
            "El aire aquí no tiene olor, ni temperatura, ni peso. "
            "Las almas que vagan por este nivel han olvidado sus nombres. "
            "Están aquí, pero no saben quiénes son. "
            "Tú todavía lo sabes. Por ahora."
        ),
        "exits": {"sur": "nivel4_cruce"},
        "locked_exits": {
            "norte": {
                "destination": "nivel5_cruce",
                "requires_challenge": "nivel5_identidad",
                "msg": "El campo del olvido te envuelve. Debes sostener tu identidad para cruzar.",
            }
        },
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "almas":    "Figuras sin cara que deambulan. Si les preguntas su nombre, no responden.",
            "vacio":    "Un vacío que no es oscuridad sino ausencia. Como el espacio antes de nacer.",
            "xochitl":  "Xochitl está aquí, pero algo en su mirada dice que también está luchando.",
        },
    },

    "nivel5_cruce": {
        "name": "Pancuecuetlacayan — Anclaje",
        "description": (
            "Lo lograste. Tu bandera flamea — en este lugar sin viento, "
            "flamea de todos modos, como si supiera que debe hacerlo. "
            "Al norte, el sexto nivel: el campo de flechas eternas."
        ),
        "exits": {"sur": "nivel5_entrada", "norte": "nivel6_entrada"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "bandera":  "Tu bandera flamea sin viento. Las almas sin nombre la miran con algo parecido al recuerdo.",
            "suelo":    "El suelo tiene color aquí, donde antes era gris. Tu presencia lo tiñe.",
        },
        "milestone": "nivel5_completado",
    },

    # ── NIVEL 6 — Temiminaloyan ───────────────────────────────────────────────
    "nivel6_entrada": {
        "name": "Temiminaloyan — Campo de Flechas",
        "description": (
            "Flechas de pedernal llueven del cielo sin origen. "
            "No hay nubes, no hay arqueros — solo proyectiles eternos "
            "que caen y desaparecen al tocar el suelo, para volver a caer. "
            "En el centro del campo, una figura cojea: un guerrero nahua "
            "con armadura destrozada que esquiva las flechas con práctica de décadas."
        ),
        "exits": {"sur": "nivel5_cruce"},
        "locked_exits": {
            "norte": {
                "destination": "nivel6_cruce",
                "requires_challenge": "nivel6_flechas",
                "msg": "Las flechas eternas bloquean el paso. Debes cruzar Temiminaloyan.",
            }
        },
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "flechas":  "Lluvia constante de pedernal. Sin patrón. Sin pausa. Sin fin.",
            "yaotl":    "Un guerrero con cojera del pie izquierdo esquiva cada flecha. Treinta años de práctica.",
            "escudos":  "Restos de escudos destrozados cubren el suelo como un mosaico de batallas perdidas.",
        },
    },

    "nivel6_cruce": {
        "name": "Temiminaloyan — Al Otro Lado",
        "description": (
            "Las flechas siguen cayendo detrás de ti, pero aquí no llegan. "
            "Una pared invisible detiene el campo. "
            "El guerrero Yaotl, si viene contigo, se detiene en el límite "
            "y mira atrás con treinta años de alivio en los ojos."
        ),
        "exits": {"sur": "nivel6_entrada", "norte": "nivel7_corredor"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "limite":   "El borde del campo. Las flechas paran aquí, como si hubiera un muro.",
            "yaotl":    "Si Yaotl viene contigo, se sienta un momento y respira. Primera vez en décadas.",
        },
        "milestone": "nivel6_completado",
    },

    # ── NIVEL 7 — Teyollocualoyan ─────────────────────────────────────────────
    "nivel7_corredor": {
        "name": "Teyollocualoyan — La Selva de las Sombras",
        "description": (
            "Los árboles del séptimo nivel no son árboles — son columnas de algo parecido "
            "a madera que gotea savia oscura, espesa, que sabe a sangre vieja. "
            "El suelo está cubierto de hongos bioluminiscentes. "
            "Cada paso tuyo los presiona y ellos responden con un destello azul-verde "
            "que dura dos segundos. Dejas un rastro de luz detrás de ti. "
            "No hay manera de ocultarse aquí. "
            "Al fondo del camino, un claro fosforescente y, sobre una piedra negra del "
            "tamaño de una casa pequeña: Itzcuintli, el Devorador de Corazones."
        ),
        "exits": {"sur": "nivel6_cruce"},
        "locked_exits": {
            "norte": {
                "destination": "nivel7_salida",
                "requires_challenge": "nivel7_itzcuintli",
                "msg": "Itzcuintli bloquea el paso al norte. Debes enfrentarlo.",
            }
        },
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "hongos":     "Bioluminiscentes. Cada pisada deja un rastro de luz azul-verde que dura dos segundos.",
            "arboles":    "Columnas de madera negra que gotea savia oscura. No son árboles. Son otra cosa.",
            "itzcuintli": "En el claro al fondo. Su lomo casi alcanza las copas negras. Tiene ocho garras por pata. La oreja izquierda no está.",
            "circulo":    "Un círculo oscuro a veinte metros donde los hongos no brillan. Perfecto. No natural.",
        },
    },

    "nivel7_salida": {
        "name": "Teyollocualoyan — Al Otro Lado del Jaguar",
        "description": (
            "El claro de Itzcuintli queda detrás. "
            "La selva de sombras se cierra y el camino desciende hacia algo húmedo. "
            "Las paredes empiezan a gotear. El goteo se vuelve chorro. "
            "Y al fondo, una cortina blanca, densa, inmóvil a pesar de que todo alrededor se mueve: "
            "el Apochcaloca."
        ),
        "exits": {"sur": "nivel7_corredor", "norte": "nivel8_entrada"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "humedad": "Las paredes gotean agua sin origen visible. El sonido cubre el rastro del jaguar.",
            "niebla":  "La cortina blanca al norte no se mueve aunque todo alrededor lo haga.",
        },
        "milestone": "nivel7_completado",
    },

    # ── NIVEL 8 — Apochcaloca ─────────────────────────────────────────────────
    "nivel8_entrada": {
        "name": "Apochcaloca — La Oscuridad Total",
        "description": (
            "Aquí la oscuridad no es falta de luz — es una presencia. "
            "Se mueve. Respira. Tiene intenciones. "
            "Las ilusiones del Mictlán viven aquí. "
            "Este es el nivel que Diego nunca superó solo."
        ),
        "exits": {"sur": "nivel7_salida"},
        "locked_exits": {
            "norte": {
                "destination": "nivel8_cruce",
                "requires_challenge": "nivel8_ilusion",
                "msg": "La oscuridad te devuelve. Las ilusiones te atrapan. Debes cruzar Apochcaloca.",
            }
        },
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "oscuridad": "No hay paredes visibles. La oscuridad es el espacio mismo.",
            "voces":     "Voces que suenan como personas que conoces. Ninguna es quien dice ser.",
            "xochitl":   "Xochitl está aquí pero apenas la percibes — el oscuro la está tocando.",
        },
    },

    "nivel8_cruce": {
        "name": "Apochcaloca — El Centro",
        "description": (
            "Has cruzado la oscuridad. En el centro del Apochcaloca, "
            "una luz tenue — no del sol, sino de algo interior — "
            "señala el camino al trono de Mictlantecuhtli. "
            "Lo que eres después de este nivel es lo que llevarás al final."
        ),
        "exits": {"sur": "nivel8_entrada", "norte": "nivel9_entrada"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "luz":       "Una luz que no tiene fuente visible. Viene de adentro de las cosas.",
            "trono":     "Al norte se intuye la presencia de Mictlantecuhtli. El trono de cráneos.",
            "xochitl":   "Xochitl está detrás de ti, entera. 'Pensé que te perdería aquí', dice.",
        },
        "milestone": "nivel8_completado",
    },

    # ── NIVEL 9 — Antesala (placeholder) ─────────────────────────────────────
    "nivel9_entrada": {
        "name": "Chicnauhmictlan — La Escalera Final",
        "description": (
            "El noveno nivel. El último.\n\n"
            "Una escalera de piedra desciende frente a ti. Cada peldaño lleva grabado\n"
            "un símbolo — algunos los reconoces: el que vio Citlali en su techo\n"
            "cuando te despidió, el que estaba tallado en el templo donde murió Xochitl.\n\n"
            "Al fondo, una luz fría que no se acerca aunque sigas bajando.\n"
            "Xochitl camina junto a ti. No dice nada todavía.\n\n"
            "Lo que hagas aquí es el legado."
        ),
        "exits": {"sur": "nivel8_cruce"},
        "locked_exits": {
            "norte": {
                "destination": "final_b",
                "requires_challenge": "nivel9_trono",
                "msg": "Mictlantecuhtli aguarda. Debes enfrentarlo.",
            }
        },
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "trono":    "Mictlantecuhtli sentado. Estático. Te estudia desde hace rato.",
            "diego":    "La sombra de Diego. Lleva cincuenta años esperando esto.",
            "xochitl":  "Xochitl a tu lado. Por primera vez, no tiene miedo.",
        },
    },
}

# ── CHALLENGES ────────────────────────────────────────────────────────────────

CHALLENGES_MICTLAN: dict[str, dict] = {
    # ── Nivel 3 — Iztepetl ────────────────────────────────────────────────────
    "nivel3_iztepetl": {
        "name": "Iztepetl — El Cerro que Corta",
        "entry_text": (
            "El cerro de obsidiana se alza ante ti. Cada saliente brilla "
            "con un filo que corta la mirada.\n\n"
            "XOCHITL: \"Iztepetl. Aquí Diego vio a sus padres — proyecciones del Mictlán "
            "diseñadas para detenerlo. Las vio y siguió. No sé si tú podrás.\"\n\n"
            "NARRADOR: La primera visión llega antes de que pongas un pie en la roca."
        ),
        "start_phase": "vision_parental",
        "phases": {
            "vision_parental": {
                "text": (
                    "Tus padres aparecen al pie del cerro. No como los recuerdas — "
                    "jóvenes, sin las marcas que dejaron los años. Te miran con el amor "
                    "específico de los padres que saben que van a perder a un hijo.\n\n"
                    "MADRE: \"No sigas. Ya encontramos a Diego. Está bien aquí.\"\n"
                    "PADRE: \"Vuelve. Nosotros cuidamos a los muertos. Tú cuida a los vivos.\"\n\n"
                    "¿Qué haces?"
                ),
                "options": [
                    {
                        "label": "[ESP] Ignorarlos — son ilusiones del Mictlán",
                        "response_text": (
                            "JUGADOR: \"Sé lo que son. El Mictlán me muestra lo que más quiero "
                            "para que me detenga. No esta vez.\"\n\n"
                            "Las figuras se disuelven sin drama. La obsidiana queda al descubierto.\n\n"
                            "XOCHITL: \"Correcto. Pero eso dolió, ¿verdad?\"\n"
                            "JUGADOR: \"Más de lo que esperaba.\"\n"
                            "[CLARIDAD TÁCTICA: ilusiones identificadas]"
                        ),
                        "sets_flag": "v2_ilusiones_ignoradas",
                        "esp_delta": 1,
                        "next_phase": "vision_diego",
                    },
                    {
                        "label": "[NAH] Hablarles — aunque sean proyecciones, merecen respuesta",
                        "response_text": (
                            "JUGADOR: \"Los amo. Pero Diego no está bien aquí — está atrapado. "
                            "Y Xochitl lleva treinta años esperando. Si pudieran verme de verdad, "
                            "me pedirían que siguiera.\"\n\n"
                            "Las figuras se detienen. La madre sonríe con algo que no es ilusión.\n"
                            "MADRE (voz que cambia): \"Sí. Eso te pediríamos.\"\n\n"
                            "Se disuelven. Pero dejan algo — un calor en el pecho que no había.\n"
                            "XOCHITL: \"Eso... no había pasado antes. ¿Qué les dijiste?\"\n"
                            "[EMPATÍA ACTIVA: el Mictlán tomó nota]"
                        ),
                        "sets_flag": "v2_ilusiones_habladas",
                        "nah_delta": 2,
                        "next_phase": "vision_diego",
                    },
                    {
                        "label": "[DUAL] Despedirte — darles lo que Diego no pudo darles",
                        "response_text": (
                            "JUGADOR: \"Diego no se despidió, ¿verdad? Subió corriendo y nunca "
                            "miró atrás. Yo sí me despido.\"\n\n"
                            "Les dices lo que habría dicho Diego si hubiera sabido "
                            "que no volvería. Las palabras no son tuyas — son las de él, "
                            "pasadas por tu boca cincuenta años tarde.\n\n"
                            "Las figuras lloran. Y entonces se abrazan entre sí y desaparecen.\n"
                            "XOCHITL (voz rota): \"Eso fue para él. No para ti.\"\n"
                            "JUGADOR: \"Por eso era lo correcto.\"\n"
                            "[ACTO DE DIEGO: cierra deuda emocional del primer nivel]"
                        ),
                        "sets_flags": ["v2_ilusiones_diego", "v2_otro_camino"],
                        "esp_delta": 1, "nah_delta": 1,
                        "next_phase": "vision_diego",
                    },
                ],
            },
            "vision_diego": {
                "text": (
                    "La segunda visión: Diego escalando este mismo cerro. "
                    "No una proyección — un recuerdo grabado en la roca, "
                    "como película en piedra. Diego sube. Le sangran las manos. "
                    "No mira hacia abajo. No mira hacia arriba. Solo sube.\n\n"
                    "Y en cierto punto — a mitad del cerro — se detiene.\n"
                    "Saca Tlachicotl. Graba algo en la obsidiana con la punta.\n\n"
                    "¿Qué ves tallado?"
                ),
                "options": [
                    {
                        "label": "[1] Acercarte a leer la inscripción",
                        "response_text": (
                            "\"PARA EL QUE VENGA DESPUÉS: "
                            "LAS VISIONES SON REALES PERO NO SON VERDAD. "
                            "EL CERRO DUELE PERO NO MATA. "
                            "SIGUE. — D.\"\n\n"
                            "XOCHITL: \"Dejó instrucciones. Sabía que alguien vendría.\"\n"
                            "JUGADOR: \"O esperaba que alguien viniera.\"\n"
                            "[MENSAJE DE DIEGO: guía para el ascenso]"
                        ),
                        "sets_flag": "nivel3_mensaje_diego",
                        "next_phase": "ascenso",
                    },
                    {
                        "label": "[2] No acercarte — subir directamente",
                        "response_text": (
                            "No necesitas la guía de Diego. Tienes la tuya.\n\n"
                            "XOCHITL: \"¿No quieres leer lo que dejó?\"\n"
                            "JUGADOR: \"Ya sé lo que dice. Sigue. Eso dice siempre.\"\n"
                            "XOCHITL (sonríe): \"Sí. Eso dice siempre.\"\n"
                            "[AUTONOMÍA: tu camino, no el de Diego]"
                        ),
                        "sets_flag": "nivel3_sin_guia",
                        "nah_delta": 1,
                        "next_phase": "ascenso",
                    },
                ],
            },
            "ascenso": {
                "text": (
                    "Empiezas a escalar. La obsidiana corta — no profundo, "
                    "pero constante. Las manos sangran. El viento arrecia.\n\n"
                    "A mitad del cerro, una visión del trono de Mictlantecuhtli "
                    "se proyecta en el cielo: el dios te observa, inmóvil, "
                    "con algo parecido a la curiosidad.\n\n"
                    "MICTLANTECUHTLI (voz que viene de todas partes): "
                    "\"¿Con qué disposición llegas al noveno nivel?\"\n\n"
                    "¿Qué respondes?"
                ),
                "options": [
                    {
                        "label": "[ESP] \"A negociar. Vengo a hacer un trato.\"",
                        "response_text": (
                            "MICTLANTECUHTLI: \"Un trato. Diego también quiso hacer un trato.\"\n"
                            "Larga pausa.\n"
                            "\"Llega primero. Hablaremos.\"\n\n"
                            "La visión desaparece. El cerro sigue. Subes.\n"
                            "[DISPOSICIÓN: negociación — Mictlantecuhtli espera un acuerdo]"
                        ),
                        "sets_flag": "disposicion_trono_negociar",
                        "esp_delta": 1,
                        "next_phase": "cima",
                    },
                    {
                        "label": "[NAH] \"A pedir. No tengo poder aquí — solo razones.\"",
                        "response_text": (
                            "MICTLANTECUHTLI: \"Un vivo que admite su posición.\"\n"
                            "Algo en la voz cambia — menos fría.\n"
                            "\"Interesante. Diego llegó convencido de que tenía poder.\"\n"
                            "\"Llega primero. Escucharé.\"\n\n"
                            "La visión desaparece. Subes.\n"
                            "[DISPOSICIÓN: súplica con razones — Mictlantecuhtli considera]"
                        ),
                        "sets_flag": "disposicion_trono_pedir",
                        "nah_delta": 2,
                        "next_phase": "cima",
                    },
                    {
                        "label": "[DUAL] \"A cumplir lo que Diego no pudo. Vengo a terminar.\"",
                        "response_text": (
                            "MICTLANTECUHTLI: \"...\"\n"
                            "El silencio dura tanto que crees que la visión terminó.\n"
                            "\"Diego. Su legado todavía está aquí. Pesado.\"\n"
                            "\"Llega. Veremos si puedes cargarlo.\"\n\n"
                            "La visión se rompe como obsidiana. Subes.\n"
                            "[DISPOSICIÓN: legado de Diego — Mictlantecuhtli toma nota]"
                        ),
                        "sets_flags": ["disposicion_trono_legado", "disposicion_trono"],
                        "esp_delta": 1, "nah_delta": 1,
                        "next_phase": "cima",
                    },
                ],
            },
            "cima": {
                "text": (
                    "La cima del Iztepetl. El descenso al norte es más corto "
                    "pero igual de afilado.\n\n"
                    "¿Cómo bajas?"
                ),
                "options": [
                    {
                        "label": "[FUERZA] Bajar rápido con el Escudo como trinco",
                        "response_text": (
                            "Pones el Escudo Ceiba bajo los pies y deslizas. "
                            "La obsidiana chilla contra la madera sagrada. "
                            "Llegas abajo en segundos — con el escudo rayado "
                            "y los brazos entumecidos.\n\n"
                            "XOCHITL: \"Eso fue... eficiente. Y completamente ridículo.\"\n"
                            "JUGADOR: \"Funciona. Eso cuenta.\"\n"
                            "[FRAGMENTO TEPECTLI: recuerdo del cerro]"
                        ),
                        "sets_flag": "nivel3_bajada_fuerza",
                        "esp_delta": 1,
                        "next_phase": None,
                        "grants_items": ["fragmento_iztepetl"],
                    },
                    {
                        "label": "[NAH] Hablarle al cerro mientras bajas — cantar el descenso",
                        "response_text": (
                            "Bajas despacio, cantando. No un himno — solo palabras "
                            "que dicen 'bajo con cuidado, gracias por dejarme subir'.\n\n"
                            "La obsidiana no es más suave. Pero el viento cesa.\n"
                            "Bajas sin que el viento corte. El cerro escuchó.\n\n"
                            "XOCHITL: \"Diego nunca cantó aquí tampoco. Tú lo haces en todos lados.\"\n"
                            "JUGADOR: \"Me lo enseñaste tú. Con las montañas.\"\n"
                            "[CANTO ACTIVO: el cerro reconoce la voz]"
                        ),
                        "sets_flags": ["nivel3_bajada_canto", "3b_canto_completo", "canto_caminante", "tiene_espejo_iztepetl"],
                        "nah_delta": 2,
                        "next_phase": None,
                        "grants_items": ["fragmento_iztepetl", "espejo_iztepetl"],
                    },
                    {
                        "label": "[RITUAL] Bajar descalzo — ofrecer las plantas de los pies",
                        "response_text": (
                            "Te quitas las sandalias. La obsidiana corta la planta de los pies "
                            "con cada paso — limpio, controlado.\n\n"
                            "No sangras más de lo que el cerro necesita.\n"
                            "Llegas abajo. Las plantas de los pies tienen marcas finas "
                            "como tatuajes de obsidiana.\n\n"
                            "XOCHITL (en voz muy baja): \"¿Por qué?\"\n"
                            "JUGADOR: \"Para que sepa que pasé. Para que recuerde.\"\n"
                            "[MARCA DEL CERRO: el Iztepetl guarda tu huella]"
                        ),
                        "sets_flags": ["nivel3_bajada_descalzo", "2c_corazon_cerro"],
                        "nah_delta": 3,
                        "next_phase": None,
                        "grants_items": ["fragmento_iztepetl", "corazon_obsidiana", "marca_cerro"],
                    },
                ],
            },
        },
    },

    # ── Nivel 4 — Itzehecayan ─────────────────────────────────────────────────
    "nivel4_viento": {
        "name": "Itzehecayan — El Viento que Corta",
        "entry_text": (
            "El viento invisible lleva pedernal en cada ráfaga.\n"
            "Ya puedes sentir los primeros cortes en los antebrazos.\n\n"
            "XOCHITL: \"Itzehecayan. El viento de obsidiana. Las almas sin guía "
            "quedan en jirones en minutos. Diego usó el Escudo — "
            "pero el Escudo solo aguanta uno o dos cruces antes de romperse aquí.\"\n\n"
            "El Xolo negro se acerca. Te olfatea. Espera."
        ),
        "start_phase": "preparacion",
        "phases": {
            "preparacion": {
                "text": (
                    "El Xolo — el perro sagrado — está frente a ti.\n"
                    "Tiene ojos de brasa apagada y el pelaje completamente negro.\n"
                    "No es amenaza. Es guía. Pero tiene condiciones.\n\n"
                    "¿Cómo te acercas?"
                ),
                "options": [
                    {
                        "label": "[NAH] Sentarte y esperar — dejar que el Xolo decida",
                        "response_text": (
                            "Te sientas en el suelo cortante. El Xolo te estudia "
                            "durante un tiempo que podría ser segundos o horas.\n\n"
                            "Entonces viene. Se sienta frente a ti. Pone la cabeza en tu regazo.\n\n"
                            "XOCHITL (susurra): \"Nunca lo había visto hacer eso.\"\n"
                            "NARRADOR: El Xolo no te pedirá nada. Solo irá delante.\n\n"
                            "[CONFIANZA GANADA: el Xolo te guía libremente]"
                        ),
                        "sets_flag": "xolo_confianza",
                        "nah_delta": 1,
                        "next_phase": "xolo_guia",
                    },
                    {
                        "label": "[ESP] Ofrecerle algo de tu inventario",
                        "response_text": (
                            "Le ofreces lo que tienes — fragmentos, agua, lo que sea.\n"
                            "El Xolo olfatea. Ignora todo excepto el agua del Chiconahuapan, "
                            "si la llevas. Si no, acepta un fragmento de todos modos.\n\n"
                            "JUGADOR: \"Un trato. Tú me guías, yo te doy esto.\"\n"
                            "XOCHITL: \"No creo que los perros del Mictlán funcionen así.\"\n"
                            "Pero el Xolo acepta el fragmento y da media vuelta hacia el viento.\n\n"
                            "[TRATO CON XOLO: guía a cambio de ofrenda]"
                        ),
                        "sets_flag": "xolo_trato",
                        "esp_delta": 1,
                        "next_phase": "xolo_guia",
                    },
                    {
                        "label": "[DUAL] Ignorar al Xolo y buscar el Caminante directamente",
                        "response_text": (
                            "El alma que vaga entre las corrientes — la has visto moverse. "
                            "Un humano, o algo que fue humano, que conoce el viento.\n\n"
                            "El Xolo te observa alejarte. No te sigue. Pero tampoco se va.\n\n"
                            "XOCHITL: \"¿Y si el Caminante no ayuda?\"\n"
                            "JUGADOR: \"Entonces vuelvo al perro.\"\n"
                            "[AUTONOMÍA: buscar ayuda humana primero]"
                        ),
                        "sets_flag": "xolo_ignorado",
                        "next_phase": "caminante_directo",
                    },
                    {
                        "label": "[ESCUCHAR] Agacharte — hay un chapoteo bajo tus pies",
                        "response_text": (
                            "No hay agua en Itzehecayan. El viento de obsidiana seca todo.\n"
                            "Y sin embargo: chapoteo. Bajo la tierra. Movimiento acuático.\n\n"
                            "XOCHITL (sorprendida): \"¿Oyes eso?\"\n\n"
                            "Pones la palma en el suelo. Frío. Húmedo por debajo.\n"
                            "Hay algo bajo el páramo. Y ese algo se acerca."
                        ),
                        "sets_flag": "escuchaste_chapoteo",
                        "nah_delta": 1,
                        "next_phase": "ahuizotl_encuentro",
                    },
                ],
            },
            "ahuizotl_encuentro": {
                "text": (
                    "Una grieta en el suelo, casi invisible bajo las partículas de viento.\n"
                    "Por ella asoma primero una cola — larga, prensil, terminada en\n"
                    "algo que parece una mano de niño.\n"
                    "Luego un cuerpo. Nutria, en tamaño. Ojos de obsidiana mojada.\n\n"
                    "AHUÍZOTL (voz telepática, sin mover la boca):\n"
                    "\"Heredero. Te siento desde el río de arriba.\n"
                    "Bajo aquí hay humedad. Hay ríos subterráneos donde el viento no llega.\n"
                    "Yo conozco las corrientes. Puedo guiarte.\"\n\n"
                    "XOCHITL: \"Es el Ahuízotl. Los ríos del mundo de arriba\n"
                    "tienen raíces que llegan hasta el Mictlán. Por eso puede estar aquí.\"\n\n"
                    "¿Qué respondes?"
                ),
                "options": [
                    {
                        "label": "[1] \"Guíame.\"",
                        "response_text": (
                            "AHUÍZOTL: \"Entra. La grieta es estrecha, pero cabes.\"\n\n"
                            "Te cuelas dentro. Un túnel natural baja suavemente.\n"
                            "En pocos minutos el zumbido del viento se apaga.\n"
                            "Puedes oír, nítida, el agua corriendo."
                        ),
                        "sets_flag": "ahuizotl_guia_aceptado",
                        "next_phase": "ahuizotl_subterraneo",
                    },
                    {
                        "label": "[2] \"¿Por qué me ayudas?\"",
                        "response_text": (
                            "AHUÍZOTL: \"La deuda del río sigue sin saldarse.\n"
                            "Y además... tú no matas. Los que no matan, me alían.\"\n\n"
                            "Una pausa.\n\n"
                            "AHUÍZOTL: \"Entra.\"\n\n"
                            "Te cuelas dentro. Un túnel natural desciende.\n"
                            "El zumbido del viento se apaga con cada paso."
                        ),
                        "sets_flag": "ahuizotl_razon_revelada",
                        "nah_delta": 1,
                        "next_phase": "ahuizotl_subterraneo",
                    },
                    {
                        "label": "[3] \"¿Qué quieres a cambio?\"",
                        "response_text": (
                            "AHUÍZOTL: \"Un favor. Cuando llegue. Lo sabrás.\"\n\n"
                            "XOCHITL (a ti, en voz baja): \"Trato abierto.\n"
                            "No te dice el precio todavía.\"\n\n"
                            "JUGADOR: \"Acepto.\"\n\n"
                            "AHUÍZOTL: \"Bien. Entra.\"\n\n"
                            "Te cuelas en la grieta. El aire cambia de inmediato:\n"
                            "seco a húmedo. Cortante a vivo."
                        ),
                        "sets_flags": ["ahuizotl_trato_abierto"],
                        "esp_delta": 1,
                        "next_phase": "ahuizotl_subterraneo",
                    },
                ],
            },
            "ahuizotl_subterraneo": {
                "text": (
                    "El Ahuízotl camina delante. Su cola-mano toca el agua\n"
                    "que corre junto a ustedes — puede leer el corriente,\n"
                    "saber exactamente dónde están, qué hay arriba, cuánto falta.\n\n"
                    "AHUÍZOTL (mientras caminan): \"El de dos sangres también vino\n"
                    "por esta ruta. Yo lo guié. No recordaba su nombre.\n"
                    "Ahora recuerdo el tuyo, aunque no me lo hayas dicho.\"\n\n"
                    "XOCHITL (muy quieta): \"¿Cómo se llama?\"\n"
                    "AHUÍZOTL: \"No se lo digo a ella. Solo a ti.\"\n\n"
                    "Más adelante, una luz. La salida. Sales al borde del Nivel 5.\n"
                    "Saltaste Itzehecayan casi entero — sin cortes nuevos.\n\n"
                    "AHUÍZOTL (asomando la cabeza desde la grieta, antes de retirarse):\n"
                    "\"Deuda casi saldada. Un favor más, heredero. Solo uno.\n"
                    "Lo pediré en los niveles que vienen. Cuando lo escuches, lo reconocerás.\"\n\n"
                    "¿Qué respondes?"
                ),
                "options": [
                    {
                        "label": "[1] \"Cuenta conmigo.\"",
                        "response_text": (
                            "AHUÍZOTL: \"Ya cuento.\"\n\n"
                            "La cola-mano desaparece bajo la grieta.\n"
                            "El sonido del agua se aleja.\n\n"
                            "XOCHITL: \"No lo había visto antes — el Ahuízotl que guía.\n"
                            "Normalmente los Ahuizotl arrastran. Este cargó.\"\n\n"
                            "[FAVOR DEL AHUÍZOTL — lo cobrará en el Nivel 7 con Itzcuintli]"
                        ),
                        "sets_flags": ["favor_ahuizotl", "nivel4_cruce_ahuizotl"],
                        "esp_delta": 1, "nah_delta": 1,
                        "next_phase": None,
                        "grants_items": ["piel_viento"],
                    },
                    {
                        "label": "[2] [Asentir en silencio]",
                        "response_text": (
                            "El Ahuízotl acepta el silencio sin quejarse.\n"
                            "La cola-mano desaparece.\n\n"
                            "XOCHITL: \"Los tratos en silencio también son tratos.\n"
                            "Más vinculantes, a veces.\"\n\n"
                            "[FAVOR DEL AHUÍZOTL — prometido en silencio]"
                        ),
                        "sets_flags": ["favor_ahuizotl", "nivel4_cruce_ahuizotl"],
                        "nah_delta": 2,
                        "next_phase": None,
                        "grants_items": ["piel_viento"],
                    },
                ],
            },
            "xolo_guia": {
                "text": (
                    "El Xolo va delante. Se mueve entre las corrientes "
                    "con una gracia que no es natural — conoce cada pausa, "
                    "cada espacio seguro entre ráfaga y ráfaga.\n\n"
                    "A mitad del cruce, el Xolo se detiene frente a un alma "
                    "que deambula sin dirección: el Caminante. "
                    "El Caminante te mira con ojos que recuerdan haber visto.\n\n"
                    "CAMINANTE: \"¿Vivo? No había vivos en mucho tiempo.\"\n\n"
                    "¿Qué le dices?"
                ),
                "options": [
                    {
                        "label": "[1] \"¿Cuánto tiempo llevas aquí?\"",
                        "response_text": (
                            "CAMINANTE: \"No sé. El viento no tiene día ni noche. "
                            "Mucho tiempo. Aprendí a moverme entre las ráfagas.\"\n\n"
                            "JUGADOR: \"¿Conoces a alguien llamado Yaotl? En el nivel siguiente.\"\n"
                            "CAMINANTE: \"Yaotl. Sí. Un guerrero. Traicionado. Cojea. "
                            "Lleva décadas en el campo de flechas. "
                            "Si vas allá... no lo confrontes de frente. Habla de la traición.\"\n\n"
                            "El Caminante te da un rollo de corteza — rutas pintadas.\n"
                            "[INFORMACIÓN DE YAOTL: clave para el Nivel 6]"
                        ),
                        "sets_flag": "caminante_trato",
                        "next_phase": "salida_viento",
                        "grants_items": ["info_yaotl", "codice_viento"],
                    },
                    {
                        "label": "[2] \"¿Puedes acompañarme al otro lado?\"",
                        "response_text": (
                            "CAMINANTE: \"Yo no puedo irme. Llevo aquí...\"\n"
                            "Pausa.\n"
                            "\"Mucho tiempo. El viento me ancla.\"\n\n"
                            "JUGADOR: \"¿Quieres que te libere?\"\n"
                            "CAMINANTE: \"No sé si se puede.\"\n"
                            "XOCHITL: \"Puede. Si alguien que aún vive reconoce que está atrapado.\"\n\n"
                            "JUGADOR: \"Estás atrapado. Lo veo. Y lo reconozco.\"\n\n"
                            "El Caminante se disuelve. No con dolor — con alivio. "
                            "Deja caer el rollo de corteza al suelo.\n"
                            "[CAMINANTE LIBERADO: reconocido y soltado]"
                        ),
                        "sets_flags": ["caminante_liberado", "caminante_trato"],
                        "nah_delta": 2,
                        "next_phase": "salida_viento",
                        "grants_items": ["info_yaotl", "codice_viento"],
                    },
                ],
            },
            "caminante_directo": {
                "text": (
                    "Encuentras al Caminante entre las corrientes. "
                    "Se mueve despacio, probando cada paso. "
                    "Tiene los ojos de alguien que lleva décadas aprendiendo un idioma "
                    "que nadie más habla.\n\n"
                    "CAMINANTE: \"¿Vivo. En el viento de obsidiana. ¿Cómo?\"\n\n"
                    "¿Qué respondes?"
                ),
                "options": [
                    {
                        "label": "[1] \"Con cuidado. ¿Me enseñas el camino?\"",
                        "response_text": (
                            "CAMINANTE: \"Aprendo solo. Nadie me enseñó.\"\n"
                            "JUGADOR: \"Entonces enséñame lo que tardaste décadas en aprender. "
                            "Te escucho.\"\n\n"
                            "El Caminante te muestra el camino — pausa aquí, "
                            "corre allá, gira cuando el viento silba grave. "
                            "Te da el códice también.\n"
                            "[CONOCIMIENTO DEL VIENTO: mapa de corrientes]"
                        ),
                        "sets_flags": ["caminante_trato", "conocimiento_mapa"],
                        "nah_delta": 1,
                        "next_phase": "salida_viento",
                        "grants_items": ["codice_viento", "info_yaotl"],
                    },
                    {
                        "label": "[2] \"¿Sabes algo de Yaotl? El guerrero del nivel siguiente.\"",
                        "response_text": (
                            "El Caminante se detiene.\n"
                            "CAMINANTE: \"Yaotl. Sí. Lo vi pasar hace décadas. "
                            "Pé izquierda rota. Traicionado por alguien a quien protegía. "
                            "No lo confrontes — habla de la traición primero. "
                            "Eso es lo que lleva dentro.\"\n\n"
                            "JUGADOR: \"¿Y el camino?\"\n"
                            "CAMINANTE: \"Sígueme.\"\n"
                            "[PERFIL DE YAOTL + guía por el viento]"
                        ),
                        "sets_flag": "caminante_trato",
                        "next_phase": "salida_viento",
                        "grants_items": ["info_yaotl", "codice_viento"],
                    },
                ],
            },
            "salida_viento": {
                "text": (
                    "Sigues el camino — por el códice o por el Xolo. "
                    "El viento sigue cortando, pero sabes cuándo agacharte.\n\n"
                    "A metros de la salida, una ráfaga más fuerte. "
                    "¿Cómo la enfrentas?"
                ),
                "options": [
                    {
                        "label": "[ESP] Usar el Escudo Ceiba para el último tramo",
                        "response_text": (
                            "El Escudo aguanta. La ráfaga lo abolla pero no lo rompe.\n"
                            "Sales al otro lado con el brazo entumecido y el escudo rayado.\n\n"
                            "XOCHITL: \"El Escudo de Diego aguanta más de lo que parece.\"\n"
                            "[CRUCE COMPLETADO — viento superado con fuerza]"
                        ),
                        "sets_flag": "nivel4_cruce_escudo",
                        "esp_delta": 1,
                        "next_phase": None,
                        "grants_items": ["piel_viento"],
                    },
                    {
                        "label": "[NAH] Agacharte y esperar — el viento cesa en ráfagas",
                        "response_text": (
                            "Te agachas. Esperas. El códice dice que cada ráfaga fuerte "
                            "va seguida de tres segundos de calma.\n\n"
                            "Tres. Dos. Uno. Corres.\n"
                            "Sales limpio. Sin cortes nuevos.\n\n"
                            "XOCHITL: \"Perfecto.\"\n"
                            "JUGADOR: \"El Caminante tardó décadas en aprender eso. "
                            "Yo lo leí en un códice. Eso es injusto.\"\n"
                            "XOCHITL: \"Así funciona el conocimiento.\"\n"
                            "[CRUCE COMPLETADO — viento superado con sabiduría]"
                        ),
                        "sets_flag": "nivel4_cruce_espera",
                        "nah_delta": 2,
                        "next_phase": None,
                        "grants_items": ["piel_viento", "pluma_huitzilin"],
                    },
                ],
            },
        },
    },

    # ── Nivel 5 — Pancuecuetlacayan ──────────────────────────────────────────
    "nivel5_identidad": {
        "name": "Pancuecuetlacayan — El Campo del Olvido",
        "entry_text": (
            "El campo te envuelve. El aire no tiene peso. "
            "Las almas que pasan frente a ti no tienen cara.\n\n"
            "XOCHITL: \"Pancuecuetlacayan. Aquí el Mictlán borra los nombres. "
            "Diego perdió el suyo por tres días. Cuando lo recuperó, "
            "era Diego-Águila-de-Dos-Sangres — él mismo lo eligió.\"\n\n"
            "NARRADOR: La primera grieta en tu memoria aparece.\n"
            "¿Cuál es tu nombre? La pregunta se siente extrañamente difícil."
        ),
        "start_phase": "perdida_identidad",
        "phases": {
            "perdida_identidad": {
                "text": (
                    "El campo te pregunta — no con palabras, con vacío.\n"
                    "Sientes que si no lo dices en voz alta, lo perderás.\n\n"
                    "¿Cómo te anclas?"
                ),
                "options": [
                    {
                        "label": "[ESP] Decir tu nombre completo en voz alta",
                        "response_text": (
                            "Lo dices. Tu nombre completo. El que te pusieron. "
                            "El que aparece en papeles. El que dice quién eres "
                            "según el mundo que dejaste atrás.\n\n"
                            "El campo retrocede un paso.\n\n"
                            "XOCHITL: \"Funciona. Por ahora.\"\n"
                            "[ANCLAJE DE NOMBRE: identidad sostenida por declaración]"
                        ),
                        "sets_flag": "ancla_nombre",
                        "esp_delta": 1,
                        "next_phase": "busqueda_bandera",
                    },
                    {
                        "label": "[NAH] Recordar un momento específico que te define",
                        "response_text": (
                            "No el nombre — el momento. Un instante concreto "
                            "en que supiste quién eras de verdad. "
                            "Lo traes al frente de la mente y te aferras a él.\n\n"
                            "El campo lo intenta. No puede quitarte el momento.\n"
                            "Los momentos son más difíciles de borrar que los nombres.\n\n"
                            "XOCHITL: \"Eso es más sabio de lo que parece.\"\n"
                            "[ANCLAJE DE MEMORIA: identidad sostenida por experiencia]"
                        ),
                        "sets_flag": "ancla_momento",
                        "nah_delta": 2,
                        "next_phase": "busqueda_bandera",
                    },
                    {
                        "label": "[DUAL] Dejarlo intentar — y ver qué queda cuando el campo termina",
                        "response_text": (
                            "No luchas. Dejas que el campo tome lo que puede.\n\n"
                            "Pierde el nombre. Pierde la cara de tus padres. "
                            "Pierde el nombre de la calle donde creciste.\n\n"
                            "Pero hay algo que el campo no puede tomar: "
                            "la razón por la que estás aquí. "
                            "Xochitl. Diego. El legado.\n\n"
                            "JUGADOR (sin voz): Todavía sé por qué vine.\n"
                            "XOCHITL (asustada): \"Eso... fue peligroso.\"\n"
                            "JUGADOR: \"Pero funcionó. Soy lo que hago, no lo que me llamo.\"\n"
                            "[IDENTIDAD DESNUDA: solo el propósito queda — más fuerte por eso]"
                        ),
                        "sets_flags": ["ancla_proposito", "ancla_rota"],
                        "nah_delta": 3,
                        "next_phase": "busqueda_bandera",
                    },
                ],
            },
            "busqueda_bandera": {
                "text": (
                    "Diego plantó una bandera aquí. Aún está. "
                    "Pero está incompleta — la tela tiene su sangre y la mitad de su nombre. "
                    "La otra mitad nunca la terminó.\n\n"
                    "XOCHITL: \"Las almas sin bandera se pierden aquí para siempre. "
                    "Diego tuvo la suya. Tú necesitas la tuya.\"\n\n"
                    "¿Qué haces con la bandera de Diego?"
                ),
                "options": [
                    {
                        "label": "[ESP] Terminar la bandera de Diego — completar su nombre",
                        "response_text": (
                            "Tomas tela del Escudo Ceiba y añades lo que Diego no terminó. "
                            "Su nombre completo, en náhuatl y español. "
                            "Su bandera queda entera.\n\n"
                            "Y la tuya... viene después, más pequeña, "
                            "cosida con hilo del borde del escudo. Juntas.\n\n"
                            "XOCHITL: \"Dos banderas. Dos nombres. Dos caminos que terminan aquí.\"\n"
                            "[BANDERA DE DIEGO COMPLETADA: legado sellado]"
                        ),
                        "sets_flags": ["bandera_diego_completa", "bandera_creada"],
                        "esp_delta": 1,
                        "next_phase": "bandera_xochitl",
                        "grants_items": ["bandera_heredero"],
                    },
                    {
                        "label": "[NAH] Crear tu propia bandera — dejando la de Diego intacta",
                        "response_text": (
                            "No tocas la bandera de Diego. Es suya.\n"
                            "La tuya la haces de lo que traes: retazos de ropa, "
                            "hilo del bolsillo, un pedazo de mapa.\n\n"
                            "No es bonita. Pero es tuya.\n\n"
                            "JUGADOR: \"La bandera de Diego quedó como llegó. "
                            "La mía viene de lo que soy ahora.\"\n"
                            "XOCHITL: \"Eso también es heredar. Diferente de copiar.\"\n"
                            "[IDENTIDAD PROPIA: tu bandera, no la de Diego]"
                        ),
                        "sets_flag": "bandera_creada",
                        "nah_delta": 2,
                        "next_phase": "bandera_xochitl",
                        "grants_items": ["bandera_propia", "hilo_bandera"],
                    },
                    {
                        "label": "[DUAL] Combinar las dos banderas en una",
                        "response_text": (
                            "Tomas la tela de Diego y la entrelazas con tela nueva.\n"
                            "Los dos nombres juntos. Las dos sangres. "
                            "Las dos historias en un mismo trapo que flamea sin viento.\n\n"
                            "XOCHITL: \"¿Eso es una bandera o un manifiesto?\"\n"
                            "JUGADOR: \"¿Hay diferencia?\"\n\n"
                            "Las almas sin cara se detienen a mirarla. "
                            "Algunas dan un paso hacia ella, como si recordaran "
                            "que también tuvieron nombre una vez.\n"
                            "[BANDERA DUAL: Diego + tú — el Mictlán la nota]"
                        ),
                        "sets_flags": ["bandera_diego_completa", "bandera_creada", "bandera_dual"],
                        "esp_delta": 1, "nah_delta": 2,
                        "next_phase": "bandera_xochitl",
                        "grants_items": ["bandera_heredero", "hilo_bandera"],
                    },
                ],
            },
            "bandera_xochitl": {
                "text": (
                    "Xochitl mira la bandera. O las banderas. "
                    "Algo en su cara cambia — lleva treinta años en el Mictlán "
                    "y nunca había visto una bandera nueva.\n\n"
                    "XOCHITL: \"Yo... no tengo bandera. Las almas que llegan sin haber "
                    "elegido nada... no tenemos. Solo estamos.\"\n\n"
                    "¿Qué haces?"
                ),
                "options": [
                    {
                        "label": "[1] Darle un pedazo de tu bandera",
                        "response_text": (
                            "Rasgas un trozo. Se lo das.\n\n"
                            "XOCHITL: \"¿Pero... esto es tuyo.\"\n"
                            "JUGADOR: \"Y ahora es tuyo también. Eso es lo que significa.\"\n\n"
                            "Xochitl sostiene el trozo de tela con las dos manos. "
                            "Como si pesara.\n\n"
                            "XOCHITL (voz muy baja): \"Nadie me había dado algo mío desde... \"\n"
                            "No termina la frase. No necesita.\n"
                            "[XOCHITL ALIADA: lazo real, no solo deuda]"
                        ),
                        "sets_flags": ["xochitl_amiga", "xochitl_bandera"],
                        "nah_delta": 2,
                        "next_phase": None,
                    },
                    {
                        "label": "[2] Ayudarla a hacer su propia bandera",
                        "response_text": (
                            "No le das la tuya. Juntos buscan material — "
                            "tela del viento, fibra del suelo del Mictlán, "
                            "el color que tiene la niebla aquí.\n\n"
                            "JUGADOR: \"¿Qué quieres que diga tu bandera?\"\n"
                            "Larga pausa.\n"
                            "XOCHITL: \"Xochitl. Solo eso. Solo mi nombre.\"\n\n"
                            "La bandera de Xochitl es pequeña y simple. "
                            "Flamea junto a la tuya.\n\n"
                            "XOCHITL: \"Gracias. Esto es... esto es mío.\"\n"
                            "[XOCHITL AUTÓNOMA: su propia identidad, no dependiente]"
                        ),
                        "sets_flags": ["xochitl_amiga", "xochitl_autonoma"],
                        "esp_delta": 1, "nah_delta": 2,
                        "next_phase": None,
                    },
                    {
                        "label": "[3] Decirle que no necesita una bandera para ser real",
                        "response_text": (
                            "JUGADOR: \"Llevas treinta años siendo Xochitl sin bandera. "
                            "La bandera no te hace más real — tú ya lo eres.\"\n\n"
                            "XOCHITL: \"Pero el campo borra a las almas sin—\"\n"
                            "JUGADOR: \"¿Te ha borrado a ti?\"\n"
                            "Silencio.\n"
                            "XOCHITL: \"No.\"\n"
                            "JUGADOR: \"Entonces ya sabes lo que te ancla. Y no es tela.\"\n\n"
                            "Xochitl se queda callada un momento largo. Luego asiente.\n"
                            "[XOCHITL FORTALECIDA: anclada por sí misma, no por objetos]"
                        ),
                        "sets_flags": ["xochitl_amiga", "xochitl_fortalecida"],
                        "nah_delta": 3,
                        "next_phase": None,
                    },
                ],
            },
        },
    },

    # ── Nivel 6 — Temiminaloyan ───────────────────────────────────────────────
    "nivel6_flechas": {
        "name": "Temiminaloyan — El Campo de Flechas",
        "entry_text": (
            "Las flechas caen. Sin origen. Sin pausa.\n"
            "Un proyectil pasa a centímetros de tu cara.\n\n"
            "XOCHITL: \"Temiminaloyan. El campo eterno. Las flechas son del Mictlán — "
            "no matan, pero duelen eternamente. Las almas aquí no mueren más. "
            "Solo esquivan. Siempre.\"\n\n"
            "El guerrero cojo levanta la vista. Te vio. Frena en seco.\n"
            "YAOTL: \"¿Vivo? En el campo de flechas... ¿cómo?\""
        ),
        "start_phase": "observacion",
        "phases": {
            "observacion": {
                "text": (
                    "Yaotl — porque ese debe ser su nombre — te estudia "
                    "con los ojos de alguien que lleva décadas sin ver nada nuevo.\n\n"
                    "Cojea del pie izquierdo. La armadura está destrozada pero lleva la postura "
                    "de un hombre que nunca olvidó ser guerrero.\n\n"
                    "¿Cómo empiezas?"
                ),
                "options": [
                    {
                        "label": "[ESP] \"Soy [tu nombre]. Vengo a cruzar. ¿Me ayudas?\"",
                        "response_text": (
                            "YAOTL: \"¿Ayuda. Directamente. Sin preámbulo.\"\n"
                            "Se ríe — un sonido que cruje como armadura vieja.\n"
                            "YAOTL: \"Me gusta. Los vivos que llegan aquí suelen "
                            "tener miedo o reverencia. Tú tienes prisa.\"\n\n"
                            "Baja la guardia un punto.\n"
                            "[DIRECTNESS APPRECIATED: Yaotl valora la franqueza]"
                        ),
                        "sets_flag": "yaotl_primer_contacto_directo",
                        "esp_delta": 1,
                        "next_phase": "desafio_principal",
                    },
                    {
                        "label": "[NAH] \"¿Cuánto tiempo llevas aquí?\"",
                        "response_text": (
                            "YAOTL: \"Tiempo. El tiempo no existe aquí.\"\n"
                            "Pausa.\n"
                            "\"En tiempo vivo... décadas. Un conquistador "
                            "al que yo protegía me abandonó en la batalla. "
                            "Morí cubriendo su retirada. Él sobrevivió.\"\n\n"
                            "No hay amargura en la voz. Solo peso.\n\n"
                            "JUGADOR: \"¿Y él?\"\n"
                            "YAOTL: \"Murió de viejo, supongo. No sé si está aquí.\"\n"
                            "[HISTORIA DE YAOTL: traición revelada — punto vulnerable]"
                        ),
                        "sets_flag": "yaotl_historia_revelada",
                        "nah_delta": 1,
                        "next_phase": "desafio_principal",
                    },
                    {
                        "label": "[DUAL] \"Sé quién eres. Yaotl. El Caminante me habló de ti.\"",
                        "requires_flag_any": ["caminante_trato"],
                        "response_text": (
                            "Yaotl se pone rígido.\n"
                            "YAOTL: \"¿El Caminante? Ese alma... ¿sigue en el viento?\"\n"
                            "JUGADOR: \"Ya no. Lo liberé.\"\n\n"
                            "Largo silencio. Yaotl mira hacia el nivel anterior.\n"
                            "YAOTL: \"Lo liberaste. Un vivo liberó a un muerto.\"\n"
                            "Otra pausa.\n"
                            "\"Dime qué necesitas.\"\n"
                            "[VÍNCULO DEL CAMINANTE: Yaotl dispuesto a ayudar desde el inicio]"
                        ),
                        "sets_flag": "yaotl_vinculo_caminante",
                        "nah_delta": 2,
                        "next_phase": "desafio_principal",
                    },
                ],
            },
            "desafio_principal": {
                "text": (
                    "Yaotl cruza los brazos. Las flechas siguen cayendo alrededor.\n"
                    "Él ni las mira — décadas de práctica.\n\n"
                    "YAOTL: \"Para cruzar este campo hay que saber esquivar "
                    "o saber convencer a las flechas de que no vales la pena.\"\n"
                    "\"Yo no puedo cruzar. Estoy atado aquí. Pero puedo enseñarte "
                    "el camino — si me das razón para hacerlo.\"\n\n"
                    "¿Qué le ofreces?"
                ),
                "options": [
                    {
                        "label": "[ESP] Demostrar destreza — esquivar sin su ayuda",
                        "response_text": (
                            "No pides nada. Empiezas a moverte entre las flechas.\n\n"
                            "El escudo. El instinto. La memoria del cuerpo.\n"
                            "No es perfecto — dos flechas rozan el hombro — "
                            "pero llegas al centro del campo.\n\n"
                            "YAOTL: \"...Bien. No muerto. Puedo respetarlo.\"\n"
                            "Se mueve hacia ti, esquivando sin pensar.\n"
                            "\"Sígueme. Te enseño el resto.\"\n"
                            "[RESPETO GANADO POR DESTREZA: Yaotl guía por mérito]"
                        ),
                        "sets_flag": "yaotl_respeto_destreza",
                        "esp_delta": 2,
                        "next_phase": "salida_flechas",
                    },
                    {
                        "label": "[NAH] Hablarle de la traición — reconocer lo que le hicieron",
                        "requires_flag_any": ["yaotl_historia_revelada", "caminante_trato"],
                        "response_text": (
                            "JUGADOR: \"Sé lo que te hizo. El conquistador. "
                            "Moriste cubriéndolo y él se fue. "
                            "Eso fue una traición y no fue culpa tuya.\"\n\n"
                            "Yaotl no responde de inmediato.\n\n"
                            "YAOTL: \"Treinta años esperando que alguien lo dijera.\"\n"
                            "No es sarcasmo. Es exactamente lo que dice.\n\n"
                            "YAOTL: \"El camino es así.\"\n"
                            "Empieza a mostrar la ruta entre las flechas.\n"
                            "[YAOTL PACIFICADO: deuda de dignidad saldada]"
                        ),
                        "sets_flags": ["yaotl_pacificado_verdad", "yaotl_dignidad"],
                        "nah_delta": 3,
                        "next_phase": "canto_yaotl",
                    },
                    {
                        "label": "[DUAL] Ofrecerle salir de aquí contigo",
                        "response_text": (
                            "JUGADOR: \"¿Quieres salir? Puedo intentarlo. "
                            "No sé cómo, pero si encontré al Caminante...\"\n\n"
                            "YAOTL: \"Las almas no pueden salir del Mictlán. "
                            "Solo bajar, nunca subir.\"\n"
                            "JUGADOR: \"No sé si eso es verdad o si nadie lo ha intentado.\"\n\n"
                            "Yaotl te mira durante un tiempo largo.\n"
                            "YAOTL: \"Si llegas al trono... pregúntale. "
                            "Mictlantecuhtli puede liberar lo que no debería estar aquí.\"\n\n"
                            "\"Mientras tanto, te guío. Si prometes preguntar.\"\n"
                            "[PROMESA AL YAOTL: deuda con el nivel 9]"
                        ),
                        "sets_flags": ["yaotl_promesa_liberacion", "yaotl_aliado_condicional"],
                        "esp_delta": 1, "nah_delta": 1,
                        "next_phase": "salida_flechas",
                    },
                ],
            },
            "canto_yaotl": {
                "text": (
                    "Yaotl te guía por el campo. A mitad del camino, para.\n\n"
                    "YAOTL: \"Diego pasó por aquí. Cantó algo. No entendí el idioma.\"\n"
                    "\"¿Tú cantas?\"\n\n"
                    "¿Qué haces?"
                ),
                "options": [
                    {
                        "label": "[NAH] Cantar el icnocuicatl — el mismo que detiene las montañas",
                        "requires_flag_any": ["canto_caminante", "nivel2_canto_nahua", "nivel2_cruce_canto"],
                        "response_text": (
                            "El mismo canto. Las palabras de orfandad y reencuentro.\n\n"
                            "Las flechas... ralentizan. No se detienen, pero "
                            "el ritmo cambia — más lento, más espaciado. "
                            "Como si el campo estuviera escuchando.\n\n"
                            "YAOTL: \"Eso que cantaste. Eso sana algo aquí.\"\n"
                            "Señala el pecho. Con una armadura destrozada encima.\n\n"
                            "YAOTL: \"Voy contigo. Hasta donde pueda.\"\n"
                            "[CANTO DE LIBERACIÓN: Yaotl se une como aliado]"
                        ),
                        "sets_flags": ["yaotl_aliado", "canto_liberacion"],
                        "nah_delta": 2,
                        "next_phase": None,
                        "grants_items": ["arco_yaotl", "bendicion_guerreros"],
                    },
                    {
                        "label": "[1] No cantar — cruzar en silencio con Yaotl",
                        "response_text": (
                            "No cantas. Cruzas.\n\n"
                            "Yaotl te guía entre las flechas con precisión de décadas.\n"
                            "Sales al otro lado. Rápido. Limpio.\n\n"
                            "YAOTL: \"Bien hecho.\"\n"
                            "No viene contigo. Pero te da el arco.\n"
                            "YAOTL: \"Por si algo en los siguientes niveles necesita ser herido.\"\n"
                            "[CRUCE COMPLETADO: arco de Yaotl obtenido]"
                        ),
                        "sets_flag": "yaotl_neutral",
                        "next_phase": None,
                        "grants_items": ["arco_yaotl", "punta_temiminaloyan"],
                    },
                ],
            },
            "salida_flechas": {
                "text": (
                    "El camino está casi claro. Un último obstáculo: "
                    "una zona donde las flechas caen más densas.\n\n"
                    "¿Cómo cruzas el tramo final?"
                ),
                "options": [
                    {
                        "label": "[ESP] Correr — pura velocidad",
                        "response_text": (
                            "Corres. Tres flechas rozan. Ninguna penetra profundo.\n"
                            "Sales al otro lado jadeando.\n\n"
                            "YAOTL (desde el campo): \"Sobreviviste. Es suficiente.\"\n"
                            "[CRUCE POR VELOCIDAD]"
                        ),
                        "sets_flag": "nivel6_cruce_velocidad",
                        "esp_delta": 1,
                        "next_phase": None,
                        "grants_items": ["punta_temiminaloyan"],
                    },
                    {
                        "label": "[NAH] Usar el Escudo — avanzar paso a paso",
                        "response_text": (
                            "El Escudo Ceiba aguanta cada impacto. "
                            "Avanzas metro a metro, sin prisa.\n\n"
                            "Llegas entero. El Escudo tiene nuevas marcas — "
                            "las flechas del Mictlán son distintas a las de obsidiana.\n\n"
                            "YAOTL (desde el campo): \"El escudo de Diego. "
                            "Reconocería ese escudo en cualquier nivel.\"\n"
                            "[CRUCE CON ESCUDO — homenaje involuntario a Diego]"
                        ),
                        "sets_flag": "nivel6_cruce_escudo",
                        "nah_delta": 1,
                        "next_phase": None,
                        "grants_items": ["punta_temiminaloyan", "bendicion_guerreros"],
                    },
                ],
            },
        },
    },

    # ── Nivel 8 — Apochcaloca ─────────────────────────────────────────────────
    "nivel8_ilusion": {
        "name": "Apochcaloca — Las Ilusiones",
        "entry_text": (
            "La oscuridad se cierra. No hay arriba ni abajo.\n"
            "La voz de Xochitl llega de lejos, luego de cerca, luego de ningún lado.\n\n"
            "XOCHITL: \"Apochcaloca. El nivel que Diego no superó solo. "
            "Las ilusiones aquí son perfectas — no hay forma de distinguirlas "
            "de la realidad excepto por lo que sabes de ti mismo.\"\n\n"
            "NARRADOR: La primera ilusión llega sin aviso."
        ),
        "start_phase": "ilusion1",
        "phases": {
            "ilusion1": {
                "text": (
                    "Ves a Diego. No una proyección — Diego de verdad, "
                    "tal como lo viste en el Nivel 3 desde la memoria de la roca. "
                    "Joven. Con la espada. Sin el peso de cincuenta años.\n\n"
                    "DIEGO-ILUSION: \"Para. Xochitl está muerta. Siempre estuvo muerta. "
                    "No hay nada que puedas hacer por ella que no haya intentado yo. "
                    "Vuelve.\"\n\n"
                    "¿Cómo respondes?"
                ),
                "options": [
                    {
                        "label": "[ESP] \"Diego no me diría eso. Eres una ilusión.\"",
                        "response_text": (
                            "DIEGO-ILUSION: \"¿Cómo sabes lo que yo diría?\"\n"
                            "JUGADOR: \"Porque vi lo que tallaste en el Iztepetl. "
                            "'Sigue.' Eso tallaste. No 'vuelve'.\"\n\n"
                            "La ilusión se quiebra. Diego se disuelve. "
                            "La oscuridad queda, pero es solo oscuridad.\n\n"
                            "XOCHITL (cerca): \"Bien. Primera ilusión rota.\"\n"
                            "[ILUSIÓN 1 SUPERADA — lógica]"
                        ),
                        "sets_flag": "ilusion1_logica",
                        "esp_delta": 1,
                        "next_phase": "ilusion2",
                    },
                    {
                        "label": "[NAH] Hablarle como si fuera Diego real",
                        "response_text": (
                            "JUGADOR: \"Diego. Sé que esto puede ser ilusión. "
                            "Pero si hay alguna parte de ti en esta imagen... "
                            "quiero que sepas que no vengo a juzgar lo que no pudiste. "
                            "Vengo a terminar lo que empezaste.\"\n\n"
                            "Larga pausa en la ilusión.\n"
                            "DIEGO-ILUSION (voz que cambia): \"...Termina, entonces.\"\n\n"
                            "Se disuelve suavemente. Como si quisiera.\n"
                            "XOCHITL (voz temblorosa): \"Eso... fue extraño. "
                            "Como si algo real lo escuchara.\"\n"
                            "[ILUSIÓN 1 SUPERADA — empatía]"
                        ),
                        "sets_flags": ["ilusion1_empatia", "ilusion1_diego_real"],
                        "nah_delta": 2,
                        "next_phase": "ilusion2",
                    },
                ],
            },
            "ilusion2": {
                "text": (
                    "La segunda ilusión: tú mismo. Pero diferente.\n"
                    "La versión que no vino. La que se quedó en el mundo de arriba, "
                    "convenció a Citlali de que Diego estaba bien, "
                    "y siguió su vida sin mirar hacia el Mictlán.\n\n"
                    "TUYOILUSION: \"Esta era la opción correcta. "
                    "¿Ves? Feliz. Tranquilo. Sin obsidiana en las manos ni "
                    "muertos a los que salvar. ¿Por qué no eres yo?\"\n\n"
                    "¿Cómo respondes?"
                ),
                "options": [
                    {
                        "label": "[ESPEJO] Usar el Espejo de Iztepetl",
                        "requires_flag_any": ["tiene_espejo_iztepetl"],
                        "response_text": (
                            "Sacas el espejo de obsidiana. "
                            "Lo apuntas hacia la ilusión.\n\n"
                            "El espejo muestra lo que hay detrás: "
                            "no un tú feliz — un vacío con forma de persona. "
                            "La ilusión no tiene interior. Solo superficie.\n\n"
                            "JUGADOR: \"Eres hueco. La felicidad que muestras "
                            "no tiene nada adentro.\"\n\n"
                            "La ilusión se quiebra. Rápido. Como si el espejo "
                            "la avergonzara de existir.\n"
                            "[ILUSIÓN 2 ROTA CON ESPEJO — directo a Ilusión 3]"
                        ),
                        "sets_flag": "ilusion2_espejo",
                        "next_phase": "ilusion3",
                    },
                    {
                        "label": "[ESP] \"Porque esa versión no puede ayudar a nadie.\"",
                        "response_text": (
                            "TUYOILUSION: \"Tampoco necesita hacerlo.\"\n"
                            "JUGADOR: \"Yo sí. No porque tenga que — porque quiero. "
                            "Eso te diferencia de mí: tú no quieres nada.\"\n\n"
                            "La ilusión vacila.\n"
                            "TUYOILUSION: \"Eso es arrogancia. Creer que tú puedes "
                            "cuando nadie más pudo.\"\n"
                            "JUGADOR: \"No. Es decisión.\"\n\n"
                            "Se disuelve.\n"
                            "[ILUSIÓN 2 SUPERADA — voluntad]"
                        ),
                        "sets_flags": ["ilusion2_voluntad", "ilusion2_liderazgo"],
                        "esp_delta": 2,
                        "next_phase": "ilusion3",
                    },
                    {
                        "label": "[NAH] \"No sé si tienes razón. Pero no me importa.\"",
                        "response_text": (
                            "JUGADOR: \"Puede que tengas razón. Quizás esa vida "
                            "era la correcta. Quizás esto es un error.\"\n"
                            "\"Pero ya estoy aquí. Y Xochitl también está aquí. "
                            "Entonces sigo.\"\n\n"
                            "TUYOILUSION: \"Esa no es razón suficiente.\"\n"
                            "JUGADOR: \"Para mí sí.\"\n\n"
                            "La ilusión no se disuelve — se desvanece, "
                            "como si perdiera interés en la discusión.\n"
                            "[ILUSIÓN 2 SUPERADA — aceptación sin certeza]"
                        ),
                        "sets_flags": ["ilusion2_aceptacion", "ilusion2_duda"],
                        "nah_delta": 2,
                        "next_phase": "ilusion3",
                    },
                ],
            },
            "ilusion3": {
                "text": (
                    "La tercera ilusión: Mictlantecuhtli. Pero no en el trono — "
                    "aquí, en la oscuridad, sin ceremonias.\n\n"
                    "MICTLANTECUHTLI-ILUSION: \"Diego te habló de mí. "
                    "Todos los vivos que llegan al Mictlán me imaginan igual: "
                    "cruel, frío, sin razones. "
                    "Pero los muertos saben algo que los vivos no: "
                    "yo no traje a nadie aquí. Ellos llegaron solos.\"\n\n"
                    "MICTLANTECUHTLI-ILUSION: \"¿Por qué crees que Xochitl está atrapada?\"\n\n"
                    "¿Qué respondes?"
                ),
                "options": [
                    {
                        "label": "[ESP] \"Porque tú la retienes. Y voy a convencerte de soltarla.\"",
                        "response_text": (
                            "MICTLANTECUHTLI-ILUSION: \"Convencer. Diego también quiso convencer.\"\n"
                            "\"La diferencia entre tú y él: tú llegaste hasta aquí. "
                            "Él se quedó en el séptimo nivel.\"\n\n"
                            "La ilusión se disuelve. En su lugar, una luz — "
                            "no grande, pero real. El laberinto del Apochcaloca.\n"
                            "[ILUSIÓN 3 SUPERADA — determinación]"
                        ),
                        "sets_flag": "ilusion3_determinacion",
                        "esp_delta": 1,
                        "next_phase": "laberinto",
                    },
                    {
                        "label": "[NAH] \"No lo sé. Vine a preguntarte.\"",
                        "response_text": (
                            "MICTLANTECUHTLI-ILUSION: \"...\"\n"
                            "Larga pausa.\n"
                            "\"Un vivo que admite ignorancia. Interesante.\"\n\n"
                            "\"Xochitl está aquí porque eligió esperar. "
                            "Las almas que esperan a alguien que prometió volver... "
                            "se quedan. Yo no las retengo. Ellas se retienen a sí mismas.\"\n\n"
                            "Esto es nuevo. Esto cambia algo.\n\n"
                            "JUGADOR: \"¿Y si la persona prometida llega?\"\n"
                            "MICTLANTECUHTLI-ILUSION: \"Pregúntame en el trono.\"\n\n"
                            "La ilusión se disuelve. El laberinto aparece.\n"
                            "[ILUSIÓN 3 SUPERADA — conocimiento sobre Xochitl]"
                        ),
                        "sets_flags": ["ilusion3_conocimiento", "xochitl_razon_espera"],
                        "nah_delta": 3,
                        "next_phase": "laberinto",
                    },
                ],
            },
            "laberinto": {
                "text": (
                    "El laberinto del Apochcaloca. Paredes de oscuridad "
                    "que se mueven cuando no las miras.\n\n"
                    "XOCHITL: \"Hay que encontrar el centro. No hay mapa.\"\n\n"
                    "Algo aparece a tu lado — si Yaotl viene contigo, "
                    "está aquí. Si tienes el Corazón de Obsidiana, late.\n\n"
                    "¿Cómo navegas?"
                ),
                "options": [
                    {
                        "label": "[CORAZON] Seguir el pulso del Corazón de Obsidiana",
                        "requires_flag_any": ["2c_corazon_cerro"],
                        "response_text": (
                            "El corazón pulsa. Una vez hacia el norte. "
                            "Dos veces hacia el este. Silencio hacia el sur.\n\n"
                            "Sigues el pulso. El laberinto intenta confundirte — "
                            "las paredes se mueven, los pasillos se duplican. "
                            "Pero el corazón siempre sabe.\n\n"
                            "Llegas al centro. Directamente. Sin pérdidas.\n\n"
                            "XOCHITL: \"¿Cómo lo hiciste?\"\n"
                            "JUGADOR: \"El cerro me dio un guía.\"\n"
                            "[LABERINTO SUPERADO CON CORAZÓN — sin desviaciones]"
                        ),
                        "sets_flag": "laberinto_corazon",
                        "nah_delta": 2,
                        "next_phase": "centro",
                        "grants_items": ["cristal_niebla"],
                    },
                    {
                        "label": "[YAOTL] Dejar que Yaotl guíe — treinta años en el Mictlán",
                        "requires_flag_any": ["yaotl_aliado"],
                        "response_text": (
                            "YAOTL: \"He estado en el Mictlán décadas. "
                            "Este nivel lo cruzé una vez, de bajada. "
                            "La lógica es inversa — lo que parece sur es norte.\"\n\n"
                            "Yaotl va delante. Se equivoca una vez. Corrige. "
                            "No pide disculpas — simplemente corrige.\n\n"
                            "Llegas al centro. Xochitl toma la mano de Yaotl "
                            "durante un segundo — el gesto de alguien que reconoce "
                            "a otro que también lleva mucho tiempo esperando.\n\n"
                            "[LABERINTO SUPERADO CON YAOTL — vínculo Xochitl-Yaotl]"
                        ),
                        "sets_flags": ["laberinto_yaotl", "xochitl_yaotl_vinculo"],
                        "nah_delta": 1,
                        "next_phase": "centro",
                        "grants_items": ["cristal_niebla"],
                    },
                    {
                        "label": "[NAH] Escuchar la voz de Xochitl — ella conoce este nivel",
                        "response_text": (
                            "XOCHITL: \"Treinta años aquí. No en este nivel, pero... "
                            "lo he cruzado en sueños. O lo que sea que tenemos "
                            "en lugar de sueños.\"\n\n"
                            "Sus instrucciones son fragmentarias pero reales. "
                            "\"Izquierda cuando el frío aumenta. Recto cuando escuchas agua.\"\n\n"
                            "Llegas al centro. Xochitl también.\n\n"
                            "XOCHITL: \"Nunca pensé que ayudaría a alguien a cruzar aquí.\"\n"
                            "JUGADOR: \"¿Y cómo te siente?\"\n"
                            "XOCHITL: \"Como si valiera la pena haber esperado.\"\n"
                            "[LABERINTO SUPERADO CON XOCHITL — validación mutua]"
                        ),
                        "sets_flags": ["laberinto_xochitl", "validacion_xochitl"],
                        "nah_delta": 2,
                        "next_phase": "centro",
                        "grants_items": ["cristal_niebla"],
                    },
                    {
                        "label": "[ESP] Avanzar a ciegas — intuición y fuerza de voluntad",
                        "response_text": (
                            "Sin guía. Sin mapa. Sin corazón que pulse.\n"
                            "Solo tú y la oscuridad.\n\n"
                            "Te pierdes tres veces. Vuelves sobre tus pasos. "
                            "A la cuarta vez, algo en ti decide: este pasillo. "
                            "No hay razón. Solo decisión.\n\n"
                            "Y funciona.\n\n"
                            "XOCHITL: \"¿Cómo supiste?\"\n"
                            "JUGADOR: \"No supe. Decidí.\"\n"
                            "[LABERINTO SUPERADO POR VOLUNTAD — sin ayuda externa]"
                        ),
                        "sets_flag": "voluntad_inquebrantable",
                        "esp_delta": 2,
                        "next_phase": "centro",
                        "grants_items": ["cristal_niebla"],
                    },
                ],
            },
            "centro": {
                "text": (
                    "El centro del Apochcaloca. Una luz sin fuente. "
                    "El laberinto queda atrás.\n\n"
                    "Xochitl está aquí. Entera. La oscuridad la intentó — no pudo.\n\n"
                    "XOCHITL: \"Ya casi. El noveno nivel está al norte. "
                    "Mictlantecuhtli está ahí. "
                    "¿Qué le vas a pedir?\"\n\n"
                    "¿Qué respondes?"
                ),
                "options": [
                    {
                        "label": "[ESP] \"A liberar a Diego y que Xochitl pueda descansar.\"",
                        "response_text": (
                            "XOCHITL: \"Diego... y yo.\"\n"
                            "Larga pausa.\n"
                            "\"¿Y tú? ¿Qué pides para ti?\"\n"
                            "JUGADOR: \"Eso no importa ahora.\"\n"
                            "XOCHITL: \"Eso es lo que decía Diego.\"\n\n"
                            "Silencio compartido.\n"
                            "[RESOLUCIÓN A — el sacrificio como camino]"
                        ),
                        "sets_flag": "resolucion_sacrificio",
                        "esp_delta": 1,
                        "next_phase": None,
                    },
                    {
                        "label": "[NAH] \"Pedir que Xochitl elija — no que sea liberada.\"",
                        "response_text": (
                            "XOCHITL: \"¿Que yo elija?\"\n"
                            "JUGADOR: \"Si puedes quedarte o irte — eso es libertad. "
                            "Si solo puedes irte porque yo lo pedí, eso es otro tipo de jaula.\"\n\n"
                            "Xochitl te mira durante un tiempo largo.\n"
                            "XOCHITL: \"Nadie me lo había preguntado así.\"\n"
                            "\"Ni siquiera Diego.\"\n\n"
                            "[AUTONOMÍA DE XOCHITL — compromiso de amor genuino]"
                        ),
                        "sets_flags": ["compromiso_amor", "xochitl_eleccion"],
                        "nah_delta": 3,
                        "next_phase": None,
                    },
                    {
                        "label": "[DUAL] \"Pedir que todos los que quedaron atrapados tengan una oportunidad.\"",
                        "response_text": (
                            "XOCHITL: \"¿Todos? ¿El Caminante, Yaotl, los que están "
                            "en el campo de flechas, los que perdieron su bandera?\"\n"
                            "JUGADOR: \"Sí.\"\n"
                            "XOCHITL: \"Eso es... mucho de pedir.\"\n"
                            "JUGADOR: \"Lo sé. Pero si no lo pido, nadie lo pedirá.\"\n\n"
                            "XOCHITL (suave): \"Diego solo pedía por mí. "
                            "Tú pides por todos.\"\n"
                            "\"Eso cambia lo que eres aquí.\"\n"
                            "[RESOLUCIÓN C — la liberación como camino]"
                        ),
                        "sets_flags": ["compromiso_amor", "resolucion_liberacion"],
                        "esp_delta": 1, "nah_delta": 2,
                        "next_phase": None,
                    },
                ],
            },
        },
    },

    # ── Nivel 7 — Teyollocualoyan ────────────────────────────────────────────
    "nivel7_itzcuintli": {
        "name": "Teyollocualoyan — Itzcuintli, el Devorador de Corazones",
        "entry_text": (
            "Caminas hacia el claro. Los hongos bajo tus pies estallan en luz azul-verde.\n"
            "Dejas un rastro brillante detrás de ti — no hay manera de ocultarse.\n\n"
            "Y lo ves.\n\n"
            "NARRADOR: Itzcuintli no es un jaguar. Lo fue, hace eras.\n"
            "Ahora es algo más grande. Su lomo casi alcanza la altura de las copas negras.\n"
            "Tiene ocho garras por pata — no cuatro. Cada colmillo es más largo que tu antebrazo.\n"
            "Su pelaje es negro con rosetas que brillan por dentro,\n"
            "como si bajo la piel hubiera brasas. Y la oreja izquierda —\n"
            "solo hay una cicatriz antigua, lisa, del tamaño de una tortilla.\n\n"
            "Te mira. No con un ojo, no con dos — con los dos al mismo tiempo\n"
            "y con algo más, un sentido que no tienes. Te ha olido. Te ha probado en el aire.\n"
            "Te conoce ya.\n\n"
            "ITZCUINTLI (rugido que se convierte en palabras, la voz vieja como una cueva):\n"
            "\"Carne y sangre en mi reino. ¿Sabes cuánto tiempo ha pasado desde mi última\n"
            "comida verdadera?\"\n\n"
            "NARRADOR: El rugido te llega al pecho.\n"
            "Los hongos bajo tus pies brillan más fuerte, asustados."
        ),
        "start_phase": "llegada",
        "phases": {
            # ── Llegada ───────────────────────────────────────────────────────
            "llegada": {
                "text": (
                    "Itzcuintli te tiene medido. Lo sientes antes de que haga nada.\n\n"
                    "XOCHITL (voz muy baja): \"Antes de que elijas qué hacer,\n"
                    "él ya eligió qué hacerte. Solo está esperando que justifiques\n"
                    "su decisión de un lado o del otro.\"\n\n"
                    "¿Qué haces mientras te observa?"
                ),
                "options": [
                    {
                        "label": "[ESP] Mantener la postura — no retroceder ni avanzar",
                        "response_text": (
                            "No te mueves. Ni un paso atrás, ni un paso adelante.\n"
                            "Dejas que Itzcuintli te lea.\n\n"
                            "ITZCUINTLI (lento): \"Quieto. El de dos sangres también se\n"
                            "quedó quieto. Veo que aprendiste de él.\"\n"
                            "Una pausa.\n"
                            "\"O aprendiste solo. Eso es peor para mí y mejor para ti.\"\n\n"
                            "[ITZCUINTLI: NEUTRAL — reconoce aplomo]"
                        ),
                        "sets_flag": "nivel7_llegada_quieto",
                        "next_phase": "propuesta",
                    },
                    {
                        "label": "[NAH] Escuchar la selva — ¿hay algo más aquí?",
                        "response_text": (
                            "Cierras los ojos un momento. Oídos abiertos.\n\n"
                            "El claro tiene dos sonidos: el rugido de Itzcuintli,\n"
                            "y algo más pequeño, más suave, en el borde oscuro a tu izquierda.\n"
                            "Un círculo donde los hongos no brillan. Ahí hay algo.\n\n"
                            "ITZCUINTLI: \"Olfateas el lugar. El de dos sangres hizo lo mismo.\n"
                            "Él no escuchó a Chantico. Tú sí la oíste, ¿verdad?\"\n"
                            "Sus brasas se calientan levemente bajo el pelaje.\n"
                            "\"Interesante.\"\n\n"
                            "[ITZCUINTLI: CURIOSO — percibiste a Chantico]"
                        ),
                        "sets_flag": "nivel7_llegada_chantico",
                        "nah_delta": 1,
                        "next_phase": "propuesta",
                    },
                    {
                        "label": "[YAOTL] Yaotl da un paso al frente (requiere aliado de Nivel 6)",
                        "requires_flag_any": ["yaotl_aliado"],
                        "response_text": (
                            "Yaotl, a tu lado, tensa el arco espiritual sin disparar.\n\n"
                            "YAOTL: \"Me conoce. No desde la muerte. Desde antes.\n"
                            "Cuando yo cazaba jaguares en los volcanes del sur,\n"
                            "hace seiscientos años, él ya era viejo.\n"
                            "Me comió un hermano. Yo le corté la oreja.\"\n\n"
                            "Itzcuintli se queda muy quieto.\n\n"
                            "ITZCUINTLI: \"El guerrero de la oreja. Seiscientos años.\n"
                            "Creí que el Temiminaloyan te tenía.\"\n"
                            "YAOTL: \"Ya no.\"\n"
                            "Un silencio que pesa décadas de parte de los dos.\n\n"
                            "ITZCUINTLI (a ti): \"Tu compañero y yo tenemos deudas viejas.\n"
                            "Las deudas viejas merecen respeto. Habla.\"\n\n"
                            "[YAOTL PRESENTADO — Itzcuintli reconoce a Yaotl: apertura diplomática]"
                        ),
                        "sets_flag": "yaotl_presento_itzcuintli",
                        "next_phase": "propuesta",
                    },
                ],
            },
            # ── Propuesta ─────────────────────────────────────────────────────
            "propuesta": {
                "text": (
                    "ITZCUINTLI: \"Bien. Ya te miré. Ya sé lo que traes.\n"
                    "Elige: responde mi acertijo, pelea, convénceme,\n"
                    "o de todos modos te como. Solo el primero te garantiza el paso.\"\n\n"
                    "¿Qué haces?"
                ),
                "options": [
                    {
                        "label": "[COMBATE] Preparar las armas — enfrentar al jaguar",
                        "response_text": (
                            "Desenvainas Tlachicotl. Alzas el Escudo Ceiba.\n"
                            "Revisas mentalmente si Tonatiuh está cargado.\n\n"
                            "ITZCUINTLI (ronroneo que suena a risa):\n"
                            "\"Ah. Escoges el camino corto. Me gusta el camino corto.\n"
                            "Se terminan rápido los que lo eligen.\"\n"
                            "Larga pausa.\n"
                            "\"Y llevas piel de mi pariente en el escudo. ¿Sabes que esa\n"
                            "piel fue de un primo mío? Un jaguar joven que los españoles\n"
                            "mataron hace cincuenta años. El de dos sangres aceptó esa piel\n"
                            "en su escudo. Tú la heredaste.\"\n"
                            "Las brasas bajo su pelaje se encienden.\n"
                            "\"¿Te preguntas si yo te perdono por cargar la piel de mi primo?\"\n\n"
                            "¿Qué respondes?"
                        ),
                        "next_phase": "combate_arma",
                    },
                    {
                        "label": "[DIPLOMACIA] \"No vengo a pelear. Vengo a pasar.\"",
                        "response_text": (
                            "ITZCUINTLI (ronroneo bajo, escéptico):\n"
                            "\"No vienes a pelear. Bien. El de dos sangres tampoco vino a pelear.\n"
                            "Pero estaba preparado para pelear si hacía falta.\n"
                            "Tú también, veo. Tienes las armas. Las llevas.\n"
                            "No me las vas a entregar, ¿verdad?\"\n\n"
                            "JUGADOR: \"No. Son mías. Pero no las usaré contigo.\"\n\n"
                            "ITZCUINTLI: \"Palabra honesta. Los que pretenden entregar\n"
                            "las armas y luego las usan mueren con las armas.\n"
                            "Tú no vas a morir con las armas, porque admites que las tienes.\"\n\n"
                            "Bajo las brasas, algo se mueve — no hostilidad. Evaluación."
                        ),
                        "next_phase": "diplomacia_declaracion",
                    },
                    {
                        "label": "[CONOCIMIENTO] \"Eres guardián, no cazador. Hay diferencia.\"",
                        "response_text": (
                            "ITZCUINTLI se detiene.\n"
                            "Sus brasas bajo el pelaje se estabilizan — ni más calientes, ni más frías.\n\n"
                            "ITZCUINTLI: \"Guardián, no cazador. Diego dijo algo parecido.\n"
                            "Fue el único vivo en seiscientos años que distinguió.\n"
                            "Ahora tú también distingues.\"\n\n"
                            "Una pausa larga.\n\n"
                            "\"Entonces escucha. Tengo un acertijo. Lo tengo desde antes\n"
                            "de que existieran los reyes que me habrían contestado bien.\n"
                            "Respóndelo y paso libre. Fállalo y... veamos.\"\n\n"
                            "ITZCUINTLI:\n"
                            "\"Soy más fuerte que el acero pero más frágil que el cristal.\n"
                            "Los reyes me buscan pero los sabios me huyen.\n"
                            "Los vivos me cargan pero los muertos me han olvidado.\n"
                            "¿Qué soy?\""
                        ),
                        "next_phase": "acertijo_pregunta",
                    },
                    {
                        "label": "[AHUIZOTL] \"El de los ríos bajos te recuerda.\"",
                        "requires_flag_any": ["favor_ahuizotl"],
                        "response_text": (
                            "Itzcuintli se queda muy quieto. Las brasas debajo de su pelaje\n"
                            "se atenúan un momento — como si hubiera reído por dentro\n"
                            "y su risa fuera hacer eso, bajar las brasas.\n\n"
                            "ITZCUINTLI: \"...\"\n\n"
                            "ITZCUINTLI: \"El de las mil patas acuáticas. El pariente menor.\n"
                            "Hace mil años me debe una lengua — me la escondió cuando\n"
                            "unos cazadores me la querían cortar. Yo le debo la vida de esa escena.\"\n\n"
                            "ITZCUINTLI: \"Dile que ya no. Que saldamos. Que si necesita otra,\n"
                            "la pida él directamente, no por mensajero.\"\n\n"
                            "ITZCUINTLI: \"Y tú, vivo que eres el mensajero... pasa.\n"
                            "No te comeré hoy. Tampoco te jugaré el acertijo.\n"
                            "El de los ríos bajos pagó por ti.\"\n\n"
                            "XOCHITL (voz baja): \"Eso es... no lo había visto antes.\n"
                            "Itzcuintli que deja pasar sin acertijo, sin combate.\n"
                            "El Ahuízotl pagó caro en dignidad para hacer eso.\"\n\n"
                            "[DEUDA DEL AHUÍZOTL CERRADA — paso libre, sin medición]"
                        ),
                        "sets_flags": ["nivel7_paso_ahuizotl", "nivel9_mictlan_nota_ahuizotl"],
                        "nah_delta": 1,
                        "next_phase": None,
                    },
                ],
            },
            # ── COMBATE ───────────────────────────────────────────────────────
            "combate_arma": {
                "text": (
                    "Itzcuintli baja de la piedra negra. Los hongos a sus patas se apagan\n"
                    "de miedo. Las brasas bajo su pelaje se encienden al máximo.\n\n"
                    "¿Con qué abres el combate?"
                ),
                "options": [
                    {
                        "label": "[TLACHICOTL] La espada de obsidiana y acero — corta carne y espíritu",
                        "response_text": (
                            "Cargas con la espada en alto. Itzcuintli no se mueve — te espera.\n"
                            "Cuando llegas a tres metros, él se mueve, y entiendes que antes\n"
                            "no se movía porque no quería gastar aliento.\n\n"
                            "Es más rápido que cualquier cosa que hayas visto.\n"
                            "Pero Tlachicotl es rápida también — la espada canta cuando la alzas.\n"
                            "Das el primer tajo. Él te esquiva torciendo el cuello como si no tuviera huesos.\n"
                            "Das el segundo. Lo rozas en el costado.\n"
                            "La obsidiana de Tlachicotl muerde el pelaje.\n\n"
                            "ITZCUINTLI RUGE. No de dolor. De aprobación.\n\n"
                            "ITZCUINTLI: \"¡El filo es viejo! ¡Me recuerda al filo del otro!\n"
                            "¡Al de dos sangres no lo dejé pasar así! ¡Él me miró y preguntó!\"\n\n"
                            "La zarpa contraataca. Pasa a dos dedos de tu cara.\n"
                            "Un corte pequeño en la mejilla sangra. Una intención, no un golpe.\n"
                            "Si hubiera querido, habrías perdido la cara."
                        ),
                        "sets_flag": "combate_arma_tlachicotl",
                        "next_phase": "combate_momento",
                    },
                    {
                        "label": "[TONATIUH] El arcabuz de plata y copal — un tiro, luego recarga lenta",
                        "response_text": (
                            "Levantas el arcabuz. Apuntas al pecho — al hueco entre las costillas\n"
                            "donde se asoman las brasas. Aprietas.\n\n"
                            "El disparo de Tonatiuh truena en la selva como si hubieras\n"
                            "roto el techo del mundo. La bala — plata con ceniza de copal —\n"
                            "se entierra en el pelaje del jaguar. Humo blanco. Olor a iglesia.\n\n"
                            "ITZCUINTLI retrocede un solo paso.\n\n"
                            "ITZCUINTLI: \"La munición mezclada. El de dos sangres usaba eso.\n"
                            "Me rozó con una hace cincuenta años — no a mí, al nahual.\n"
                            "Yo estaba mirando. Yo recuerdo.\"\n\n"
                            "La herida cierra sola en segundos. Las brasas queman la bala desde adentro.\n"
                            "La escupen al suelo humeante.\n\n"
                            "ITZCUINTLI: \"No bastó. Recarga. Voy a contar. Lento. Para que alcances.\"\n\n"
                            "Cuenta: uno... dos... tres... Recargas con manos torpes.\n"
                            "Cuatro... cinco... Terminas. Seis. Itzcuintli salta."
                        ),
                        "sets_flag": "combate_arma_tonatiuh",
                        "next_phase": "combate_momento",
                    },
                    {
                        "label": "[ESCUDO + ESPADA] Defensa primero, filo después — postura de tlamatini-guerrero",
                        "response_text": (
                            "Alzas el Escudo Ceiba al frente. Tlachicotl al costado, baja.\n"
                            "Avanzas como se avanza en una iglesia vacía: con respeto y con miedo.\n"
                            "Itzcuintli nota el cambio de postura. No ataca de inmediato.\n\n"
                            "ITZCUINTLI: \"Postura de dos caras. Defensa primero, filo después.\n"
                            "Eso lo enseñaban los tlamatini-guerreros antes. Hace mucho.\n"
                            "Los vivos olvidaron esa postura. Tú la recuerdas.\"\n\n"
                            "Itzcuintli salta al fin — no directo. Cae al lado, rodando.\n"
                            "Prueba tu flanco. Giras con el escudo. La zarpa choca contra la ceiba.\n"
                            "La madera gime — no se rompe. Tu brazo del escudo se entumece hasta el hombro.\n\n"
                            "Respondes con Tlachicotl desde abajo, a la barriga.\n"
                            "La punta roza. La barriga del jaguar es calor puro.\n"
                            "Tu muñeca se quema un momento al contacto."
                        ),
                        "sets_flag": "combate_arma_escudo",
                        "next_phase": "combate_momento",
                    },
                    {
                        "label": "[ARCABUZ + ESCUDO] Disparo desde defensa — postura española",
                        "response_text": (
                            "Levantas Tonatiuh con la mano derecha. El escudo, alzado, cubre medio cuerpo.\n"
                            "Postura de arcabucero formado — la que los tercios enseñaban.\n\n"
                            "ITZCUINTLI (ronroneo): \"Postura de conquistador. Las he visto muchas.\"\n\n"
                            "Disparas. Itzcuintli se lanza al suelo como un gato se esconde bajo un mueble\n"
                            "— la bala le pasa por encima del lomo, raspándole los pelos.\n"
                            "Olor a pelo chamuscado.\n\n"
                            "El jaguar se levanta con un rugido de humillación y de satisfacción al mismo tiempo.\n\n"
                            "ITZCUINTLI: \"¡MEJOR, MEJOR! ¡HACE MIL AÑOS QUE NO ME AGACHO!\"\n\n"
                            "Ataca. No puedes recargar con una mano.\n"
                            "Tienes que elegir: soltar el escudo para recargar, o pelear cuerpo a cuerpo."
                        ),
                        "sets_flag": "combate_arma_arcabuz_escudo",
                        "next_phase": "combate_momento",
                    },
                ],
            },
            "combate_momento": {
                "text": (
                    "Itzcuintli carga. No es embestida — es tormenta.\n"
                    "Ocho garras. Dos colmillos. Un lomo del tamaño de una casa.\n\n"
                    "¿Cómo respondes?"
                ),
                "options": [
                    {
                        "label": "[ESP] Esquivar lateral — rodar hacia el lado",
                        "response_text": (
                            "Ruedas. Los hongos estallan bajo tu cuerpo, dejando un surco de luz.\n"
                            "La zarpa pasa donde estaba tu cabeza. Te pones de pie con Tlachicotl en alto.\n"
                            "Itzcuintli ya está girando para volver a atacar. Has ganado dos segundos.\n\n"
                            "XOCHITL: \"Bien. Pero no puedes seguir esquivando eternamente.\"\n\n"
                            "Tienes esos dos segundos. El siguiente golpe te alcanza de costado.\n"
                            "No profundo — pero tres cortes largos en el brazo. Sangras."
                        ),
                        "sets_flag": "combate_esquiva_lateral",
                        "esp_delta": 1,
                        "next_phase": "combate_derrota",
                    },
                    {
                        "label": "[NAH] Bloquear con el Escudo Ceiba — absorber el golpe",
                        "response_text": (
                            "El Escudo Ceiba recibe la zarpa completa.\n"
                            "El golpe es monumental. La madera cruje — no se rompe,\n"
                            "pero cruje como si el bosque entero se quejara.\n"
                            "Tu brazo se entumece. Algo en el hombro chasquea — no roto, pero cercano.\n\n"
                            "ITZCUINTLI: \"El escudo de Diego. Reconocería ese escudo en cualquier nivel.\"\n\n"
                            "El jaguar retrocede un paso. Te mira con algo parecido al respeto.\n"
                            "Pero aprovecha que tu brazo está fuera de combate para atacar de nuevo."
                        ),
                        "sets_flag": "combate_bloqueo_escudo",
                        "next_phase": "combate_derrota",
                    },
                    {
                        "label": "[DUAL] Saltar hacia arriba — agarrar una rama de los árboles negros",
                        "response_text": (
                            "Saltas. Agarras una rama de las columnas negras. Subes a pulso.\n"
                            "Itzcuintli pasa debajo sin encontrar blanco.\n\n"
                            "ITZCUINTLI: \"¡Arriba! ¡Muy vivo eres para estar tan cerca de estar muerto!\"\n\n"
                            "Desde la rama, tienes tres segundos antes de que el jaguar salte.\n"
                            "Arrojas Tlachicotl desde arriba — la espada cae sobre el hombro izquierdo del jaguar.\n"
                            "Se clava. No profundo, pero entra.\n\n"
                            "Itzcuintli RUGE. Con Tlachicotl clavada en el hombro se ve enorme desde arriba.\n"
                            "Y entonces salta hacia ti."
                        ),
                        "sets_flag": "combate_ventaja_vertical",
                        "esp_delta": 1, "nah_delta": 1,
                        "next_phase": "combate_derrota",
                    },
                    {
                        "label": "[DESESPERADO] Cargar hacia él — espada en punta como lanza",
                        "response_text": (
                            "Cargas. Tlachicotl al frente, punta primero.\n"
                            "Itzcuintli no se lo espera — los vivos no cargan contra él.\n"
                            "La punta de Tlachicotl se hunde en el hombro del jaguar.\n"
                            "La obsidiana entra cinco dedos — corta pelaje, cuero, músculo, hueso, espíritu.\n\n"
                            "Itzcuintli RUGE. De verdad esta vez. No aprobatorio. Dolor.\n\n"
                            "Pero tu posición es fatal.\n"
                            "Estás a medio metro de sus colmillos. Su cabeza gira. Su mandíbula se abre.\n\n"
                            "Elegiste el ataque más desesperado.\n"
                            "Tu espada está clavada en él.\n"
                            "¿Qué haces?"
                        ),
                        "sets_flag": "combate_carga_frontal",
                        "next_phase": "combate_climax",
                    },
                    {
                        "label": "[HUIR] Girar y correr — darle la espalda al jaguar",
                        "response_text": (
                            "Giras. Corres. Tlachicotl en la mano, el escudo al hombro.\n"
                            "No miras atrás. Los hongos estallan bajo tus pies\n"
                            "dejando una ruta de luz que Itzcuintli podría seguir con los ojos cerrados.\n\n"
                            "Dos segundos. Tres. Cuatro. Esperas la zarpa en la nuca.\n\n"
                            "La zarpa no llega.\n\n"
                            "ITZCUINTLI (a tus espaldas, voz de cueva):\n"
                            "\"Corre, carne. Corre bien. Yo no corro a los que huyen.\n"
                            "Les perdono la espalda. Pero recuerda: cuando te duermas en los\n"
                            "niveles que vienen, yo voy a estar en tus sueños. Te voy a decir,\n"
                            "cada noche, que podrías haber peleado un poco más.\n"
                            "Y tú te vas a preguntar si es verdad. Corre.\"\n\n"
                            "XOCHITL (cuando llegas al borde del claro): \"Bueno. Estás vivo.\"\n"
                            "JUGADOR (sin aliento): \"Estoy vivo.\"\n"
                            "XOCHITL: \"Diego no hubiera huido. Pero Diego está del otro lado.\n"
                            "Tú sigues aquí. Los vivos y los muertos miden distinto.\"\n\n"
                            "[HUIDA — Itzcuintli te perseguirá en sueños en Nivel 8]"
                        ),
                        "sets_flags": ["nivel7_huida", "nivel9_mictlan_nota_huida", "itzcuintli_sueños"],
                        "esp_delta": -1, "nah_delta": -1,
                        "next_phase": None,
                    },
                ],
            },
            "combate_climax": {
                "text": (
                    "Tlachicotl está clavada en el hombro de Itzcuintli.\n"
                    "Sus colmillos están a diez centímetros de tu cara.\n"
                    "El jaguar herido y tú están quietos, respirando pesado.\n\n"
                    "¿Qué haces con tu otro brazo?"
                ),
                "options": [
                    {
                        "label": "[1] Soltar la espada — retirarte antes de que muerda",
                        "response_text": (
                            "Sueltas a Tlachicotl. Ruedas hacia atrás.\n"
                            "La espada queda clavada en el jaguar — la espada que perteneció a Diego,\n"
                            "que bendijeron un sacerdote y un tlamatini, que cortó al Nahual de Obsidiana.\n"
                            "Clavada en un hombro que no es tuyo.\n\n"
                            "ITZCUINTLI te mira. Baja la cabeza. Con la boca —\n"
                            "despacio, con una delicadeza absurda para un ser de su tamaño —\n"
                            "agarra el mango de Tlachicotl y la saca del hombro.\n"
                            "La deja caer sobre los hongos, frente a ti.\n\n"
                            "ITZCUINTLI: \"Tuya. No quiero la espada del de dos sangres.\n"
                            "Pero tampoco olvidaré que la soltaste cuando importaba.\"\n\n"
                            "[TLACHICOTL RECUPERADA — Itzcuintli nota cobardía táctica]"
                        ),
                        "sets_flags": ["combate_suelto_espada", "nivel9_mictlan_nota_cobardía"],
                        "next_phase": "combate_derrota",
                    },
                    {
                        "label": "[2] Girar la hoja dentro de la herida — más daño, más riesgo",
                        "response_text": (
                            "Giras la hoja dentro. Itzcuintli aúlla.\n"
                            "Pero te muerde — el colmillo izquierdo te entra por el hombro derecho.\n"
                            "Profundo. Sientes crujir algo.\n\n"
                            "Por unos segundos ambos están unidos —\n"
                            "su colmillo en tu hombro, tu espada en el suyo.\n"
                            "Respirando pesado. Sangre revuelta.\n\n"
                            "Entonces el jaguar se separa. Tú caes hacia atrás.\n"
                            "Él queda de pie, con Tlachicotl todavía en el hombro, humeante.\n\n"
                            "ITZCUINTLI (entre respiraciones):\n"
                            "\"Eso sí lo sentí. No me habían herido así desde el cazador\n"
                            "que me cortó la oreja. Seiscientos años.\"\n"
                            "Baja la cabeza. Lento. Tlachicotl cae de su hombro.\n\n"
                            "[ITZCUINTLI GRAVEMENTE HERIDO — primer herido en 600 años]"
                        ),
                        "sets_flags": ["combate_giro_hoja", "itzcuintli_herido", "nivel9_mictlan_nota_combate"],
                        "esp_delta": 2,
                        "next_phase": "combate_victoria",
                    },
                    {
                        "label": "[3] Sacar el cuchillo con la otra mano — clavarle el ojo lateral",
                        "response_text": (
                            "Sacas el cuchillo pequeño con la zurda.\n"
                            "Lo clavas en el ojo que te queda frente — no del todo,\n"
                            "solo lo alcanzas lateralmente. Pero alcanzas.\n\n"
                            "Itzcuintli retrocede. Un ojo herido. Un hombro con Tlachicotl adentro.\n"
                            "Sangra por dos lugares. Su pelaje que arde por dentro humea.\n\n"
                            "ITZCUINTLI: \"...\"\n\n"
                            "ITZCUINTLI: \"Felicidades, carne-persistente.\n"
                            "Acabas de hacer historia en el Mictlán.\"\n\n"
                            "[ITZCUINTLI GRAVEMENTE HERIDO — historia en el Mictlán]"
                        ),
                        "sets_flags": ["combate_cuchillo_ojo", "itzcuintli_herido", "nivel9_mictlan_nota_combate"],
                        "esp_delta": 2, "nah_delta": 1,
                        "next_phase": "combate_victoria",
                    },
                ],
            },
            "combate_victoria": {
                "text": (
                    "Itzcuintli está herido. Tres pasos atrás. Sangra.\n"
                    "Las brasas bajo su pelaje se atenúan — no se apagan, pero se atenúan.\n\n"
                    "ITZCUINTLI: \"Eso sí lo sentí.\"\n\n"
                    "Tlachicotl está al suelo entre los dos, humeante.\n"
                    "¿Qué haces?"
                ),
                "options": [
                    {
                        "label": "[1] Recuperar Tlachicotl",
                        "response_text": (
                            "ITZCUINTLI: \"Ven. Ven a sacarla. No te voy a atacar.\n"
                            "Te la ganaste con obsidiana dentro de mí.\"\n\n"
                            "Te acercas con cuidado. Pones la mano en la empuñadura. Jalas.\n"
                            "Tlachicotl sale con un ruido de ventosa —\n"
                            "arrastrando pelaje, sangre y un olor a volcán extinto.\n"
                            "La hoja ahora tiene una línea roja a lo largo del acero que antes no tenía.\n"
                            "Se ha alimentado del dios-jaguar. Ha evolucionado.\n\n"
                            "XOCHITL (voz baja): \"Diego nunca llegó a esto.\n"
                            "Tlachicotl ahora lleva la marca del guardián.\"\n\n"
                            "ITZCUINTLI: \"Ve al Apochcaloca. Cura tus heridas en la niebla.\n"
                            "Y dile a Mictlantecuhtli, de mi parte, que hoy aprendí algo nuevo.\n"
                            "Él lo respetará.\"\n\n"
                            "[TLACHICOTL EVOLUCIONADA — línea de fuego]\n"
                            "[ITZCUINTLI HERIDO POR UN MORTAL — primera vez en 600 años]"
                        ),
                        "sets_flags": ["tlachicotl_evolucionada", "nivel9_mictlan_nota_combate",
                                       "itzcuintli_mensaje_para_mictlan"],
                        "esp_delta": 1,
                        "next_phase": None,
                    },
                    {
                        "label": "[2] Dejar la espada — \"Es tuya. En pago.\"",
                        "response_text": (
                            "ITZCUINTLI: \"...\"\n\n"
                            "ITZCUINTLI: \"La rechazo. Es tuya. Ven. Sácala.\n"
                            "No voy a cargar con la espada del de dos sangres el resto de la eternidad.\"\n\n"
                            "Caminas. La recuperas.\n\n"
                            "ITZCUINTLI: \"Generoso con algo que ya no me importa.\n"
                            "Pero la intención vale. Dile a Mictlantecuhtli que viniste con generosidad.\n"
                            "Él lo considera.\"\n\n"
                            "[TLACHICOTL RECUPERADA + ITZCUINTLI RESPETA GENEROSIDAD]"
                        ),
                        "sets_flags": ["tlachicotl_evolucionada", "nivel9_mictlan_nota_combate",
                                       "nivel9_mictlan_nota_generosidad"],
                        "next_phase": None,
                    },
                    {
                        "label": "[3] \"Perdóname la vida.\"",
                        "response_text": (
                            "Larga pausa.\n\n"
                            "ITZCUINTLI: \"Pedir perdón de la vida al que ya no puede quitártela\n"
                            "es redundante, carne. Pero lo respeto. Eres joven,\n"
                            "para los estándares del Mictlán.\"\n\n"
                            "\"Pasa. Lleva tu espada. Llévate algo más:\n"
                            "la oreja que me falta nunca la recuperé.\n"
                            "La perdiste tú también, ¿no? Algo. Alguien.\"\n\n"
                            "NARRADOR: Itzcuintli te mira y ves en sus ojos algo de ti\n"
                            "que tú no sabes que tienes. Una pérdida sin nombre.\n\n"
                            "ITZCUINTLI: \"El Mictlantecuhtli va a preguntarte sobre eso.\n"
                            "Prepara una respuesta honesta.\"\n\n"
                            "[MARCA DE ITZCUINTLI — visión profética; Nivel 9 reconoce]"
                        ),
                        "sets_flags": ["tlachicotl_evolucionada", "nivel9_mictlan_nota_combate",
                                       "marca_itzcuintli", "nivel9_mictlan_pregunta_perdida"],
                        "nah_delta": 1,
                        "next_phase": None,
                    },
                ],
            },
            "combate_derrota": {
                "text": (
                    "Estás de rodillas. Un ojo inflamado.\n"
                    "Sangre por dos heridas. Itzcuintli sobre ti, los colmillos a diez centímetros del cuello.\n\n"
                    "Esperas el golpe.\n\n"
                    "El golpe no viene.\n\n"
                    "ITZCUINTLI: \"Peleaste bien, carne. Mal, pero bien.\n"
                    "Mal porque no me podías ganar. Bien porque no dejaste de intentar.\n"
                    "Eso en mi reino vale más que el acierto.\"\n\n"
                    "\"Los cobardes no llegan a esta piedra. Tú llegaste. Peleaste. Perdiste.\n"
                    "Los tres verbos en orden, como deben ser.\"\n\n"
                    "¿Qué dices?"
                ),
                "options": [
                    {
                        "label": "[1] \"Mátame y termina.\"",
                        "response_text": (
                            "ITZCUINTLI (ronroneo):\n"
                            "\"Prisa. No. El Mictlán no tiene prisa. Aprende eso antes de morir, carne.\n"
                            "Los que mueren con prisa resucitan con prisa también,\n"
                            "y la prisa los hace volver a morir.\n"
                            "Sin prisa se muere bien, y quedarse así es descansar.\"\n\n"
                            "\"Pasa. No pido más.\"\n\n"
                            "XOCHITL: \"Diego no hubiera dicho eso. Tú lo dijiste.\n"
                            "No sé si eso es valentía o agotamiento. Puede ser las dos.\"\n\n"
                            "[DERROTA HONORABLE — Itzcuintli perdona la vida]"
                        ),
                        "sets_flags": ["nivel7_derrota_honorable", "nivel9_mictlan_nota_combate"],
                        "esp_delta": 1,
                        "next_phase": None,
                    },
                    {
                        "label": "[2] \"Déjame pasar.\"",
                        "response_text": (
                            "ITZCUINTLI: \"Eso es lo que iba a hacer.\n"
                            "Pero me gusta que lo pidas.\n"
                            "Los vivos dignos piden. Los indignos exigen. Pasa.\"\n\n"
                            "XOCHITL (mientras te levantas):\n"
                            "\"Diego nunca peleó con él. Pero hablaba de Itzcuintli con respeto.\n"
                            "Decía: 'el viejo jaguar vio nacer el Mictlán'.\n"
                            "Tú lo enfrentaste con una espada.\n"
                            "No sé si eso es valiente o estúpido. Probablemente las dos cosas.\"\n\n"
                            "[DERROTA HONORABLE — paso concedido]"
                        ),
                        "sets_flags": ["nivel7_derrota_honorable", "nivel9_mictlan_nota_combate"],
                        "next_phase": None,
                    },
                    {
                        "label": "[3] \"¿Por qué no me matas?\"",
                        "response_text": (
                            "ITZCUINTLI: \"Pregunta buena. La respuesta:\n"
                            "porque llevo mil años comiendo, y me aburrí.\n"
                            "Porque el de dos sangres me hizo una pregunta parecida\n"
                            "y me hizo pensar tres días.\n"
                            "Porque a veces es más interesante dejar vivo que matar.\n"
                            "Porque mi oreja cortada me recuerda que yo también fui\n"
                            "perdonado una vez.\"\n\n"
                            "\"Pasa.\"\n\n"
                            "XOCHITL: \"Nadie le había preguntado eso antes. Ni Diego.\"\n"
                            "JUGADOR: \"Diego preguntó el acertijo. Yo pregunté la razón. Son diferentes.\"\n"
                            "XOCHITL: \"Sí. Lo son.\"\n\n"
                            "[DERROTA HONORABLE — Itzcuintli reflexiona, pasa con respeto mutuo]"
                        ),
                        "sets_flags": ["nivel7_derrota_honorable", "nivel9_mictlan_nota_combate",
                                       "itzcuintli_reflexion"],
                        "nah_delta": 2,
                        "next_phase": None,
                    },
                ],
            },
            # ── DIPLOMACIA ────────────────────────────────────────────────────
            "diplomacia_declaracion": {
                "text": (
                    "ITZCUINTLI: \"Vas a pasar. Pero no me vas a convencer con palabras.\n"
                    "Con palabras convenció el de dos sangres al Mictlantecuhtli, no a mí.\n"
                    "A mí se me convence con hechos.\"\n\n"
                    "\"Mira a tu alrededor.\"\n\n"
                    "NARRADOR: Los hongos bajo tus pies brillan intermitentes.\n"
                    "Hay un círculo, a unos veinte metros, donde los hongos NO brillan.\n"
                    "Un círculo negro en un mar de luz. Perfecto. Obviamente no natural.\n\n"
                    "ITZCUINTLI:\n"
                    "\"Adentro de ese círculo vive Chantico. La pequeña. La gata del hogar\n"
                    "que fue devorada por una tormenta hace trescientos años y quedó atrapada aquí.\n"
                    "Ella no hace daño a nadie. Pero duerme en ese círculo,\n"
                    "y su sueño mancha la luz.\"\n\n"
                    "\"Entra al círculo. Despiértala con cuidado. Dile que Itzcuintli\n"
                    "le pide que salga a respirar.\n"
                    "Si lo haces sin alterarla, te dejaré pasar.\n"
                    "Si la asustas, ella me pedirá que te mate, y yo le haré caso.\"\n\n"
                    "¿Qué preguntas antes de entrar?"
                ),
                "options": [
                    {
                        "label": "[1] \"¿Por qué no lo haces tú?\"",
                        "response_text": (
                            "ITZCUINTLI: \"No puedo. Soy demasiado grande para el círculo.\n"
                            "Mi sombra sola la aterraría. Por eso necesito alguien pequeño. Vivo. Como tú.\"\n\n"
                            "XOCHITL (en voz muy baja): \"Itzcuintli pidiendo ayuda.\n"
                            "Eso tampoco lo había visto.\""
                        ),
                        "next_phase": "chantico_entrada",
                    },
                    {
                        "label": "[2] \"Lo haré.\"",
                        "response_text": (
                            "ITZCUINTLI: \"Bien. Ve. Despacio. Sin armas en la mano.\n"
                            "La espada al cinto. El arcabuz a la espalda. El escudo colgado.\n"
                            "Camina como si visitaras a tu abuela enferma.\"\n\n"
                            "XOCHITL: \"Camina como si visitaras a tu abuela enferma.\n"
                            "¿Los jaguares del Mictlán tienen abuelas?\"\n"
                            "JUGADOR: \"Supongo que sí.\""
                        ),
                        "next_phase": "chantico_entrada",
                    },
                    {
                        "label": "[3] \"¿Y si ella no confía en mí?\"",
                        "response_text": (
                            "ITZCUINTLI: \"No confiará. Pero los que no confían a veces escuchan.\n"
                            "Tu trabajo es que ella escuche. No que confíe.\"\n\n"
                            "Larga pausa.\n\n"
                            "ITZCUINTLI (más suave): \"Lleva trescientos años ahí.\n"
                            "Sin que nadie le hable. Sin que nadie la vea.\n"
                            "Lo que necesita no es confianza. Es presencia.\"\n\n"
                            "XOCHITL: \"Treinta años aquí. Sin que nadie me viera.\n"
                            "Entiendo lo que dice.\""
                        ),
                        "sets_flag": "nivel7_chantico_comprendes",
                        "nah_delta": 1,
                        "next_phase": "chantico_entrada",
                    },
                ],
            },
            "chantico_entrada": {
                "text": (
                    "Bajas las armas. Caminas al círculo. Veinte pasos. Diez. Cinco. Entras.\n\n"
                    "NARRADOR: Adentro, la oscuridad es total.\n"
                    "Los hongos del exterior siguen brillando, pero su luz no penetra —\n"
                    "se queda en el borde, como si tuviera miedo.\n"
                    "Tus ojos tardan en adaptarse. Hueles a ceniza fría. A hogar apagado hace mucho.\n\n"
                    "Y ves dos ojos. Pequeños. Del tamaño de monedas. A tu altura. En el suelo.\n\n"
                    "CHANTICO (voz como gato doméstico si los gatos hablaran —\n"
                    "pequeña, pero con algo muy viejo debajo):\n"
                    "\"¿Quién.\"\n\n"
                    "No es pregunta. Es declaración. 'Quién.'"
                ),
                "options": [
                    {
                        "label": "[1] Agacharte a su altura y extender la mano — sin hablar",
                        "response_text": (
                            "No dices nada.\n"
                            "Solo te agachas. Extiendes la mano, palma arriba, hacia los dos ojos.\n\n"
                            "Silencio.\n\n"
                            "Los ojos te estudian. Luego se acercan, despacio.\n"
                            "Un hocico pequeño, frío, te olisquea los dedos.\n\n"
                            "CHANTICO: \"Los que no hablan respetan.\n"
                            "Me levanto porque no me obligas con palabra. Vamos.\"\n\n"
                            "La gata sale contigo. Sin necesidad de explicaciones.\n"
                            "Su pelaje es del color de la ceniza acumulada. Muy pequeña comparada con Itzcuintli.\n"
                            "Pero se ve vieja de una manera que el tamaño no alcanza a medir.\n\n"
                            "[MODO MÁXIMO — respeto sin palabras]"
                        ),
                        "sets_flag": "chantico_silencio",
                        "nah_delta": 2,
                        "next_phase": "diplomacia_exito",
                    },
                    {
                        "label": "[2] \"Soy un vivo. Vengo de parte de Itzcuintli.\"",
                        "response_text": (
                            "CHANTICO (los ojos se estrechan):\n"
                            "\"Vivo. Itzcuintli. Dos palabras que me molestan. Vete.\"\n\n"
                            "NARRADOR: Sientes que si te quedas más, la gata va a llorar.\n"
                            "Y si llora, Itzcuintli lo sabrá.\n"
                            "Sales del círculo despacio.\n\n"
                            "ITZCUINTLI (cuando llegas): \"La asustaste. Entra otra vez.\n"
                            "Esta vez, piensa antes de hablar.\"\n\n"
                            "[PRUEBA FALLIDA — segunda oportunidad]"
                        ),
                        "next_phase": "chantico_segunda",
                    },
                ],
            },
            "chantico_segunda": {
                "text": (
                    "Entras otra vez. Los dos ojos te esperan exactamente donde los dejaste.\n"
                    "No se fueron. Solo observaban.\n\n"
                    "CHANTICO: \"Volviste.\"\n\n"
                    "¿Qué haces ahora?"
                ),
                "options": [
                    {
                        "label": "[NAH] \"Itzcuintli te pide que salgas a respirar.\"",
                        "response_text": (
                            "CHANTICO: \"Respirar. Llevo... llevo tiempo sin.\"\n"
                            "Pausa.\n"
                            "\"¿Cuánto?\"\n\n"
                            "JUGADOR: \"Trescientos años, según Itzcuintli.\"\n\n"
                            "CHANTICO: \"Trescientos. Ese número me duele.\n"
                            "Pero gracias por la verdad. Me levanto.\"\n\n"
                            "La gata se levanta. Pequeña, vieja, cubierta de ceniza.\n"
                            "Te sigue fuera del círculo.\n\n"
                            "CHANTICO (fuera, oliendo el aire): \"Huele a selva.\n"
                            "A hongos. A calor lejano. No estaba tan mal lo que olía por fuera.\"\n\n"
                            "[PRUEBA SUPERADA — modo tierno]"
                        ),
                        "sets_flag": "chantico_verdad",
                        "nah_delta": 1,
                        "next_phase": "diplomacia_exito",
                    },
                    {
                        "label": "[APRESURARSE] Intentar agarrarla — ya perdiste demasiado tiempo",
                        "response_text": (
                            "Extiendes los brazos para agarrar a Chantico.\n\n"
                            "La gata maúlla — un sonido que es puro terror.\n\n"
                            "Afuera, Itzcuintli RUGE.\n\n"
                            "Cuando sales del círculo, el jaguar está de pie y sus brasas\n"
                            "están al máximo — más brillantes que cuando entraste al claro.\n\n"
                            "ITZCUINTLI: \"La asustaste. Dos veces. Ella llora.\n"
                            "Y cuando llora me pide cosas, y yo no puedo decirle que no.\n"
                            "Pelea, entonces. Sin rencor. Una lástima.\"\n\n"
                            "[DIPLOMACIA FALLIDA — combate forzado con Itzcuintli enojado]"
                        ),
                        "sets_flag": "chantico_asustada",
                        "esp_delta": -1,
                        "next_phase": "combate_forzado",
                    },
                ],
            },
            "diplomacia_exito": {
                "text": (
                    "Chantico sale del círculo contigo.\n\n"
                    "ITZCUINTLI (desde la piedra):\n"
                    "\"Hermana menor. Te llevé cuidado.\"\n\n"
                    "CHANTICO (enojada, pero tierna):\n"
                    "\"Mmph. Tardaste.\"\n\n"
                    "NARRADOR: Itzcuintli ronronea. Chantico ronronea.\n"
                    "Por un momento la selva huele a hogar encendido.\n\n"
                    "ITZCUINTLI: \"Pasa, carne. Con mi bendición.\n"
                    "Y si alguna vez vuelves — y los héroes siempre vuelven —\n"
                    "Chantico se acordará de ti.\"\n\n"
                    "CHANTICO (pequeña junto a Itzcuintli):\n"
                    "\"Me acuerdo de pocas cosas. Me acordaré de ti.\"\n\n"
                    "ITZCUINTLI: \"Llévate algo.\"\n\n"
                    "NARRADOR: Itzcuintli baja la cabeza. Una de sus rosetas —\n"
                    "las que brillan por dentro — se apaga al desprenderse.\n"
                    "Cae sobre los hongos como una moneda. La levantas. Es tibia.\n"
                    "Late levemente, como si tuviera pulso propio.\n\n"
                    "ITZCUINTLI: \"Úsala para encender fuego cuando todo lo demás falle.\n"
                    "Funciona una sola vez. Úsala bien.\"\n\n"
                    "¿Qué respondes?"
                ),
                "options": [
                    {
                        "label": "[1] \"Gracias. Por Chantico también.\"",
                        "response_text": (
                            "CHANTICO (ronroneo pequeño): \"Yo no necesitaba que me sacaran.\n"
                            "Pero... sí quería que alguien viniera.\"\n\n"
                            "ITZCUINTLI: \"Eso es lo más honesto que ha dicho en trescientos años.\"\n\n"
                            "XOCHITL (mientras caminas al borde del claro):\n"
                            "\"Itzcuintli. No sé si lo he visto tratar a alguien así. Ni a Diego.\n"
                            "Diplomacia con Itzcuintli — eso es nuevo.\n"
                            "Nadie lo había hecho antes, ni con Chantico.\n"
                            "Acabas de descubrir algo de este nivel que llevaba siglos guardado.\"\n\n"
                            "[DIPLOMACIA COMPLETA — Roseta + Chantico en memoria]"
                        ),
                        "sets_flags": ["nivel7_diplomacia", "nivel9_mictlan_nota_diplomacia",
                                       "chantico_en_memoria", "itzcuintli_bendicion"],
                        "nah_delta": 2,
                        "next_phase": None,
                        "grants_items": ["roseta_itzcuintli"],
                    },
                    {
                        "label": "[2] \"Usaré la roseta bien. Lo prometo.\"",
                        "response_text": (
                            "ITZCUINTLI: \"Las promesas al Mictlán se cumplen.\n"
                            "No porque yo lo vigile. Sino porque este lugar recuerda.\"\n\n"
                            "XOCHITL: \"Eso también es nuevo. Itzcuintli explica sus advertencias.\n"
                            "Normalmente solo devora.\"\n\n"
                            "Caminas hacia el borde del claro. Los hongos\n"
                            "brillan más suaves debajo de tus pies — como si el lugar\n"
                            "te agradeciera algo.\n\n"
                            "[DIPLOMACIA COMPLETA — Roseta obtenida, Mictlán notará]"
                        ),
                        "sets_flags": ["nivel7_diplomacia", "nivel9_mictlan_nota_diplomacia",
                                       "itzcuintli_bendicion"],
                        "nah_delta": 1,
                        "next_phase": None,
                        "grants_items": ["roseta_itzcuintli"],
                    },
                ],
            },
            # ── ACERTIJO ──────────────────────────────────────────────────────
            "acertijo_pregunta": {
                "text": (
                    "ITZCUINTLI:\n"
                    "\"Soy más fuerte que el acero pero más frágil que el cristal.\n"
                    "Los reyes me buscan pero los sabios me huyen.\n"
                    "Los vivos me cargan pero los muertos me han olvidado.\n"
                    "¿Qué soy?\""
                ),
                "options": [
                    {
                        "label": "[1] El orgullo",
                        "response_text": (
                            "ITZCUINTLI se queda quieto un momento largo.\n\n"
                            "ITZCUINTLI: \"Correcto, carne-lista. El orgullo.\n"
                            "Diego también lo sabía. Él tenía mucho, ese.\n"
                            "Pero aprendió a domarlo. O intentó.\"\n\n"
                            "Las brasas bajo su pelaje se enfrían — no apagan, enfrían.\n"
                            "Como un brasero que ya no necesita más leña.\n\n"
                            "ITZCUINTLI: \"Ve. No te comeré hoy.\"\n\n"
                            "XOCHITL: \"Diego tardó menos. Pero tú también lo supiste.\n"
                            "El orgullo. Que ambos lo tengan, ¿no crees?\"\n\n"
                            "[ACERTIJO CORRECTO A LA PRIMERA — paso libre]"
                        ),
                        "sets_flags": ["nivel7_acertijo_correcto", "nivel9_mictlan_nota_acertijo"],
                        "nah_delta": 2,
                        "next_phase": None,
                    },
                    {
                        "label": "[2] El poder",
                        "response_text": (
                            "ITZCUINTLI (ronroneo tibio):\n"
                            "\"Cerca. Muy cerca. Pero el poder es efecto, no causa.\n"
                            "Los poderosos son poderosos porque algo los impulsa por dentro.\n"
                            "Ese algo es lo que pregunto. Piensa otra vez.\"\n\n"
                            "ITZCUINTLI: \"Te doy una segunda oportunidad.\n"
                            "El de dos sangres acertó a la primera.\n"
                            "Tú vas segunda. Que sea buena.\"\n\n"
                            "[SEGUNDA OPORTUNIDAD — respuesta incorrecta]"
                        ),
                        "sets_flag": "acertijo_intento_poder",
                        "next_phase": "acertijo_segunda",
                    },
                    {
                        "label": "[3] La memoria",
                        "response_text": (
                            "ITZCUINTLI (gruñido):\n"
                            "\"Equivocado. Los muertos SÍ recuerdan.\n"
                            "Nosotros somos memoria. Los vivos nos olvidan a nosotros,\n"
                            "no al revés. Si la respuesta fuera memoria, el acertijo sería\n"
                            "al contrario: 'los muertos me cargan pero los vivos me han olvidado'.\n"
                            "Piensa mejor.\"\n\n"
                            "ITZCUINTLI: \"Segunda oportunidad.\n"
                            "No la uses para decir otra cosa que me insulte.\"\n\n"
                            "[SEGUNDA OPORTUNIDAD — respuesta incorrecta]"
                        ),
                        "sets_flag": "acertijo_intento_memoria",
                        "next_phase": "acertijo_segunda",
                    },
                    {
                        "label": "[4] El miedo",
                        "response_text": (
                            "ITZCUINTLI (carcajada grave, como derrumbe lejano):\n"
                            "\"¡El miedo! ¡El miedo es útil, carne!\n"
                            "Los reyes no buscan el miedo — lo tienen de sobra.\n"
                            "Los sabios no huyen del miedo — lo respetan.\n"
                            "Lo que pregunto no es útil. Es un lujo.\n"
                            "El miedo es herramienta. Mala respuesta.\"\n\n"
                            "ITZCUINTLI: \"Segunda oportunidad. Última.\n"
                            "Después, viene el combate.\"\n\n"
                            "[SEGUNDA OPORTUNIDAD — respuesta incorrecta]"
                        ),
                        "sets_flag": "acertijo_intento_miedo",
                        "next_phase": "acertijo_segunda",
                    },
                ],
            },
            "acertijo_segunda": {
                "text": (
                    "Una segunda oportunidad.\n"
                    "Itzcuintli espera. El acertijo sigue en el aire.\n\n"
                    "\"Soy más fuerte que el acero pero más frágil que el cristal.\n"
                    "Los reyes me buscan pero los sabios me huyen.\n"
                    "Los vivos me cargan pero los muertos me han olvidado.\"\n\n"
                    "¿Qué es?"
                ),
                "options": [
                    {
                        "label": "[1] El orgullo",
                        "response_text": (
                            "ITZCUINTLI: \"Tarde, pero correcto.\"\n"
                            "Una pausa.\n"
                            "\"Diego fue primero. Tú vas segundo. Eso ya lo sabes y no voy\n"
                            "a pretender que no importa. Importa. Pero acertaste.\"\n\n"
                            "Las brasas se enfrían.\n\n"
                            "\"Pasa. Y aprende a pensar antes de hablar.\n"
                            "El siguiente que te ponga a prueba puede no tener segunda oportunidad.\"\n\n"
                            "XOCHITL: \"Tardaste. Pero bien. No todos aciertan al principio.\n"
                            "Aciertan los que piensan, aunque tarden.\"\n\n"
                            "[ACERTIJO CORRECTO A LA SEGUNDA — paso con nota]"
                        ),
                        "sets_flags": ["nivel7_acertijo_segunda", "nivel9_mictlan_nota_acertijo"],
                        "esp_delta": 1,
                        "next_phase": None,
                    },
                    {
                        "label": "[2] El poder",
                        "response_text": (
                            "ITZCUINTLI: \"Ya dijiste eso.\"\n"
                            "Sus brasas se encienden.\n"
                            "\"Dos errores. El acertijo no tiene tercera.\"\n"
                            "\"Como te dije al principio: responde o te como de todos modos.\n"
                            "No respondiste. Así que nos comemos.\"\n\n"
                            "NARRADOR: Itzcuintli baja de la piedra negra.\n"
                            "Los hongos a sus patas se apagan de miedo.\n"
                            "Tu espada ya la tienes desenvainada."
                        ),
                        "sets_flag": "combate_forzado_por_acertijo",
                        "next_phase": "combate_forzado",
                    },
                    {
                        "label": "[3] La memoria",
                        "response_text": (
                            "ITZCUINTLI: \"Ya te expliqué por qué no.\n"
                            "Dos errores. El acertijo no tiene tercera.\"\n"
                            "Sus colmillos aparecen — no agresivos, resignados.\n\n"
                            "\"Una lástima. Peleaste bien hasta que llegaste aquí.\"\n\n"
                            "NARRADOR: Itzcuintli baja de la piedra. El combate es forzoso."
                        ),
                        "sets_flag": "combate_forzado_por_acertijo",
                        "next_phase": "combate_forzado",
                    },
                    {
                        "label": "[4] El miedo",
                        "response_text": (
                            "ITZCUINTLI: \"...\"\n\n"
                            "ITZCUINTLI: \"Dos errores iguales. El miedo dos veces.\n"
                            "Eso dice algo de ti que no sé si quiero saber.\"\n\n"
                            "\"El acertijo no tiene tercera. Ya lo sabes.\"\n\n"
                            "NARRADOR: Itzcuintli baja de la piedra. Resignado casi.\n"
                            "Hay algo de tristeza en la forma en que sus brasas se encienden."
                        ),
                        "sets_flag": "combate_forzado_por_acertijo",
                        "next_phase": "combate_forzado",
                    },
                ],
            },
            "combate_forzado": {
                "text": (
                    "Itzcuintli avanza. El combate es ahora inevitable.\n"
                    "No es el mismo que si lo hubieras elegido — él está decidido,\n"
                    "no divertido. Es más rápido. Más frío.\n\n"
                    "No puedes vencerlo en este estado.\n"
                    "Solo decides cómo termina esto."
                ),
                "options": [
                    {
                        "label": "[1] Pelear hasta el final — derrota honorable",
                        "response_text": (
                            "Peleas. Tres flechas no, pero tres zarpas sí te alcanzan.\n"
                            "Caes de rodillas. Sangras. El jaguar te tiene.\n\n"
                            "ITZCUINTLI: \"Fallaste el acertijo y no dejaste de pelear.\n"
                            "Eso dice más de ti que las dos respuestas incorrectas.\"\n\n"
                            "\"Pasa. Herido. Pero pasa.\"\n\n"
                            "[COMBATE FORZADO — derrota, paso concedido por valor]"
                        ),
                        "sets_flags": ["nivel7_derrota_honorable", "nivel9_mictlan_nota_combate",
                                       "nivel9_mictlan_nota_acertijo"],
                        "esp_delta": 1,
                        "next_phase": None,
                    },
                    {
                        "label": "[2] Intentar diplomacia de último momento",
                        "response_text": (
                            "Bajas las armas.\n\n"
                            "JUGADOR: \"Pare. Por favor. Cometí un error. Dos.\n"
                            "Debí haber pensado más. Pero sigo estando aquí.\"\n\n"
                            "ITZCUINTLI (deteniéndose): \"...\"\n\n"
                            "\"La diplomacia después de fallar el acertijo dos veces.\n"
                            "Eso no lo había visto.\"\n"
                            "Una pausa que se hace muy larga.\n"
                            "\"Me divierte. Pasa. Pero recuerda esto:\n"
                            "la diplomacia funciona antes de que te fallen las palabras,\n"
                            "no después. Aprende la diferencia.\"\n\n"
                            "[COMBATE FORZADO — evitado con humildad de último momento]"
                        ),
                        "sets_flags": ["nivel7_derrota_digna", "nivel9_mictlan_nota_acertijo"],
                        "nah_delta": 1,
                        "next_phase": None,
                    },
                    {
                        "label": "[3] Correr — huir antes de que el combate empiece",
                        "response_text": (
                            "Giras. Corres.\n\n"
                            "ITZCUINTLI (a tus espaldas):\n"
                            "\"Fallaste el acertijo y huiste del combate.\n"
                            "Eso también es una respuesta. La peor, pero una respuesta.\"\n\n"
                            "La zarpa no llega.\n\n"
                            "XOCHITL (cuando llegas al borde): \"Estás vivo.\"\n"
                            "JUGADOR: \"Estoy vivo.\"\n"
                            "XOCHITL: \"Sí. Eso es algo.\"\n\n"
                            "[HUIDA TRAS ACERTIJO FALLIDO — sin combate, reputación mínima]"
                        ),
                        "sets_flags": ["nivel7_huida", "nivel9_mictlan_nota_huida",
                                       "nivel9_mictlan_nota_acertijo", "itzcuintli_sueños"],
                        "esp_delta": -1, "nah_delta": -1,
                        "next_phase": None,
                    },
                ],
            },
        },
    },

    # ── Nivel 9 — Trono de Mictlantecuhtli (placeholder mínimo) ──────────────
    "nivel9_trono": {
        "name": "Chicnauhmictlan — Ante Mictlantecuhtli",
        "entry_text": (
            "La escalera baja. Es de piedra, lisa, gastada por algo que no fueron pies.\n"
            "Cada peldaño tiene grabado un símbolo. No los reconoces todos, pero algunos sí:\n"
            "el que vio Citlali en su techo cuando te despidió.\n"
            "El que estaba en la pared del templo donde murió Xochitl.\n\n"
            "NARRADOR: Bajas y bajas. La luz del fondo no se acerca, como si la escalera\n"
            "fuera infinita. Pero las cuentas que llevas — las heridas, las cicatrices,\n"
            "las palabras dichas, las palabras tragadas — sí se hacen más pesadas\n"
            "con cada peldaño.\n\n"
            "XOCHITL (caminando junto a ti, tan presente como nunca):\n"
            "\"Vamos.\""
        ),
        "start_phase": "escalera",
        "phases": {

            # ── PARTE 1 — Escalera y llegada al salón ───────────────────────
            "escalera": {
                "text": (
                    "La escalera no termina donde debería. Sigues bajando.\n"
                    "Xochitl a tu lado. Ni delante ni atrás — junto a ti.\n\n"
                    "¿Qué le dices?"
                ),
                "options": [
                    {
                        "label": "[1] \"¿Tienes miedo?\"",
                        "response_text": (
                            "XOCHITL:\n"
                            "\"Sí. Y eso me sorprende. Llevo cuatrocientos años muerta.\n"
                            "No tendría que tener miedo de nada. Pero estoy temblando.\n"
                            "Mira — bueno, no me veas, ya sabes cómo flotamos los espíritus.\n"
                            "Pero si me pudieras tocar la mano, la sentirías temblar.\"\n\n"
                            "Sigues bajando. La luz del fondo crece."
                        ),
                        "next_phase": "salon",
                    },
                    {
                        "label": "[2] \"¿Estás lista para volver a verlo?\"",
                        "response_text": (
                            "XOCHITL (pausa):\n"
                            "\"No. No estoy lista. Pero llevo cincuenta años no estando lista.\n"
                            "Si espero a estarlo, me quedo sin tiempo otra vez.\"\n\n"
                            "Sigues bajando. La luz crece despacio."
                        ),
                        "next_phase": "salon",
                    },
                    {
                        "label": "[3] [Silencio] Caminar sin hablar",
                        "response_text": (
                            "XOCHITL (después de un momento):\n"
                            "\"...\"\n"
                            "\"Bueno. Yo también. Hay momentos en los que las palabras estorban.\"\n\n"
                            "Bajas en silencio. La luz del fondo finalmente se acerca."
                        ),
                        "nah_delta": 1,
                        "next_phase": "salon",
                    },
                ],
            },

            # ── Llegada al salón ─────────────────────────────────────────────
            "salon": {
                "text": (
                    "NARRADOR: La escalera termina.\n\n"
                    "Sales a un salón inmenso. No tiene techo visible — donde debería estar\n"
                    "el techo hay solo oscuridad pura, sin estrellas, como si alguien hubiera\n"
                    "tachado el cielo. El piso es de obsidiana pulida — tan pulida que refleja\n"
                    "todo lo que pasa por encima como un espejo negro.\n\n"
                    "Columnas de hueso humano se levantan en hileras a tu izquierda y a tu derecha.\n"
                    "Cientos. Miles. Cada una hecha de huesos perfectamente apilados,\n"
                    "sin pegamento, sin amarres. Solo equilibrio antiguo.\n\n"
                    "Al fondo, un trono de cráneos. Y sobre el trono, sentado: Él.\n\n"
                    "NARRADOR: Es alto. Más alto de lo que un cuerpo puede ser.\n"
                    "Es un esqueleto, pero no uno cualquiera. La calavera está coronada\n"
                    "con cráneos más pequeños formando una corona apilada.\n"
                    "Sus cuencas arden con una luz fría, como dos luciérnagas en cavernas.\n"
                    "En su mano izquierda: un puñado de polvo blanco que deja caer y vuelve\n"
                    "a recoger, como un hombre aburrido jugando con arena.\n\n"
                    "XOCHITL (muy quieta): \"Ese. Ese es.\"\n\n"
                    "¿Cómo llegas ante él?"
                ),
                "options": [
                    {
                        "label": "[ESP] Avanzar directo — sin detenerte",
                        "response_text": (
                            "Caminas sin detenerte. Cien pasos. Mil.\n"
                            "La distancia es elástica — el piso de obsidiana refleja tu silueta\n"
                            "deformándola: a veces te ves como tú, a veces como Diego.\n\n"
                            "Llegas al pie del trono.\n"
                            "Las luces en sus cuencas se han girado, despacio, hacia ti.\n\n"
                            "MICTLANTECUHTLI (voz que es muchas voces a la vez, todas viejas):\n"
                            "\"Vaya. Otro. ¿Cuántos de ustedes tienen que venir\n"
                            "antes de entender? Los vivos no pertenecen aquí.\n"
                            "Y sin embargo, vienen. Y vienen. Y vienen.\""
                        ),
                        "esp_delta": 1,
                        "next_phase": "escaneo",
                    },
                    {
                        "label": "[NAH] Detenerte a la mitad del salón — observar primero",
                        "response_text": (
                            "Te detienes. Observas el salón entero antes de avanzar.\n"
                            "Cuentas las columnas. Notas el patrón de los huesos.\n"
                            "El piso que te refleja con caras que no son del todo tuyas.\n\n"
                            "Cuando llegas ante él, has tomado el tiempo de leerlo.\n\n"
                            "MICTLANTECUHTLI:\n"
                            "\"Vaya. Otro. Pero este se detuvo a la mitad.\"\n"
                            "Una pausa.\n"
                            "\"El de dos sangres también se detuvo. A la misma distancia.\n"
                            "Hay algo en ese peldaño que detiene a los que piensan.\""
                        ),
                        "nah_delta": 1,
                        "next_phase": "escaneo",
                    },
                ],
            },

            # ── PARTE 2 — El escaneo ─────────────────────────────────────────
            "escaneo": {
                "text": (
                    "El polvo blanco se queda quieto en la mano de Mictlantecuhtli.\n"
                    "Sube, toma la forma de tu cara. Te estudia.\n\n"
                    "MICTLANTECUHTLI (despacio, como quien lee):\n"
                    "\"Llegaste con la espada del de dos sangres. Tlachicotl.\n"
                    "La hoja huele a cosas que ya ha cortado. Y a cosas que aún va a cortar.\"\n\n"
                    "\"Hueles a Citlali. La curandera del pueblo de arriba.\n"
                    "La que le enseñó al de dos sangres a respetarme.\n"
                    "Su olor a copal te sigue. Bien.\"\n\n"
                    "\"Te leí. Me llevó tiempo porque traes equipaje. Mucho equipaje.\"\n\n"
                    "¿Qué haces mientras te lee?"
                ),
                "options": [
                    {
                        "label": "[DEFAULT] Escuchar sin hablar — dejar que termine",
                        "response_text": (
                            "MICTLANTECUHTLI:\n"
                            "\"Quieto. El de dos sangres también se quedó quieto.\n"
                            "Ustedes aprenden de él o aprenden solos.\n"
                            "Cualquiera de las dos cosas funciona conmigo.\"\n\n"
                            "\"Ahora hablemos. ¿A qué viniste?\""
                        ),
                        "next_phase": "declaracion",
                    },
                    {
                        "label": "[YAOTL] Yaotl da un paso al frente (requiere aliado de Nivel 6)",
                        "requires_flag_any": ["yaotl_aliado"],
                        "response_text": (
                            "Yaotl, a tu lado, se pone junto a ti.\n\n"
                            "MICTLANTECUHTLI (las luces en sus cuencas cambian):\n"
                            "\"Yaotl. Mi guerrero más viejo. Está aquí. Contigo.\n"
                            "No frente a mí, sino a tu lado.\"\n\n"
                            "MICTLANTECUHTLI: \"Yaotl. Te pregunté hace cuatro siglos\n"
                            "por qué disparabas. No supiste responder.\n"
                            "Vienes hoy con un caminante. ¿Tienes la respuesta?\"\n\n"
                            "YAOTL (firme):\n"
                            "\"Disparé porque me dijeron que la guerra era eterna.\n"
                            "Hoy sé que no lo era. Hoy descansaré, si me dejas.\n"
                            "Pero antes, acompaño a este. Le debo un canto.\"\n\n"
                            "MICTLANTECUHTLI (pausa larga):\n"
                            "\"Yaotl no se mueve por nadie. Que se mueva por ti\n"
                            "dice más de ti que toda tu dualidad junta.\"\n\n"
                            "\"Hablemos. ¿A qué viniste?\""
                        ),
                        "sets_flag": "nivel9_yaotl_testimonio",
                        "nah_delta": 1,
                        "next_phase": "declaracion",
                    },
                    {
                        "label": "[ITZCUINTLI COMBATE] \"Ya hablé con Itzcuintli.\" (requiere combate ganado)",
                        "requires_flag_any": ["itzcuintli_herido"],
                        "response_text": (
                            "MICTLANTECUHTLI (las luces se intensifican un momento):\n"
                            "\"Heriste a Itzcuintli.\"\n\n"
                            "Pausa larga, fría.\n\n"
                            "\"Itzcuintli es viejo. Más viejo que yo, en algunos sentidos.\n"
                            "Lo he visto pelear con cientos. Pocos lo tocaron. Tú lo tocaste.\"\n\n"
                            "\"No sé si admirarte o tenerte rabia.\n"
                            "Probablemente las dos cosas.\n"
                            "Pero estás parado frente a mí con la herida de su zarpa en el hombro\n"
                            "y eso te hace serio. Vamos a hablar como serios.\"\n\n"
                            "\"¿A qué viniste?\""
                        ),
                        "esp_delta": 1,
                        "sets_flag": "nivel9_guerrero_probado",
                        "next_phase": "declaracion",
                    },
                    {
                        "label": "[ITZCUINTLI DIPLOMACIA] \"Itzcuintli me bendijo.\" (requiere diplomacia)",
                        "requires_flag_any": ["itzcuintli_bendicion", "chantico_en_memoria"],
                        "response_text": (
                            "MICTLANTECUHTLI:\n"
                            "\"Itzcuintli te bendijo. Eso le pasa... nunca.\n"
                            "Lo último fue hace cuatrocientos años, con el de dos sangres.\n"
                            "Y solo a medias.\"\n\n"
                            "\"Y no solo eso: despertaste a Chantico. Mi gata.\n"
                            "La hermana menor de Itzcuintli.\n"
                            "Llevaba siglos durmiendo. Yo la creía perdida.\n"
                            "Tú la levantaste.\"\n\n"
                            "MICTLANTECUHTLI:\n"
                            "\"Caminante, me obligas a recalibrar quién eres.\"\n\n"
                            "\"¿A qué viniste?\""
                        ),
                        "nah_delta": 1,
                        "sets_flag": "nivel9_bendicion_reconocida",
                        "next_phase": "declaracion",
                    },
                ],
            },

            # ── PARTE 3 — Las tres declaraciones ────────────────────────────
            "declaracion": {
                "text": (
                    "MICTLANTECUHTLI:\n"
                    "\"Ahora hablemos. ¿A qué viniste?\"\n\n"
                    "El polvo blanco vuelve a caer en su mano."
                ),
                "options": [
                    {
                        "label": "[1] \"Vengo por las almas tomadas antes de tiempo.\"",
                        "response_text": (
                            "MICTLANTECUHTLI:\n"
                            "\"Almas. ¿Cuáles, caminante? Aquí tengo millones.\n"
                            "Llevo aquí desde antes de que tu lengua tuviera nombre.\n"
                            "Niños recién nacidos. Viejos que esperaron mucho.\n"
                            "Madres que no terminaron de criar.\"\n\n"
                            "\"¿Cuáles 'antes de tiempo' me reclamas?\"\n\n"
                            "JUGADOR: \"Las que se llevaron las grietas. Las que cruzaron sin morir realmente.\"\n\n"
                            "MICTLANTECUHTLI:\n"
                            "\"Las grietas. Sí. Esas almas las cuento. Las llevo apuntadas.\n"
                            "Y sí, son injustas. Lo sé.\n"
                            "Pero las grietas no las hice yo. Para resolverlo tendrás que entender\n"
                            "por qué se abren. Y eso, mi querido caminante, es lo que el acertijo final\n"
                            "preguntará. Si llegas. Si pasas todo lo que falta.\"\n\n"
                            "\"Pero antes de seguir con eso, hablemos de él. De Diego.\n"
                            "Porque tarde o temprano vas a preguntar.\"\n"
                            "\"Pregunta.\""
                        ),
                        "sets_flag": "declaracion_almas",
                        "next_phase": "preguntas_diego",
                    },
                    {
                        "label": "[2] \"Diego Xólotl de Guzmán. ¿Dónde está?\"",
                        "response_text": (
                            "MICTLANTECUHTLI (silencio incómodo):\n"
                            "\"Ah. Diego. Entonces eres TÚ. El que venía después.\n"
                            "Me preguntaba cuándo aparecerías.\"\n\n"
                            "\"He estado contando. Cincuenta años. Todos los días.\n"
                            "Sabía que vendría alguien. Lo que no sabía era qué clase.\n"
                            "Y veo que viniste con armas, con espíritu, con preguntas.\"\n\n"
                            "\"Está aquí. Por supuesto. Está aquí desde que cerró las grietas\n"
                            "anteriores y se quedó como tapa para que no se volvieran a abrir\n"
                            "tan pronto. Lo que no funcionó: se abrieron igual.\n"
                            "Diego está aquí, abajo. Sentado donde nadie lo molesta. Esperando.\"\n\n"
                            "\"Esperándote, supongo. Aunque él no lo dijo así.\n"
                            "Él dijo: 'esperando que pase el tiempo'. Pero el tiempo aquí no pasa.\n"
                            "Así que algo sí esperaba. Y resultaste ser tú.\"\n\n"
                            "\"Pregunta.\""
                        ),
                        "sets_flag": "declaracion_diego",
                        "next_phase": "preguntas_diego",
                    },
                    {
                        "label": "[3] \"Las puertas. Necesito cerrarlas.\"",
                        "response_text": (
                            "MICTLANTECUHTLI (el polvo blanco se forma en una columna que no cae):\n"
                            "\"Las puertas. Hablemos de las puertas, entonces.\n"
                            "¿Sabes cómo se hicieron, caminante? No las hice yo.\n"
                            "Las hicimos entre tres: yo, tu lado del mundo,\n"
                            "y el equilibrio mismo, que no es un dios pero a veces hace de dios.\"\n\n"
                            "\"Las puertas no son una protección. Son una limitación.\n"
                            "Una limitación impuesta por miedo.\n"
                            "Miedo de los vivos a los muertos. Miedo de los muertos a los vivos.\n"
                            "Miedo de los dos lados a mezclarse demasiado.\"\n\n"
                            "\"Pero antes de seguir con eso, hablemos de Diego.\n"
                            "Porque tarde o temprano vas a preguntar. Pregunta.\""
                        ),
                        "sets_flag": "declaracion_puertas",
                        "next_phase": "preguntas_diego",
                    },
                ],
            },

            # ── PARTE 4 — Las tres preguntas sobre Diego ─────────────────────
            "preguntas_diego": {
                "text": (
                    "MICTLANTECUHTLI aguarda. El polvo blanco juega entre sus dedos.\n\n"
                    "¿Qué preguntas sobre Diego?"
                ),
                "options": [
                    {
                        "label": "[1] \"¿Qué le hiciste?\"",
                        "response_text": (
                            "MICTLANTECUHTLI:\n"
                            "\"¿Qué le hice?\"\n"
                            "\"Nada. Él tomó una decisión. La más estúpida y valiente\n"
                            "que he visto en mil años.\"\n\n"
                            "\"Diego entró aquí hace cincuenta años buscando el alma de una niña.\n"
                            "Ana. Tenía siete años. Murió de fiebre.\n"
                            "Un tzitzimitl la trajo sin permiso. Diego vino a recuperarla.\"\n\n"
                            "\"Yo le propuse el acertijo. Él lo resolvió.\n"
                            "Eso lo cuentas en los pueblos. Lo que no cuentan:\n"
                            "después del acertijo, Diego — en lugar de irse con Ana —\n"
                            "se quedó parado donde tú estás ahora. Y me dijo:\n"
                            "'Las grietas se van a abrir otra vez en cincuenta años.\n"
                            "Lo sé. Tú lo sabes. Necesito que aguanten más. Me quedo de tapón.'\"\n\n"
                            "\"Yo le respondí: 'Si te quedas de tapón, no vuelves a tu pueblo.\n"
                            "No envejeces. No mueres como los hombres deben morir.\n"
                            "Te quedas aquí — vivo en la frontera — hasta que las grietas\n"
                            "se abran de todos modos. Cosa que pasará.'\"\n\n"
                            "\"Diego dijo: 'Lo sé. Lo acepto. En cincuenta años, alguien va a venir.\n"
                            "Y ese alguien quizá sí cure el agujero.'\"\n\n"
                            "MICTLANTECUHTLI (despacio):\n"
                            "\"Tú eres ese alguien.\""
                        ),
                        "sets_flag": "pregunta_que_le_hiciste",
                        "next_phase": "encuentro_diego",
                    },
                    {
                        "label": "[2] \"¿Está vivo?\"",
                        "response_text": (
                            "MICTLANTECUHTLI (pausa):\n"
                            "\"Esa es la pregunta correcta. Y la respuesta:\n"
                            "depende de cómo definas 'vivo'.\"\n\n"
                            "\"Su corazón late. Lo escucho desde donde estoy.\n"
                            "Su sangre corre. Sus ojos miran y ven.\n"
                            "Si lo tocas — y dudo que se deje — sentirías calor.\"\n\n"
                            "\"Pero no envejece. No se cansa. No duerme.\n"
                            "Está vivo en el sentido animal de la palabra,\n"
                            "pero no en el sentido humano.\n"
                            "Los humanos viven de cambiar. Diego no cambia hace cincuenta años.\n"
                            "Lleva cincuenta años siendo el mismo hombre del día que entró.\n"
                            "Y eso, caminante, no es vida. Es algo más.\"\n\n"
                            "\"Algo que él aceptó a sabiendas. No lo engañé.\n"
                            "Le dije: 'Esto que vas a hacer es peor que morir'.\n"
                            "Él dijo: 'Lo sé. Lo hago igual'.\"\n\n"
                            "\"Lo más honesto es decir: Diego no está vivo ni muerto.\n"
                            "Diego está EN DEUDA. Cargando una deuda con el equilibrio.\n"
                            "Hasta que tú vengas — y aquí estás — a relevarlo o a no relevarlo.\""
                        ),
                        "sets_flag": "pregunta_esta_vivo",
                        "next_phase": "encuentro_diego",
                    },
                    {
                        "label": "[3] \"¿Está aquí?\"",
                        "response_text": (
                            "MICTLANTECUHTLI:\n"
                            "\"Aquí mismo. En este nivel. A no más de doscientos pasos.\"\n\n"
                            "Levanta el brazo izquierdo — no con un dedo, con toda la mano\n"
                            "abierta — hacia el lado izquierdo del salón.\n\n"
                            "MICTLANTECUHTLI:\n"
                            "\"Por allá. Detrás de la quinta columna de huesos contando desde aquí.\n"
                            "Hay un claro. Una pequeña hoguera que él mantiene encendida.\n"
                            "Y junto a la hoguera, sentado en una piedra, él.\"\n\n"
                            "\"No mira hacia acá. Nunca mira hacia este trono.\n"
                            "Lleva cincuenta años sin mirar hacia aquí. Mira siempre el fuego.\"\n\n"
                            "\"Sabe que estás aquí. Te oyó bajar la escalera.\n"
                            "Ha estado oyendo cruzar los niveles, uno por uno.\n"
                            "Pero no se ha levantado. Está esperando que vayas tú.\"\n\n"
                            "MICTLANTECUHTLI: \"Xochitl no puede ir contigo.\"\n"
                            "XOCHITL (sobresalto): \"¿Qué?\"\n"
                            "MICTLANTECUHTLI: \"Si te ve junto al caminante, habla a ti primero.\n"
                            "Y eso no le sirve al caminante. Espérate aquí.\n"
                            "Diego va a verte después. Te lo prometo.\"\n"
                            "XOCHITL (mirándote): \"Ve. Yo me espero.\""
                        ),
                        "sets_flag": "pregunta_esta_aqui",
                        "next_phase": "encuentro_diego",
                    },
                ],
            },

            # ── PARTE 5 — Encuentro con Diego ────────────────────────────────
            "encuentro_diego": {
                "text": (
                    "NARRADOR: Dejas el trono atrás. Caminas hacia el lado izquierdo del salón,\n"
                    "contando columnas. Una. Dos. Tres. Cuatro. Cinco.\n\n"
                    "Detrás de la quinta columna: un claro redondo con suelo de obsidiana\n"
                    "ligeramente menos pulido que el resto, como si alguien lo hubiera\n"
                    "caminado muchas veces y lo hubiera gastado a su gusto.\n\n"
                    "En el centro, una hoguera. Las llamas son de un color que no existe\n"
                    "en el mundo de arriba — entre azul y blanco, sin calor pero con luz.\n\n"
                    "Junto a la hoguera, sentado en una piedra: un hombre.\n"
                    "Manos entre las rodillas. Cabeza inclinada. Pelo largo, gris,\n"
                    "atado con cuero. Camisa que algún día fue blanca. Botas gastadas.\n"
                    "En el cinturón: una vaina vacía. La espada que le correspondía la cargas tú.\n\n"
                    "NARRADOR: Diego.\n\n"
                    "No se levanta. Habla sin levantar la cabeza — voz rasposa, guardada décadas:\n\n"
                    "DIEGO: \"Llegaste. Pasa. Siéntate.\n"
                    "Hay otra piedra del otro lado de la hoguera. La puse hace cuarenta años.\n"
                    "Por si acaso.\"\n\n"
                    "Hay, en efecto, otra piedra. Te sientas. La hoguera entre los dos.\n\n"
                    "DIEGO (finalmente levanta la mirada):\n"
                    "\"Eres más joven de lo que esperaba. Pero todos son siempre más jóvenes\n"
                    "de lo que uno esperaba, ¿no? Cuando uno se queda quieto cincuenta años,\n"
                    "el resto del mundo le parece niño.\"\n\n"
                    "¿Qué respondes?"
                ),
                "options": [
                    {
                        "label": "[1] \"¿Cómo sabías que vendría alguien?\"",
                        "response_text": (
                            "DIEGO:\n"
                            "\"Las grietas. Las cuento. Cuando la quinta vibración\n"
                            "me llegó al pecho, supe que el techo aguantaba pero ya no por mucho.\n"
                            "Calculé: cincuenta años son cincuenta años.\n"
                            "Alguien tendría que venir.\""
                        ),
                        "next_phase": "diego_revelacion",
                    },
                    {
                        "label": "[2] \"¿Cómo sabías que sería yo?\"",
                        "response_text": (
                            "DIEGO:\n"
                            "\"No sabía que serías tú. No sabía qué cara ibas a tener.\n"
                            "Pero sí sabía algunas cosas:\n"
                            "Que cargarías mi sangre — porque las grietas se atan a la sangre\n"
                            "del que las tapa. Que cargarías mi espada — porque las armas\n"
                            "reconocen a sus dueños y vuelven a la familia.\n"
                            "Y que cargarías un dolor mío — porque mis dolores\n"
                            "no se mueren conmigo si me quedo aquí. Se trasladan.\n"
                            "Lo siento por eso.\""
                        ),
                        "next_phase": "diego_revelacion",
                    },
                    {
                        "label": "[3] [Silencio] Sostener la mirada sin hablar",
                        "response_text": (
                            "Sostienes la mirada.\n\n"
                            "Pasa un tiempo largo. Diego no la aparta.\n\n"
                            "DIEGO (al fin):\n"
                            "\"Buen silencio. No me lo esperaba.\n"
                            "Casi todos los que se sientan en esa piedra empiezan a hablar.\n"
                            "Algunos lloran. Algunos me gritan. Tú esperas. Diferente.\""
                        ),
                        "nah_delta": 1,
                        "next_phase": "diego_revelacion",
                    },
                ],
            },

            # ── La revelación de Diego ────────────────────────────────────────
            "diego_revelacion": {
                "text": (
                    "DIEGO:\n"
                    "\"Voy a contarte lo que no se cuenta en los pueblos.\n"
                    "No porque tenga miedo de que se sepa.\n"
                    "Sino porque ya no me sirve guardarlo. Y a ti puede servirte oírlo.\"\n\n"
                    "DIEGO (mirando el fuego frío):\n"
                    "\"Ana. La niña que vine a recuperar hace cincuenta años. La recuperé.\n"
                    "Pero no era la primera niña que perdí. Era la cuarta.\n"
                    "Las primeras tres no las pude salvar. Una se llamaba Tonantzin.\n"
                    "Otra Luz. La tercera no llegué a saber su nombre.\"\n\n"
                    "\"Ana fue mi cuarta oportunidad. La tomé. Pero llegué a esta escalera\n"
                    "con cuatro pesos en la espalda, no con uno.\n"
                    "Mictlantecuhtli me ofreció el acertijo. Lo resolví.\n"
                    "Pero antes de irme, miré hacia arriba y me dije:\n"
                    "'Si subo, voy a vivir treinta o cuarenta años más.\n"
                    "Y en esos años van a morir más Anas, más Tonantzines.\n"
                    "Porque las grietas siguen. Porque yo solo cerré una.'\"\n\n"
                    "\"Y me quedé.\"\n\n"
                    "DIEGO (pausa):\n"
                    "\"No fue heroísmo. Fue cobardía, casi. Cobardía de subir y ver\n"
                    "la siguiente Ana morir y no poder hacer nada.\n"
                    "Cincuenta años pensando esto. La conclusión: en parte fue heroísmo\n"
                    "y en parte fue cobardía. Como casi todo lo importante que hace un hombre.\"\n\n"
                    "¿Qué respondes?"
                ),
                "options": [
                    {
                        "label": "[1] \"Eso lo entiendo.\"",
                        "response_text": (
                            "DIEGO:\n"
                            "\"Bueno. Que alguien lo entienda — aunque sea uno solo —\n"
                            "me quita peso. Gracias.\""
                        ),
                        "next_phase": "diego_pedido",
                    },
                    {
                        "label": "[2] \"No lo entiendo. Pero te creo.\"",
                        "response_text": (
                            "DIEGO:\n"
                            "\"Honesto. Mejor que entender es creer.\n"
                            "El que entiende a veces se cree con derecho a opinar.\n"
                            "El que cree solo te acompaña.\n"
                            "Eso te lo agradezco más.\""
                        ),
                        "nah_delta": 1,
                        "next_phase": "diego_pedido",
                    },
                    {
                        "label": "[3] \"¿Y Xochitl?\"",
                        "response_text": (
                            "DIEGO (el rostro se le endurece, no por enojo, por culpa):\n"
                            "\"Ah. Eso. Sí. Ibas a llegar ahí.\"\n\n"
                            "\"Hace cincuenta años, en una pelea distinta, en un templo distinto —\n"
                            "un tzitzimitl me agarró a Xochitl.\n"
                            "Y otro tzitzimitl, más grande, iba al pueblo.\n"
                            "Yo escogí. Fui por el grande.\n"
                            "El que tenía a Xochitl la mató mientras yo no estaba.\"\n\n"
                            "\"Eso no se cuenta tampoco. Para el pueblo, fui héroe — salvé el pueblo.\n"
                            "Para mí, fui asesino — dejé morir a la niña que confiaba en mí.\"\n\n"
                            "\"He cargado eso cincuenta años. La cargo todavía.\"\n\n"
                            "DIEGO (pausa):\n"
                            "\"Subió contigo, ¿verdad? ¿Qué le dijiste?\"\n\n"
                            "JUGADOR: \"Le dije la verdad. Que el Mictlán te tenía.\n"
                            "No le mentí.\"\n\n"
                            "DIEGO:\n"
                            "\"Gracias por eso. Yo no fui capaz de decírselo en su momento.\n"
                            "Cobardía, otra vez.\""
                        ),
                        "sets_flag": "diego_hablo_xochitl",
                        "nah_delta": 1,
                        "next_phase": "diego_pedido",
                    },
                ],
            },

            # ── La petición de Diego ─────────────────────────────────────────
            "diego_pedido": {
                "text": (
                    "DIEGO (después de un silencio largo):\n"
                    "\"Caminante.\"\n\n"
                    "\"Mictlantecuhtli te va a hacer un acertijo.\n"
                    "El mismo formato del que me hizo a mí, pero pregunta distinta.\n"
                    "La pregunta esta vez es sobre las puertas — por qué se debilitan.\"\n\n"
                    "\"Antes de que vayas y respondas, quiero pedirte una cosa.\"\n\n"
                    "\"No respondas pensando en mí.\n"
                    "No respondas para liberarme, ni para reemplazarme, ni para honrarme.\n"
                    "Responde pensando en lo que tú entendiste de los nueve niveles.\n"
                    "Lo que tú aprendiste. Lo que tú quieres para los pueblos de arriba.\"\n\n"
                    "\"Si tu respuesta me libera, bien. Si no, también bien.\n"
                    "Llevo cincuenta años aquí. Cincuenta más no es mucho más.\n"
                    "Pero si tu respuesta te traiciona a ti — para honrarme a mí —\n"
                    "entonces no aprendiste nada del Mictlán.\n"
                    "Y mi sacrificio no sirvió.\"\n\n"
                    "\"¿Lo prometes?\"\n\n"
                    "¿Qué respondes?"
                ),
                "options": [
                    {
                        "label": "[1] \"Lo prometo.\"",
                        "response_text": (
                            "DIEGO:\n"
                            "\"Bien. Una promesa. Siempre se cobran.\n"
                            "Esta también, pero la cobro yo, no Mictlantecuhtli.\n"
                            "Y la cobro suavemente.\""
                        ),
                        "sets_flag": "promesa_a_diego",
                        "nah_delta": 1,
                        "next_phase": "despedida_diego",
                    },
                    {
                        "label": "[2] \"No te puedo prometer eso. Voy a pensar en ti igual.\"",
                        "response_text": (
                            "DIEGO:\n"
                            "\"Honesto. Como tú decidas pensar en mí, lo aguantaré.\n"
                            "Pero por favor — te lo pido sin compromiso —\n"
                            "no decidas algo que detestes a largo plazo solo por mi memoria.\n"
                            "La memoria pesa, pero no debe gobernar.\""
                        ),
                        "next_phase": "despedida_diego",
                    },
                    {
                        "label": "[3] \"Lo intentaré.\"",
                        "response_text": (
                            "DIEGO:\n"
                            "\"Intentar es lo único que pedimos los muertos.\n"
                            "Los vivos siempre intentan. Algunos hasta lo logran. Bien.\""
                        ),
                        "sets_flag": "compromiso_parcial_diego",
                        "next_phase": "despedida_diego",
                    },
                    {
                        "label": "[XOCHITL] Xochitl te toca el brazo antes de responder",
                        "requires_flag_any": ["compromiso_amor"],
                        "response_text": (
                            "Xochitl aparece junto a ti — Mictlantecuhtli la dejó acercarse.\n\n"
                            "DIEGO (mirándola, sin palabras al principio):\n"
                            "\"...\"\n"
                            "DIEGO: \"Hola, Xochitl.\"\n"
                            "XOCHITL (firme, mirándolo): \"Hola, Diego.\"\n\n"
                            "Un silencio que tiene cincuenta años dentro.\n\n"
                            "XOCHITL (a ti, sin dejar de mirar a Diego):\n"
                            "\"Lo que prometiste — recuérdalo ahora.\n"
                            "Sea lo que sea que él te pida.\"\n\n"
                            "DIEGO (despacio):\n"
                            "\"Le prometiste algo.\"\n"
                            "JUGADOR: \"Sí.\"\n"
                            "DIEGO: \"Bien. Eso... eso está bien.\n"
                            "Yo no se lo prometí nunca. Tú sí. Eso te hace mejor.\"\n\n"
                            "\"Entonces: ¿lo prometes?\""
                        ),
                        "sets_flags": ["promesa_a_diego", "reencuentro_diego_xochitl"],
                        "nah_delta": 2,
                        "next_phase": "despedida_diego",
                    },
                ],
            },

            # ── Despedida de Diego ────────────────────────────────────────────
            "despedida_diego": {
                "text": (
                    "DIEGO (se levanta — por primera vez en cincuenta años):\n\n"
                    "NARRADOR: No es metáfora. Son cincuenta años.\n"
                    "Se levanta despacio, como quien recuerda cómo era ser cuerpo.\n"
                    "Estira los brazos. Mira sus manos como si no las reconociera.\n\n"
                    "DIEGO:\n"
                    "\"Vete. Está esperándote allá.\n"
                    "Haz tu parte. Yo me quedo aquí — por última vez quiero dejar\n"
                    "la hoguera apagándose sola, sin que la apague yo.\n"
                    "Después subo. Sea cual sea tu decisión.\"\n\n"
                    "¿Cómo te despides?"
                ),
                "options": [
                    {
                        "label": "[1] \"Gracias.\"",
                        "response_text": (
                            "DIEGO:\n"
                            "\"Por nada. Y también — gracias a ti, por venir.\n"
                            "La espera fue la parte más dura.\""
                        ),
                        "next_phase": "regreso_trono",
                    },
                    {
                        "label": "[2] \"Hasta luego, Diego.\"",
                        "response_text": (
                            "DIEGO:\n"
                            "\"Hasta luego. Si todo sale bien, en breve.\n"
                            "Si no, también, pero más tarde.\""
                        ),
                        "next_phase": "regreso_trono",
                    },
                    {
                        "label": "[3] Darle la mano antes de irte",
                        "response_text": (
                            "Extiendes la mano.\n\n"
                            "Diego la mira un momento — como si no estuviera seguro\n"
                            "de que funcionara todavía. Luego la estrecha.\n\n"
                            "Su mano está caliente. Viva. Real.\n\n"
                            "DIEGO (muy bajo):\n"
                            "\"...\"\n\n"
                            "\"Ojalá Xochitl me hubiera dado esa mano alguna vez.\n"
                            "Pero no se la pedí cuando podía.\n"
                            "Tú la pediste a tu Xochitl. Mejor.\""
                        ),
                        "sets_flag": "apretón_mano_diego",
                        "nah_delta": 1,
                        "next_phase": "regreso_trono",
                    },
                ],
            },

            # ── Regreso al trono ─────────────────────────────────────────────
            "regreso_trono": {
                "text": (
                    "NARRADOR: Te levantas. Caminas de regreso al trono.\n"
                    "Cuentas las columnas al revés. Cinco. Cuatro. Tres. Dos. Una.\n\n"
                    "Mictlantecuhtli no se ha movido.\n"
                    "El polvo blanco sigue jugando entre sus dedos.\n"
                    "Xochitl está parada — no flotando, parada — al lado del trono,\n"
                    "esperándote. Algo en ella ha cambiado, aunque no sabes qué.\n\n"
                    "XOCHITL (muy bajo, solo para ti): \"¿Cómo te fue?\"\n\n"
                    "¿Qué dices?"
                ),
                "options": [
                    {
                        "label": "[1] \"Es persona. Ya no es leyenda.\"",
                        "response_text": (
                            "XOCHITL:\n"
                            "\"Sí. A mí también me pasó eso, pero hace cincuenta años.\n"
                            "Bienvenido a verlo como humano.\"\n\n"
                            "MICTLANTECUHTLI:\n"
                            "\"Caminante. Lo viste. Hablaste. Sentiste lo que tenías que sentir.\n"
                            "Bien. Ahora, si me permites, vuelvo a mi función. Acertijo.\""
                        ),
                        "next_phase": "decision_previa",
                    },
                    {
                        "label": "[2] \"Me pidió algo. Que no decida por él.\"",
                        "response_text": (
                            "XOCHITL:\n"
                            "\"Los que han estado mucho tiempo solos siempre piden algo.\n"
                            "Espero que sea algo que puedas darle.\"\n\n"
                            "MICTLANTECUHTLI:\n"
                            "\"Caminante. Lo viste. Lo que Diego te pidió — eso es tuyo.\n"
                            "Yo no intervengo ahí. Pero sí me concierne lo siguiente.\n"
                            "Acertijo.\""
                        ),
                        "next_phase": "decision_previa",
                    },
                    {
                        "label": "[3] \"Después te cuento. Ahora viene el acertijo.\"",
                        "response_text": (
                            "XOCHITL:\n"
                            "\"Después. Sí. Ve.\"\n\n"
                            "MICTLANTECUHTLI (algo en la postura cambia — casi aprobación):\n"
                            "\"El vivo que enfoca. Bien. Acertijo.\""
                        ),
                        "esp_delta": 1,
                        "next_phase": "decision_previa",
                    },
                ],
            },

            # ── PARTE 6 — Decisión previa al acertijo ────────────────────────
            "decision_previa": {
                "text": (
                    "MICTLANTECUHTLI:\n"
                    "\"Pero antes del acertijo, una decisión preliminar.\n"
                    "Acabas de verlo. Hablaron. Saliste con una postura.\n"
                    "Necesito saber con cuál te quedas.\"\n\n"
                    "¿Qué quieres ahora con respecto a Diego?"
                ),
                "options": [
                    {
                        "label": "[1] \"Quiero que descanse. Que salga de aquí.\"",
                        "response_text": (
                            "MICTLANTECUHTLI:\n"
                            "\"Para que Diego deje de estar aquí, hay tres caminos.\n"
                            "Uno: alguien lo reemplaza — tú.\n"
                            "Dos: la grieta se cura de raíz — eso requiere entender\n"
                            "por qué se abre, y eso es el acertijo.\n"
                            "Tres: aceptamos que la grieta va a abrirse\n"
                            "y aprendemos a vivir con eso.\"\n\n"
                            "\"La uno es tu sacrificio. La dos es el balance. La tres es la liberación.\n"
                            "Tu pregunta orienta cómo te presento las opciones.\n"
                            "El acertijo decide cuál tomas.\""
                        ),
                        "sets_flag": "prioridad_liberar_diego",
                        "next_phase": "acertijo",
                    },
                    {
                        "label": "[2] \"Quiero entender qué opciones existen realmente.\"",
                        "response_text": (
                            "MICTLANTECUHTLI:\n"
                            "\"Mmm. Esa respuesta no esperaba.\n"
                            "Diego ya tenía la respuesta antes de bajar.\n"
                            "Tú vienes con la pregunta abierta. Eso es muy distinto.\"\n\n"
                            "\"Te voy a decir lo que yo veo, después de tantos siglos:\n"
                            "las puertas son un parche. Mal puesto. Mal pensado.\n"
                            "Lo que hace falta no es cerrarlas mejor.\n"
                            "Lo que hace falta es entender por qué las pusimos.\n"
                            "Y, si encontramos el por qué — y si vemos que ya no aplica — quitarlas.\"\n\n"
                            "\"Pero eso es lo más difícil de todo.\n"
                            "Más difícil que cerrarlas mejor. Mucho más.\n"
                            "El acertijo te lo explica. Escucha bien.\""
                        ),
                        "sets_flag": "prioridad_entender",
                        "nah_delta": 1,
                        "next_phase": "acertijo",
                    },
                    {
                        "label": "[3] \"Quiero lo que sea mejor para los pueblos de arriba.\"",
                        "response_text": (
                            "MICTLANTECUHTLI (pausa):\n"
                            "\"Los pueblos.\"\n\n"
                            "\"No Diego. No tú. Los pueblos.\"\n\n"
                            "Una pausa que se siente larga, y termina con algo\n"
                            "que podría interpretarse como respeto.\n\n"
                            "MICTLANTECUHTLI:\n"
                            "\"Diego siempre pensó en los pueblos. Pero tú lo dices diferente.\n"
                            "Diego decía: 'proteger a los pueblos'. Tú dices: 'lo mejor para ellos'.\n"
                            "La diferencia es sutil y es todo.\n"
                            "Proteger implica que están en peligro. Mejorar implica que pueden crecer.\"\n\n"
                            "\"Escucha el acertijo con eso en mente.\""
                        ),
                        "sets_flag": "prioridad_pueblos",
                        "nah_delta": 1,
                        "next_phase": "acertijo",
                    },
                ],
            },

            # ── PARTE 7 — El acertijo final ──────────────────────────────────
            "acertijo": {
                "text": (
                    "MICTLANTECUHTLI (el polvo blanco sube en una columna\n"
                    "que toma la forma de una puerta antigua de madera carcomida):\n\n"
                    "\"Una pregunta. La que des decide el final de tu visita —\n"
                    "y el destino del de dos sangres.\"\n\n"
                    "\"No hay segunda oportunidad.\"\n\n"
                    "\"Pregunta:\"\n\n"
                    "\"¿Por qué las puertas se debilitan cada cincuenta años?\""
                ),
                "options": [
                    {
                        "label": "[1] \"Porque los vivos olvidan a los muertos.\"",
                        "response_text": (
                            "MICTLANTECUHTLI (pausa larga):\n"
                            "\"Bien. No es la respuesta canónica. Pero tampoco es errada.\"\n\n"
                            "\"Los vivos olvidan a los muertos. Es verdad.\n"
                            "Cada cincuenta años, los nietos de los nietos ya no recuerdan\n"
                            "los nombres de los antepasados. Los altares de Día de Muertos\n"
                            "se llenan de fotos, pero las fotos pierden caras con el tiempo.\n"
                            "Los nombres se borran de las lápidas. Las historias se cuentan menos.\n"
                            "Y cuando los muertos pierden su ancla en el recuerdo de los vivos,\n"
                            "las puertas pierden tensión. Se debilitan. Se agrietan.\"\n\n"
                            "\"Tu respuesta es nahua. Profundamente nahua.\n"
                            "La nuestra siempre fue una cultura de memoria, de ofrenda,\n"
                            "de mantener los nombres vivos.\"\n\n"
                            "\"Esta respuesta lleva al camino de la liberación con condiciones.\n"
                            "Diego sube contigo. Fundan una escuela de memoria.\n"
                            "Cada cincuenta años, los nuevos guardianes recuerdan a los muertos\n"
                            "por nombre. Las grietas se mantienen pequeñas. No se cierran.\n"
                            "No se abren del todo. Solo se contienen.\"\n\n"
                            "XOCHITL (al oír esto, en voz muy baja): \"Podría funcionar.\"\n\n"
                            "MICTLANTECUHTLI: \"¿Aceptas este camino?\"\n\n"
                            "JUGADOR: \"Sí. Los pueblos van a recordar.\"\n\n"
                            "MICTLANTECUHTLI (y algo en el salón cambia — las columnas\n"
                            "de hueso vibran, un solo tono bajo, como aprobación de los muertos):\n"
                            "\"Entonces ve. Diego te sigue.\""
                        ),
                        "sets_flags": ["eleccion_final_c", "acertijo_olvido"],
                        "nah_delta": 2,
                        "next_phase": None,
                    },
                    {
                        "label": "[2] \"Porque los muertos envidian a los vivos.\"",
                        "response_text": (
                            "MICTLANTECUHTLI (la luz en sus cuencas se apaga un instante, luego vuelve):\n"
                            "\"Mmm.\"\n\n"
                            "\"Esa respuesta la he oído. No es la primera vez.\n"
                            "Pero es errada — al menos parcialmente.\n"
                            "Los muertos no envidian a los vivos. Los muertos extrañan a los vivos.\n"
                            "Quien envidia quiere lo del otro. Quien extraña recuerda lo propio\n"
                            "que ya no tiene. Son emociones distintas.\"\n\n"
                            "\"Pero tu respuesta apunta a algo cierto: hay tensión entre los dos lados.\n"
                            "Los muertos quieren — algunos quieren — volver.\n"
                            "Los vivos quieren controlar. Esa tensión existe.\"\n\n"
                            "\"Tu respuesta dice 'los muertos quieren lo de los vivos'.\n"
                            "La única forma de calmar a los muertos en esa lógica\n"
                            "es darles a uno de los vivos. Tú.\"\n\n"
                            "\"Es el camino del sacrificio. Tu lugar aquí.\n"
                            "Diego sube. Tú te quedas. Guardián nuevo, tapa nueva.\n"
                            "Las puertas aguantan otros cincuenta años, quizás más.\"\n\n"
                            "XOCHITL (muy quieta): \"...\"\n\n"
                            "JUGADOR: \"Acepto. Yo me quedo.\"\n\n"
                            "MICTLANTECUHTLI:\n"
                            "\"Entonces el contrato es tuyo.\n"
                            "Diego va a discutir — siempre discute. Pero va a aceptar.\n"
                            "Porque sabe que no tienes miedo. Y el miedo es lo que\n"
                            "hace que los guardianes fallen a la larga.\"\n\n"
                            "MICTLANTECUHTLI: \"Bienvenido al Mictlán, guardián.\""
                        ),
                        "sets_flags": ["eleccion_final_a", "acertijo_envidia"],
                        "esp_delta": 2,
                        "next_phase": None,
                    },
                    {
                        "label": "[3] \"Porque no debería haber puertas. Ambos mundos son uno.\"",
                        "response_text": (
                            "MICTLANTECUHTLI (pausa muy larga):\n"
                            "\"Sí.\"\n\n"
                            "\"Esa es la respuesta más antigua.\n"
                            "La que solo unos pocos han escuchado en mil años.\n"
                            "Y aún menos han dado.\"\n\n"
                            "\"Las puertas no debilitan porque sí.\n"
                            "Debilitan porque están mal puestas.\n"
                            "Porque vida y muerte no son dos cosas separadas que necesiten frontera.\n"
                            "Son un mismo flujo, con dos modos.\n"
                            "La puerta interrumpe el flujo. El flujo se enoja.\n"
                            "Se debilita la puerta. Cada cincuenta años, el flujo recuerda\n"
                            "que está mal y empuja.\"\n\n"
                            "\"La solución no es reforzar la puerta. Es disolverla.\n"
                            "Hacer que vida y muerte se toquen sin barrera, pero también sin caos.\n"
                            "Un nuevo pacto.\"\n\n"
                            "\"Esta respuesta lleva al camino del balance.\n"
                            "Diego sube contigo. Las puertas se vuelven permeables.\n"
                            "Los dos mundos vuelven a tocarse.\n"
                            "El costo: las tres reliquias de Diego — Tlachicotl, Tonatiuh,\n"
                            "el Escudo Ceiba — quedan aquí. Conmigo. Como sello del nuevo pacto.\"\n\n"
                            "XOCHITL (mirándote, en voz baja):\n"
                            "\"El nuevo pacto. Eso era lo que él hubiera querido si hubiera\n"
                            "podido imaginarlo. Pero solo lo imaginas cuando ya bajaste\n"
                            "los nueve niveles y viste desde adentro.\"\n\n"
                            "JUGADOR: \"Acepto. El pacto nuevo.\"\n\n"
                            "MICTLANTECUHTLI:\n"
                            "\"Las reliquias al trono. Tú al mundo de arriba.\n"
                            "Diego también. Y los dos mundos, juntos, como siempre debieron ser.\"\n\n"
                            "Las columnas de hueso vibran. No de susto. De alivio."
                        ),
                        "sets_flags": ["eleccion_final_b", "acertijo_balance"],
                        "esp_delta": 1, "nah_delta": 1,
                        "next_phase": None,
                    },
                    {
                        "label": "[4] \"Porque el miedo crea las grietas.\"",
                        "response_text": (
                            "MICTLANTECUHTLI (la luz de las cuencas se intensifica):\n"
                            "\"Esa.\"\n\n"
                            "\"Esa es una respuesta que muy pocos vivos han dado.\n"
                            "Y casi ninguno la entendió a fondo cuando la dijo.\"\n\n"
                            "\"El miedo crea las grietas. Sí.\n"
                            "El miedo de los vivos a los muertos. El miedo de los pueblos al Mictlán.\n"
                            "El miedo a que las criaturas crucen. El miedo a que el orden caiga.\n"
                            "Cada miedo tira un golpe pequeño contra las puertas.\n"
                            "Cada cincuenta años, los miedos acumulados ganan.\"\n\n"
                            "\"Las puertas no son la cura para el miedo. Son su síntoma.\n"
                            "Si quieres cerrar las puertas para siempre,\n"
                            "tienes que cerrar el miedo.\n"
                            "Y el miedo no se cierra. El miedo se vive — se entiende —\n"
                            "se acepta — y se transforma.\"\n\n"
                            "\"Esta respuesta requiere más coraje que las otras.\n"
                            "Porque la solución no es construir un muro.\n"
                            "La solución es enseñarle a los pueblos\n"
                            "a no tener miedo del Mictlán.\"\n\n"
                            "\"Si confirmas: Diego sube contigo.\n"
                            "Fundan una escuela de aceptación.\n"
                            "No de memoria — eso fue la respuesta uno.\n"
                            "No de pacto nuevo — eso fue la tres.\n"
                            "Donde se enseña a los vivos que la muerte no es enemiga.\"\n\n"
                            "MICTLANTECUHTLI (pausa muy larga — algo que no habías visto antes:\n"
                            "el polvo blanco cae de su mano y no lo recoge):\n"
                            "\"Yo también les tengo miedo a ustedes.\n"
                            "Llevo siglos teniéndoles miedo.\n"
                            "Por eso esto está como está.\n"
                            "Las puertas las pedimos también nosotros, los muertos.\n"
                            "No solo los vivos.\"\n\n"
                            "XOCHITL (apenas en voz audible): \"Lo dijo. Lo dijo de verdad.\"\n\n"
                            "JUGADOR: \"Entonces los dos aprendemos. Juntos.\"\n\n"
                            "MICTLANTECUHTLI:\n"
                            "\"Entonces los dos aprendemos.\n"
                            "Ve. Diego te sigue.\n"
                            "Y la escuela — yo mando a alguien también.\n"
                            "Para aprender, no para vigilar.\"\n\n"
                            "Algo en el salón cambia. Las columnas de hueso ya no están frías.\n"
                            "Hay calor en el Mictlán — quizás el primero en siglos."
                        ),
                        "sets_flags": ["eleccion_final_c", "acertijo_miedo",
                                       "mictlan_reconoce_miedo", "nivel9_co_maestros"],
                        "nah_delta": 3,
                        "next_phase": None,
                    },
                ],
            },
        },
    },
}
