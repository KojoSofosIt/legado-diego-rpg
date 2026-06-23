"""World content: rooms, items, creatures, NPCs."""

ROOMS = {
    # ── MUNDO MORTAL ──────────────────────────────────────────────────────────
    "altar_diego": {
        "name": "Altar de Diego",
        "description": (
            "Una choza humilde al borde del pueblo. El olor a copal llena el cuarto. "
            "Sobre un altar de piedra volcánica descansan flores de cempasúchil y una foto "
            "descolorida de un guerrero con dos manchas de sangre en el rostro. "
            "Citlali está sentada junto al fuego, mirándote."
        ),
        "exits": {"norte": "plaza_pueblo", "este": "casa_citlali"},
        "items": [],
        "creatures": [],
        "npcs": ["citlali"],
        "features": {
            "altar":  "Foto de Diego: hombre alto, ojos claros, espada de obsidiana al cinto.",
            "copal":  "Brasas de copal que dibujan espirales que no siguen el viento.",
            "flores": "Cempasúchil fresco. Alguien lo renueva cada día.",
        },
    },

    "plaza_pueblo": {
        "name": "Plaza de Tlacopan",
        "description": (
            "La plaza central. Un ahuehuete centenario da sombra a una fuente seca. "
            "Los vecinos te evitan con la mirada, pero te observan. "
            "Al norte el camino se adentra en las barrancas."
        ),
        "exits": {"sur": "altar_diego", "norte": "camino_barrancas", "este": "mercado"},
        "items": [],
        "creatures": [],
        "npcs": ["rodrigo"],
        "features": {
            "ahuehuete": "El árbol viejo tiene marcas de garras en la corteza — demasiado altas para un perro.",
            "fuente":    "Seca desde hace décadas. En el fondo hay una moneda negra con un cráneo.",
        },
    },

    "casa_citlali": {
        "name": "Casa de Citlali",
        "description": (
            "Estantes hasta el techo con frascos, raíces y cosas que prefieren no nombrarse. "
            "En el centro, sobre un petate, tres objetos aguardan: "
            "una espada de obsidiana, un arcabuz con plumas de quetzal y un escudo de piel de jaguar."
        ),
        "exits": {"oeste": "altar_diego"},
        "items": ["tlachicotl", "tonatiuh", "escudo_ceiba", "copal_sagrado"],
        "creatures": [],
        "npcs": [],
        "features": {
            "espada":  "Tlachicotl. La hoja refleja algo que no está en el cuarto.",
            "arcabuz": "Tonatiuh. Plumas de quetzal descoloridas. Huele a pólvora vieja y copal.",
            "escudo":  "Escudo Ceiba. Piel de jaguar sobre madera sagrada. Emite calor al tocarlo.",
            "frascos": "Docenas de frascos con etiquetas en náhuatl. Citlali sabe exactamente qué hay en cada uno.",
        },
    },

    "mercado": {
        "name": "Mercado del Pueblo",
        "description": (
            "Tres puestos bajo un techo de palma. La vendedora te mira con ojo clínico — "
            "ya sabe quién eres. Tiene hierbas medicinales en el mostrador."
        ),
        "exits": {"oeste": "plaza_pueblo"},
        "items": ["hierbas_curativas"],
        "creatures": [],
        "npcs": ["vendedora"],
        "features": {
            "puestos": "Hierbas, velas, amuletos. Nada de armas — esas las guarda Citlali.",
        },
    },

    "camino_barrancas": {
        "name": "Camino a las Barrancas",
        "description": (
            "El sendero se estrecha y los árboles se cierran sobre tu cabeza. "
            "El aire huele a tierra mojada y a algo metálico, como sangre vieja. "
            "Las barrancas esperan al norte."
        ),
        "exits": {"sur": "plaza_pueblo", "norte": "barrancas_entrada"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "arboles":  "Marcas en la corteza: círculos y espirales que Diego dejó en su tiempo.",
            "sendero":  "Huellas en el barro. Una de ellas tiene forma de mano humana.",
        },
    },

    # ── BARRANCAS DEL COBRE ───────────────────────────────────────────────────
    "barrancas_entrada": {
        "name": "Entrada a las Barrancas",
        "description": (
            "Paredes de roca rojiza se alzan veinte metros a cada lado. "
            "El eco no funciona como debería — tus pasos regresan con retraso. "
            "Un fragmento de obsidiana brilla entre las piedras del suelo."
        ),
        "exits": {"sur": "camino_barrancas", "norte": "claro_bosque", "este": "ribera_rio"},
        "items": ["fragmento_obsidiana"],
        "creatures": [],
        "npcs": [],
        "features": {
            "paredes":  "Roca volcánica con petroglifos: figuras que se transforman de animal a humano.",
            "eco":      "Tu voz regresa cambiada. No del todo como la mandaste.",
        },
    },

    "ribera_rio": {
        "name": "Ribera del Río Oscuro",
        "description": (
            "Un río de aguas negras y lentas bordea las barrancas. "
            "El sonido del agua imita a veces el llanto de un niño. "
            "Algo se mueve bajo la superficie."
        ),
        "exits": {"oeste": "barrancas_entrada"},
        "items": [],
        "creatures": ["ahuizotl"],
        "npcs": [],
        "features": {
            "rio":    "Aguas oscuras. Huelen a petricor y a algo más antiguo.",
            "orilla": "El barro tiene marcas: patas de animal que terminan en dedos humanos.",
        },
    },

    "claro_bosque": {
        "name": "Claro del Bosque",
        "description": (
            "Los árboles se abren en un círculo como si algo los hubiera empujado. "
            "La luz cae más fría aquí. Una figura sentada en una piedra "
            "levanta la vista cuando llegas."
        ),
        "exits": {"sur": "barrancas_entrada", "norte": "ruinas_templo"},
        "items": [],
        "creatures": [],
        "npcs": ["xochitl"],
        "features": {
            "piedra": "Glifos tallados en la piedra donde está Xochitl. Los reconoces: son del Mictlán.",
            "luz":    "Las sombras de Xochitl apuntan en dirección equivocada.",
        },
    },

    "ruinas_templo": {
        "name": "Ruinas del Templo",
        "description": (
            "Muros de piedra volcánica inclinados sin caer — algo los sostiene desde adentro. "
            "Un tzitzimitl patrulla entre los escombros: "
            "esqueleto descarnado adornado con cuchillos de pedernal."
        ),
        "exits": {"sur": "claro_bosque", "norte": "cueva_nahual"},
        "items": [],
        "creatures": ["tzitzimitl"],
        "npcs": [],
        "features": {
            "muros":      "Relieves de estrellas y huesos. Templo para pedir paso seguro en eclipses.",
            "escombros":  "Entre los escombros hay algo enterrado. El tzitzimitl lo vigila.",
        },
    },

    "cueva_nahual": {
        "name": "Cueva del Nahual",
        "description": (
            "La cueva huele a bestia y a obsidiana caliente. "
            "Las paredes brillan con cuarzo negro. "
            "El Nahual de Obsidiana aguarda al fondo: un coyote descarnado del tamaño de un caballo "
            "con costillas de obsidiana que brillan verde enfermo."
        ),
        "exits": {"sur": "ruinas_templo"},
        "locked_exits": {
            "norte": {
                "destination": "portal_mictlan",
                "requires": "obsidiana_bendita",
                "msg": "El portal al norte está sellado con magia antigua. Necesitas la Obsidiana Bendita para abrirlo.",
            }
        },
        "items": ["hierbas_fuertes"],
        "creatures": ["nahual_obsidiana"],
        "npcs": [],
        "features": {
            "paredes":  "Obsidiana en bruto. En las piezas más grandes ves reflejos de cosas que no están aquí.",
            "rastros":  "Arañazos profundos en el suelo. Algo grande, furioso y paciente.",
        },
    },

    "portal_mictlan": {
        "name": "Portal al Mictlán",
        "description": (
            "Un arco de piedra volcánica al fondo de la cueva. "
            "Los bordes vibran con una luz que no es luz — la ausencia ordenada de oscuridad. "
            "A través del arco se ve el primer nivel del Mictlán."
        ),
        "exits": {"sur": "cueva_nahual"},
        "locked_exits": {
            "norte": {
                "destination": "nivel1_orilla",
                "requires_defeated": "nahual_obsidiana",
                "msg": "El arco está inactivo. Solo quien ha vencido al guardián puede cruzarlo.",
            }
        },
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "arco": "Los nueve niveles del Mictlán están tallados en el arco. El noveno muestra un trono de cráneos.",
        },
    },

    # ── MICTLÁN — NIVEL 1 ─────────────────────────────────────────────────────
    "nivel1_orilla": {
        "name": "Apanohuaia — Orilla del Chiconahuapan",
        "description": (
            "El río de los muertos. Aguas negras que fluyen en sentido contrario al que deberían. "
            "La orilla está hecha de huesos compactados. "
            "Un Guardián del Río bloquea el único paso al otro lado."
        ),
        "exits": {"sur": "portal_mictlan"},
        "locked_exits": {
            "norte": {
                "destination": "nivel1_cruce",
                "requires_defeated": "guardian_rio",
                "msg": "El Guardián del Río bloquea el paso. Debes derrotarlo o encontrar otra manera.",
            }
        },
        "items": ["agua_mictlan"],
        "creatures": ["guardian_rio"],
        "npcs": [],
        "features": {
            "rio":       "Chiconahuapan. Las aguas del olvido. Sumergirte sin protección borra tu nombre.",
            "orilla":    "Millones de huesos compactados. Cada uno fue una persona.",
            "otro_lado": "La orilla opuesta es oscura y silenciosa. El segundo nivel del Mictlán.",
        },
    },

    "nivel1_cruce": {
        "name": "Apanohuaia — Orilla Opuesta",
        "description": (
            "Has cruzado el primer río del Mictlán. "
            "Detrás de ti el Chiconahuapan sigue fluyendo al revés. "
            "Adelante, el camino desciende hacia las montañas del segundo nivel. "
            "Lo que Diego vivió aquí, tú lo estás viviendo ahora."
        ),
        "exits": {"sur": "nivel1_orilla", "norte": "nivel2_entrada"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "oscuridad": "El segundo nivel, Tepectli Monamictlan, se oye antes de verse: un latido profundo que sacude el suelo.",
        },
        "milestone": "acto1_completado",
    },

    # ── MICTLÁN — NIVEL 2 ─────────────────────────────────────────────────────
    "nivel2_entrada": {
        "name": "Tepectli Monamictlan — Corredor de las Montañas",
        "description": (
            "Las paredes crecen a cada lado. El aire huele a polvo, a piedra aplastada, "
            "a algo ancestral que se mueve bajo la tierra. "
            "Un sonido profundo y rítmico sacude el suelo. BOOM. Pausa. BOOM. "
            "Dos paredes de roca del tamaño de un templo se abren y se cierran sin descanso."
        ),
        "exits": {"sur": "nivel1_cruce"},
        "locked_exits": {
            "norte": {
                "destination": "nivel2_cruce",
                "requires_challenge": "nivel2_montanas",
                "msg": "Las montañas que chocan bloquean el paso. Debes cruzarlas.",
            }
        },
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "montanas": "Dos paredes de roca viva. Cinco segundos abiertas, tres cerradas. El ritmo nunca cambia.",
            "polvo":    "En el suelo hay arañazos del Escudo Ceiba — la marca que Diego dejó hace cincuenta años.",
        },
    },

    "nivel2_cruce": {
        "name": "Tepectli Monamictlan — Al Otro Lado",
        "description": (
            "El camino se abre ante ti. El sonido de las montañas queda atrás, amortiguado. "
            "Adelante, el aire cambia de nuevo. Huele a algo frío. A algo afilado. "
            "Las vetas negras en las paredes anuncian el nivel siguiente."
        ),
        "exits": {"sur": "nivel2_entrada", "norte": "nivel3_entrada"},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {
            "paredes":    "Obsidiana en las vetas de la roca. El brillo aumenta conforme avanzas.",
            "fragmento":  "Una piedra lisa caída de las montañas — cálida como si guardara calor propio.",
        },
        "milestone": "nivel2_completado",
    },

    # ── FINALES (destinos del Nivel 9, placeholders) ──────────────────────────
    "final_a": {
        "name": "El Sacrificio",
        "description": (
            "Te quedas. El Mictlán te acepta como su guardián. "
            "Las puertas se sellan detrás de ti para siempre."
        ),
        "exits": {},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {},
        "ending": True,
        "ending_id": "final_a",
    },

    "final_b": {
        "name": "El Balance",
        "description": (
            "Las puertas se sellan con tu sangre dual. Vuelves al mundo mortal. "
            "Diego y Xochitl quedan libres."
        ),
        "exits": {},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {},
        "ending": True,
        "ending_id": "final_b",
    },

    "final_c": {
        "name": "La Liberación",
        "description": (
            "Con el canto que Diego nunca pudo dar, liberas a todos los que quedaron atrapados. "
            "Los dos mundos se separan en paz."
        ),
        "exits": {},
        "items": [],
        "creatures": [],
        "npcs": [],
        "features": {},
        "ending": True,
        "ending_id": "final_c",
    },
}

ITEMS = {
    "tlachicotl": {
        "name": "Tlachicotl",
        "description": (
            "Espada de obsidiana volcánica y acero toledano. La hoja absorbe la luz. "
            "Al empuñarla sientes rabia y tristeza que no son tuyas."
        ),
        "type": "weapon",
        "damage": 9,
        "weakness_bonus_vs": "nahual_obsidiana",
    },
    "tonatiuh": {
        "name": "Tonatiuh",
        "description": (
            "Arcabuz con plumas de quetzal y jade. Balas de plata fundida con copal. "
            "Letales para criaturas del inframundo. Quedan pocas — úsalo con sabiduría."
        ),
        "type": "weapon",
        "damage": 13,
        "weakness_bonus_vs": "tzitzimitl",
    },
    "escudo_ceiba": {
        "name": "Escudo Ceiba",
        "description": (
            "Escudo de piel de jaguar sobre madera de ceiba sagrada. "
            "Repele proyectiles y maldiciones. Emite calor al sostenerlo."
        ),
        "type": "shield",
        "damage": 4,
        "defense": 5,
    },
    "copal_sagrado": {
        "name": "Copal Sagrado",
        "description": "Resina consagrada. El humo ahuyenta espíritus y debilita criaturas del inframundo.",
        "type": "ritual",
        "combat_bonus": 6,
        "weakness_bonus_vs": "ahuizotl",
        "use_msg": "Enciendes el copal. El humo sube en espiral y la criatura retrocede, quemada.",
    },
    "caracola_quetzalcoatl": {
        "name": "Caracola de Quetzalcóatl",
        "description": (
            "Su sonido imita el llamado del dios serpiente. "
            "Confunde guardianes que sirven a poderes mayores."
        ),
        "type": "ritual",
        "combat_bonus": 8,
        "weakness_bonus_vs": "guardian_rio",
        "use_msg": "Soplas la caracola. El sonido llena el espacio y la criatura se tambalea, desorientada.",
    },
    "obsidiana_bendita": {
        "name": "Obsidiana Bendita",
        "description": "Fragmento consagrado por ritual. Sella portales y abre caminos entre mundos.",
        "type": "key",
        "use_msg": "La obsidiana brilla al acercarse al portal. El sello se rompe con un sonido de huesos.",
    },
    "tamales_citlali": {
        "name": "Tamales de Citlali",
        "description": "Tamales de frijol y chile en hoja de maíz. Para el camino.",
        "type": "healing",
        "healing": 30,
    },
    "hierbas_curativas": {
        "name": "Hierbas Curativas",
        "description": "Árnica, romero y ruda. Curan heridas menores.",
        "type": "healing",
        "healing": 15,
    },
    "hierbas_fuertes": {
        "name": "Hierbas del Mictlán",
        "description": "Solo crecen cerca de portales al inframundo. Más potentes que cualquier medicina mortal.",
        "type": "healing",
        "healing": 25,
    },
    "agua_mictlan": {
        "name": "Agua del Chiconahuapan",
        "description": "Un cuenco de hueso con el agua del río de los muertos. Paradójicamente, restaura a los vivos.",
        "type": "healing",
        "healing": 20,
        "take_msg": "El agua fría te quema la mano, pero la guardas.",
    },
    "fragmento_obsidiana": {
        "name": "Fragmento de Obsidiana",
        "description": "Obsidiana volcánica. Afilado como navaja. Algo en él vibra.",
        "type": "lore",
    },
    "escamas_ahuizotl": {
        "name": "Escamas del Ahuízotl",
        "description": "Escamas duras con reflejo azul-negro. Citlali sabrá para qué sirven.",
        "type": "lore",
    },
    # ── Nivel 2 — Tepectli Monamictlan ────────────────────────────────────────
    "fragmento_tepectli": {
        "name": "Fragmento de Tepectli",
        "description": (
            "Piedra arrancada de las costillas del Mictlán. Cálida al tacto. "
            "Guarda la memoria del cruce — ningún fragmento es igual al otro."
        ),
        "type": "lore",
    },
    "polvo_tepectli": {
        "name": "Polvo de Tepectli",
        "description": (
            "Ceniza de las montañas que chocan, recogida tras calmarlas con canto. "
            "Componente ritual de mezclas curativas del Mictlán."
        ),
        "type": "ritual",
        "combat_bonus": 5,
        "use_msg": "El polvo se disuelve en el aire con un sonido de hueso y canto.",
    },
    "guano_murcielago": {
        "name": "Guano de Murciélago Sagrado",
        "description": (
            "De los murciélagos ciegos de la cresta del Tepectli. "
            "Sus oídos perciben lo invisible. Componente alquímico raro."
        ),
        "type": "lore",
    },
}

CREATURES = {
    "ahuizotl": {
        "name": "Ahuízotl",
        "description": (
            "Criatura del tamaño de un perro grande con cuerpo de nutria y "
            "cola que termina en una mano humana. Ojos de obsidiana mojada."
        ),
        "combat_desc": (
            "El Ahuízotl agita su cola-mano. Sus ojos no parpadean. "
            "El llanto que emite suena demasiado humano."
        ),
        "hp": 30,
        "attack": 6,
        "defense": 2,
        "weakness_hint": "El humo sagrado lo quema.",
        "weakness_bonus_vs_item": "copal_sagrado",
        "loot": ["escamas_ahuizotl"],
    },
    "tzitzimitl": {
        "name": "Tzitzimitl",
        "description": (
            "Demonio estelar: esqueleto con cuchillos de pedernal por dedos. "
            "Ata dentro de sí las estrellas que devoró."
        ),
        "combat_desc": (
            "El Tzitzimitl extiende sus brazos-cuchillo. "
            "El aire enfría varios grados. Ataca en ráfagas rápidas."
        ),
        "hp": 40,
        "attack": 8,
        "defense": 3,
        "weakness_hint": "Las balas de plata lo atraviesan.",
        "weakness_bonus_vs_item": "tonatiuh",
        "loot": ["caracola_quetzalcoatl"],
    },
    "nahual_obsidiana": {
        "name": "Nahual de Obsidiana",
        "description": (
            "Coyote descarnado del tamaño de un caballo. "
            "Costillas de obsidiana verde. Su sombra se mueve independiente de su cuerpo."
        ),
        "combat_desc": (
            "El Nahual te rodea con movimientos imposibles. "
            "Su sombra ataca primero, el cuerpo después. "
            "'Hueles a él... al que nos cazaba...' gruñe."
        ),
        "hp": 45,
        "attack": 10,
        "defense": 4,
        "weakness_hint": "La hoja de obsidiana sagrada corta su sombra.",
        "weakness_bonus_vs_item": "tlachicotl",
        "loot": ["obsidiana_bendita"],
    },
    "guardian_rio": {
        "name": "Guardián del Río",
        "description": (
            "Figura de agua negra sin forma definida. "
            "Cuando habla, el sonido llega desde todas las direcciones."
        ),
        "combat_desc": (
            "El Guardián se expande bloqueando el paso. "
            "Voz: '¿Por qué cruzas, vivo?' "
            "La caracola lo desestabiliza."
        ),
        "hp": 35,
        "attack": 7,
        "defense": 4,
        "weakness_hint": "El sonido de la caracola lo confunde.",
        "weakness_bonus_vs_item": "caracola_quetzalcoatl",
        "loot": [],
    },
}

NPCS = {
    "citlali": {
        "name": "Citlali",
        "description": "Anciana curandera. Conoció a Diego antes de que entrara al Mictlán.",
        "dialogue": [
            "Las estrellas sangraron anoche. No es metáfora. "
            "Ve a mi casa — las reliquias de Diego son tuyas. Al este de aquí.",
        ],
        "gives_item": "tamales_citlali",
        "give_msg": "Citlali envuelve tamales en hoja de maíz sin mirarte. 'Para el camino.'",
    },
    "rodrigo": {
        "name": "Capitán Rodrigo",
        "description": "Capitán español con sombras bajo los ojos. Sus hombres desaparecieron en las barrancas.",
        "dialogue": [
            "Mis hombres no vuelven del río al este de las barrancas. "
            "Algo los atrae. Cuídate del agua oscura.",
        ],
        "gives_item": None,
    },
    "vendedora": {
        "name": "Doña Esperanza",
        "description": "Vendedora del mercado. Lleva décadas aquí y ha visto de todo.",
        "dialogue": [
            "Las hierbas del mostrador son tuyas, tómalas. "
            "El copal fuerte está en casa de Citlali — ese es el que sirve contra criaturas.",
        ],
        "gives_item": None,
    },
    "xochitl": {
        "name": "Xochitl",
        "description": "Espíritu de una joven que murió hace treinta años. Lleva ropa de esa época.",
        "dialogue": [
            "Diego me prometió que alguien vendría. Eres tú. "
            "El Nahual está en la cueva al norte del templo. Necesitas Tlachicotl para herirlo de verdad. "
            "Y para entrar al Mictlán necesitas lo que él guarda.",
        ],
        "gives_item": None,
    },
}

# ── CHALLENGES ────────────────────────────────────────────────────────────────
# Each challenge is a multi-phase choice sequence triggered by a
# requires_challenge locked exit. Completing it sets
# "challenge_{challenge_id}_done" on the player.

from content.levels_mictlan import ITEMS_MICTLAN, ROOMS_MICTLAN, CHALLENGES_MICTLAN

ITEMS.update(ITEMS_MICTLAN)
ROOMS.update(ROOMS_MICTLAN)

CHALLENGES: dict[str, dict] = {
    "nivel2_montanas": {
        "name": "Tepectli Monamictlan — Las Montañas que Chocan",
        "entry_text": (
            "Las ves. Dos paredes de roca viva, cada una del tamaño de un templo,\n"
            "se abren y cierran rítmicamente. Cinco segundos abiertas, tres cerradas.\n"
            "Con cada golpe, el suelo tiembla bajo tus pies.\n\n"
            "XOCHITL: \"Tepectli Monamictlan. Las costillas del Mictlán. No son roca —\n"
            "son los huesos del mundo de abajo, y todavía respiran.\""
        ),
        "start_phase": "observacion",
        "phases": {
            # ── Phase 1: observe before acting ──────────────────────────────
            "observacion": {
                "text": (
                    "Tienes un momento para observar antes de actuar.\n"
                    "¿Cómo te preparas?"
                ),
                "options": [
                    {
                        "label": "[ESP] Calcular el ritmo — contar los segundos entre impactos",
                        "response_text": (
                            "Te agachas fuera del alcance y cuentas.\n"
                            "Uno, dos, tres, cuatro, cinco — abiertas.\n"
                            "Seis, siete, ocho — cerradas. Constante como un metrónomo.\n\n"
                            "JUGADOR: \"Cinco segundos. Veinte pasos. Es justo. Pero posible.\"\n"
                            "XOCHITL: \"Si corres rápido. Si el polvo no te resbala.\n"
                            "Si el miedo no te congela a medio camino. Muchos 'si', ¿no?\"\n\n"
                            "[OBSERVACIÓN TÁCTICA: ritmo identificado]"
                        ),
                        "sets_flag": "nivel2_obs_calculo",
                        "next_phase": "cruce",
                    },
                    {
                        "label": "[NAH] Escuchar la respiración — ¿está viva de verdad?",
                        "response_text": (
                            "Cierras los ojos. Ignoras el estruendo superficial\n"
                            "y buscas algo más profundo. Ahí está: debajo del golpe,\n"
                            "un sonido suave, casi tierno. Las montañas gimen al separarse.\n"
                            "Como si no quisieran abrirse. Como si tuvieran frío sin la otra.\n\n"
                            "XOCHITL (en voz baja): \"¿Lo oyes? Tienen miedo. Están solas cuando\n"
                            "se separan. Chocan para sentirse juntas. Llevan haciéndolo desde\n"
                            "que el Mictlán existe.\"\n\n"
                            "[PERCEPCIÓN ESPIRITUAL: cantar puede calmarlas]"
                        ),
                        "sets_flag": "nivel2_obs_escuchar",
                        "next_phase": "cruce",
                    },
                    {
                        "label": "[DUAL] Buscar señales de Diego — marcas en la roca",
                        "response_text": (
                            "Examinas la roca. Encuentras arañazos profundos — la marca\n"
                            "del Escudo Ceiba — y sangre seca, oscurecida por cincuenta años.\n"
                            "Debajo, talladas con la punta de Tlachicotl, dos palabras:\n\n"
                            "JUGADOR (leyendo): \"'NO CORRAS. CANTA.'\"\n"
                            "XOCHITL: \"¿Eso dice? Diego nunca cantó aquí. Lo sé. Entonces…\n"
                            "¿por qué lo talló? ¿Lo dejó para ti?\"\n\n"
                            "[SEÑAL DE DIEGO: cantar desbloqueado]"
                        ),
                        "sets_flag": "nivel2_obs_diego",
                        "next_phase": "cruce",
                    },
                ],
            },
            # ── Phase 2: main crossing choice ────────────────────────────────
            "cruce": {
                "text": (
                    "Las montañas siguen su ritmo eterno.\n"
                    "Es momento de cruzar. ¿Cómo lo haces?"
                ),
                "options": [
                    {
                        "label": "[FUERZA] Correr con el Escudo Ceiba en alto",
                        "response_text": (
                            "Levantas el Escudo Ceiba. La madera de ceiba vibra en tus manos,\n"
                            "como si supiera lo que viene. Corres.\n\n"
                            "El escudo absorbe el golpe con un crujido que sientes en los dientes.\n"
                            "La fuerza te lanza hacia adelante. Ruedas por el polvo al otro lado,\n"
                            "tosiendo, con el brazo entumecido hasta el hombro.\n\n"
                            "XOCHITL: \"¡Estás vivo! Wow. Estás hecho mierda, pero vivo.\""
                        ),
                        "sets_flag": "nivel2_cruce_fuerza",
                        "esp_delta": 2,
                        "next_phase": None,
                        "grants_items": ["fragmento_tepectli"],
                    },
                    {
                        "label": "[SABIDURÍA] Cantar para calmar las montañas",
                        "requires_flag_any": ["nivel2_obs_escuchar", "nivel2_obs_diego"],
                        "response_text": (
                            "Te paras frente al corredor de la muerte.\n"
                            "En lugar de correr, abres la boca.\n"
                            "Diego dejó el mensaje: 'NO CORRAS. CANTA.'"
                        ),
                        "next_phase": "cantar",
                    },
                    {
                        "label": "[INGENIO] Buscar otro camino — escalar, cavar, rodear",
                        "response_text": (
                            "Decides no cruzar de frente. Hay que ser más astuto."
                        ),
                        "next_phase": "ingenio",
                    },
                    {
                        "label": "[RITUAL] Ofrecer sangre propia a la roca",
                        "response_text": (
                            "Algo te dice que la roca espera. No velocidad — algo más viejo.\n"
                            "Desenvainas Tlachicotl. Con la punta de obsidiana te cortas\n"
                            "la palma de la mano izquierda. Una línea limpia. La sangre cae.\n\n"
                            "La roca BEBE. La sangre desaparece al contacto, absorbida\n"
                            "como agua en arena seca.\n\n"
                            "XOCHITL (en voz baja): \"Sangre viva. La roca del Mictlán no había\n"
                            "probado sangre viva en cincuenta años. Desde Diego.\"\n\n"
                            "Las montañas se abren. Despacio. Con reverencia."
                        ),
                        "sets_flag": "nivel2_cruce_sangre",
                        "next_phase": "sangre",
                    },
                ],
            },
            # ── Phase 3a: singing sub-choices ─────────────────────────────────
            "cantar": {
                "text": "¿Qué cantas?",
                "options": [
                    {
                        "label": "[NAH] Un icnocuicatl en náhuatl puro — canto de orfandad",
                        "response_text": (
                            "Las palabras salen temblorosas al principio,\n"
                            "pero la melodía las sostiene. Un icnocuicatl — canto que\n"
                            "las madres nahuas usaban para calmar a los niños que lloraban\n"
                            "por sus muertos. Las palabras hablan de separación y reencuentro.\n\n"
                            "Las montañas... se detienen.\n\n"
                            "No de golpe. Gradualmente. Las dos paredes quedan abiertas,\n"
                            "temblando levemente. Como un niño que deja de llorar pero\n"
                            "aún tiene los labios temblorosos.\n\n"
                            "XOCHITL (susurra): \"¿Ves ese polvo que cae de la cima?\n"
                            "No es polvo. Son lágrimas.\"\n\n"
                            "Cruzas sin prisa. Al salir, una piedra lisa y cálida cae\n"
                            "de la pared — un regalo.\n"
                            "JUGADOR: \"Gracias, abuelas.\"\n"
                            "XOCHITL: \"Abuelas. Sí. Diego las llamó 'obstáculo'.\n"
                            "Tú las llamas 'abuelas'. Por eso estás aquí y él se quedó abajo.\""
                        ),
                        "sets_flags": ["nivel2_cruce_canto", "nivel2_canto_nahua", "voz_montanas"],
                        "nah_delta": 3,
                        "next_phase": None,
                        "grants_items": ["fragmento_tepectli", "polvo_tepectli"],
                    },
                    {
                        "label": "[ESP] Un rezo colonial en español — oración de protección",
                        "response_text": (
                            "Cantas un Ave María. Las palabras salen del fondo de la garganta,\n"
                            "donde las guardaba tu abuela paterna.\n\n"
                            "Las montañas dudan. Su ritmo se desacelera. No se detienen del todo —\n"
                            "diez segundos de apertura en lugar de cinco.\n"
                            "XOCHITL: \"No lo entienden del todo. El idioma les es extraño.\n"
                            "Pero sienten la intención. Eso te da tiempo.\"\n\n"
                            "Cruzas con pasos firmes — un trote digno.\n"
                            "Las montañas se cierran detrás de ti con un golpe suave."
                        ),
                        "sets_flags": ["nivel2_cruce_canto", "nivel2_canto_esp"],
                        "esp_delta": 1, "nah_delta": 1,
                        "next_phase": None,
                        "grants_items": ["fragmento_tepectli"],
                    },
                    {
                        "label": "[DUAL] Alternar versos en náhuatl y español",
                        "response_text": (
                            "Empiezas en náhuatl. Las palabras antiguas salen como agua\n"
                            "de manantial. Luego, sin pensarlo, deslizas un verso en español.\n"
                            "Y vuelves al náhuatl. Los dos idiomas se trenzan como hilos\n"
                            "de un huipil — algo que no es ni uno ni otro sino ambos.\n\n"
                            "Las montañas se detienen.\n\n"
                            "Pero esta vez no solo se detienen. Se ABREN. Completamente.\n"
                            "Más de lo que se han abierto jamás — un salón ancho bañado\n"
                            "en una luz que viene de las propias paredes de roca.\n\n"
                            "XOCHITL (se lleva las manos a la boca):\n"
                            "\"Eso no lo había visto nunca. Ni con Diego. Ni con nadie.\n"
                            "Las costillas del Mictlán se están abriendo PARA TI.\"\n\n"
                            "Caminas entre las montañas. Las paredes vibran suavemente\n"
                            "con la resonancia de tu canto, como si tararearan contigo.\n"
                            "JUGADOR: \"Dos mundos. Una canción. Así debería ser siempre.\"\n"
                            "XOCHITL: \"Diego era un puente, pero no sabía que lo era.\n"
                            "Tú lo sabes. Tú lo eliges. Eso lo cambia todo.\""
                        ),
                        "sets_flags": [
                            "nivel2_cruce_canto", "nivel2_canto_dual",
                            "voz_montanas", "bendicion_osea",
                        ],
                        "nah_delta": 2,
                        "next_phase": None,
                        "grants_items": ["fragmento_tepectli", "polvo_tepectli"],
                    },
                ],
            },
            # ── Phase 3b: ingenuity sub-choices ───────────────────────────────
            "ingenio": {
                "text": "¿Qué intentas?",
                "options": [
                    {
                        "label": "[1] Escalar por encima de las montañas",
                        "response_text": (
                            "La superficie tiene grietas y salientes. Escalable. Difícil.\n\n"
                            "Subes. Las manos se raspan. A medio camino las montañas CHOCAN\n"
                            "debajo de ti — la vibración casi te suelta.\n\n"
                            "Llegas a la cima. El Mictlán se extiende en todas direcciones\n"
                            "como un paisaje de hueso y ceniza. En un nicho de la cresta,\n"
                            "un nido: murciélagos del Mictlán, ciegos, que te escuchan\n"
                            "con curiosidad.\n\n"
                            "XOCHITL: \"Astuto. Diego hubiera aprobado. Él siempre decía\n"
                            "que el camino más obvio tiene las trampas más grandes.\""
                        ),
                        "sets_flag": "nivel2_cruce_escalar",
                        "esp_delta": 1,
                        "next_phase": None,
                        "grants_items": ["fragmento_tepectli", "guano_murcielago"],
                    },
                    {
                        "label": "[2] Cavar por debajo de las montañas",
                        "response_text": (
                            "El suelo es ceniza compactada. Siglos de polvo. Excavable.\n\n"
                            "Cavas con Tlachicotl como pala improvisada. El túnel se forma\n"
                            "despacio. A medio metro, tus dedos tocan huesos — los restos\n"
                            "de otros que intentaron cruzar y no lo lograron. Fragmentos\n"
                            "de armadura nahua, sandalias podridas, un cuchillo roto.\n\n"
                            "JUGADOR: \"Descansen. Yo paso por aquí, pero no los olvido.\"\n"
                            "XOCHITL: \"Eso es más respeto del que este lugar acostumbra ver.\n"
                            "Los muertos aquí no reciben oraciones. Solo olvido.\"\n\n"
                            "Sales al otro lado cubierto de ceniza y polvo de hueso. Vivo."
                        ),
                        "sets_flag": "nivel2_cruce_cavar",
                        "nah_delta": 1,
                        "next_phase": None,
                        "grants_items": ["fragmento_tepectli"],
                    },
                ],
            },
            # ── Phase 3c: blood offering crossing ────────────────────────────
            "sangre": {
                "text": (
                    "Las montañas se han abierto. Tu mano sangra.\n"
                    "¿Cómo cruzas?"
                ),
                "options": [
                    {
                        "label": "[1] Cruzar rápido, sin mirar atrás",
                        "response_text": (
                            "Aprietas la mano herida y corres. No sabes cuánto durará.\n\n"
                            "Sales al otro lado. Detrás de ti las montañas se cierran\n"
                            "con furia renovada — más fuerte que antes. Como si la ofrenda\n"
                            "las hubiera despertado y estuvieran frustradas de que te fuiste tan rápido.\n"
                            "XOCHITL: \"Ofreciste. Bien. Pero también huiste.\n"
                            "El Mictlán nota esas cosas. La ofrenda fue sincera.\n"
                            "La salida fue cobarde. Se equilibra.\""
                        ),
                        "sets_flag": "nivel2_cruce_sangre_rapido",
                        "nah_delta": 1,
                        "next_phase": None,
                        "grants_items": ["fragmento_tepectli"],
                    },
                    {
                        "label": "[2] Caminar despacio, con dignidad",
                        "response_text": (
                            "Caminas sin prisa. Cada gota de sangre es absorbida al instante.\n\n"
                            "A medio camino te detienes. Miras la pared izquierda. La derecha.\n"
                            "Las montañas están quietas. No quieren cerrarse mientras estés adentro.\n\n"
                            "Pones la mano ensangrentada sobre la pared izquierda.\n"
                            "JUGADOR: \"Gracias por dejarme pasar.\"\n\n"
                            "La roca tiembla bajo tu palma. Cuando retiras la mano,\n"
                            "tu huella queda grabada en la piedra — roja sobre gris,\n"
                            "como una pintura rupestre nueva.\n\n"
                            "XOCHITL (voz quebrada): \"Diego ofreció sangre de enemigos.\n"
                            "Tú diste la tuya. Eso importa. En este lugar, eso importa mucho.\"\n\n"
                            "Las montañas se cierran suavemente detrás de ti.\n"
                            "Suavemente. Por primera vez desde que existen."
                        ),
                        "sets_flags": ["nivel2_cruce_sangre_digna", "cicatriz_tepectli"],
                        "nah_delta": 2,
                        "next_phase": None,
                        "grants_items": ["fragmento_tepectli"],
                    },
                ],
            },
        },
    },
}

CHALLENGES.update(CHALLENGES_MICTLAN)
