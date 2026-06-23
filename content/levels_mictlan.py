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

    # ── NIVEL 7 — Corredor del Frío ───────────────────────────────────────────
    "nivel7_corredor": {
        "name": "Itztlan — Corredor del Frío Eterno",
        "description": (
            "El séptimo nivel del Mictlán: un corredor de hielo y silencio. "
            "Las paredes son cristal negro que refleja versiones tuyas "
            "que tomaron otros caminos. Fríos. Quietos. "
            "Al fondo, una grieta de oscuridad total: el octavo nivel."
        ),
        "exits": {"sur": "nivel6_cruce", "norte": "nivel8_entrada"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "cristal":  "Paredes de hielo negro. Cada reflejo muestra una versión diferente de ti.",
            "frio":     "Un frío que no quema — congela los pensamientos en el lugar donde están.",
            "grieta":   "Al norte, la oscuridad del Apochcaloca. Ni luz ni forma. Solo ausencia.",
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
        "exits": {"sur": "nivel7_corredor"},
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
        "name": "Chicnauhmictlan — Antesala del Trono",
        "description": (
            "El noveno nivel. El último. "
            "El trono de cráneos de Mictlantecuhtli se alza al fondo del salón. "
            "Xochitl aprieta tu mano. Diego espera — su forma apenas visible "
            "entre las sombras del techo infinito. "
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
                        "requires_flag_any": ["yaotl_historia_revelada", "caminante_trato", "info_yaotl"],
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

    # ── Nivel 9 — Trono de Mictlantecuhtli (placeholder mínimo) ──────────────
    "nivel9_trono": {
        "name": "Chicnauhmictlan — El Trono",
        "entry_text": (
            "Mictlantecuhtli. El señor de los muertos. Sentado en el trono de cráneos.\n"
            "No te ataca. No habla primero.\n"
            "Solo espera — con la paciencia de quien ha tenido el tiempo eterno para practicarla.\n\n"
            "XOCHITL: \"Aquí estamos. Ahora habla.\""
        ),
        "start_phase": "trono",
        "phases": {
            "trono": {
                "text": (
                    "Mictlantecuhtli:\n"
                    "\"Has llegado hasta aquí. Diego llegó al séptimo nivel. "
                    "Tú llegaste al noveno. Eso merece consideración.\"\n\n"
                    "\"Habla.\"\n\n"
                    "¿Qué le pides?"
                ),
                "options": [
                    {
                        "label": "[A] \"Liberar a Diego. Él cumplió lo que debía.\"",
                        "response_text": (
                            "MICTLANTECUHTLI: \"Diego no cumplió. Se quedó. "
                            "Pero tú llegaste en su lugar. Eso tiene peso.\"\n\n"
                            "Silencio largo.\n\n"
                            "\"Un alma sale. Una entra. Eso es el balance.\"\n"
                            "Sus ojos te miran.\n"
                            "\"¿Estás dispuesto?\"\n\n"
                            "JUGADOR: \"Sí.\"\n\n"
                            "El trono brilla. El final comienza."
                        ),
                        "sets_flag": "eleccion_final_a",
                        "next_phase": None,
                    },
                    {
                        "label": "[B] \"Balance — Xochitl libre, Diego libre, yo de vuelta.\"",
                        "response_text": (
                            "MICTLANTECUHTLI: \"El balance. Diego lo intentó — "
                            "no tenía con qué pagarlo.\"\n"
                            "\"Tú tienes sangre de dos mundos. Eso puede ser el precio.\"\n\n"
                            "\"¿Ofreces tu sangre dual como sello?\"\n"
                            "JUGADOR: \"Sí.\"\n\n"
                            "El trono acepta. Algo en ti cambia — no se pierde, "
                            "pero queda marcado para siempre."
                        ),
                        "sets_flag": "eleccion_final_b",
                        "next_phase": None,
                    },
                    {
                        "label": "[C] \"Liberar a todos los que eligieron quedarse esperando.\"",
                        "requires_flag_any": ["compromiso_amor", "resolucion_liberacion"],
                        "response_text": (
                            "MICTLANTECUHTLI: \"Todos.\"\n"
                            "No es pregunta.\n\n"
                            "\"Ningún vivo ha pedido eso.\"\n\n"
                            "Larga pausa. La más larga.\n\n"
                            "\"Las almas que eligieron esperar pueden elegir de nuevo. "
                            "Esa es la libertad que pides: el derecho a elegir.\"\n\n"
                            "\"El costo es el canto que los dos mundos puedan escuchar.\"\n"
                            "\"¿Tienes esa voz?\"\n\n"
                            "JUGADOR: \"Lo averiguamos.\""
                        ),
                        "sets_flag": "eleccion_final_c",
                        "next_phase": None,
                    },
                ],
            },
        },
    },
}
